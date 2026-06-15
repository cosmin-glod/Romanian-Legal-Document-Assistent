# Raport evaluare

**Model**: `qwen2.5:3b-instruct-q4_K_M`
**k (chunks regăsite)**: 4
**Total întrebări evaluate**: 5

## Metrici globale

- Refusal accuracy: **80%** (4/5)
- Breadcrumb recall@4 (excl. refusal cases): **100%** (3/3)
- Keyword coverage (cazuri non-refusal): **33%** (3 cazuri)
- Contract pass rate (R1..R6): **80%** (4/5)
- Latency medie: **47.3s** per întrebare

## Pe categorie

| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |
|---|---|---|---|---|---|
| casatorie | 1 | 0% | 100% | 100% | 24.9s |
| locuire | 2 | 100% | 100% | 100% | 21.8s |
| nastere | 2 | 100% | 100% | 50% | 84.0s |

## Pe dificultate

| Dificultate | N | Refusal corect | Recall@k | Contract valid |
|---|---|---|---|---|
| easy | 5 | 80% | 100% | 80% |

## Distribuția violărilor de contract

- `R2_UNCITED`: 1

## Cazuri cu probleme (2)


### smoke-nastere-01 — nastere / easy
**Întrebare**: Ce documente îmi trebuie pentru înregistrarea nașterii copilului meu, dacă sunt căsătorit cu partenera?
**Răspuns**: Nașterea copilului este înregistrată la Stare Civilă. Documentele necesare sunt:
- Actele de identitate ale tale și ale partenerului/partenerei
- Certificatul medical constatator al nașterii care trebuie să poarte număr de înregistrare, dat…
**Status**: recall=True · refusal_correct=True · contract_valid=False
**Violations**: ['R2_UNCITED']
**Top breadcrumbs**: ['Nașterea > Suntem căsătoriți', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Tatăl recunoaște copilul', 'Nașterea > Suntem căsătoriți']

### smoke-casatorie-01 — casatorie / easy
**Întrebare**: Pot să mă căsătoresc la 16 ani?
**Răspuns**: Nu am suficiente informații în sursele disponibile pentru a răspunde.
**Status**: recall=True · refusal_correct=False · contract_valid=True
**Top breadcrumbs**: ['Căsătoria > Condiții pentru a te căsători > 📌 Vârsta minimă pentru căsătorie', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate', 'Căsătoria > Ne căsătorim în străinătate']
