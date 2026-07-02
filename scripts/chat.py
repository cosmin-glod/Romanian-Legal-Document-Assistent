"""Interactive chat CLI: question → retrieval → local LLM answer.

The REPL is conversational: each turn is answered with the prior turns as
context, so follow-up questions ("dar dacă nu suntem căsătoriți?") resolve
against what was already discussed. Grounding rules still apply — the answer
must come from the sources retrieved for the current turn.

If the assistant detects that the user wants to pre-fill a form, the REPL
transitions into form-collection mode: it lists the required fields, accepts
a natural-language paragraph from the user, runs LLM extraction, validates,
and either generates the PDF or reports back missing/invalid fields.

Usage:
    uv run python scripts/chat.py
    uv run python scripts/chat.py "Care este vârsta minimă pentru căsătorie?"
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.extractor import extract
from licenta.form_registry import (
    FORMS,
    FormDef,
    capability_answer,
    detect_capability_intent,
    detect_conversational_intent,
    detect_form_intent,
    looks_administrative,
    problem_field_names,
)
from licenta.generator import DEFAULT_MODEL, chat_reply, generate
from licenta.retriever import Retriever

MAX_LLM_TURNS = 2  # try LLM extraction this many times before falling back
MAX_FORM_ATTEMPTS = 4
FORMS_OUTPUT_DIR = Path("data/forms")
HISTORY_TURNS = 4  # prior user/assistant turns fed back as conversation context


def _prior_turns(history: list[dict]) -> list[dict]:
    """Last HISTORY_TURNS user/assistant messages as plain dialogue."""
    turns = [
        {"role": m["role"], "content": m["content"]}
        for m in history
        if m["role"] in ("user", "assistant")
    ]
    return turns[-HISTORY_TURNS * 2 :]


def _retrieval_query(history: list[dict], question: str) -> str:
    """Prepend the previous user turn so a bare follow-up still retrieves on the
    right topic. Generation gets the full history; this only steers retrieval."""
    prior_users = [m["content"] for m in history if m["role"] == "user"]
    if prior_users:
        return f"{prior_users[-1]} {question}"
    return question


# ---------------------------- Q&A turn ----------------------------

def _answer_one(
    retriever: Retriever, question: str, k: int, model: str, history: list[dict]
):
    hits = retriever.query(_retrieval_query(history, question), k=k)
    answer = generate(question, hits, model=model, history=_prior_turns(history))

    print("\n" + "=" * 80)
    print(f"Q: {question}")
    print("-" * 80)
    print(answer.text)
    if answer.schema.documents_mentioned:
        print()
        print("Documente menționate:")
        for d in answer.schema.documents_mentioned:
            print(f"  - {d}")
    print("-" * 80)
    cited = set(answer.schema.cited_source_indices)
    print(
        f"Surse (citate marcate cu *)  | attempts={answer.attempts}  "
        f"valid={answer.valid}  form_offer={answer.schema.form_offer!r}"
    )
    for i, h in enumerate(answer.sources, 1):
        marker = "*" if i in cited else " "
        print(f" {marker}[S{i}] {h.metadata['breadcrumb']}")
    if answer.violations:
        print()
        print("Violations neretransformabile:")
        for v in answer.violations:
            print(f"  - [{v.rule_id}] {v.message}")
    print("=" * 80)
    return answer


# ---------------------------- form turn ----------------------------

def _required_field_summary(form_def: FormDef) -> str:
    """Render the form's schema as a human-readable list of required fields."""
    lines: list[str] = []
    for name, info in form_def.schema.model_fields.items():
        desc = info.description or name
        lines.append(f"  - {name}: {desc}")
    return "\n".join(lines)


def _format_field_value(value) -> str:
    if value is None:
        return "·"
    return str(value)


def _show_partial(form, form_def: FormDef) -> None:
    print("\nCâmpuri colectate până acum:")
    for name in form_def.schema.model_fields:
        print(f"  {name}: {_format_field_value(getattr(form, name))}")


