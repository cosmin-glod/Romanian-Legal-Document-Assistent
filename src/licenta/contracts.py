"""Output contracts for the RAG answer.

Implements the verification layer that KES_2026 (Gheorghe et al., 2026) names
as future work: explicit checks on the LLM output beyond "did the model say
something." The LLM emits a typed JSON schema; post-hoc rules then catch
silent failures (invalid citations, fabricated documents, missing refusals)
that traditional refusal-tuning leaves undetected.

The schema is fed to Ollama as a JSON-mode constraint, so the model is forced
to emit structurally valid JSON. The rules below run on the parsed structure.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel, Field

from licenta.retriever import Hit

# R4 matching tolerances. A document name counts as grounded when at least
# DOC_COVERAGE_MIN of its significant tokens are matched in the cited sources,
# where a token matches if its longest common prefix with a source token is at
# least TOKEN_PREFIX_MIN of the shorter token's length. The prefix rule absorbs
# Romanian inflection (declarație/declarația, primăria/primăriei) and the
# diacritic-stripping absorbs ș/ş, ț/ţ, ă, â, î — the two failure modes that
# made the older plain-substring R4 over-flag (see data/eval/r4_audit.md).
TOKEN_PREFIX_MIN = 0.7
DOC_COVERAGE_MIN = 0.6
_MIN_DOC_LEN = 6  # skip short/generic document names entirely


def _normalize(text: str) -> str:
    """Lowercase, strip diacritics, keep alphanumerics + spaces."""
    stripped = (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    return re.sub(r"[^a-z0-9 ]", " ", stripped)


def _significant_tokens(text: str) -> list[str]:
    return [t for t in _normalize(text).split() if len(t) > 3]


def _token_matches(tok: str, source_tokens: set[str]) -> bool:
    for s in source_tokens:
        shorter = min(len(tok), len(s))
        # longest common prefix
        lcp = 0
        for a, b in zip(tok, s):
            if a != b:
                break
            lcp += 1
        if shorter and lcp / shorter >= TOKEN_PREFIX_MIN:
            return True
    return False


def _document_is_grounded(doc: str, source_tokens: set[str]) -> bool:
    doc_tokens = _significant_tokens(doc)
    if not doc_tokens:
        return True  # nothing substantive to verify
    covered = sum(1 for t in doc_tokens if _token_matches(t, source_tokens))
    return covered / len(doc_tokens) >= DOC_COVERAGE_MIN


class AnswerSchema(BaseModel):
    """What the LLM must emit. Used as JSON-schema constraint for Ollama."""

    answer_text: str = Field(
        description="Răspunsul în limba română, concis și clar."
    )
    is_refusal: bool = Field(
        description=(
            "True doar dacă SURSELE nu conțin informații suficiente "
            "pentru a răspunde. Altfel false."
        )
    )
    cited_source_indices: list[int] = Field(
        default_factory=list,
        description=(
            "Indicii surselor citate (1-indexed). Listă goală doar dacă "
            "is_refusal este true."
        ),
    )
    documents_mentioned: list[str] = Field(
        default_factory=list,
        description=(
            "Lista exactă a documentelor administrative menționate în "
            "răspuns (ex: 'certificat medical constatator al nașterii'). "
            "Listă goală dacă nu se menționează niciun document."
        ),
    )
    form_offer: str | None = Field(
        default=None,
        description=(
            "Dacă utilizatorul cere ajutor pentru a completa un formular "
            "administrativ, setează aici id-ul formularului din lista "
            "disponibilă (ex: 'declaratie_nume_copil'). În toate celelalte "
            "cazuri lasă null."
        ),
    )


@dataclass(frozen=True)
class Violation:
    rule_id: str
    message: str


# -------- validation rules --------

def _rule_answer_present(ans: AnswerSchema) -> list[Violation]:
    if not ans.answer_text.strip():
        return [Violation("R1_EMPTY", "Câmpul answer_text este gol.")]
    return []


def _rule_refusal_or_citations(ans: AnswerSchema) -> list[Violation]:
    if not ans.is_refusal and not ans.cited_source_indices:
        return [
            Violation(
                "R2_UNCITED",
                "Răspuns afirmativ fără nicio citație. Trebuie cel puțin o sursă.",
            )
        ]
    return []


def _rule_citation_indices_valid(
    ans: AnswerSchema, sources: list[Hit]
) -> list[Violation]:
    n = len(sources)
    out: list[Violation] = []
    for idx in ans.cited_source_indices:
        if not (1 <= idx <= n):
            out.append(
                Violation(
                    "R3_BAD_CITATION",
                    f"Citație [S{idx}] invalidă; surse disponibile: [S1..S{n}].",
                )
            )
    return out


def _rule_documents_grounded(
    ans: AnswerSchema, sources: list[Hit]
) -> list[Violation]:
    """Each named document should appear (case-insensitive substring) in at
    least one of the cited sources. Catches the most visible fabrication
    failure mode for this domain."""
    if not ans.documents_mentioned or not ans.cited_source_indices:
        return []
    n = len(sources)
    cited_text = " ".join(
        sources[i - 1].text
        for i in ans.cited_source_indices
        if 1 <= i <= n
    )
    source_tokens = set(_significant_tokens(cited_text))
    out: list[Violation] = []
    for doc in ans.documents_mentioned:
        if len(doc.strip()) < _MIN_DOC_LEN:  # skip short/generic names
            continue
        if not _document_is_grounded(doc, source_tokens):
            out.append(
                Violation(
                    "R4_FABRICATED_DOC",
                    f"Document '{doc}' nu apare în sursele citate.",
                )
            )
    return out


def _rule_refusal_has_no_docs(ans: AnswerSchema) -> list[Violation]:
    """When the model refuses, it cannot mention documents — there are no
    cited sources to ground them. Catches a fabrication mode that R4
    misses because R4 short-circuits when there are no citations."""
    if ans.is_refusal and ans.documents_mentioned:
        return [
            Violation(
                "R5_REFUSAL_WITH_DOCS",
                f"Răspuns de tip refuz, dar documents_mentioned nu este gol: "
                f"{ans.documents_mentioned}. Documentele trebuie eliminate.",
            )
        ]
    return []


def _rule_no_form_ids_in_docs(
    ans: AnswerSchema, form_ids: set[str]
) -> list[Violation]:
    """documents_mentioned is for document NAMES, not internal form_ids. If a
    form_id leaks in there, it's a confusion bug — flag it."""
    if not ans.documents_mentioned:
        return []
    out: list[Violation] = []
    for doc in ans.documents_mentioned:
        if doc.strip().lower() in form_ids:
            out.append(
                Violation(
                    "R6_FORM_ID_IN_DOCS",
                    f"'{doc}' este un id de formular, nu un nume de document. "
                    f"Trebuie pus în form_offer, nu în documents_mentioned.",
                )
            )
    return out


