# Manual faithfulness sample — triangulating lexical keyword recall

**Run:** `runs/20260604_200902_qwen2.5_3b_temp0_audit` (3B, temp=0).
**Why:** lexical keyword recall (36% on 3B) is an exact-substring lower bound — it ignores synonyms/paraphrase and penalizes correct-but-terse answers. To see what it actually measures, 15 non-refusal answers (5 per event) were hand-scored against their cited sources: **correct** (fully grounded + complete), **partial** (right topic, incomplete or role/detail confusion), **wrong** (ungrounded or substantively incorrect).

| Case | Verdict | Note |
|---|---|---|
| nastere-01 | correct | document list matches source exactly |
| nastere-02 | correct | issuer of medical certificate, grounded |
| nastere-03 | **wrong** | retrieval miss (cited embassy chunk); answer generic + "Ministerul Public" irrelevant |
| nastere-05 | partial | mostly grounded; "certificat de naștere al mamei" not in cited chunk |
| nastere-06 | correct | private-clinic certificate, grounded |
| casatorie-01 | partial | "18 ani" omits the 16-with-consent exception in source |
| casatorie-02 | partial | correct conclusion (same-sex banned) but garbled, conflated reasoning |
| casatorie-06 | partial | explains kinship degrees but buries the actual prohibition |
| casatorie-09 | partial | documents grounded; phrasing noisy |
| casatorie-11 | **wrong** | no citation (R2), recommends docs incl. invented "certificat de căsătoreanța" |
| locuire-01 | partial | "find the property" — misses the notar step the source stresses |
| locuire-02 | **wrong** | cited the *seller's* documents chunk; buyer question under-answered |
| locuire-03 | correct | rental-contract contents, grounded |
| locuire-05 | partial | conflates owner/tenant obligations |
| locuire-06 | **wrong** | lists tenant *obligations* as tenant *rights*; rights/obligations + role confusion |

## Result (n=15)

- **Correct: 4 (27%)**, **Partial: 7 (47%)**, **Wrong: 4 (27%)**.
- The 36% lexical recall is consistent with this: it sits between the fully-correct rate (27%) and the partially-grounded rate, confirming it is a **noisy lower bound**, not a literal "36% correct."
- The recurring real failure on 3B is not fabrication but **role/relation confusion** (owner↔tenant, rights↔obligations) and **retrieval misses** that the model answers anyway. Two of the four "wrong" cases are retrieval-grounded failures the contract layer does *not* catch (the answer cites a real but wrong-topic chunk) — reinforcing that contracts catch fabrication, while topical mis-grounding and over-refusal remain open.

## For the thesis

Report this as a one-paragraph triangulation under the metrics: lexical recall understates quality (many "partial" answers are useful and mostly grounded) but the hand-scored correct rate (27%) confirms 3B answer quality is mediocre and motivates the larger model / better retrieval. Honest, cheap, and avoids over-claiming the 36%.
