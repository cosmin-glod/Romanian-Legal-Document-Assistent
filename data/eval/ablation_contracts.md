# A5 — true contracts-OFF vs contracts-ON ablation

**Run:** deterministic (temp=0), current pipeline (hardened R4, R7 active), n=68, via `scripts/ablation_contracts.py`. Per case we record the *first-attempt* violations (what would be served with the layer OFF) and the *post-retry* violations (what the layer ON does), from `generate().first_attempt_violations` vs `.violations`.

Definitions:
- **Contracts OFF** = serve the first model answer as-is.
- **Contracts ON** = retry once on violation; if still invalid, **withhold** (controlled refusal).

## Result (evaluated set R1–R6; R7 reported separately as a detector)

| Regime | Served clean | Served flawed | Withheld |
|---|---|---|---|
| **Fără contracte (OFF)** | 27 | **41 (60%)** | 0 |
| **Cu contracte (ON)** | 58 | **0** | 10 |

- OFF flawed = 41: **37 are only *missing citations* (R2)** — unverifiable, content possibly fine — plus 4 with a content/other issue (R6×3, R1×1).
- The retry loop **repairs 31** of the 41 (mostly by adding the missing citations).
- ON **withholds 10** cases: R4 fabrication (11 occurrences) + residual R2 (3). Zero flawed answers reach the citizen.

## Key finding: missing citations mask fabrication

On the first attempt, ungrounded-document fabrication (R4) is **invisible**, because R4 only runs when citations exist and 41/68 first answers have none (R2). The retry adds citations — and only then can R4 detect that the listed documents are not in the cited sources, exposing **10 fabrication cases** that the layer then withholds. R2 + retry is therefore a *prerequisite* for R4: traceability must be enforced before grounding can be checked. This is a structural argument for the contract layer beyond the per-rule counts.

## Honest framing

"60% served flawed without the layer" is dominated by *unverifiable* (uncited) answers, not wrong content; we report the split explicitly. The strong claim the ablation supports is narrower and cleaner: **with the layer, every served answer is cited and grounded, and 10/68 latent fabrications are withheld rather than served as authoritative — at the cost of 10 controlled refusals.**
