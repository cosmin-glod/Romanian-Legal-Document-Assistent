"""Streamlit UI for the citizen-assistant prototype.

Layout: chat in a centered, reading-width main column; sources + generated forms
in the sidebar. When the user expresses form-filling intent (detected via either
the LLM's `form_offer` field or the keyword fallback), a form-collection block
opens under the chat. It uses up to MAX_LLM_TURNS LLM extraction passes, then
falls back to deterministic field-by-field manual entry. Manual fields are shown
with their Romanian labels (from the form spec), grouped by section. The same
components power the CLI in scripts/chat.py — this file is purely the UI layer.

Run:
    uv run streamlit run streamlit_app.py

Against the remote (Kaggle) model endpoint:
    OLLAMA_HOST=https://<your-tunnel>.trycloudflare.com ./scripts/demo_remote.sh
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make the src/ package importable without an editable install.
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

import streamlit as st

from licenta.extractor import expected_llm_calls, extract
from licenta.form_registry import (
    FORMS,
    FormDef,
    capability_answer,
    detect_capability_intent,
    detect_form_intent,
    problem_field_names,
)
from licenta.generator import DEFAULT_MODEL, generate
from licenta.retriever import Retriever

MAX_LLM_TURNS = 2
FORMS_OUTPUT_DIR = Path("data/forms")

# Friendly, fill-in-the-blank examples shown as input placeholders, keyed by the
# field "kind" declared in the form spec. Purely cosmetic guidance.
_KIND_PLACEHOLDER: dict[str, str] = {
    "cnp": "ex: 1850412220011 (13 cifre)",
    "id_series": "ex: RT (2 litere mari)",
    "id_number": "ex: 234567 (6 cifre)",
    "date": "ex: 2024-03-15 (AAAA-LL-ZZ)",
    "sex": "M (masculin) sau F (feminin)",
    "iban": "ex: RO49AAAA1B31007593840000",
    "amount": "ex: 1500 (RON)",
    "int": "ex: 10",
}


# ---------------------------- caching ----------------------------

@st.cache_resource(show_spinner="Încarc modelul de regăsire (bge-m3, ~2 GB)…")
def get_retriever() -> Retriever:
    return Retriever()


@st.cache_resource(show_spinner="Pornesc modelul de generare…")
def warm_llm() -> bool:
    """Force the Ollama backend to load the model into memory once, at app
    start, so the first user prompt isn't slowed by a cold model load."""
    import ollama

    try:
        ollama.chat(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": "ping"}],
            options={"num_predict": 1},
        )
    except Exception:
        return False
    return True


# How many prior turns (user+assistant) to feed back as conversation context.
HISTORY_TURNS = 4


# ---------------------------- session state ----------------------------

def _new_conversation() -> dict:
    return {"title": "Întrebare nouă", "history": [], "form_state": None}


def _init_state() -> None:
    if "conversations" not in st.session_state:
        st.session_state.conversations = [_new_conversation()]
    if "active" not in st.session_state:
        st.session_state.active = 0


def _conv() -> dict:
    """The active conversation (its own history + form state)."""
    return st.session_state.conversations[st.session_state.active]


# ---------------------------- styling ----------------------------

# One responsive style block. Goals:
#   - comfortable reading measure on wide screens (centered, capped width),
#     full-bleed with smaller gutters on phones;
#   - long unbroken tokens (CNP, IBAN, URLs) must wrap, never cause a horizontal
#     scrollbar;
#   - a readable, fixed sidebar on desktop (it overlays full-width on mobile,
#     so only widen it above the breakpoint).
_CSS = """
<style>
  .block-container, [data-testid="stMainBlockContainer"] {
      max-width: 940px;
      margin: 0 auto;
      padding-top: 2.2rem;
      padding-bottom: 6rem;
      padding-left: 2rem;
      padding-right: 2rem;
  }
  @media (max-width: 680px) {
      .block-container, [data-testid="stMainBlockContainer"] {
          padding-left: 1rem; padding-right: 1rem;
      }
  }
  /* Streamlit 1.57 lays each markdown block inside a chat message as a
     shrink-to-content flex child: a short block sizes to its longest line's
     text width, but the <li> bullet indent isn't counted, so the longest item
     overflows by the indent and drops its last word to a new line. Force the
     blocks to fill the message width — they then wrap only at the real edge. */
  [data-testid="stChatMessageContent"] {
      width: 100% !important;
      flex: 1 1 auto !important;
      min-width: 0 !important;
  }
  [data-testid="stChatMessage"] [data-testid="stElementContainer"],
  [data-testid="stChatMessage"] [data-testid="stMarkdown"],
  [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"],
  [data-testid="stChatMessage"] ul,
  [data-testid="stChatMessage"] ol {
      width: 100% !important;
  }
  /* Only break a word when it would otherwise overflow (long CNP/IBAN/URL).
     `break-word` (not `anywhere`) leaves normal-text wrapping untouched, so a
     line never breaks early while there is still horizontal room. */
  [data-testid="stChatMessage"] p,
  [data-testid="stChatMessage"] li,
  [data-testid="stChatMessage"] code { overflow-wrap: break-word; }
  @media (min-width: 768px) {
      [data-testid="stSidebar"] { min-width: 300px; max-width: 300px; }
  }
  [data-testid="stSidebar"] [data-testid="stCaptionContainer"],
  [data-testid="stSidebar"] p { overflow-wrap: break-word; }
</style>
"""


