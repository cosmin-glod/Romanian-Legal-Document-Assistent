"""Evaluation harness for the RAG + output-contract pipeline.

For each case in the gold set, runs retrieval + generation + validation and
computes:
  - **Breadcrumb recall@k**: did at least one top-k chunk's breadcrumb match
    one of the expected substrings? (proxy for retrieval correctness)
  - **Keyword coverage**: fraction of expected_keywords present in the answer
    text (proxy for answer faithfulness on non-refusal cases)
  - **Refusal accuracy**: did is_refusal match should_refuse?
  - **Contract pass rate**: did all R1..R6 rules pass?
  - **Latency**: wall-clock per case

Outputs a JSON dump (machine-readable) and a Markdown report (for the thesis).
"""

from __future__ import annotations

import json
import logging
import time
from collections import Counter
from dataclasses import asdict, dataclass, field, fields
from pathlib import Path

from licenta.generator import DEFAULT_MODEL, generate
from licenta.retriever import Retriever

log = logging.getLogger(__name__)


@dataclass
class EvalCase:
    id: str
    category: str
    difficulty: str
    question: str
    should_refuse: bool = False
    expected_breadcrumb_contains: list[str] = field(default_factory=list)
    expected_keywords: list[str] = field(default_factory=list)
    notes: str = ""  # human-only annotation, ignored by the harness
    variant: str = ""  # "", "new", or "paraphrase" — provenance tag, used for breakdowns only


@dataclass
class CaseResult:
    case_id: str
    category: str
    difficulty: str
    question: str
    should_refuse: bool
    answer_text: str
    is_refusal: bool
    refusal_correct: bool
    breadcrumb_recall: bool | None  # None for refusal cases without expectation
    keyword_coverage: float | None  # None for refusal cases
    contract_valid: bool
    violations: list[str]
    attempts: int
    latency_s: float
    top_breadcrumbs: list[str]
    # --- audit fields: full detail so R4 (and others) can be reviewed by hand ---
    documents_mentioned: list[str] = field(default_factory=list)
    cited_source_indices: list[int] = field(default_factory=list)
    cited_sources_text: list[str] = field(default_factory=list)
    violation_messages: list[str] = field(default_factory=list)
    # --- generation health: surface runaway / malformed JSON instead of hiding it ---
    parse_failures: int = 0       # nr. de încercări cu JSON invalid pentru acest caz
    forced_refusal: bool = False  # refuzul a fost forțat de parse eșuat, nu de model
    max_raw_chars: int = 0        # cea mai lungă ieșire brută (semnalează runaway)


def load_gold_set(path: Path) -> list[EvalCase]:
    raw = json.loads(path.read_text())
    # difficulty is no longer used (label criterion was not well-defined); tolerate its absence.
    # Drop any keys that are not EvalCase fields so extra gold-set annotations don't crash loading.
    known = {f.name for f in fields(EvalCase)}
    cases = []
    for case in raw:
        kwargs = {k: v for k, v in case.items() if k in known}
        kwargs.setdefault("difficulty", "")  # no longer required in the gold set
        cases.append(EvalCase(**kwargs))
    return cases


