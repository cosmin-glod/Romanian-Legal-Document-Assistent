"""Generate all thesis figures from the evaluation data.

Outputs vector PDFs into template-redactare/images/ for \\includegraphics.
Style: clean matplotlib, consistent palette, grid, tight layout.

Usage:
    uv run python scripts/plots.py
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "template-redactare" / "images"
# Sweep + mechanism outputs land here after extracting Kaggle's results.zip into
# data/eval/ (the bundle root). Per-config dir = data/eval/runs/<label>.
RUNS = ROOT / "data" / "eval" / "runs"
RUN_3B = RUNS / "3b_q4"
RUN_7B = RUNS / "7b_q4"

C3B, C7B = "#4C72B0", "#DD8452"  # 3B blue, 7B orange
CACC, CWARN, CBAD = "#55A868", "#C7B500", "#C44E52"

plt.rcParams.update(
    {
        "font.size": 11,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "axes.axisbelow": True,
        "figure.dpi": 120,
        "savefig.bbox": "tight",
    }
)


def _load(run: Path) -> list[dict]:
    return json.loads((run / "results.json").read_text())


def _save(fig, name: str) -> None:
    IMG.mkdir(parents=True, exist_ok=True)
    fig.savefig(IMG / f"{name}.pdf")
    plt.close(fig)
    print(f"wrote images/{name}.pdf")


def _grouped_bar(ax, labels, vals3b, vals7b, ylabel, fmt="{:.0f}"):
    x = range(len(labels))
    w = 0.38
    b1 = ax.bar([i - w / 2 for i in x], vals3b, w, label="3B-Q4", color=C3B)
    b2 = ax.bar([i + w / 2 for i in x], vals7b, w, label="7B-Q4", color=C7B)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel(ylabel)
    for bars in (b1, b2):
        for bar in bars:
            ax.annotate(
                fmt.format(bar.get_height()),
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha="center", va="bottom", fontsize=8,
            )
    ax.legend()


# ---- metrics from a results.json ----
def _metrics(d):
    n = len(d)
    ref = 100 * sum(r["refusal_correct"] for r in d) / n
    rec_rel = [r for r in d if r["breadcrumb_recall"] is not None]
    rec = 100 * sum(1 for r in rec_rel if r["breadcrumb_recall"]) / len(rec_rel)
    kw_c = [r["keyword_coverage"] for r in d if r["keyword_coverage"] is not None]
    kw = 100 * sum(kw_c) / len(kw_c)
    con = 100 * sum(r["contract_valid"] for r in d) / n
    lat = sum(r["latency_s"] for r in d) / n
    return ref, rec, kw, con, lat


def fig_metrics_global(d3, d7):
    m3, m7 = _metrics(d3), _metrics(d7)
    labels = ["Refusal\nacc.", "Recall@4", "Lexical kw\nrecall", "Contract\npass"]
    fig, ax = plt.subplots(figsize=(7, 4))
    _grouped_bar(ax, labels, m3[:4], m7[:4], "%", "{:.0f}")
    ax.set_ylim(0, 105)
    ax.set_title("Metrici globale: 3B vs 7B (n=68)")
    _save(fig, "fig_metrics_global")


def fig_refusal_by_difficulty(d3, d7):
    def by_diff(d):
        out = {}
        for diff in ("easy", "medium", "hard"):
            rs = [r for r in d if r["difficulty"] == diff]
            out[diff] = 100 * sum(r["refusal_correct"] for r in rs) / len(rs)
        return out
    a, b = by_diff(d3), by_diff(d7)
    fig, ax = plt.subplots(figsize=(6, 4))
    _grouped_bar(ax, ["Ușor", "Mediu", "Dificil"],
                 [a["easy"], a["medium"], a["hard"]],
                 [b["easy"], b["medium"], b["hard"]], "Refusal accuracy (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Refusal accuracy pe dificultate")
    _save(fig, "fig_refusal_by_difficulty")


def fig_contract_by_category(d3, d7):
    cats = ["nastere", "casatorie", "locuire"]
    def by_cat(d):
        return [100 * sum(r["contract_valid"] for r in d if r["category"] == c)
                / sum(1 for r in d if r["category"] == c) for c in cats]
    fig, ax = plt.subplots(figsize=(6, 4))
    _grouped_bar(ax, ["Naștere", "Căsătorie", "Locuire"],
                 by_cat(d3), by_cat(d7), "Contract pass rate (%)")
    ax.set_ylim(0, 105)
    ax.set_title("Contract pass rate pe categorie")
    _save(fig, "fig_contract_by_category")


def fig_violations(d3, d7):
    rules = ["R2", "R3", "R4", "R5"]
    keys = ["R2_UNCITED", "R3_BAD_CITATION", "R4_FABRICATED_DOC", "R5_REFUSAL_WITH_DOCS"]
    def counts(d):
        return [sum(r["violations"].count(k) for r in d) for k in keys]
    fig, ax = plt.subplots(figsize=(6, 4))
    _grouped_bar(ax, rules, counts(d3), counts(d7), "Număr de violări")
    ax.set_title("Distribuția violărilor de contract pe regulă")
    _save(fig, "fig_violations")


def fig_failure_modes(d3, d7):
    def fm(d):
        spur = sum(1 for r in d if r["is_refusal"] and not r["should_refuse"])
        fab = sum(1 for r in d if "R4_FABRICATED_DOC" in r["violations"])
        return spur, fab
    s3, f3 = fm(d3)
    s7, f7 = fm(d7)
    fig, ax = plt.subplots(figsize=(6, 4))
    _grouped_bar(ax, ["Refuz spurious\n(eșec dominant)", "Fabricare (R4)"],
                 [s3, f3], [s7, f7], f"Cazuri (din {len(d3)})")
    ax.set_title("Mod de eșec dominant: refuz spurious vs fabricare")
    _save(fig, "fig_failure_modes")


def fig_r4_hardening():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.6))
    ax1.bar(["Înainte", "După"], [20, 11], color=[CBAD, CACC])
    ax1.set_ylabel("Semnalări R4 (ocurențe)")
    ax1.set_title("R4: înainte/după întărire")
    for i, v in enumerate([20, 11]):
        ax1.annotate(str(v), (i, v), ha="center", va="bottom")
    ax2.bar(["Înainte", "După"], [81, 85], color=[C3B, CACC])
    ax2.set_ylabel("Contract pass rate (%)")
    ax2.set_ylim(0, 100)
    ax2.set_title("Contract pass (temp 0)")
    for i, v in enumerate([81, 85]):
        ax2.annotate(f"{v}%", (i, v), ha="center", va="bottom")
    fig.suptitle("Întărirea R4 (normalizare diacritice + flexiune)")
    _save(fig, "fig_r4_hardening")


def fig_faithfulness():
    fig, ax = plt.subplots(figsize=(5.5, 3.6))
    vals = [27, 47, 27]
    bars = ax.bar(["Corect", "Parțial", "Incorect"], vals,
                  color=[CACC, CWARN, CBAD])
    ax.set_ylabel("% din eșantion (n=15)")
    ax.set_title("Evaluare manuală a fidelității (3B)")
    for bar, v in zip(bars, vals):
        ax.annotate(f"{v}%", (bar.get_x() + bar.get_width() / 2, v),
                    ha="center", va="bottom")
    _save(fig, "fig_faithfulness")


def fig_latency(d3, d7):
    cats = ["nastere", "casatorie", "locuire"]
    def by_cat(d):
        return [sum(r["latency_s"] for r in d if r["category"] == c)
                / sum(1 for r in d if r["category"] == c) for c in cats]
    fig, ax = plt.subplots(figsize=(6, 4))
    _grouped_bar(ax, ["Naștere", "Căsătorie", "Locuire"],
                 by_cat(d3), by_cat(d7), "Latență medie (s)", "{:.0f}")
    ax.set_title("Latență end-to-end pe categorie")
    _save(fig, "fig_latency")


# ---- retrieval score plots (R7) ----
def _scores():
    return json.loads((ROOT / "data/eval/retrieval_scores.json").read_text())


def fig_score_dist():
    s = _scores()
    spur = [r["top1"] for r in s if r["is_refusal"] and not r["should_refuse"]]
    corr = [r["top1"] for r in s if r["is_refusal"] and r["should_refuse"]]
    ans = [r["top1"] for r in s if not r["is_refusal"]]
    groups = [spur, corr, ans]
    labels = ["Refuz spurious\n(răspuns prezent)", "Refuz corect\n(în afara domeniului)", "Răspuns dat"]
    colors = [CBAD, C3B, CACC]
    fig, ax = plt.subplots(figsize=(7, 4.3))
    for i, (g, c) in enumerate(zip(groups, colors)):
        jitter = [i + 0.06 * ((k % 7) - 3) for k in range(len(g))]
        ax.scatter(jitter, g, color=c, alpha=0.7, s=22, edgecolors="none")
        ax.plot([i - 0.25, i + 0.25], [sum(g) / len(g)] * 2, color="black", lw=2)
    ax.axhline(0.64, color="red", ls="--", lw=1.3, label="Prag R7 = 0.64")
    ax.set_xticks(range(3))
    ax.set_xticklabels(labels)
    ax.set_ylabel("Similaritate top-1 (cosine)")
    ax.set_title("Distribuția scorului de regăsire și pragul R7")
    ax.legend()
    _save(fig, "fig_score_dist")


def fig_r7_sweep():
    s = _scores()
    spur = [r["top1"] for r in s if r["is_refusal"] and not r["should_refuse"]]
    corr = [r["top1"] for r in s if r["is_refusal"] and r["should_refuse"]]
    Ts = [0.58 + 0.01 * i for i in range(16)]
    caught = [sum(1 for v in spur if v >= T) for T in Ts]
    fps = [sum(1 for v in corr if v >= T) for T in Ts]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(Ts, caught, "-o", color=CACC, label="Refuzuri spurioase detectate")
    ax.plot(Ts, fps, "-s", color=CBAD, label="Fals pozitive (refuz corect)")
    ax.axvline(0.64, color="red", ls="--", lw=1.2, label="Prag ales = 0.64")
    ax.set_xlabel("Prag de similaritate T")
    ax.set_ylabel("Număr de cazuri")
    ax.set_title("R7: detecție vs fals pozitive în funcție de prag")
    ax.legend()
    _save(fig, "fig_r7_sweep")


def fig_ablation():
    abl = json.loads((ROOT / "data/eval/ablation_contracts.json").read_text())
    def noR7(vs):
        return [v for v in vs if v != "R7_OVERREFUSAL"]
    n = len(abl)
    off_flawed = sum(1 for r in abl if noR7(r["off_violations"]))
    off_clean = n - off_flawed
    withheld = sum(1 for r in abl if noR7(r["on_violations"]))
    on_clean = n - withheld
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    x = [0, 1]
    ax.bar(x, [off_clean, on_clean], 0.55, color=CACC, label="Servit corect/ancorat")
    ax.bar([0], [off_flawed], 0.55, bottom=[off_clean], color=CBAD,
           label="Servit cu defect")
    ax.bar([1], [withheld], 0.55, bottom=[on_clean], color=CWARN,
           label="Reținut (refuz controlat)")
    ax.set_xticks(x)
    ax.set_xticklabels(["Fără contracte", "Cu contracte"])
    ax.set_ylabel(f"Cazuri (din {n})")
    ax.set_title("Ablație: ce ajunge la cetățean")
    ax.annotate(f"{off_flawed} cu defect", (0, off_clean + off_flawed / 2),
                ha="center", va="center", color="white", fontsize=9)
    ax.annotate(f"{withheld} reținute", (1, on_clean + withheld / 2),
                ha="center", va="center", fontsize=9)
    ax.annotate("0 servite cu defect", (1, on_clean - 4), ha="center",
                va="top", fontsize=8, color="white")
    ax.legend(loc="lower center", fontsize=8)
    _save(fig, "fig_ablation")


_FORM_LABELS = {
    "declaratie_nume_copil": "nume copil",
    "recunoastere_paternitate": "paternitate",
    "cerere_alocatie_copil": "alocație",
    "cerere_indemnizatie_crestere": "indemnizație",
    "declaratie_casatorie": "căsătorie",
    "declaratie_necasatorit": "necăsătorit",
    "contract_inchiriere": "închiriere",
}


def fig_forms():
    rows = json.loads((ROOT / "data/eval/forms_results.json").read_text())
    by: dict[str, list[int]] = {}
    for r in rows:
        ok, tot = by.setdefault(r["form_id"], [0, 0])
        by[r["form_id"]] = [ok + r["fields_ok"], tot + r["fields_total"]]
    labels, accs = [], []
    for fid, (ok, tot) in by.items():
        labels.append(_FORM_LABELS.get(fid, fid))
        accs.append(100 * ok / tot)
    overall = 100 * sum(r["fields_ok"] for r in rows) / sum(r["fields_total"] for r in rows)
    order = sorted(range(len(accs)), key=lambda i: accs[i])
    labels = [labels[i] for i in order]
    accs = [accs[i] for i in order]
    fig, ax = plt.subplots(figsize=(7, 4.2))
    bars = ax.barh(labels, accs, color=C3B)
    ax.axvline(overall, color=CBAD, ls="--", lw=1.3,
               label=f"Acuratețe globală {overall:.0f}%")
    ax.set_xlim(0, 100)
    ax.set_xlabel("Acuratețe la nivel de câmp (%)")
    ax.set_title("Extracția pentru pre-completare, pe formular")
    for bar, a in zip(bars, accs):
        ax.annotate(f"{a:.0f}%", (a, bar.get_y() + bar.get_height() / 2),
                    va="center", ha="right", color="white", fontsize=9)
    ax.legend(loc="lower left")
    _save(fig, "fig_forms")


EVENT_COLORS = {"nastere": "#4C72B0", "casatorie": "#C44E52", "locuire": "#55A868"}
EVENT_RO = {"nastere": "Naștere", "casatorie": "Căsătorie", "locuire": "Locuire"}


def fig_corpus():
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from licenta.chunker import chunk_dump
    chunks = chunk_dump(ROOT / "data/cezicelegea_dump.json")
    from collections import Counter
    per = Counter(c.slug for c in chunks)
    sizes = [len(c.text) for c in chunks]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.8))
    evs = ["nastere", "casatorie", "locuire"]
    ax1.bar([EVENT_RO[e] for e in evs], [per[e] for e in evs],
            color=[EVENT_COLORS[e] for e in evs])
    ax1.set_ylabel("Fragmente (chunks)")
    ax1.set_title(f"Fragmente pe eveniment (total {len(chunks)})")
    for i, e in enumerate(evs):
        ax1.annotate(str(per[e]), (i, per[e]), ha="center", va="bottom")
    ax2.hist(sizes, bins=20, color=C3B, edgecolor="white")
    ax2.axvline(3000, color=CBAD, ls="--", lw=1.2, label="MAX_CHARS = 3000")
    ax2.set_xlabel("Dimensiune fragment (caractere)")
    ax2.set_ylabel("Număr de fragmente")
    ax2.set_title("Distribuția dimensiunii fragmentelor")
    ax2.legend()
    _save(fig, "fig_corpus")


def _chunk_embeddings():
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    import chromadb
    from licenta.index import CHROMA_DIR, COLLECTION
    c = chromadb.PersistentClient(path=str(ROOT / CHROMA_DIR)).get_collection(COLLECTION)
    g = c.get(include=["embeddings", "metadatas"])
    import numpy as np
    return np.array(g["embeddings"]), [m["slug"] for m in g["metadatas"]]


def fig_embeddings():
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (registers 3d projection)
    E, slugs = _chunk_embeddings()
    X = E - E.mean(0)
    _, S, Vt = np.linalg.svd(X, full_matrices=False)
    P = X @ Vt[:3].T
    ev = (S ** 2 / (S ** 2).sum())[:3] * 100  # explained variance per component
    fig = plt.figure(figsize=(7, 5.5))
    ax = fig.add_subplot(projection="3d")
    for e in ("nastere", "casatorie", "locuire"):
        m = [i for i, s in enumerate(slugs) if s == e]
        ax.scatter(P[m, 0], P[m, 1], P[m, 2], s=26, alpha=0.8, label=EVENT_RO[e],
                   color=EVENT_COLORS[e], edgecolors="none", depthshade=True)
    ax.set_xlabel(f"PC1 ({ev[0]:.0f}%)")
    ax.set_ylabel(f"PC2 ({ev[1]:.0f}%)")
    ax.set_zlabel(f"PC3 ({ev[2]:.0f}%)")
    ax.set_title("Proiecție PCA 3D a fragmentelor (BGE-M3, 1024→3)")
    ax.view_init(elev=18, azim=-62)
    ax.legend(loc="upper left")
    _save(fig, "fig_embeddings")


def fig_confusion(d3, d7):
    import numpy as np
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 4))
    for ax, d, name in ((axes[0], d3, "3B (M1)"), (axes[1], d7, "7B (T4)")):
        m = np.zeros((2, 2), int)  # rows=should_refuse, cols=is_refusal
        for r in d:
            m[int(r["should_refuse"]), int(r["is_refusal"])] += 1
        ax.imshow(m, cmap="Blues")
        ax.set_xticks([0, 1], ["Răspuns", "Refuz"])
        ax.set_yticks([0, 1], ["Trebuie\nrăspuns", "Trebuie\nrefuz"])
        for i in range(2):
            for j in range(2):
                ax.text(j, i, m[i, j], ha="center", va="center",
                        color="white" if m[i, j] > m.max() / 2 else "black",
                        fontsize=14)
        ax.set_title(name)
        ax.set_xlabel("Decizia modelului")
    fig.suptitle("Matrice de confuzie a refuzului")
    _save(fig, "fig_confusion")


def fig_latency_dist(d3, d7):
    fig, ax = plt.subplots(figsize=(6.5, 4))
    for i, (d, c, name) in enumerate(((d3, C3B, "3B (M1)"), (d7, C7B, "7B (T4)"))):
        lat = [r["latency_s"] for r in d]
        jit = [i + 0.06 * ((k % 9) - 4) for k in range(len(lat))]
        ax.scatter(jit, lat, alpha=0.6, color=c, s=20, edgecolors="none")
        ax.plot([i - 0.25, i + 0.25], [sum(lat) / len(lat)] * 2, color="black", lw=2)
    ax.set_xticks([0, 1], ["3B (M1)", "7B (T4)"])
    ax.set_ylabel("Latență per întrebare (s)")
    ax.set_title("Distribuția latenței end-to-end")
    _save(fig, "fig_latency_dist")


def fig_recall_by_event(d3, d7):
    evs = ["nastere", "casatorie", "locuire"]
    def rec(d):
        out = []
        for e in evs:
            rs = [r for r in d if r["category"] == e and r["breadcrumb_recall"] is not None]
            out.append(100 * sum(1 for r in rs if r["breadcrumb_recall"]) / len(rs))
        return out
    fig, ax = plt.subplots(figsize=(6, 4))
    _grouped_bar(ax, [EVENT_RO[e] for e in evs], rec(d3), rec(d7), "Recall@4 (%)")
    ax.set_ylim(0, 105)
    ax.set_title("Breadcrumb recall@4 pe eveniment")
    _save(fig, "fig_recall_by_event")


def fig_forms_class():
    rows = json.loads((ROOT / "data/eval/forms_results.json").read_text())
    ok: dict[str, int] = {}
    tot: dict[str, int] = {}
    for r in rows:
        for v in r["per_field"].values():
            tot[v["cls"]] = tot.get(v["cls"], 0) + 1
            ok[v["cls"]] = ok.get(v["cls"], 0) + (1 if v["ok"] else 0)
    classes = ["structured", "name", "freetext"]
    ro = {"structured": "structurate\n(CNP, date, CI)", "name": "nume",
          "freetext": "text liber\n(adresă)"}
    accs = [100 * ok[c] / tot[c] for c in classes]
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar([ro[c] for c in classes], accs, color=[C3B, CACC, CWARN])
    ax.set_ylim(0, 105)
    ax.set_ylabel("Acuratețe (%)")
    ax.set_title("Extracție formulare: acuratețe pe clasă de câmp")
    for b, a in zip(bars, accs):
        ax.annotate(f"{a:.0f}%", (b.get_x() + b.get_width() / 2, a),
                    ha="center", va="bottom")
    _save(fig, "fig_forms_class")


_SWEEP_LABELS = ["3B-Q4", "3B-Q8", "3B-FP16", "7B-Q4", "14B-Q4", "RoLlama-8B"]
_SWEEP_KEYS = ["3b_q4", "3b_q8", "3b_fp16", "7b_q4", "14b_q4", "rollama3_8b_q4"]


def _sweep_data():
    import csv
    rows = {r[""]: r for r in csv.DictReader(open(RUNS / "summary.csv"))}
    judge = {}
    for k in _SWEEP_KEYS:
        j = json.loads((RUNS / k / "judge.json").read_text())
        tot = sum(j.values()) or 1
        judge[k] = round(100 * j.get("corect", 0) / tot)
    return rows, judge


def fig_quant_scale():
    rows, _ = _sweep_data()
    metrics = [("refusal", "Refusal acc."), ("contract", "Contract pass"),
               ("kw", "Lexical recall")]
    import numpy as np
    x = np.arange(len(_SWEEP_KEYS)); w = 0.26
    colors = [C3B, CACC, CWARN]
    fig, ax = plt.subplots(figsize=(8, 4.3))
    for i, (key, lab) in enumerate(metrics):
        vals = [float(rows[k][key]) for k in _SWEEP_KEYS]
        ax.bar(x + (i - 1) * w, vals, w, label=lab, color=colors[i])
    ax.set_xticks(x); ax.set_xticklabels(_SWEEP_LABELS)
    ax.set_ylabel("%"); ax.set_ylim(0, 100)
    _n = rows[_SWEEP_KEYS[0]].get("n", "")
    ax.set_title(f"Cuantizare, scară și model RO-specializat (n={_n})")
    ax.legend(loc="upper left", fontsize=8)
    ax.axvspan(-0.5, 2.5, color="gray", alpha=0.06)
    ax.text(1, 96, "sweep cuantizare 3B", ha="center", fontsize=8, color="gray")
    _save(fig, "fig_quant_scale")


def fig_judge():
    rows, judge = _sweep_data()
    vals = [judge[k] for k in _SWEEP_KEYS]
    fig, ax = plt.subplots(figsize=(7, 3.8))
    bars = ax.bar(_SWEEP_LABELS, vals, color=[C3B, CACC, CWARN, C7B, CBAD, "#8172B3"])
    ax.set_ylabel("Răspunsuri corecte (judecător) %"); ax.set_ylim(0, 100)
    ax.set_title("Fidelitate judecată de LLM (14B), pe configurație")
    for b, v in zip(bars, vals):
        ax.annotate(f"{v}%", (b.get_x()+b.get_width()/2, v), ha="center", va="bottom")
    _save(fig, "fig_judge")


def main():
    # Only the figures actually included in the thesis (others were removed during
    # the edit pass; some also rely on fields no longer in the gold set, e.g.
    # `difficulty`, so regenerating them would error).
    d3, d7 = _load(RUN_3B), _load(RUN_7B)
    # Cap. 3 — corpus
    fig_corpus()
    fig_embeddings()
    # Cap. 4 — sweep + mechanism
    fig_quant_scale()
    fig_judge()
    fig_failure_modes(d3, d7)
    fig_score_dist()
    fig_r7_sweep()
    fig_forms()


if __name__ == "__main__":
    main()
