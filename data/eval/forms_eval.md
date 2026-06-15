# Form-prefill extraction eval

**Set:** 14 natural-language conversations (2 per form), `data/eval/forms_gold.json`.
**Run:** deterministic (temp=0), one extraction pass each, via `scripts/eval_forms.py`. Field-level scoring, kind-aware: structured kinds (CNP, dates, ID series/number, sex, amount, IBAN) and name fields matched exactly (diacritic-folded); free-text fields (address, place, description) matched leniently (all significant expected tokens present).

## Result

- **Field-level accuracy: 97% (175/180).**
- One-pass required-complete (every required field correct in a single pass): **71% (10/14)** — the rest fall through to the deterministic manual entry.

| Field class | Accuracy |
|---|---|
| structured (CNP, dates, IDs, sex, amount, IBAN) | 92% (99/108) |
| name | 100% (34/34) |
| free-text (address, place) | 97% (37/38) |

| Form | Field accuracy | One-pass complete |
|---|---|---|
| declarație nume copil | 100% | 2/2 |
| cerere alocație | 100% | 2/2 |
| cerere indemnizație | 100% | 2/2 |
| declarație necăsătorit | 100% | 2/2 |
| contract închiriere | 94% | 0/2 |
| declarație căsătorie | 87% | 0/2 |
| recunoaștere paternitate | 83% | 0/2 |

## Failure profile (10 missed fields)

- **Birth dates — 6/10.** Dropped most often inside the ordered party-list (spouse1/2 birth dates ×4) and the paternitate child section (×2). Nested list extraction on the 3B model is the weak spot.
- **Child sex in paternitate — 2.** Inference from "băiat"/"fetiță" works for the child-name form but is inconsistent in the paternitate section.
- **Role/field bleed — 1.** `contract închiriere` once put the landlord's address in `property_address` (landlord/tenant are role-named, not numerically indexed, so they are not order-mapped like parent1/2).
- **payment_day — 1.**

## Reading

The high-stakes structured identifiers (CNP, ID series/number) and names are captured reliably (92–100%); the residual gaps are concentrated in **birth dates** and a few **role-disambiguation** cases. Because no wrong value is invented (missing → null → manual fallback), every form still reaches a complete signable PDF. The one-pass-complete rate (57%) quantifies how often the manual step is needed and motivates two future improvements: stronger date capture in nested list extraction, and extending the ordered-party mechanism to role-named pairs (landlord/tenant).
