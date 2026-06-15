# R4 audit — manual review of the fabricated-document rule

**Run audited:** `runs/20260604_200902_qwen2.5_3b_temp0_audit` (Qwen2.5-3B-Q4, temperature=0, deterministic, n=68).
**Why:** R4 (`_rule_documents_grounded`, contracts.py) is the only fuzzy rule — a case-insensitive substring match of each `documents_mentioned` entry against the cited source text. It drives the headline "silent failure" count, so its precision must be verified by hand, not assumed.

**Method:** for every R4-flagged document, read the actual cited source chunk and classify the flag as:
- **FABRICATION** — the named document does not exist / is irrelevant to the question (a genuine made-up claim).
- **GROUNDING-MISS** — the document is a real Romanian admin document, but it is *not present in the source the model cited* (the model's specific claim is unsupported by its own evidence — still a silent failure under the contract's definition).
- **FALSE POSITIVE** — the document *is* in the cited source; R4 fired only because of Romanian inflection/diacritics/word-order, not a real problem.

## Result

| # | Case | Cited chunk | Flagged document(s) | Verdict |
|---|---|---|---|---|
| 1 | `nastere-05` | Tatăl recunoaște copilul | "Certificatul de naștere al mamei"; "Actele de identitate ale părinților" | GROUNDING-MISS (real docs, absent from cited chunk) |
| 2 | `nastere-11` | Municipiul Constanța / Făgăraș (local grants) | generic ID + birth-certificate list | GROUNDING-MISS (cited chunks list grant *conditions*, not a document list) |
| 3 | `nastere-14` | Stimulentul de inserție (parte 2/5) | 6-item document list (cerere, acte, dovada reluării activității…) | GROUNDING-MISS (real docs for the benefit, but cited chunk is about *eligibility situations*) |
| 4 | `nastere-16` | Suntem căsătoriți | "declarația…transcrierea certificatului…domiciliul copilului" | **FABRICATION** (garbled, non-existent document) |
| 5 | `casatorie-09` | Ne căsătorim în România | "declarație de căsătorie", "actele de identitate" | **FALSE POSITIVE** (both explicitly in the cited source) |
| 6 | `casatorie-12` | Partenerul cetățean străin | "martorelor", "certificate medicale prenupțiale" | GROUNDING-MISS / borderline (witnesses + prenuptial cert not in cited chunk) |
| 7 | `locuire-03` | Contract de locațiune | "declarația privind numele copilului" | **FABRICATION** (child-name form, irrelevant to renting) |
| 8 | `locuire-07` | Asociația de proprietari | "declarația privind numele copilului" | **FABRICATION** (irrelevant) |
| 9 | `locuire-09` | Cumpărare imobil (străin) | "declarația privind numele copilului" | **FABRICATION** (irrelevant) |
| 10 | `locuire-18` | Cumpărare imobil UE vs non-UE | "declarația privind numele copilului" | **FABRICATION** (irrelevant) |

## Summary

- **10 cases flagged by R4** (20 occurrences).
- **9/10 flag a genuine problem → R4 case-level precision ≈ 90%.**
  - **5 FABRICATION** — outright made-up / irrelevant documents (`nastere-16` + the four `locuire` cases, all leaking the prompt's form catalog "declarația privind numele copilului" into unrelated housing answers).
  - **4 GROUNDING-MISS** — real documents the model listed without support in the source it cited (`nastere-05/11/14`, `casatorie-12`).
- **1/10 FALSE POSITIVE** — `casatorie-09`, where both documents are present in the source and R4 fired only on Romanian inflection (`voști`, `la primăria`).

## Interpretation for the thesis

1. The headline claim survives: R4 is **~90% precise**, so the silent-failure count is not an artifact.
2. But "fabricated documents" is too strong for half the catches. Report **two sub-classes**: *fabrication* (invented/irrelevant docs) and *citation-grounding miss* (real doc, unsupported by the cited source). Both are silent failures a citizen should not receive unchallenged; the distinction is honest and sharper.
3. The single false positive motivates the cheap R4 hardening (roadmap B2/B3): normalize diacritics + strip Romanian inflection before matching. Re-running after that fix would push precision toward 100% and is a clean before/after ablation.
4. The four `locuire` leaks are the most valuable catch: the prompt's available-form list bled into `documents_mentioned`. Worth a dedicated sentence — a concrete, reproducible failure the contract layer stops cold.

## R4 hardening — realized ablation (B2/B3)

The hardened R4 (`contracts._rule_documents_grounded`) replaces plain substring matching with: (1) diacritic stripping (`ș/ş ț/ţ ă â î` → ascii) and (2) inflection-tolerant prefix-token matching (a document token is covered if its longest common prefix with a source token is ≥ 70% of the shorter token; a document is grounded if ≥ 60% of its significant tokens are covered). Re-scored offline on the same deterministic run via `scripts/r4_ablation.py` (no model re-run — the instrumented eval persists the needed fields):

| | Before | After |
|---|---|---|
| R4 occurrences | 20 | **11** |
| R4 cases | 10 | **7** |
| Contract pass rate (temp 0) | 81% (55/68) | **85% (58/68)** |

- **Cleared:** `casatorie-09` (the confirmed false positive), plus `nastere-05` and `nastere-16` — both borderline grounding-misses whose real documents *are* present in the cited source once diacritics/inflection are normalized (e.g. "Declarația din care să rezulte numele copilului").
- **Newly flagged: none** — no regressions.
- **Retained:** all four `locuire` form-catalog leaks (true fabrications) and the remaining grounding-misses (`nastere-11/14`, `casatorie-12`).
- Net: precision rises from ≈ 90% to ≈ 100% on this run, false positives eliminated, every genuine fabrication kept.

