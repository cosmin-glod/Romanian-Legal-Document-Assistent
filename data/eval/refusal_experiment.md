# D2 experiment — can prompt calibration fix spurious refusals?

**Motivation.** On the deterministic 3B run, 21 cases are spurious refusals (in-domain question, answer present, but model refused), and **19 of 21 had the answer already retrieved** — i.e. this is a *generation/calibration* failure, not a retrieval one. Intent-aware retrieval (C1) would touch at most 2 of 21; the right lever is the refusal instruction itself.

**Setup.** Targeted, deterministic (temp=0), via `scripts/refusal_experiment.py`. Re-generate only with a **refusal-calibrated** system prompt (rule 4 rewritten: *answer whenever the sources contain the information, even partially; refuse only if the topic is entirely absent; when in doubt with a relevant source, answer*). Baseline `is_refusal` is reused from the stored run. Two subsets:
- **spurious** (n=21, `should_refuse=false` but refused) — want these to flip to a grounded answer;
- **control** (n=12, `should_refuse=true`, out-of-domain) — must stay refused.

## Result

| Subset | Baseline correct | Refined correct | Δ |
|---|---|---|---|
| Spurious (recover = answer) | 0/21 | 5/21 | **+5** |
| Control (keep refusing) | 10/12 | 9/12 | **−1** |
| Combined refusal accuracy | 10/33 | **14/33** | **+4** |

- **Recovered (5):** `casatorie-05`, `-08`, `-10`, `-14`, `-15`. Of these, `casatorie-14` returns an *empty* answer (degenerate, would be caught by R1), so **genuine recoveries ≈ 4**; the rest are grounded answers about post-marriage name options.
- **Broken (1):** `casatorie-19` ("Cum divorțez?", out-of-domain) flipped refuse→answer — a fabrication the contract layer (R2/R4) would still flag.

## Interpretation

- Prompt calibration is a **partial lever**: it recovers ~20% of spurious refusals at the cost of one correct refusal. Net positive on refusal accuracy, but not a clean win.
- Because 19/21 spurious refusals already had the answer retrieved and prompting recovers only ~4, the dominant failure is largely a **model-calibration limit of the 3B**, not a prompt bug — consistent with the 7B halving the spurious rate. This argues for (a) model scale and (b) an explicit **R7 over-refusal rule** that flags `is_refusal=true` when a high-similarity source was retrieved, rather than relying on the prompt alone.
- The calibrated prompt is **not adopted as default**: trading a correct refusal for recoveries weakens the refusal guarantee the contract layer depends on. It is reported as a probe.