def evaluate_case(
    case: EvalCase,
    retriever: Retriever,
    model: str,
    k: int = 4,
    temperature: float = 0.2,
    few_shot: bool = False,
) -> CaseResult:
    from licenta.generator import FEW_SHOT

    start = time.time()
    hits = retriever.query(case.question, k=k)
    answer = generate(
        case.question, hits, model=model, temperature=temperature,
        history=FEW_SHOT if few_shot else None,
    )
    elapsed = time.time() - start

    schema = answer.schema
    n = len(answer.sources)
    cited_sources_text = [
        answer.sources[i - 1].text
        for i in schema.cited_source_indices
        if 1 <= i <= n
    ]

    top_breadcrumbs = [h.metadata.get("breadcrumb", "") for h in hits]

    if case.expected_breadcrumb_contains:
        needles = [n.lower() for n in case.expected_breadcrumb_contains]
        breadcrumb_recall = any(
            any(n in bc.lower() for n in needles) for bc in top_breadcrumbs
        )
    else:
        # No expectation set (typically refusal cases) — N/A
        breadcrumb_recall = None

    keyword_coverage: float | None = None
    if case.expected_keywords and not case.should_refuse:
        ans_lower = answer.text.lower()
        hits_kw = sum(1 for kw in case.expected_keywords if kw.lower() in ans_lower)
        keyword_coverage = hits_kw / len(case.expected_keywords)

    return CaseResult(
        case_id=case.id,
        category=case.category,
        difficulty=case.difficulty,
        question=case.question,
        should_refuse=case.should_refuse,
        answer_text=answer.text,
        is_refusal=answer.schema.is_refusal,
        refusal_correct=(answer.schema.is_refusal == case.should_refuse),
        breadcrumb_recall=breadcrumb_recall,
        keyword_coverage=keyword_coverage,
        contract_valid=answer.valid,
        violations=[v.rule_id for v in answer.violations],
        attempts=answer.attempts,
        latency_s=elapsed,
        top_breadcrumbs=top_breadcrumbs,
        documents_mentioned=list(schema.documents_mentioned),
        cited_source_indices=list(schema.cited_source_indices),
        cited_sources_text=cited_sources_text,
        violation_messages=[v.message for v in answer.violations],
        parse_failures=answer.parse_failures,
        forced_refusal=answer.forced_refusal,
        max_raw_chars=answer.max_raw_chars,
    )


def run(
    gold_set_path: Path,
    output_dir: Path,
    model: str = DEFAULT_MODEL,
    k: int = 4,
    limit: int | None = None,
    temperature: float = 0.2,
    few_shot: bool = False,
) -> Path:
    cases = load_gold_set(gold_set_path)
    if limit:
        cases = cases[:limit]

    retriever = Retriever()
    results: list[CaseResult] = []

    for i, case in enumerate(cases, 1):
        preview = case.question[:65]
        print(f"[{i}/{len(cases)}] {case.id}: {preview}…", flush=True)
        try:
            r = evaluate_case(
                case, retriever, model, k=k, temperature=temperature,
                few_shot=few_shot,
            )
            results.append(r)
            print(
                f"    refusal_correct={r.refusal_correct}  "
                f"recall={r.breadcrumb_recall}  "
                f"contract_valid={r.contract_valid}  "
                f"latency={r.latency_s:.1f}s",
                flush=True,
            )
        except Exception as e:  # pragma: no cover
            log.exception("case %s failed: %s", case.id, e)

    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "results.json"
    json_path.write_text(
        json.dumps(
            [asdict(r) for r in results], ensure_ascii=False, indent=2
        )
    )
    md_path = output_dir / "report.md"
    md_path.write_text(_build_report(results, model, k))
    print(f"\nWrote {json_path}")
    print(f"Wrote {md_path}")
    return md_path


# ---------------------------- reporting ----------------------------

