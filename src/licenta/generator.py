"""Generator: question + retrieved chunks → validated answer.

Pipeline per turn:
  1. Build system + user messages with sources numbered [S1..Sn].
  2. Call Ollama with JSON-schema constraint (AnswerSchema).
  3. Parse JSON; validate against post-hoc rules in contracts.py.
  4. If violations and retries remain, append violation feedback and retry.
  5. Return final Answer with any unresolved violations attached.

The schema-constrained call + post-hoc validation together implement the
output contract that KES_2026 names as future work.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field

import ollama
from pydantic import ValidationError

from licenta.contracts import (
    AnswerSchema,
    Violation,
    schema_for_ollama,
    validate,
    violations_to_feedback,
)
from licenta.form_registry import form_catalog_for_prompt
from licenta.retriever import Hit

# Override via env (e.g. LICENTA_MODEL=qwen2.5:3b-instruct-q8_0 for the recommended
# deploy config). Default stays Q4 — the config used by the local mechanism analyses.
DEFAULT_MODEL = os.environ.get("LICENTA_MODEL", "qwen2.5:3b-instruct-q4_K_M")

# Hard cap on generated tokens. The JSON-schema grammar lets a model ramble
# inside a string field until the context limit (runaway -> truncated -> invalid
# JSON, see _call_model). Real answers fit well under this; the cap bounds the
# runaway tail (mean latency was dominated by a few 100k-char generations).
MAX_OUTPUT_TOKENS = int(os.environ.get("LICENTA_NUM_PREDICT", "1024"))

SYSTEM_PROMPT_TEMPLATE = """Ești un asistent care ajută cetățenii români să înțeleagă proceduri administrative (naștere, căsătorie, locuire).

