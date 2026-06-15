# Context — Asistent conversațional proceduri administrative (licență)

Glossary of the ubiquitous language. Definitions only — no implementation detail.

## Domain terms

- **Eveniment de viață (life event)** — top-level citizen scenario the corpus is organized around: *naștere*, *căsătorie*, *locuire*. Each maps to one source page on cezicelegea.ro and one `slug`.
- **Breadcrumb** — the heading path of a section inside a life-event page (e.g. `Nașterea > Tatăl recunoaște copilul`). Identifies *which branch of the decision tree* a piece of text belongs to. Used both as embedding context and as the retrieval-recall ground truth.
- **Secțiune (section)** — a single heading + its body text + bullets, carrying its breadcrumb. Unit produced by the scraper.
- **Chunk (fragment)** — an indexable unit: one section, or a sentence-boundary split of an oversized section, with the breadcrumb prefixed into the embedded text. The corpus has 149 chunks.
- **Output contract (contract de ieșire)** — the verification layer over the LLM answer. Two parts: (1) a typed JSON **schema** the model is forced to emit; (2) **post-hoc rules R1–R6** checking semantic properties (citations present/valid, documents grounded, no fabrication). Distinct from the *form-field* validators, which reuse the same pattern for PDF prefill.
- **Silent failure (eșec silențios)** — a model answer that *looks* valid to the citizen (a fluent answer or a clean refusal) but is unsupported by the sources. The class of error R1–R6 exist to catch; named as future work in Gheorghe et al. (2026).
- **Refusal (refuz controlat)** — the model declining because the sources do not contain the answer (`is_refusal=true`). A *correct* refusal is desired for out-of-domain questions; a *spurious* refusal (sources do contain the answer) is a failure.
- **Gold set (set de aur)** — the manually curated evaluation set. **68 cases** (not 60), used to compute the five metrics.
- **Form prefill (pre-completare)** — separate subsystem: extract form fields from conversation → validate format → render signable PDF. Triggered by `form_offer` / deterministic keyword intent.

## Metrics (evaluation vocabulary)

- **Refusal accuracy** — `is_refusal == should_refuse`.
- **Breadcrumb recall@k** — at least one of the top-k retrieved breadcrumbs contains an expected substring. *Proxy for retrieval correctness only.*
- **Keyword coverage** — fraction of expected keywords present in the answer text. *Proxy for faithfulness, not faithfulness itself.*
- **Contract pass rate** — fraction of cases with zero R1–R6 violations.
- **Silent-failure count** — cases where a contract rule fired. NOTE: a rule firing is *not yet verified* to be a genuinely wrong answer (esp. R4 substring matching); treat as upper bound until human-audited.