# R7 threshold: a refusal is suspect when the top retrieved source has cosine
# similarity at or above this value — empirically the answer was usually present.
# Calibrated on the gold set: 0.64 separates spurious refusals (answer present,
# top1 up to 0.799) from correct out-of-domain refusals (top1 up to 0.630),
# catching 16/21 spurious refusals with zero false positives on the 10 correct
# refusals (see data/eval/r7_calibration.md). This is the only rule that targets
# the dominant, otherwise contract-invisible failure mode: over-refusal.
R7_OVERREFUSAL_SCORE = 0.64


def _rule_no_over_refusal(
    ans: AnswerSchema, sources: list[Hit]
) -> list[Violation]:
    """Flag a refusal that is contradicted by a high-similarity retrieved
    source. A clean refusal otherwise passes R1--R6; R7 makes the contract
    layer aware of over-refusal, the dominant failure mode. On violation the
    generator retries with feedback, giving the model a chance to answer."""
    if not ans.is_refusal or not sources:
        return []
    best = max(range(len(sources)), key=lambda i: sources[i].score)
    top = sources[best].score
    if top >= R7_OVERREFUSAL_SCORE:
        # Name the specific source so the retry knows which [S#] to read —
        # a generic "re-read the sources" recovers far less on a small model.
        return [
            Violation(
                "R7_OVERREFUSAL",
                f"Ai refuzat, dar sursa [S{best + 1}] are similaritate {top:.2f} "
                f"(prag {R7_OVERREFUSAL_SCORE}) cu întrebarea. Citește [S{best + 1}] "
                f"și răspunde din ea dacă informația există; refuză doar dacă "
                f"subiectul lipsește complet din SURSE.",
            )
        ]
    return []


def validate(answer: AnswerSchema, sources: list[Hit]) -> list[Violation]:
    # Imported here to avoid circular import at module load.
    from licenta.form_registry import FORMS

    form_ids = {fid.lower() for fid in FORMS}
    violations: list[Violation] = []
    violations.extend(_rule_answer_present(answer))
    violations.extend(_rule_refusal_or_citations(answer))
    violations.extend(_rule_citation_indices_valid(answer, sources))
    violations.extend(_rule_documents_grounded(answer, sources))
    violations.extend(_rule_refusal_has_no_docs(answer))
    violations.extend(_rule_no_form_ids_in_docs(answer, form_ids))
    violations.extend(_rule_no_over_refusal(answer, sources))
    return violations


def violations_to_feedback(violations: list[Violation]) -> str:
    """Render violations as a Romanian message for retry."""
    lines = ["Răspunsul anterior a încălcat următoarele reguli:"]
    for v in violations:
        lines.append(f"- [{v.rule_id}] {v.message}")
    lines.append(
        "Te rog reformulează răspunsul respectând regulile. "
        "Folosește doar informații prezente în SURSE."
    )
    return "\n".join(lines)


def schema_for_ollama() -> dict[str, Any]:
    """JSON schema in a form Ollama accepts via the `format` param."""
    return AnswerSchema.model_json_schema()
