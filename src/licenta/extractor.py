"""LLM-powered form-field extraction (spec-driven, section-based).

The form's fields are partitioned into thematic sections (declared in the
:class:`~licenta.forms.FormSpec`). Each section is extracted with a small
sub-schema (typically 3–6 fields), then mapped back onto the flat form. Small
quantized models (Qwen2.5-3B-Q4) drop fields when a single schema has many
slots; per-section sub-schemas keep extraction stable.

State is carried across user turns by merging non-null extracted fields into an
accumulated form. The merge rejects values that fail the per-field format regex,
preventing bad LLM guesses (e.g. a CNP in an id-number slot) from polluting
accumulated state.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

import ollama
from pydantic import BaseModel, Field as PydField, ValidationError, create_model

import os

from licenta.forms import Field, sections_of, submodel
from licenta.form_registry import FormDef

DEFAULT_MODEL = os.environ.get("LICENTA_MODEL", "qwen2.5:3b-instruct-q4_K_M")

log = logging.getLogger(__name__)


# ---- deterministic date harvest (fills date fields the LLM drops) ----

_RO_MONTHS = {
    "ianuarie": 1, "februarie": 2, "martie": 3, "aprilie": 4, "mai": 5,
    "iunie": 6, "iulie": 7, "august": 8, "septembrie": 9, "octombrie": 10,
    "noiembrie": 11, "decembrie": 12,
}
_DATE_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_DATE_DMY = re.compile(r"\b(\d{1,2})[./](\d{1,2})[./](\d{4})\b")
_DATE_TEXT = re.compile(
    r"\b(\d{1,2})\s+(" + "|".join(_RO_MONTHS) + r")\s+(\d{4})\b", re.IGNORECASE
)


def _dates_in_text(text: str) -> list[str]:
    """All dates in appearance order, normalized to YYYY-MM-DD."""
    found: list[tuple[int, str]] = []
    for m in _DATE_ISO.finditer(text):
        found.append((m.start(), f"{m[1]}-{m[2]}-{m[3]}"))
    for m in _DATE_DMY.finditer(text):
        found.append((m.start(), f"{int(m[3]):04d}-{int(m[2]):02d}-{int(m[1]):02d}"))
    for m in _DATE_TEXT.finditer(text):
        mo = _RO_MONTHS[m[2].lower()]
        found.append((m.start(), f"{int(m[3]):04d}-{mo:02d}-{int(m[1]):02d}"))
    seen: set[str] = set()
    out: list[str] = []
    for _, d in sorted(found):
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out


_SEX_M = re.compile(r"\b(b[ăa]iat|b[ăa]ie[țt]el|fiu(?:l)?|masculin)\b", re.IGNORECASE)
_SEX_F = re.compile(r"\b(fat[ăa]|fiic[ăa]|feti[țt][ăa]|feminin)\b", re.IGNORECASE)
_DAY = re.compile(r"\b(?:ziua|data|pe data)\s+(\d{1,2})\b(?!\s*[./-])", re.IGNORECASE)


def _fill_missing_deterministic(
    form_def: FormDef, form: BaseModel, text: str
) -> list[str]:
    """Fill date/sex/day fields the LLM dropped, via regex on the raw text.
    Best-effort, in field order; values still pass the format validator."""
    changed: list[str] = []

    # dates — usually in the same order as the date fields
    empty_dates = [
        f.name for f in form_def.spec.fields
        if f.kind == "date" and not getattr(form, f.name, None)
    ]
    for name, value in zip(empty_dates, _dates_in_text(text)):
        setattr(form, name, value)
        changed.append(name)

    # sex — infer a single value from gendered child/person words
    sex = "M" if _SEX_M.search(text) else ("F" if _SEX_F.search(text) else None)
    if sex:
        for f in form_def.spec.fields:
            if f.kind == "sex" and not getattr(form, f.name, None):
                setattr(form, f.name, sex)
                changed.append(f.name)

    # payment day — int fields whose name mentions a day
    days = _DAY.findall(text)
    if days:
        day_fields = [
            f.name for f in form_def.spec.fields
            if f.kind == "int" and "day" in f.name and not getattr(form, f.name, None)
        ]
        for name, value in zip(day_fields, days):
            setattr(form, name, value)
            changed.append(name)

    return changed


@dataclass
class ExtractionResult:
    form: BaseModel
    errors: list[str]
    fields_extracted_this_turn: list[str]

    @property
    def is_complete(self) -> bool:
        return not self.errors


SECTION_PROMPT = """Extrage din textul utilizatorului datele pentru secțiunea „{section}" a formularului „{form}".

