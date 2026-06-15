# Kaggle 7B baseline run

Runs the same evaluation harness on **Qwen2.5-7B-Instruct-Q4_K_M** via Kaggle's free T4 GPU, then produces a comparison report against the local 3B run.

## One-time setup

### 1. Bundle the code as a Kaggle Dataset

From the project root:

```bash
cd /Users/cosminglod/Desktop/licenta
zip -r /tmp/licenta-code.zip \
    src/licenta \
    data/cezicelegea_dump.json \
    data/eval/gold_set.json \
    data/eval/gold_set_smoke.json
```

This produces a ~500 KB zip with **only** the code and the input data the notebook needs (no `.venv`, no PDFs, no LaTeX, no Chroma index — that's rebuilt on Kaggle).

### 2. Upload to Kaggle

1. Go to https://www.kaggle.com/datasets and click **New Dataset**.
2. Drag `/tmp/licenta-code.zip` into the uploader.
3. Title: **`licenta-code`** (this exact slug is referenced by the notebook).
4. Visibility: **Private** (keeps your code private; Kaggle notebooks you own can still mount it).
5. Click **Create**.

### 3. Create the notebook

1. Go to https://www.kaggle.com/code and click **New Notebook**.
2. **Settings panel (right side):**
   - Accelerator: **GPU T4 x2** (or **GPU P100** if available)
   - Internet: **On** (needed for Ollama install + HuggingFace model download)
3. **Add Data** (right side): search **`licenta-code`** and add your dataset.
4. **File → Upload Notebook** → select `kaggle/eval_7b.ipynb` from this repo.
5. Save.

## Running the notebook

Click **Run All**. End-to-end timing on a T4:

| Step | Time |
|---|---|
| Install Ollama | ~30 s |
| Pull Qwen2.5-7B-Q4 (~4.5 GB download) | 3–5 min |
| Install Python deps | ~30 s |
| Download bge-m3 + build Chroma index | 3–5 min |
| Run 68-case eval | 25–40 min |
| **Total** | **~35–50 min** |

## After it finishes

The notebook writes:
- `/kaggle/working/eval_7b/results.json` — machine-readable per-case results
- `/kaggle/working/eval_7b/report.md` — human-readable summary report

Both appear in the **Output** panel on the right. Click **Download** to pull them locally, then drop them in `data/eval/runs/<timestamp>_qwen2.5_7b-instruct-q4_K_M/` and you have a direct 3B-vs-7B comparison.

## When to re-run

- After editing the gold set: re-bundle, replace the Kaggle Dataset (the dataset has versioning so you don't lose old runs), re-run.
- After changing the contract rules or generator: same.
- Free tier: 30 GPU-hours / week, ~12 h per session — well within budget for this eval.