Reguli stricte:
1. Răspunzi DOAR în limba română.
2. Te bazezi EXCLUSIV pe SURSE. Nu inventa documente, termene, instituții sau cifre.
3. Citează sursele prin indici (ex: surse 1 și 3 → cited_source_indices=[1, 3]).
4. Dacă SURSELE nu conțin răspunsul, setează is_refusal=true și răspunde: "Nu am suficiente informații în sursele disponibile pentru a răspunde."
5. În câmpul documents_mentioned, listează DOAR nume reale de documente administrative care apar explicit în SURSE și pe care le menționezi în răspuns (ex: „certificat medical constatator al nașterii", „carte de identitate"). NU pune aici id-uri de formulare (ex: „declaratie_nume_copil") — acelea aparțin câmpului form_offer. Dacă is_refusal este true, lasă documents_mentioned gol.
6. Răspunsul trebuie să fie concis, structurat și ușor de înțeles.

Formulare disponibile pentru pre-completare:
{forms_catalog}

7. Câmpul form_offer este INDEPENDENT de is_refusal și de surse. Se setează doar pe baza intenției utilizatorului, nu pe baza informațiilor din surse.
   - Dacă utilizatorul cere explicit ajutor pentru a COMPLETA, PREGĂTI sau GENERA un formular sau o declarație din lista de mai sus — exemple: „vreau să completez declarația privind numele copilului", „ajută-mă să fac declarația", „pregătește-mi formularul", „cum o pre-completăm?" — setează form_offer la id-ul corespunzător din listă (ex: "declaratie_nume_copil"). Setează-l chiar dacă is_refusal=true.
   - În toate celelalte cazuri (informare, întrebări despre documente, întrebări despre proceduri) lasă form_offer null.

Format de ieșire: JSON valid conform schemei AnswerSchema."""


def _build_system_prompt() -> str:
    return SYSTEM_PROMPT_TEMPLATE.format(forms_catalog=form_catalog_for_prompt())


SYSTEM_PROMPT = _build_system_prompt()

USER_TEMPLATE = """SURSE:
{sources}

ÎNTREBARE: {question}"""

log = logging.getLogger(__name__)


# Few-shot exemplars, passed as prior turns. They demonstrate the three
# behaviors the 3B most often gets wrong: (1) ANSWER when the sources contain
# the information, even partially (anti over-refusal); (2) refuse cleanly when
# the topic is absent; (3) populate documents_mentioned only with real document
# names from the sources. Each assistant turn is a valid AnswerSchema JSON.
FEW_SHOT: list[dict] = [
    {
        "role": "user",
        "content": (
            "SURSE:\n[S1] [Căsătoria > Condiții pentru a te căsători > Vârsta "
            "minimă] Amândoi trebuie să aveți minim 18 ani. Ca excepție, te poți "
            "căsători de la 16 ani, cu aviz medical și încuviințarea părinților.\n\n"
            "ÎNTREBARE: Care este vârsta minimă pentru căsătorie?"
        ),
    },
    {
        "role": "assistant",
        "content": (
            '{"answer_text": "Vârsta minimă este 18 ani. Ca excepție, te poți '
            'căsători de la 16 ani, cu aviz medical și încuviințarea părinților.", '
            '"is_refusal": false, "cited_source_indices": [1], '
            '"documents_mentioned": [], "form_offer": null}'
        ),
    },
    {
        "role": "user",
        "content": (
            "SURSE:\n[S1] [Nașterea > Am domiciliul în România] Pentru a "
            "înregistra nașterea, ai nevoie de certificatul medical constatator "
            "al nașterii și de actele de identitate ale părinților.\n\n"
            "ÎNTREBARE: Ce documente îmi trebuie pentru înregistrarea nașterii?"
        ),
    },
    {
        "role": "assistant",
        "content": (
            '{"answer_text": "Ai nevoie de certificatul medical constatator al '
            'nașterii și de actele de identitate ale părinților.", '
            '"is_refusal": false, "cited_source_indices": [1], '
            '"documents_mentioned": ["certificat medical constatator al nașterii", '
            '"carte de identitate"], "form_offer": null}'
        ),
    },
    {
        "role": "user",
        "content": (
            "SURSE:\n[S1] [Locuire > Despre contractul de locațiune] Contractul "
            "de închiriere nu trebuie încheiat în fața unui notar; este suficient "
            "un contract scris și semnat de ambele părți.\n\n"
            "ÎNTREBARE: Cum îmi reînnoiesc pașaportul?"
        ),
    },
    {
        "role": "assistant",
        "content": (
            '{"answer_text": "Nu am suficiente informații în sursele disponibile '
            'pentru a răspunde.", "is_refusal": true, "cited_source_indices": [], '
            '"documents_mentioned": [], "form_offer": null}'
        ),
    },
]


@dataclass
class Answer:
    schema: AnswerSchema
    sources: list[Hit]
    model: str
    violations: list[Violation] = field(default_factory=list)
    attempts: int = 1
    # Violations of the FIRST model attempt, before any retry. Lets an ablation
    # compare "contracts off" (serve the first answer as-is) vs "contracts on"
    # (retry on violation, withhold if still invalid).
    first_attempt_violations: list[Violation] = field(default_factory=list)
    # Diagnostics for runaway / malformed generations (see _call_model). A model
    # can ramble inside the JSON string field until truncation -> invalid JSON.
    # These are recorded so the failure is auditable instead of silently becoming
    # a refusal.
    parse_failures: int = 0          # nr. de încercări cu JSON invalid (parse eșuat)
    forced_refusal: bool = False     # refuz produs din parse eșuat, nu din decizia modelului
    max_raw_chars: int = 0           # lungimea celei mai lungi ieșiri brute (semnalează runaway)

    @property
    def text(self) -> str:
        return self.schema.answer_text

    @property
    def valid(self) -> bool:
        return not self.violations


def _format_sources(hits: list[Hit]) -> str:
    return "\n\n".join(f"[S{i}] {h.text}" for i, h in enumerate(hits, 1))


def _refusal(
    model: str,
    sources: list[Hit],
    parse_failures: int = 0,
    forced: bool = False,
    max_raw_chars: int = 0,
) -> Answer:
    return Answer(
        schema=AnswerSchema(
            answer_text="Nu am suficiente informații în sursele disponibile pentru a răspunde.",
            is_refusal=True,
            cited_source_indices=[],
            documents_mentioned=[],
        ),
        sources=sources,
        model=model,
        parse_failures=parse_failures,
        forced_refusal=forced,
        max_raw_chars=max_raw_chars,
    )


def _call_model(
    messages: list[dict], model: str, temperature: float
) -> tuple[AnswerSchema | None, int]:
    """Returns (parsed schema or None, length of the raw output in characters).
    The length is reported on success and on failure so the caller can flag
    runaway generations (very long output truncated into invalid JSON)."""
    resp = ollama.chat(
        model=model,
        messages=messages,
        format=schema_for_ollama(),
        options={"temperature": temperature, "num_predict": MAX_OUTPUT_TOKENS},
    )
    raw = resp["message"]["content"]
    try:
        return AnswerSchema.model_validate_json(raw), len(raw)
    except ValidationError as e:
        log.warning("schema parse failed (raw_len=%d): %s; raw=%r", len(raw), e, raw[:300])
        return None, len(raw)


def generate(
    question: str,
    hits: list[Hit],
    model: str = DEFAULT_MODEL,
    temperature: float = 0.2,
    max_retries: int = 1,
    system_prompt: str = SYSTEM_PROMPT,
    history: list[dict] | None = None,
) -> Answer:
    """`history` is an optional list of prior turns ({"role","content"}) so the
    model can resolve follow-up questions ("și la căsătorie?"). Grounding rules
    still apply: the answer must come from the SOURCES of the current turn."""
    if not hits:
        return _refusal(model, [])

    base_user = USER_TEMPLATE.format(
        sources=_format_sources(hits), question=question.strip()
    )
    messages: list[dict] = [{"role": "system", "content": system_prompt}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": base_user})

    first_violations: list[Violation] = []
    parse_failures = 0
    max_raw = 0
    for attempt in range(1, max_retries + 2):
        log.info("attempt %d: model=%s sources=%d", attempt, model, len(hits))
        parsed, raw_len = _call_model(messages, model, temperature)
        max_raw = max(max_raw, raw_len)
        if parsed is None:
            parse_failures += 1
            if attempt <= max_retries:
                messages.append(
                    {
                        "role": "user",
                        "content": "Răspunsul nu a fost JSON valid. Reformulează respectând schema AnswerSchema.",
                    }
                )
                continue
            return _refusal(
                model, hits, parse_failures=parse_failures,
                forced=True, max_raw_chars=max_raw,
            )

        violations = validate(parsed, hits)
        if attempt == 1:
            first_violations = violations
        if not violations:
            return Answer(
                schema=parsed, sources=hits, model=model, attempts=attempt,
                first_attempt_violations=first_violations,
                parse_failures=parse_failures, max_raw_chars=max_raw,
            )

        log.info("attempt %d: %d violation(s)", attempt, len(violations))
        if attempt <= max_retries:
            messages.append(
                {"role": "assistant", "content": parsed.model_dump_json()}
            )
            messages.append(
                {"role": "user", "content": violations_to_feedback(violations)}
            )
            continue

        return Answer(
            schema=parsed,
            sources=hits,
            model=model,
            violations=violations,
            attempts=attempt,
            first_attempt_violations=first_violations,
            parse_failures=parse_failures,
            max_raw_chars=max_raw,
        )

    return _refusal(
        model, hits, parse_failures=parse_failures,
        forced=parse_failures > 0, max_raw_chars=max_raw,
    )
