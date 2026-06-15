"""Central registry of forms the assistant can fill in.

Built from the spec catalog in :mod:`licenta.forms`. The chat layer looks here
to (i) advertise forms when the user expresses form-filling intent, (ii) pick
the schema for LLM extraction, and (iii) pick the renderer once data is
collected.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from pydantic import BaseModel

from licenta.forms import (
    CATALOG,
    FormSpec,
    build_schema,
    field_format_regex,
    make_validator,
)
from licenta.prefill import render as render_pdf


@dataclass(frozen=True)
class FormDef:
    form_id: str
    display_name: str
    description: str
    spec: FormSpec
    schema: type[BaseModel]
    validate_fn: Callable[[BaseModel], list[str]]
    render_fn: Callable[[BaseModel, Path], Path]
    field_format_regex: dict[str, re.Pattern]
    trigger_action_keywords: tuple[str, ...] = ()
    trigger_topic_keywords: tuple[str, ...] = ()


def _build(spec: FormSpec) -> FormDef:
    return FormDef(
        form_id=spec.form_id,
        display_name=spec.display_name,
        description=spec.description,
        spec=spec,
        schema=build_schema(spec),
        validate_fn=make_validator(spec),
        render_fn=lambda data, out, _s=spec: render_pdf(_s, data, out),
        field_format_regex=field_format_regex(spec),
        trigger_action_keywords=spec.trigger_action_keywords,
        trigger_topic_keywords=spec.trigger_topic_keywords,
    )


FORMS: dict[str, FormDef] = {spec.form_id: _build(spec) for spec in CATALOG}


def form_catalog_for_prompt() -> str:
    """Renderable list of (form_id, description) for embedding into prompts."""
    return "\n".join(
        f"- {fid}: {d.display_name}. {d.description}" for fid, d in FORMS.items()
    )


# Phrases that signal a meta/capability question ("what can you do?", "what
# forms can you fill?"). These are about the assistant itself, not the
# cezicelegea.ro corpus, so they must be answered from the registry rather than
# routed to RAG (which would refuse — the corpus has no info about the bot).
def _fold(text: str) -> str:
    """Lowercase + strip diacritics, so matching is robust to ă/â/î/ș/ț and to
    users mixing diacritics inconsistently."""
    return (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )


# Stored diacritic-free; queries are folded before comparison.
_CAPABILITY_CUES = (
    "ce formulare", "care formulare", "ce documente poti", "ce poti completa",
    "ce poti face", "cu ce ma poti", "cu ce poti ajuta", "ce stii sa faci",
    "ce ajutor", "cum ma poti ajuta", "ce poti sa faci", "ce poti",
    "cu ce ajuti",
)


def detect_capability_intent(query: str) -> bool:
    """True if the user is asking what the assistant can do / which forms it
    can fill. Answered deterministically from the registry, not via RAG."""
    q = _fold(query)
    return any(cue in q for cue in _CAPABILITY_CUES)


def capability_answer() -> str:
    """User-facing description of capabilities, built from the registry so it
    never drifts from the actual catalog."""
    lines = [
        "Te pot ajuta cu două lucruri:",
        "",
        "1. **Întrebări despre proceduri** de naștere, căsătorie și locuire, "
        "cu răspunsuri bazate pe cezicelegea.ro și surse citate.",
        "2. **Pre-completarea următoarelor formulare** (generez un PDF semnabil):",
    ]
    for defn in FORMS.values():
        lines.append(f"   - **{defn.display_name}** — {defn.description}")
    lines.append("")
    lines.append(
        "Pentru a completa un formular, scrie de exemplu: "
        "„vreau să completez declarația de căsătorie”."
    )
    return "\n".join(lines)


def detect_form_intent(query: str) -> str | None:
    """Deterministic keyword-based intent detection. Used as a fallback when
    the LLM fails to set form_offer. A query matches a form if it contains at
    least one ACTION keyword and one TOPIC keyword of that form."""
    q = query.lower()
    for form_id, defn in FORMS.items():
        if not defn.trigger_action_keywords or not defn.trigger_topic_keywords:
            continue
        has_action = any(kw in q for kw in defn.trigger_action_keywords)
        has_topic = any(kw in q for kw in defn.trigger_topic_keywords)
        if has_action and has_topic:
            return form_id
    return None


def problem_field_names(form_def: FormDef, form: BaseModel) -> list[str]:
    """Field names that are missing (required) or fail format validation."""
    problems: list[str] = []
    fmt = form_def.field_format_regex or {}
    required = {f.name for f in form_def.spec.fields if f.required}
    for name in form_def.schema.model_fields:
        val = getattr(form, name)
        if not val:
            if name in required:
                problems.append(name)
            continue
        if name in fmt and not fmt[name].match(str(val)):
            problems.append(name)
    return problems
