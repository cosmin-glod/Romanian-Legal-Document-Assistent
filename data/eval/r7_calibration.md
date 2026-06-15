# R7 calibration — over-refusal detection rule

**Idea.** A clean refusal passes R1–R6, so the contract layer is blind to over-refusal — the dominant failure (34% on 3B, §spurious refusal). R7 makes it visible: flag `is_refusal=true` when the top retrieved source's cosine similarity is at or above a threshold, because empirically the answer was then present.

**Calibration data.** Top-1 retrieval similarity per gold case (k=4, BGE-M3), grouped by outcome on the deterministic 3B run:

| Group | n | top-1 min | median | max |
|---|---|---|---|---|
| Spurious refusal (refused, answer present) | 21 | 0.564 | 0.678 | 0.799 |
| Correct refusal (out-of-domain) | 10 | 0.456 | 0.556 | **0.630** |
| Answered (not refused) | 37 | 0.559 | 0.740 | 0.803 |

Correct (legitimate) refusals never exceed 0.630; spurious refusals run higher. Threshold sweep:

| T | spurious caught | correct-refusal false positives |
|---|---|---|
| 0.62 | 17/21 | 1 |
| 0.63 | 16/21 | 1 |
| **0.64** | **16/21** | **0** |
| 0.66 | 14/21 | 0 |
| 0.70 | 7/21 | 0 |

**Chosen: T = 0.64.** Detects **16/21 spurious refusals (76% recall) with 0 false positives** on legitimate refusals (100% precision on the refusal set). Compare the prompt-only lever (D2): 5/21 recovered with 1 false positive. R7 is the stronger, cleaner mechanism.

**Mechanism.** R7 is a detection rule like R1–R6. When it fires, the generator's existing retry loop re-prompts with the R7 feedback ("a source has high similarity; re-read and answer if the information exists"), giving an automatic recovery path without a separate code path.

**Caveat.** T is calibrated on this gold set; it is a cosine value specific to BGE-M3 on this corpus and would need recalibration for another embedding model or domain. Reported as such.
