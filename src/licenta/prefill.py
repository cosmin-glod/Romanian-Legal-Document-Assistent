"""Form pre-filling: validated schema instance + spec → filled PDF.

Generic, spec-driven renderer. Uses fpdf2 with a TTF font that supports
Romanian diacritics (Arial on macOS by default; override via LICENTA_FONT_PATH).

The renderer assumes the form has already passed its validator — it does not
re-check missing required fields.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

from fpdf import FPDF
from pydantic import BaseModel

from licenta.forms import FormSpec, parse_declaration_date, render_body

DEFAULT_FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_PATH = os.environ.get("LICENTA_FONT_PATH", DEFAULT_FONT_PATH)

log = logging.getLogger(__name__)


class _RomanianPDF(FPDF):
    FONT_NAME = "MainFont"

    def __init__(self) -> None:
        super().__init__()
        if not Path(FONT_PATH).exists():
            raise FileNotFoundError(
                f"Romanian-capable font not found at {FONT_PATH}. "
                "Set LICENTA_FONT_PATH env var to a TTF that supports ă â î ș ț."
            )
        self.add_font(self.FONT_NAME, "", FONT_PATH)
        self.add_font(self.FONT_NAME, "B", FONT_PATH)
        self.set_auto_page_break(auto=True, margin=20)

    def heading(self, line1: str, line2: str | None = None) -> None:
        self.set_font(self.FONT_NAME, size=16)
        self.cell(0, 10, line1, align="C", new_x="LMARGIN", new_y="NEXT")
        if line2:
            self.set_font(self.FONT_NAME, size=12)
            self.cell(0, 8, line2, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(6)

    def para(self, text: str, size: int = 11) -> None:
        self.set_font(self.FONT_NAME, size=size)
        self.multi_cell(0, 7, text.strip())
        self.ln(2)

    def line_label(self, text: str) -> None:
        self.set_font(self.FONT_NAME, size=11)
        self.cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")

    def signature_line(self, label: str, width: float = 90) -> None:
        self.set_font(self.FONT_NAME, size=11)
        self.cell(width, 7, f"{label}: ____________________")


def render(spec: FormSpec, data: BaseModel, out_path: Path) -> Path:
    """Render any form to a signable PDF from its spec + a schema instance."""
    pdf = _RomanianPDF()
    pdf.add_page()
    pdf.heading(spec.title, spec.subtitle)

    values = {f.name: getattr(data, f.name, None) for f in spec.fields}

    for paragraph in render_body(spec, values).split("\n\n"):
        pdf.para(paragraph)

    pdf.ln(4)
    dd = values.get("declaration_date")
    if dd:
        try:
            dd = parse_declaration_date(str(dd)).strftime("%d.%m.%Y")
        except ValueError:
            pass
        pdf.line_label(f"Data: {dd}")
    if values.get("declaration_place"):
        pdf.line_label(f"Locul: {values['declaration_place']}")
    pdf.ln(12)

    for label in spec.signatures:
        pdf.signature_line(label, width=90)
    pdf.ln(8)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))
    log.info("wrote %s", out_path)
    return out_path
