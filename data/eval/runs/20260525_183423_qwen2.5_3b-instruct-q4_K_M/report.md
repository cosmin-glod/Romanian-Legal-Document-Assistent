# Raport evaluare

**Model**: `qwen2.5:3b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 3

## Metrici globale

- Refusal accuracy: **100%** (3/3)
- Breadcrumb recall@4 (excl. refusal cases): **33%** (1/3)
- Keyword coverage (cazuri non-refusal): **50%** (3 cazuri)
- Contract pass rate (R1..R6): **67%** (2/3)
- Latency medie: **54.2s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| nastere | 3 | 100% | 33% | 67% | 54.2s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 3 | 100% | 33% | 67% |

## Distribuția violărilor de contract

- `R4_FABRICATED_DOC`: 1

## Cazuri cu probleme (3)


### nastere-01 — nastere / easy
**Întrebare**: Ce documente îmi trebuie pentru înregistrarea nașterii copilului meu, dacă sunt căsătorit cu partenera?
**Răspuns**: Nașterea copilului este înregistrată la Stare Civilă atât dacă părinții sunt căsătoriți, cât și dacă sunt recunoașteți de un alt părinte. Documentele necesare pentru înregistrarea nașterii sunt următoarele:

1. Actele de identitate ale tale…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R4_FABRICATED_DOC']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### nastere-02 — nastere / easy
**Întrebare**: Cine eliberează certificatul medical constatator al nașterii?
**Răspuns**: Certificatul medical constatator al nașterii este eliberați de medicul care a asistat la naștere sau de medicul șef de secție de obstetrică-ginecologie.
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate', 'Nașterea > Am domiciliul în România', 'Nașterea > Am domiciliul în străinătate']

### nastere-03 — nastere / easy
**Întrebare**: Unde se înregistrează nașterea copilului meu dacă a fost născut într-un spital în România?
**Răspuns**: Nașterea unui copil care a fost născut într-un spital în România se poate înregistra la Primaria unde locuiește părinții sau la Serviciul de Stare Civil al acesteia. Poți consulta lista completă a primariilor și serviciilor de stare civil d…
**Status**: recall=False · refusal_correct=True · contract_valid=True
**Top breadcrumbs**: ['Nașterea > Vreau să înregistrez nașterea la ambasadă', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Vreau să înregistrez nașterea la ambasada țării mele de origine', 'Nașterea > Suntem căsătoriți']
