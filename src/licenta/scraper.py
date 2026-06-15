"""Scraper for cezicelegea.ro life-event pages.

Server-rendered HTML, no auth, robots.txt permits all crawlers.
Each life event is a single deep page with nested h1→h4 headings forming a
decision tree. We flatten it into a list of sections, each carrying its
breadcrumb path so chunks remain self-locating after retrieval.
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag

BASE = "https://cezicelegea.ro"
USER_AGENT = "Mozilla/5.0 (licenta-thesis-scraper; contact: glodcosmin@gmail.com)"
LIFE_EVENTS = [
    ("nastere", "Nașterea"),
    ("casatorie", "Căsătoria"),
    ("locuire", "Locuirea"),
]

DONATION_MARKER = "trimite un sms cu textul PUTEM"

log = logging.getLogger(__name__)


@dataclass
class Section:
    heading: str
    level: int
    breadcrumb: list[str]
    text: str
    bullets: list[str] = field(default_factory=list)


@dataclass
class LifeEventDoc:
    slug: str
    title: str
    url: str
    intro: str
    sections: list[Section]


def fetch(url: str) -> str:
    log.info("GET %s", url)
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    resp.raise_for_status()
    return resp.text


def _clean(text: str) -> str:
    return " ".join(text.split())


def _norm_tokens(s: str) -> set[str]:
    return set(s.lower().split())


def _compatible(label: str, heading: str) -> bool:
    """A tab-button label names a section if it matches the section heading.

    The site abbreviates some button labels relative to the full heading (e.g.
    button ``Vreau să transcriu certificatul la autoritățile române`` vs heading
    ``...certificatul de naștere la autoritățile române``), so exact equality is
    too strict. We accept exact match, prefix containment, or high token overlap
    (Jaccard ≥ 0.7) — loose enough to absorb abbreviations, tight enough to keep
    siblings like ``... român`` / ``... străin`` distinct."""
    a, b = label.lower().strip(), heading.lower().strip()
    if a == b or a in b or b in a:
        return True
    ta, tb = _norm_tokens(a), _norm_tokens(b)
    if not ta or not tb:
        return False
    return len(ta & tb) / len(ta | tb) >= 0.7


def _is_donation_block(node: Tag) -> bool:
    """The site repeats a donation pitch as an h3 across nearly every leaf
    section. It's noise for RAG — drop it everywhere."""
    return DONATION_MARKER in node.get_text()


def parse(html: str, slug: str, title: str, url: str) -> LifeEventDoc:
    """Reconstruct the decision tree from the page's pre-order DFS layout.

    The site is an Alpine.js state machine: every *content* node is an ``<h2>``
    (so heading level alone is flat and useless), while the *choices* leading to
    its children are emitted right after it as ``<h3>`` tab buttons. The whole
    tree is serialised depth-first (pre-order) in document order. We rebuild the
    real breadcrumb with a stack: each content node records the child labels
    declared by its tab buttons; when a later ``<h2>`` matches a label expected
    by some node on the stack, we pop down to it and nest underneath.
    """
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main", id="content")
    if main is None:
        raise ValueError(f"no <main id=content> in {url}")

    h1 = main.find("h1")
    page_title = _clean(h1.get_text()) if h1 else title
    intro_tag = main.find("h4")
    intro = _clean(intro_tag.get_text()) if intro_tag else ""

    sections: list[Section] = []
    # Stack of open tree nodes: {"breadcrumb": [...], "children": set[str]}.
    stack: list[dict] = []
    current: Section | None = None
    current_node: dict | None = None
    root_seen = False

    def flush():
        nonlocal current
        if current is not None and (current.text.strip() or current.bullets):
            sections.append(current)
        current = None

    for node in main.descendants:
        if not isinstance(node, Tag):
            continue
        name = node.name

        # h3 inside a <button> is a navigation tab: it names a *child* of the
        # current content node, not a section of its own.
        if name == "h3" and node.find_parent("button") is not None:
            label = _clean(node.get_text())
            if not label or _is_donation_block(node) or label.lower() == "înapoi":
                continue
            if current_node is not None:
                current_node["children"].add(label)
            continue

        # Content node: an <h2>, or a stray non-button <h3>.
        if name == "h2" or (name == "h3" and node.find_parent("button") is None):
            if _is_donation_block(node):
                continue
            heading = _clean(node.get_text())
            if not heading:
                continue
            flush()

            if not root_seen:
                # First content node is the page's root question; it represents
                # the event itself, so its breadcrumb is just the event title.
                root_seen = True
                breadcrumb = [page_title]
            else:
                # Find the deepest open ancestor that declared this as a child,
                # then pop everything below it. On no match we keep the current
                # context (do NOT empty the stack) to avoid breaking later
                # siblings — a single abbreviated label would otherwise cascade.
                idx = next(
                    (
                        i
                        for i in range(len(stack) - 1, -1, -1)
                        if any(_compatible(c, heading) for c in stack[i]["children"])
                    ),
                    None,
                )
                if idx is not None:
                    del stack[idx + 1:]
                breadcrumb = stack[-1]["breadcrumb"] + [heading]

            current_node = {"breadcrumb": breadcrumb, "children": set()}
            stack.append(current_node)
            current = Section(
                heading=heading,
                level=len(breadcrumb),
                breadcrumb=breadcrumb,
                text="",
            )
        elif name == "p" and current is not None:
            t = _clean(node.get_text())
            if t:
                current.text += (" " if current.text else "") + t
        elif name == "li" and current is not None:
            t = _clean(node.get_text())
            if t:
                current.bullets.append(t)

    flush()

    sections = _dedupe_sections(sections)
    return LifeEventDoc(
        slug=slug,
        title=page_title,
        url=url,
        intro=intro,
        sections=sections,
    )


def _dedupe_sections(sections: list[Section]) -> list[Section]:
    """Drop sections that are pure-duplicate (same breadcrumb + text). The
    decision-tree layout sometimes re-emits identical leaves under different
    branches; preserving them inflates the index without adding info."""
    seen: set[tuple] = set()
    out: list[Section] = []
    for s in sections:
        key = (tuple(s.breadcrumb), s.text, tuple(s.bullets))
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
    return out


def scrape_all(out_path: Path, delay_s: float = 1.0) -> None:
    docs: list[dict] = []
    for slug, title in LIFE_EVENTS:
        url = f"{BASE}/ro/{slug}"
        html = fetch(url)
        doc = parse(html, slug, title, url)
        log.info(
            "  %s: %d sections, %d total bullets, ~%d chars",
            slug,
            len(doc.sections),
            sum(len(s.bullets) for s in doc.sections),
            sum(len(s.text) for s in doc.sections),
        )
        docs.append(asdict(doc))
        time.sleep(delay_s)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(docs, ensure_ascii=False, indent=2))
    log.info("wrote %s", out_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    scrape_all(Path(__file__).resolve().parents[2] / "data" / "cezicelegea_dump.json")

