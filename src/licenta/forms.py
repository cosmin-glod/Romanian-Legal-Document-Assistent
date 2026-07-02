"""Spec-driven form engine + the catalog of supported forms.

Each form is declared once as a :class:`FormSpec` (a list of typed
:class:`Field`s grouped into sections, a PDF body template, and trigger
keywords). From that single spec we derive:

- a Pydantic schema (all fields optional ``str`` — extraction must be free to
  leave a field null rather than invent a value);
- a post-hoc validator (required-field + per-kind format checks);
- a per-field format-regex map (used by the extractor to reject malformed
  values at merge time);
- a PDF renderer (see :mod:`licenta.prefill`);
- a section-based extractor (see :mod:`licenta.extractor`).

This mirrors the output-contract pattern: the schema constrains structure,
post-hoc rules verify semantics. Adding a form is data, not code.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field as dfield
from datetime import date, datetime

from pydantic import BaseModel, Field as PydField, create_model

# ---------------------------- field kinds ----------------------------

# kind -> compiled format regex (absent kind = free text, no format check)
_KIND_REGEX: dict[str, re.Pattern] = {
    # First digit is the sex/century marker (1-9); 0 is never assigned.
    "cnp": re.compile(r"^[1-9]\d{12}$"),
    "id_series": re.compile(r"^[A-Z]{2}$"),
    "id_number": re.compile(r"^\d{6}$"),
    "date": re.compile(r"^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"),
    "sex": re.compile(r"^[MF]$"),
    "iban": re.compile(r"^RO\d{2}[A-Za-z0-9]{16,30}$"),
    "amount": re.compile(r"^\d+([.,]\d{1,2})?$"),
    "int": re.compile(r"^\d+$"),
}

# kind -> hint appended to the field description (guides the LLM extractor)
_KIND_HINT: dict[str, str] = {
    "cnp": "CNP, exact 13 cifre, fără spații.",
    "id_series": "Seria CI: EXACT 2 litere mari (ex: RT).",
    "id_number": "Numărul CI: EXACT 6 cifre.",
    "date": "Format ZZ.LL.AAAA (zi.lună.an).",
    "sex": "'M' (masculin) sau 'F' (feminin). Deduce din context: fiu/băiat/băiețel/soț=M, fiică/fată/fetiță/soție=F.",
    "iban": "IBAN românesc (începe cu RO).",
    "amount": "Sumă în RON, doar cifre (ex: 1500 sau 1500.50).",
    "int": "Număr întreg.",
}


@dataclass(frozen=True)
class Field:
    name: str
    label: str
    kind: str = "text"
    section: str = "Detalii"
    required: bool = True


@dataclass(frozen=True)
class FormSpec:
    form_id: str
    display_name: str
    description: str
    title: str  # PDF heading
    subtitle: str  # PDF sub-heading
    fields: tuple[Field, ...]
    body: str  # PDF prose, {field_name} placeholders
    signatures: tuple[str, ...]
    trigger_action_keywords: tuple[str, ...]
    trigger_topic_keywords: tuple[str, ...]


# ---------------------------- derived artifacts ----------------------------

def submodel(name: str, fields: list[Field] | tuple[Field, ...]) -> type[BaseModel]:
    """Dynamic Pydantic model from a list of fields (all ``str | None``)."""
    definitions: dict = {}
    for f in fields:
        hint = _KIND_HINT.get(f.kind, "")
        desc = f"{f.label}." + (f" {hint}" if hint else "")
        definitions[f.name] = (str | None, PydField(default=None, description=desc))
    return create_model(name, **definitions)  # type: ignore[call-overload]


def build_schema(spec: FormSpec) -> type[BaseModel]:
    """Dynamic Pydantic model for the whole form (every field ``str | None``)."""
    return submodel(spec.form_id, spec.fields)


def field_format_regex(spec: FormSpec) -> dict[str, re.Pattern]:
    return {f.name: _KIND_REGEX[f.kind] for f in spec.fields if f.kind in _KIND_REGEX}


def make_validator(spec: FormSpec):
    """Return a ``form -> list[str]`` validator: required-present + format."""
    regexes = field_format_regex(spec)
    required = [(f.name, f.label) for f in spec.fields if f.required]

    def validate(form: BaseModel) -> list[str]:
        errors: list[str] = []
        for name, label in required:
            if not getattr(form, name, None):
                errors.append(f"Lipsă: {label} (câmpul {name}).")
        for name, rx in regexes.items():
            val = getattr(form, name, None)
            if val and not rx.match(str(val)):
                errors.append(f"Format invalid pentru {name}: '{val}'.")
        return errors

    return validate


def sections_of(spec: FormSpec) -> dict[str, list[Field]]:
    """Fields grouped by section, preserving declaration order."""
    out: dict[str, list[Field]] = {}
    for f in spec.fields:
        out.setdefault(f.section, []).append(f)
    return out


class _SafeDict(dict):
    def __missing__(self, key: str) -> str:  # noqa: D401
        return "____"


def render_body(spec: FormSpec, values: dict[str, str | None]) -> str:
    clean = {k: (v if v else "____") for k, v in values.items()}
    return spec.body.format_map(_SafeDict(clean))


def parse_declaration_date(value: str) -> date:
    return datetime.strptime(value, "%d.%m.%Y").date()


# ============================ THE CATALOG ============================

def _party(prefix: str, label: str, section: str, *, with_birth: bool = False
           ) -> tuple[Field, ...]:
    fields = [
        Field(f"{prefix}_full_name", f"Numele complet ({label})", "text", section),
        Field(f"{prefix}_cnp", f"CNP ({label})", "cnp", section),
        Field(f"{prefix}_address", f"Adresa de domiciliu ({label})", "text", section),
        Field(f"{prefix}_id_series", f"Seria CI ({label})", "id_series", section),
        Field(f"{prefix}_id_number", f"Numărul CI ({label})", "id_number", section),
    ]
    if with_birth:
        fields.append(Field(f"{prefix}_birth_date", f"Data nașterii ({label})",
                            "date", section))
    return tuple(fields)


_META = (
    Field("declaration_date", "Data declarației", "date", "Detalii declarație"),
    Field("declaration_place", "Locul declarației", "text", "Detalii declarație"),
)

# Shared action verbs that signal form-filling intent (paired with each form's
# topic keywords in detect_form_intent).
_ACTIONS: tuple[str, ...] = (
    "completez", "completam", "completăm", "precompletez", "completeaza",
    "completează", "fac", "facem", "pregatesc", "pregătesc", "pregatim",
    "pregătim", "pregateste", "pregătește", "generez", "generam", "generăm",
    "genereaza", "generează", "ajuta", "ajută", "vreau", "doresc",
)


CATALOG: tuple[FormSpec, ...] = (
    # ---------------- NAȘTERE ----------------
    FormSpec(
        form_id="declaratie_nume_copil",
        display_name="Declarație privind numele copilului",
        description=(
            "Declarație prin care părinții cu nume de familie diferite declară ce "
            "nume va purta copilul. Necesară la înregistrarea nașterii."
        ),
        title="DECLARAȚIE",
        subtitle="privind numele pe care îl va purta copilul",
        fields=(
            *_party("parent1", "primul părinte", "Primul părinte"),
            *_party("parent2", "al doilea părinte", "Al doilea părinte"),
            Field("child_given_name", "Prenumele copilului", "text", "Copilul"),
            Field("child_sex", "Sexul copilului", "sex", "Copilul"),
            Field("declared_family_name", "Numele de familie declarat", "text", "Copilul"),
            *_META,
        ),
        body=(
            "Subsemnații {parent1_full_name}, CNP {parent1_cnp}, domiciliat(ă) în "
            "{parent1_address}, CI seria {parent1_id_series} nr. {parent1_id_number}, "
            "și {parent2_full_name}, CNP {parent2_cnp}, domiciliat(ă) în "
            "{parent2_address}, CI seria {parent2_id_series} nr. {parent2_id_number}, "
            "în calitate de părinți,\n\n"
            "declarăm pe propria răspundere că prenumele copilului nostru este "
            "«{child_given_name}», iar numele de familie pe care îl va purta este "
            "«{declared_family_name}».\n\n"
            "Declarație dată în temeiul Codului Civil și al legislației privind "
            "starea civilă."
        ),
        signatures=("Semnătura părinte 1", "Semnătura părinte 2"),
        trigger_action_keywords=_ACTIONS,
        trigger_topic_keywords=(
            "nume copil", "numele copilului", "declaratie nume", "declarația numelui",
            "numele copilului",
        ),
    ),
    FormSpec(
        form_id="recunoastere_paternitate",
        display_name="Declarație de recunoaștere a copilului",
        description=(
            "Declarație prin care tatăl recunoaște un copil născut în afara "
            "căsătoriei, dată în fața ofițerului de stare civilă sau a notarului."
        ),
        title="DECLARAȚIE DE RECUNOAȘTERE",
        subtitle="a copilului din afara căsătoriei",
        fields=(
            *_party("father", "tatăl", "Tatăl"),
            Field("mother_full_name", "Numele complet (mama)", "text", "Mama"),
            Field("mother_cnp", "CNP (mama)", "cnp", "Mama"),
            Field("child_full_name", "Numele copilului", "text", "Copilul"),
            Field("child_sex", "Sexul copilului", "sex", "Copilul"),
            Field("child_birth_date", "Data nașterii copilului", "date", "Copilul"),
            *_META,
        ),
        body=(
            "Subsemnatul {father_full_name}, CNP {father_cnp}, domiciliat în "
            "{father_address}, CI seria {father_id_series} nr. {father_id_number}, "
            "declar pe propria răspundere că recunosc copilul {child_full_name}, "
            "de sex {child_sex}, născut la data de {child_birth_date}, "
            "având ca mamă pe {mother_full_name}, CNP {mother_cnp}.\n\n"
            "Recunosc că sunt tatăl acestui copil și sunt de acord cu stabilirea "
            "filiației față de mine."
        ),
        signatures=("Semnătura tatălui", "Semnătura mamei"),
        trigger_action_keywords=_ACTIONS,
        trigger_topic_keywords=(
            "recunoastere", "recunoaștere", "recunosc", "paternitate",
            "tatal recunoaste", "tatăl recunoaște",
        ),
    ),
    FormSpec(
        form_id="cerere_alocatie_copil",
        display_name="Cerere pentru alocația de stat pentru copii",
        description=(
            "Cerere pentru acordarea alocației de stat pentru copii, depusă de "
            "unul dintre părinți după înregistrarea nașterii."
        ),
        title="CERERE",
        subtitle="pentru acordarea alocației de stat pentru copii",
        fields=(
            *_party("applicant", "solicitant", "Solicitant"),
            Field("child_full_name", "Numele copilului", "text", "Copilul"),
            Field("child_cnp", "CNP (copil)", "cnp", "Copilul"),
            Field("child_birth_date", "Data nașterii copilului", "date", "Copilul"),
            Field("iban", "Cont bancar (IBAN)", "iban", "Cont bancar"),
            *_META,
        ),
        body=(
            "Subsemnatul {applicant_full_name}, CNP {applicant_cnp}, domiciliat în "
            "{applicant_address}, CI seria {applicant_id_series} nr. "
            "{applicant_id_number}, solicit acordarea alocației de stat pentru "
            "copilul {child_full_name}, CNP {child_cnp}, născut la data de "
            "{child_birth_date}.\n\n"
            "Solicit virarea alocației în contul IBAN {iban}."
        ),
        signatures=("Semnătura solicitantului",),
        trigger_action_keywords=_ACTIONS,
        trigger_topic_keywords=("alocatie", "alocația", "alocatia", "alocație"),
    ),
    FormSpec(
        form_id="cerere_indemnizatie_crestere",
        display_name="Cerere pentru indemnizația de creștere a copilului",
        description=(
            "Cerere pentru indemnizația lunară de creștere a copilului, depusă de "
            "părintele aflat în concediu de creștere."
        ),
        title="CERERE",
        subtitle="pentru indemnizația de creștere a copilului",
        fields=(
            *_party("parent", "părinte", "Părinte solicitant"),
            Field("employer", "Angajatorul / sursa de venit", "text", "Venit"),
            Field("child_full_name", "Numele copilului", "text", "Copilul"),
            Field("child_cnp", "CNP (copil)", "cnp", "Copilul"),
            Field("child_birth_date", "Data nașterii copilului", "date", "Copilul"),
            Field("iban", "Cont bancar (IBAN)", "iban", "Cont bancar"),
            *_META,
        ),
        body=(
            "Subsemnatul {parent_full_name}, CNP {parent_cnp}, domiciliat în "
            "{parent_address}, CI seria {parent_id_series} nr. {parent_id_number}, "
            "angajat la {employer}, solicit acordarea indemnizației de creștere a "
            "copilului {child_full_name}, CNP {child_cnp}, născut la data de "
            "{child_birth_date}.\n\n"
            "Solicit virarea indemnizației în contul IBAN {iban}."
        ),
        signatures=("Semnătura solicitantului",),
        trigger_action_keywords=_ACTIONS,
        trigger_topic_keywords=(
            "indemnizatie", "indemnizația", "indemnizatia", "concediu crestere",
            "concediu creștere", "crestere copil", "creștere copil",
        ),
    ),
    # ---------------- CĂSĂTORIE ----------------
    FormSpec(
        form_id="declaratie_casatorie",
        display_name="Declarație de căsătorie",
        description=(
            "Declarația de căsătorie depusă la primărie de viitorii soți înainte "
            "de oficierea căsătoriei."
        ),
        title="DECLARAȚIE DE CĂSĂTORIE",
        subtitle="depusă în vederea încheierii căsătoriei",
        fields=(
            *_party("spouse1", "primul viitor soț", "Primul viitor soț",
                    with_birth=True),
            *_party("spouse2", "al doilea viitor soț", "Al doilea viitor soț",
                    with_birth=True),
            Field("family_name_after", "Numele de familie după căsătorie", "text",
                  "Numele după căsătorie"),
            *_META,
        ),
        body=(
            "Subsemnații {spouse1_full_name}, CNP {spouse1_cnp}, născut(ă) la "
            "{spouse1_birth_date}, domiciliat(ă) în {spouse1_address}, CI seria "
            "{spouse1_id_series} nr. {spouse1_id_number}, și {spouse2_full_name}, "
            "CNP {spouse2_cnp}, născut(ă) la {spouse2_birth_date}, domiciliat(ă) în "
            "{spouse2_address}, CI seria {spouse2_id_series} nr. {spouse2_id_number}, "
            "declarăm că dorim să încheiem căsătoria și că nu există impedimente "
            "legale.\n\n"
            "Numele de familie pe care îl vom purta după căsătorie este "
            "«{family_name_after}»."
        ),
        signatures=("Semnătura primului soț", "Semnătura celui de-al doilea soț"),
        trigger_action_keywords=_ACTIONS,
        trigger_topic_keywords=(
            "casatorie", "căsătorie", "casatoresc", "căsătoresc",
            "declaratie de casatorie", "ma casatoresc", "mă căsătoresc",
        ),
    ),
    FormSpec(
        form_id="declaratie_necasatorit",
        display_name="Declarație privind starea civilă (necăsătorit)",
        description=(
            "Declarație pe propria răspundere că persoana nu a mai fost căsătorită "
            "și nu există impedimente la căsătorie."
        ),
        title="DECLARAȚIE PE PROPRIA RĂSPUNDERE",
        subtitle="privind starea civilă",
        fields=(
            *_party("declarant", "declarant", "Declarant"),
            *_META,
        ),
        body=(
            "Subsemnatul {declarant_full_name}, CNP {declarant_cnp}, domiciliat în "
            "{declarant_address}, CI seria {declarant_id_series} nr. "
            "{declarant_id_number}, declar pe propria răspundere, cunoscând "
            "prevederile legii penale privind falsul în declarații, că nu am mai "
            "fost căsătorit(ă) și că nu există impedimente legale pentru încheierea "
            "căsătoriei."
        ),
        signatures=("Semnătura declarantului",),
        trigger_action_keywords=_ACTIONS,
        trigger_topic_keywords=(
            "necasatorit", "necăsătorit", "starea civila", "starea civilă",
            "propria raspundere", "celibat",
        ),
    ),
    # ---------------- LOCUIRE ----------------
    FormSpec(
        form_id="contract_inchiriere",
        display_name="Contract de închiriere (locațiune)",
        description=(
            "Model de contract de închiriere între proprietar (locator) și chiriaș "
            "(locatar) pentru un imobil."
        ),
        title="CONTRACT DE ÎNCHIRIERE",
        subtitle="(contract de locațiune)",
        fields=(
            *_party("landlord", "proprietar", "Proprietar (locator)"),
            *_party("tenant", "chiriaș", "Chiriaș (locatar)"),
            Field("property_address", "Adresa imobilului", "text", "Imobil"),
            Field("property_description", "Descrierea imobilului", "textarea",
                  "Imobil", required=False),
            Field("rent_amount", "Chiria lunară (RON)", "amount", "Condiții"),
            Field("payment_day", "Ziua plății chiriei", "int", "Condiții"),
            Field("deposit_amount", "Garanția (RON)", "amount", "Condiții"),
            Field("duration_months", "Durata (luni)", "int", "Condiții"),
            Field("start_date", "Data începerii", "date", "Condiții"),
            *_META,
        ),
        body=(
            "Între {landlord_full_name}, CNP {landlord_cnp}, domiciliat în "
            "{landlord_address}, CI seria {landlord_id_series} nr. "
            "{landlord_id_number}, în calitate de LOCATOR, și {tenant_full_name}, "
            "CNP {tenant_cnp}, domiciliat în {tenant_address}, CI seria "
            "{tenant_id_series} nr. {tenant_id_number}, în calitate de LOCATAR, se "
            "încheie prezentul contract de închiriere.\n\n"
            "Obiectul contractului este imobilul situat în {property_address} "
            "({property_description}).\n\n"
            "Chiria lunară este de {rent_amount} RON, plătibilă în ziua "
            "{payment_day} a fiecărei luni. Garanția este de {deposit_amount} RON. "
            "Contractul se încheie pe o durată de {duration_months} luni, începând "
            "cu data de {start_date}."
        ),
        signatures=("Semnătura locatorului", "Semnătura locatarului"),
        trigger_action_keywords=_ACTIONS,
        trigger_topic_keywords=(
            "inchiriere", "închiriere", "inchiriez", "închiriez", "chirie",
            "locatiune", "locațiune", "contract de inchiriere", "contract de chirie",
        ),
    ),
)