def _manual_fill(form_def: FormDef, accumulated):
    """Field-by-field interactive prompts for any missing/invalid field."""
    current = accumulated.model_copy()
    fmt = form_def.field_format_regex or {}

    print("\n" + "-" * 80)
    print("Mod manual: te întreb câmp cu câmp. Apasă Enter pentru a sări un câmp.")
    print("-" * 80)

    while True:
        problems = problem_field_names(form_def, current)
        if not problems:
            return current
        for name in problems:
            info = form_def.schema.model_fields[name]
            desc = info.description or name
            hint = ""
            if name in fmt:
                hint = f"  [format: {fmt[name].pattern}]"
            try:
                val = input(f"\n  {name}{hint}\n    {desc}\n  > ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                return current
            if not val:
                continue
            if name in fmt and not fmt[name].match(val):
                print(
                    f'  Valoarea „{val}" nu se potrivește cu formatul '
                    f"{fmt[name].pattern}. Te rog re-încearcă mai târziu."
                )
                continue
            setattr(current, name, val)
        # Loop again only if still incomplete; user may have skipped fields
        # and want to be re-prompted.
        if problem_field_names(form_def, current) == problems:
            # No progress this loop — user is skipping; exit gracefully
            return current


def _run_form_collection(form_def: FormDef, model: str) -> None:
    print("\n" + "*" * 80)
    print(f"Pregătim formularul: {form_def.display_name}")
    print(form_def.description)
    print()
    print("Câmpuri necesare:")
    print(_required_field_summary(form_def))
    print()
    print(
        "Scrie într-un singur mesaj toate informațiile pe care le ai. "
        "Voi extrage automat ce pot. Scrie /manual pentru a completa "
        "câmp cu câmp."
    )
    print("*" * 80)

    accumulated = form_def.schema()
    used_llm_turns = 0

    while used_llm_turns < MAX_LLM_TURNS:
        try:
            user_text = input("\n[formular] > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n(Renunțat la formular.)")
            return
        if not user_text:
            print("(Niciun text — te rog spune ce date ai.)")
            continue
        if user_text.lower() in {"exit", "renunt", "renunț", ":q"}:
            print("(Renunțat la formular.)")
            return
        if user_text.lower() in {"/manual", "manual"}:
            break

        used_llm_turns += 1
        result = extract(user_text, form_def, accumulated=accumulated, model=model)
        accumulated = result.form

        if result.fields_extracted_this_turn:
            print(
                f"\nAm extras: {', '.join(result.fields_extracted_this_turn)}"
            )
        else:
            print("\n(Nu am putut extrage câmpuri noi din mesajul tău.)")
        _show_partial(accumulated, form_def)

        if result.is_complete:
            _finalize(form_def, accumulated)
            return

        print(f"\nMai lipsesc/sunt invalide {len(result.errors)} câmpuri:")
        for e in result.errors:
            print(f"  - {e}")
        if used_llm_turns < MAX_LLM_TURNS:
            print(
                "\nTrimite-mi datele lipsă într-un mesaj nou, "
                "sau scrie /manual pentru a trece la completare câmp cu câmp."
            )

    # LLM turns exhausted or user requested manual mode: complete deterministically.
    print(
        f"\n(Trec în mod manual pentru câmpurile rămase după "
        f"{used_llm_turns} runde LLM.)"
    )
    accumulated = _manual_fill(form_def, accumulated)
    _finalize(form_def, accumulated)


def _finalize(form_def: FormDef, form) -> None:
    errors = form_def.validate_fn(form)
    if errors:
        print("\nFormularul este incomplet — nu pot genera PDF-ul:")
        for e in errors:
            print(f"  - {e}")
        return
    out_path = FORMS_OUTPUT_DIR / f"{form_def.form_id}.pdf"
    form_def.render_fn(form, out_path)
    print(f"\n✓ Formular generat: {out_path}")


# ---------------------------- main loop ----------------------------

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("question", nargs="?", help="single question; omit for REPL")
    p.add_argument("-k", type=int, default=4, help="number of chunks to retrieve")
    p.add_argument("-m", "--model", default=DEFAULT_MODEL)
    args = p.parse_args()

    logging.basicConfig(level=logging.WARNING, format="%(message)s")
    retriever = Retriever()
    history: list[dict] = []  # conversation turns, shared across the REPL

    def handle(question: str) -> None:
        # Capability/meta questions are answered from the registry, not RAG.
        if detect_capability_intent(question):
            print("\n" + "=" * 80)
            print(capability_answer())
            print("=" * 80)
            history.append({"role": "user", "content": question})
            history.append({"role": "assistant", "content": capability_answer()})
            return
        # Personal/meta questions are answered from history, not RAG.
        # Administrative/form intent wins (a mixed message still goes to RAG).
        if (
            detect_conversational_intent(question)
            and not detect_form_intent(question)
            and not looks_administrative(question)
        ):
            reply = chat_reply(question, _prior_turns(history), args.model)
            print("\n" + "=" * 80)
            print(reply)
            print("=" * 80)
            history.append({"role": "user", "content": question})
            history.append({"role": "assistant", "content": reply})
            return
        answer = _answer_one(retriever, question, args.k, args.model, history)
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer.text})
        # Hybrid intent detection: trust LLM if it set form_offer, else fall
        # back to rule-based keyword match for high-confidence triggers.
        form_id = answer.schema.form_offer or detect_form_intent(question)
        if not form_id:
            return
        if not answer.schema.form_offer:
            print(f"\n(intent detectat prin keyword fallback: {form_id})")
        form_def = FORMS.get(form_id)
        if form_def is None:
            print(f"\n(form_offer='{form_id}' nu este în registru; ignorat.)")
            return
        try:
            confirm = input(
                f'\nVrei să completăm acum „{form_def.display_name}"? '
                "(enter = da, n = nu) "
            ).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if confirm in {"n", "nu", "no"}:
            return
        _run_form_collection(form_def, args.model)

    if args.question:
        handle(args.question)
        return

    print("Chat ready. Introdu o întrebare (sau 'exit' / Ctrl-D).")
    while True:
        try:
            q = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not q:
            continue
        if q.lower() in {"exit", "quit", ":q"}:
            return
        handle(q)


if __name__ == "__main__":
    main()