# ---------------------------- rendering helpers ----------------------------

def _render_sidebar() -> None:
    with st.sidebar:
        st.header("Întrebări recente")
        if st.button("➕ Întrebare nouă", use_container_width=True):
            st.session_state.conversations.append(_new_conversation())
            st.session_state.active = len(st.session_state.conversations) - 1
            st.rerun()
        for i, conv in enumerate(st.session_state.conversations):
            label = conv["title"] if conv["title"] else "Întrebare nouă"
            prefix = "▶ " if i == st.session_state.active else "　"
            if st.button(
                f"{prefix}{label}", key=f"conv_{i}", use_container_width=True
            ):
                st.session_state.active = i
                st.rerun()
        st.divider()

        st.header("Surse")
        last_with_sources = next(
            (m for m in reversed(_conv()["history"]) if m.get("sources")),
            None,
        )
        if last_with_sources:
            cited = set(last_with_sources.get("cited", []))
            st.caption("★ = sursă citată în ultimul răspuns")
            for i, src in enumerate(last_with_sources["sources"], start=1):
                marker = "**★**" if i in cited else "·"
                st.markdown(f"{marker} **S{i}** — {src['breadcrumb']}")
                st.caption(src["url"])
        else:
            st.caption("Întreabă ceva pentru a vedea sursele citate.")

        st.divider()
        st.header("Formulare generate")
        pdfs = (
            sorted(
                FORMS_OUTPUT_DIR.glob("*.pdf"),
                key=lambda p: p.stat().st_mtime,
                reverse=True,
            )[:5]
            if FORMS_OUTPUT_DIR.exists()
            else []
        )
        if not pdfs:
            st.caption("Niciun formular generat încă.")
        for pdf in pdfs:
            with open(pdf, "rb") as f:
                st.download_button(
                    f"⬇ {pdf.name}",
                    f.read(),
                    file_name=pdf.name,
                    mime="application/pdf",
                    use_container_width=True,
                    key=f"sidebar_dl_{pdf}",
                )

        st.divider()
        st.caption(
            f"Model generare: `{DEFAULT_MODEL}`\n\n"
            "Regăsire: BAAI/bge-m3 + Chroma\n\n"
            "Contracte de ieșire: schemă Pydantic + reguli R1–R7"
        )


def _render_welcome() -> None:
    """Friendly empty state with one-click example prompts."""
    with st.container(border=True):
        st.markdown("#### 👋 Bun venit")
        st.markdown(
            "Pune o întrebare despre **naștere**, **căsătorie** sau **locuire**, "
            "ori cere-mi să îți **pre-completez un formular**. Răspunsurile sunt "
            "bazate pe surse citate din *cezicelegea.ro*."
        )
        st.caption("Încearcă un exemplu:")
        examples = [
            "Ce documente îmi trebuie pentru înregistrarea nașterii?",
            "Care este vârsta minimă pentru căsătorie?",
            "Vreau să completez declarația de căsătorie.",
        ]
        for j, ex in enumerate(examples):
            if st.button(ex, key=f"ex_{j}", use_container_width=True):
                _handle_question(ex)
                st.rerun()