Reguli stricte:
1. Lasă un câmp NULL dacă utilizatorul nu l-a furnizat. NU inventa nume, CNP-uri, adrese sau sume.
2. Respectă formatul indicat în descrierea fiecărui câmp (CNP 13 cifre; seria CI 2 litere mari; numărul CI 6 cifre; date YYYY-MM-DD; sume doar cifre).
3. Nu pune valori de tip „necunoscut", „TBD" sau ghilimele goale — lasă null.
4. Extrage datele calendaristice care apar („născut la", „din data de", „azi") în format YYYY-MM-DD.
5. Pentru sex, deduce din context: „fiu/băiat/băiețel" = M, „fiică/fată/fetiță" = F.

Câmpuri de extras:
{field_list}

Format de ieșire: JSON valid conform schemei furnizate."""


def _call_with_schema(
    system: str,
    user_text: str,
    schema: type[BaseModel],
    model: str,
    temperature: float = 0.1,
) -> BaseModel:
    resp = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_text.strip()},
        ],
        format=schema.model_json_schema(),
        options={"temperature": temperature},
    )
    raw = resp["message"]["content"]
    try:
        return schema.model_validate_json(raw)
    except ValidationError as e:
        log.warning("extraction parse failed: %s; raw=%r", e, raw[:300])
        return schema()


def _merge(
    accumulated: BaseModel,
    new: BaseModel,
    field_format_regex: dict | None = None,
) -> tuple[BaseModel, list[str]]:
    """Copy non-null, non-empty fields from new into accumulated. Returns
    (updated_form, changed_field_names). Values failing a per-field format
    regex are rejected so the LLM's bad-format guesses don't persist."""
    merged = accumulated.model_copy()
    changed: list[str] = []
    for name in type(accumulated).model_fields:
        if not hasattr(new, name):
            continue
        new_val = getattr(new, name)
        if new_val is None or new_val == "":
            continue
        if field_format_regex and name in field_format_regex:
            if not field_format_regex[name].match(str(new_val)):
                log.info("rejected %s=%r (failed format regex)", name, new_val)
                continue
        if new_val != getattr(merged, name):
            setattr(merged, name, new_val)
            changed.append(name)
    return merged, changed


# Fields named like ``spouse1_full_name`` form an ordered "party group": the
# numeric suffix encodes appearance order. Small models reliably extract a LIST
# of people in order but conflate two parallel sub-schemas (parent1 vs parent2),
# so we extract such groups as one ordered list and map element i -> prefix i+1.
_PARTY_RE = re.compile(r"^(?P<base>[a-z]+?)(?P<idx>\d+)_(?P<suffix>.+)$")

PARTIES_PROMPT = """Extrage TOATE persoanele menționate în text, în ORDINEA apariției, pentru formularul „{form}". Fiecare persoană este un element în lista parties.

Pentru FIECARE persoană completează toate câmpurile care apar în text:
{field_list}

Reguli stricte:
- Prima persoană = cea care vorbește la persoana I („eu", „subsemnatul", „mă numesc").
- A doua persoană = „soția mea" / „soțul meu" / „partenerul" / „celălalt" / „chiriașul".
- Lasă null orice câmp care nu apare. NU inventa.
- CNP: exact 13 cifre. Data nașterii: format YYYY-MM-DD (extrage-o dacă apare „născut(ă) la").
- Seria CI are EXACT 2 litere; numărul CI are EXACT 6 cifre. NICIODATĂ nu le combina.

EXEMPLE buletin:
- „seria CJ, nr 234567" → id_series='CJ', id_number='234567'
- „CI seria BX 123456" → id_series='BX', id_number='123456'
- „buletinul RT 789012" → id_series='RT', id_number='789012'"""


def _party_groups(fields) -> dict[str, dict[int, dict[str, Field]]]:
    groups: dict[str, dict[int, dict[str, Field]]] = {}
    for f in fields:
        m = _PARTY_RE.match(f.name)
        if m:
            base, idx, suffix = m["base"], int(m["idx"]), m["suffix"]
            groups.setdefault(base, {}).setdefault(idx, {})[suffix] = f
    return {b: idxs for b, idxs in groups.items() if len(idxs) >= 2}


def _extract_party_group(
    user_text: str, base: str, idxs: dict[int, dict[str, Field]],
    form: str, model: str,
) -> dict[str, str]:
    # Union of suffixes (use the lowest index's fields for labels/kinds).
    first = idxs[min(idxs)]
    party_fields = [
        Field(suffix, fld.label, fld.kind, "party") for suffix, fld in first.items()
    ]
    item = submodel(f"{base}_party_item", party_fields)
    wrapper = create_model(
        f"{base}_party_list",
        parties=(list[item], PydField(default_factory=list)),  # type: ignore[valid-type]
    )
    field_list = "\n".join(f"- {f.name}: {f.label}" for f in party_fields)
    parsed = _call_with_schema(
        PARTIES_PROMPT.format(form=form, field_list=field_list), user_text, wrapper, model
    )
    updates: dict[str, str] = {}
    ordered_idx = sorted(idxs)
    for pos, party in enumerate(getattr(parsed, "parties", [])):
        if pos >= len(ordered_idx):
            break
        prefix_idx = ordered_idx[pos]
        for suffix in idxs[prefix_idx]:
            val = getattr(party, suffix, None)
            if val:
                updates[f"{base}{prefix_idx}_{suffix}"] = val
    return updates


def expected_llm_calls(form_def: FormDef) -> int:
    """How many LLM calls one extraction pass makes: one per ordered party
    group + one per section that still has non-party fields. Lets the UI show
    an accurate estimate instead of a hardcoded number."""
    spec = form_def.spec
    groups = _party_groups(spec.fields)
    grouped = {
        f"{base}{idx}_{suffix}"
        for base, idxs in groups.items()
        for idx, sfx in idxs.items()
        for suffix in sfx
    }
    calls = len(groups)
    for _section, fields in sections_of(spec).items():
        if any(f.name not in grouped for f in fields):
            calls += 1
    return calls


def extract(
    user_text: str,
    form_def: FormDef,
    accumulated: BaseModel | None = None,
    model: str = DEFAULT_MODEL,
) -> ExtractionResult:
    """Section-based extraction for any form. Numeric party groups (parent1/
    parent2, spouse1/spouse2) are extracted as an ordered list to preserve who
    is who; remaining fields are extracted per section. New non-null fields are
    merged into `accumulated` (created empty if None)."""
    if accumulated is None:
        accumulated = form_def.schema()

    spec = form_def.spec
    groups = _party_groups(spec.fields)
    grouped_names = {
        f"{base}{idx}_{suffix}"
        for base, idxs in groups.items()
        for idx, sfx in idxs.items()
        for suffix in sfx
    }
    updates: dict[str, str] = {}

    # 1) ordered party groups
    for base, idxs in groups.items():
        updates.update(
            _extract_party_group(user_text, base, idxs, spec.display_name, model)
        )

    # 2) remaining fields, per section
    for section, fields in sections_of(spec).items():
        rest = [f for f in fields if f.name not in grouped_names]
        if not rest:
            continue
        sub = submodel(f"{spec.form_id}__{section}", rest)
        field_list = "\n".join(f"- {f.name}: {f.label}" for f in rest)
        prompt = SECTION_PROMPT.format(
            section=section, form=spec.display_name, field_list=field_list
        )
        parsed = _call_with_schema(prompt, user_text, sub, model)
        for f in rest:
            val = getattr(parsed, f.name, None)
            if val:
                updates[f.name] = val

    diff = form_def.schema(**updates)
    merged, changed = _merge(accumulated, diff, form_def.field_format_regex)
    # Deterministic fallback for date/sex/day fields the LLM dropped.
    changed += _fill_missing_deterministic(form_def, merged, user_text)
    return ExtractionResult(
        form=merged,
        errors=form_def.validate_fn(merged),
        fields_extracted_this_turn=changed,
    )