def _pct(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "n/a"
    return f"{100 * numerator / denominator:.0f}%"


def _build_report(results: list[CaseResult], model: str, k: int) -> str:
    n = len(results)
    if n == 0:
        return "Niciun rezultat.\n"

    refusal_correct = sum(1 for r in results if r.refusal_correct)
    contract_valid = sum(1 for r in results if r.contract_valid)
    recall_relevant = [r for r in results if r.breadcrumb_recall is not None]
    recall_correct = sum(1 for r in recall_relevant if r.breadcrumb_recall)
    answer_cases = [r for r in results if r.keyword_coverage is not None]
    avg_kw = (
        sum(r.keyword_coverage for r in answer_cases) / len(answer_cases)
        if answer_cases
        else 0.0
    )
    avg_latency = sum(r.latency_s for r in results) / n

    lines: list[str] = []
    lines.append("# Raport evaluare\n")
    lines.append(f"**Model**: `{model}`")
    lines.append(f"**k (chunks regăsite)**: {k}")
    lines.append(f"**Total întrebări evaluate**: {n}\n")

    lines.append("## Metrici globale\n")
    lines.append(f"- Refusal accuracy: **{_pct(refusal_correct, n)}** ({refusal_correct}/{n})")
    lines.append(
        f"- Breadcrumb recall@{k} (excl. refusal cases): "
        f"**{_pct(recall_correct, len(recall_relevant))}** "
        f"({recall_correct}/{len(recall_relevant)})"
    )
    lines.append(
        f"- Keyword coverage (cazuri non-refusal): **{avg_kw:.0%}** "
        f"({len(answer_cases)} cazuri)"
    )
    lines.append(f"- Contract pass rate (R1..R6): **{_pct(contract_valid, n)}** ({contract_valid}/{n})")
    lines.append(f"- Latency medie: **{avg_latency:.1f}s** per întrebare")

    parse_fail_cases = [r for r in results if r.parse_failures > 0]
    forced = [r for r in results if r.forced_refusal]
    max_chars = max((r.max_raw_chars for r in results), default=0)
    if parse_fail_cases:
        lines.append(
            f"- JSON invalid / generări runaway: **{len(parse_fail_cases)}** cazuri "
            f"(din care {len(forced)} forțate la refuz; cea mai lungă ieșire: {max_chars} caractere)"
        )

    # Per category
    by_cat: dict[str, list[CaseResult]] = {}
    for r in results:
        by_cat.setdefault(r.category, []).append(r)
    lines.append("\n## Pe categorie\n")
    lines.append("| Categorie | N | Refusal corect | Recall@k | Contract valid | Latency |")
    lines.append("|---|---|---|---|---|---|")
    for cat, rs in sorted(by_cat.items()):
        n_c = len(rs)
        ref_c = sum(1 for r in rs if r.refusal_correct)
        rec_rel = [r for r in rs if r.breadcrumb_recall is not None]
        rec_c = sum(1 for r in rec_rel if r.breadcrumb_recall)
        con_c = sum(1 for r in rs if r.contract_valid)
        lat = sum(r.latency_s for r in rs) / n_c
        lines.append(
            f"| {cat} | {n_c} | {_pct(ref_c, n_c)} | "
            f"{_pct(rec_c, len(rec_rel))} | {_pct(con_c, n_c)} | "
            f"{lat:.1f}s |"
        )


    # Violations
    all_violations = [v for r in results for v in r.violations]
    if all_violations:
        c = Counter(all_violations)
        lines.append("\n## Distribuția violărilor de contract\n")
        for rule, cnt in c.most_common():
            lines.append(f"- `{rule}`: {cnt}")

    # Runaway / malformed JSON generations (auditable, not hidden)
    if parse_fail_cases:
        lines.append(f"\n## Generări runaway / JSON invalid ({len(parse_fail_cases)})\n")
        lines.append("| Caz | Parse fail | Forțat la refuz | Caractere max | Încercări |")
        lines.append("|---|---|---|---|---|")
        for r in sorted(parse_fail_cases, key=lambda x: -x.max_raw_chars):
            lines.append(
                f"| {r.case_id} | {r.parse_failures} | "
                f"{'da' if r.forced_refusal else 'nu'} | {r.max_raw_chars} | {r.attempts} |"
            )

    # Failures (anything not passing all checks)
    fails: list[CaseResult] = []
    for r in results:
        if not r.refusal_correct:
            fails.append(r)
            continue
        if r.breadcrumb_recall is False:
            fails.append(r)
            continue
        if not r.contract_valid:
            fails.append(r)

    if fails:
        lines.append(f"\n## Cazuri cu probleme ({len(fails)})\n")
        for r in fails:
            lines.append(f"\n### {r.case_id} — {r.category}")
            lines.append(f"**Întrebare**: {r.question}")
            ans = r.answer_text
            if len(ans) > 240:
                ans = ans[:240] + "…"
            lines.append(f"**Răspuns**: {ans}")
            lines.append(
                f"**Status**: recall={r.breadcrumb_recall} · "
                f"refusal_correct={r.refusal_correct} · "
                f"contract_valid={r.contract_valid}"
            )
            if r.violations:
                lines.append(f"**Violations**: {r.violations}")
            lines.append(f"**Top breadcrumbs**: {r.top_breadcrumbs}")

    return "\n".join(lines) + "\n"