def _render_history() -> None:
    for msg in _conv()["history"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("documents_mentioned"):
                items = "\n".join(f"- {d}" for d in msg["documents_mentioned"])
                st.markdown(f"**Documente menționate:**\n{items}")
            if msg.get("violations"):
                for v in msg["violations"]:
                    st.warning(f"[{v['rule_id']}] {v['message']}")


# ---------------------------- form flow ----------------------------

def _start_form(form_id: str) -> None:
    form_def = FORMS[form_id]
    _conv()["form_state"] = {
        "form_id": form_id,
        "accumulated": form_def.schema(),
        "llm_turns_used": 0,
        "mode": "llm",
    }


def _close_form() -> None:
    _conv()["form_state"] = None


def _render_collected(form_def: FormDef, accumulated) -> None:
    """Collected-fields view: Romanian labels, grouped by section, with a
    filled/empty marker per field."""
    with st.expander("Vezi câmpurile colectate", expanded=False):
        current_section = None
        for f in form_def.spec.fields:
            if f.section != current_section:
                current_section = f.section
                st.markdown(f"**{f.section}**")
            val = getattr(accumulated, f.name)
            mark = "✅" if val else "⬜"
            st.markdown(f"{mark} {f.label}: {val if val else '—'}")


def _render_manual_form(form_def: FormDef, fs: dict, problems: list[str]) -> None:
    """Field-by-field manual entry. Labels are the Romanian labels from the
    spec; fields are grouped by their section; format guidance comes from the
    schema field description."""
    st.markdown(
        "**Completare manuală** — introdu datele rămase. "
        "Sub fiecare câmp vezi formatul așteptat."
    )
    fmt = form_def.field_format_regex or {}
    # Iterate the spec in declaration order so sections stay grouped/ordered.
    remaining = [f for f in form_def.spec.fields if f.name in problems]
    by_name = {f.name: f for f in remaining}

    with st.form("manual_form"):
        new_values: dict[str, str] = {}
        current_section = None
        for f in remaining:
            if f.section != current_section:
                current_section = f.section
                st.markdown(f"##### {f.section}")
            info = form_def.schema.model_fields[f.name]
            new_values[f.name] = st.text_input(
                f.label,
                help=info.description,
                placeholder=_KIND_PLACEHOLDER.get(f.kind, ""),
                key=f"manual_{f.name}",
            )
        submitted = st.form_submit_button(
            "💾 Salvează datele", use_container_width=True
        )
    if submitted:
        for name, val in new_values.items():
            val = val.strip()
            if not val:
                continue
            field = by_name[name]
            if name in fmt and not fmt[name].match(val):
                example = _KIND_PLACEHOLDER.get(field.kind, "")
                st.error(
                    f"„{field.label}”: valoarea „{val}” nu are formatul corect"
                    + (f" ({example})." if example else ".")
                )
                continue
            setattr(fs["accumulated"], name, val)
        st.rerun()


def _render_form_block() -> None:
    fs = _conv()["form_state"]
    if not fs:
        return
    form_def = FORMS[fs["form_id"]]

    with st.container(border=True):
        st.subheader(f"📄 {form_def.display_name}")
        st.caption(form_def.description)

        all_fields = list(form_def.schema.model_fields)
        problems = problem_field_names(form_def, fs["accumulated"])
        filled = len(all_fields) - len(problems)
        st.progress(
            filled / len(all_fields),
            text=f"{filled} din {len(all_fields)} câmpuri completate",
        )

        _render_collected(form_def, fs["accumulated"])

        # Final state: complete and render PDF.
        errors = form_def.validate_fn(fs["accumulated"])
        if not errors:
            out_path = FORMS_OUTPUT_DIR / f"{form_def.form_id}.pdf"
            try:
                form_def.render_fn(fs["accumulated"], out_path)
            except Exception as e:  # pragma: no cover
                st.error(f"Eroare la generarea PDF-ului: {e}")
                return
            st.success("✅ Formular complet.")
            with open(out_path, "rb") as f:
                st.download_button(
                    "⬇ Descarcă PDF",
                    f.read(),
                    file_name=out_path.name,
                    mime="application/pdf",
                    use_container_width=True,
                    key="final_dl",
                )
            if st.button("Închide formular", key="close_form", use_container_width=True):
                _close_form()
                st.rerun()
            return

        # LLM extraction mode.
        if fs["mode"] == "llm" and fs["llm_turns_used"] < MAX_LLM_TURNS:
            st.markdown(
                f"**Completare asistată** — runda {fs['llm_turns_used'] + 1} din "
                f"{MAX_LLM_TURNS}. Scrie într-un singur mesaj tot ce știi; "
                "extrag automat câmpurile."
            )
            with st.form(f"llm_form_{fs['llm_turns_used']}", clear_on_submit=True):
                text = st.text_area(
                    "Datele tale:",
                    height=140,
                    placeholder=(
                        "Ex: Eu sunt Ion Popescu, CNP 1850412220011, locuiesc în "
                        "Str. Florilor 12, București. Buletinul meu: seria RT, nr "
                        "234567. ..."
                    ),
                )
                submitted = st.form_submit_button(
                    "✨ Extrage câmpurile", use_container_width=True
                )
            if st.button(
                "Trec la completarea manuală",
                key=f"to_manual_{fs['llm_turns_used']}",
                use_container_width=True,
            ):
                fs["mode"] = "manual"
                st.rerun()
            if submitted and text.strip():
                n_calls = expected_llm_calls(form_def)
                with st.spinner(
                    f"Extrag câmpurile din mesajul tău ({n_calls} apeluri LLM)…"
                ):
                    result = extract(text, form_def, accumulated=fs["accumulated"])
                fs["accumulated"] = result.form
                fs["llm_turns_used"] += 1
                if result.fields_extracted_this_turn:
                    st.toast(
                        f"Am extras: {', '.join(result.fields_extracted_this_turn)}",
                        icon="✅",
                    )
                else:
                    st.toast("Nu am putut extrage câmpuri noi.", icon="⚠️")
                st.rerun()
            return

        # Manual mode (LLM turns exhausted or user requested).
        fs["mode"] = "manual"
        _render_manual_form(form_def, fs, problems)


# ---------------------------- chat handler ----------------------------

def _prior_turns(history: list[dict]) -> list[dict]:
    """Last HISTORY_TURNS user/assistant messages as plain dialogue, for
    conversation context (drops per-message metadata)."""
    turns = [
        {"role": m["role"], "content": m["content"]}
        for m in history
        if m["role"] in ("user", "assistant")
    ]
    return turns[-HISTORY_TURNS * 2 :]


def _handle_question(question: str) -> None:
    conv = _conv()
    if not conv["history"]:  # title the conversation after its first question
        conv["title"] = (question[:32] + "…") if len(question) > 32 else question
    conv["history"].append({"role": "user", "content": question})

    # Capability/meta questions ("what forms can you fill?") are about the
    # assistant, not the corpus — answer deterministically, skip RAG.
    if detect_capability_intent(question):
        conv["history"].append(
            {"role": "assistant", "content": capability_answer()}
        )
        return

    prior = _prior_turns(conv["history"][:-1])  # exclude the just-added question
    retriever = get_retriever()
    with st.spinner("Caut surse…"):
        hits = retriever.query(question, k=4)
    with st.spinner("Generez răspunsul (verificat cu contracte de ieșire)…"):
        answer = generate(question, hits, history=prior)

    conv["history"].append(
        {
            "role": "assistant",
            "content": answer.text,
            "sources": [
                {
                    "breadcrumb": h.metadata.get("breadcrumb"),
                    "url": h.metadata.get("url"),
                }
                for h in hits
            ],
            "cited": list(answer.schema.cited_source_indices),
            "documents_mentioned": list(answer.schema.documents_mentioned),
            "violations": [
                {"rule_id": v.rule_id, "message": v.message} for v in answer.violations
            ],
        }
    )

    # Trigger form flow if intent detected (LLM-set OR keyword fallback).
    form_id = answer.schema.form_offer or detect_form_intent(question)
    if form_id and form_id in FORMS and conv["form_state"] is None:
        _start_form(form_id)


# ---------------------------- main ----------------------------

def main() -> None:
    st.set_page_config(
        page_title="Asistent administrație publică",
        layout="wide",
        page_icon="📄",
        initial_sidebar_state="collapsed",
    )
    _init_state()
    st.markdown(_CSS, unsafe_allow_html=True)

    st.title("Asistent pentru proceduri administrative")

    _render_sidebar()
    _render_history()
    _render_form_block()

    if not _conv()["history"] and _conv()["form_state"] is None:
        _render_welcome()

    if question := st.chat_input("Întreabă despre naștere, căsătorie sau locuire…"):
        _handle_question(question)
        st.rerun()


if __name__ == "__main__":
    main()
