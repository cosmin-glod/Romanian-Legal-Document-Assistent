"""Analyze how many silent failures the contract layer caught.

Reads existing results.json files (one per model run) and reports, per model:
  - Total cases evaluated
  - Cases that triggered at least one contract violation
  - Violation count per rule (R1..R6)
  - "Silent failure" count: violations that would have produced a
    plausible-but-wrong answer to a citizen if the contract weren't there
    (R4_FABRICATED_DOC, R2_UNCITED, R5_REFUSAL_WITH_DOCS, R6_FORM_ID_IN_DOCS)
  - 3 concrete example cases per violation type (case_id + answer snippet)

Usage:
    uv run python scripts/without_contracts_analysis.py
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

RUNS = {
    "3B (M1 local)": Path("data/eval/runs/20260527_203812_qwen2.5_3b-instruct-q4_K_M/results.json"),
    "7B (Kaggle T4)": Path("data/eval/runs/20260528_kaggle_qwen2.5_7b-instruct-q4_K_M/results.json"),
}

# Rules that, if disabled, would let plausible-but-ungrounded answers reach the user.
SILENT_FAILURE_RULES = {
    "R2_UNCITED",            # affirmative without citation → claims with no source
    "R4_FABRICATED_DOC",     # invented document names not in any cited source
    "R5_REFUSAL_WITH_DOCS",  # refusal with phantom documents
    "R6_FORM_ID_IN_DOCS",    # form-id polluting document list
}


def analyze(label: str, path: Path) -> dict:
    raw = json.loads(path.read_text())
    n = len(raw)
    n_invalid = 0
    n_silent_failures = 0
    rule_counts: Counter[str] = Counter()
    examples: dict[str, list[dict]] = defaultdict(list)

    for case in raw:
        violations = case.get("violations", []) or []
        if not violations:
            continue
        n_invalid += 1
        had_silent_failure = False
        for v in violations:
            rule_counts[v] += 1
            if v in SILENT_FAILURE_RULES:
                had_silent_failure = True
                if len(examples[v]) < 3:
                    examples[v].append(
                        {
                            "case_id": case["case_id"],
                            "question": case["question"],
                            "answer_excerpt": case["answer_text"][:200]
                            + ("…" if len(case["answer_text"]) > 200 else ""),
                        }
                    )
        if had_silent_failure:
            n_silent_failures += 1

    return {
        "label": label,
        "path": path,
        "n_total": n,
        "n_invalid": n_invalid,
        "n_silent_failures": n_silent_failures,
        "rule_counts": dict(rule_counts),
        "examples": dict(examples),
    }


def fmt_pct(n: int, total: int) -> str:
    if total == 0:
        return "n/a"
    return f"{100 * n / total:.0f}%"


def main() -> None:
    print('# Analiza: ce ar fi „scăpat" fără stratul de contracte\n')
    print(
        "Întrebare: din cazurile evaluate, în câte răspunsul s-ar fi părut "
        "valid pentru utilizator (refuz sau răspuns afirmativ) dar a fost "
        "marcat ca incorect de cel puțin o regulă R1..R6?\n"
    )

    all_stats = []
    for label, path in RUNS.items():
        if not path.exists():
            print(f"⚠️  {label}: missing {path}")
            continue
        stats = analyze(label, path)
        all_stats.append(stats)

    if not all_stats:
        return

    print("## Tabel sintetic\n")
    print("| Model | Total cazuri | Cazuri cu violare | Eșecuri silențioase | Reducerea ratei silențioase față de 3B |")
    print("|---|---|---|---|---|")
    baseline = None
    for s in all_stats:
        silent_pct = 100 * s["n_silent_failures"] / s["n_total"]
        if baseline is None:
            baseline = silent_pct
            reduction = "—"
        else:
            reduction = f"{baseline - silent_pct:.0f} pp"
        print(
            f"| {s['label']} | {s['n_total']} | "
            f"{s['n_invalid']} ({fmt_pct(s['n_invalid'], s['n_total'])}) | "
            f"{s['n_silent_failures']} ({fmt_pct(s['n_silent_failures'], s['n_total'])}) | "
            f"{reduction} |"
        )

    print("\n## Distribuția violărilor pe regulă\n")
    print("| Regulă | " + " | ".join(s["label"] for s in all_stats) + " |")
    print("|---|" + "---|" * len(all_stats))
    all_rules = sorted({r for s in all_stats for r in s["rule_counts"]})
    for rule in all_rules:
        row = f"| `{rule}` |"
        for s in all_stats:
            row += f" {s['rule_counts'].get(rule, 0)} |"
        print(row)

    print("\n## Headline numbers pentru teză\n")
    for s in all_stats:
        n_silent = s["n_silent_failures"]
        n_total = s["n_total"]
        print(
            f"- **{s['label']}**: fără stratul de contracte, "
            f"**{n_silent} din {n_total}** răspunsuri "
            f"({fmt_pct(n_silent, n_total)}) ar fi fost servite cetățeanului "
            f"ca informație autoritară, deși conțin fabricare, lipsă "
            f"de citații sau pollution de formulare în documente."
        )

    print("\n## Exemple concrete (max 3 per regulă, per model)\n")
    for s in all_stats:
        if not s["examples"]:
            continue
        print(f"\n### {s['label']}\n")
        for rule, exs in sorted(s["examples"].items()):
            print(f"**{rule}** ({s['rule_counts'][rule]} apariții total):")
            for e in exs:
                print(f"- `{e['case_id']}` — \"{e['question']}\"")
                print(f"  > {e['answer_excerpt']}")
            print()


if __name__ == "__main__":
    main()
