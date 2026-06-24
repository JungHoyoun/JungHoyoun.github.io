from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "JungHoyoun_CV_EN.md"
OUTPUT = ROOT / "assets" / "files" / "JungHoyoun_CV_EN.pdf"


def inline(text: str) -> str:
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"&lt;(https?://[^&]+)&gt;", r"\1", text)
    return text


def build_pdf() -> None:
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="Name",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=24,
            spaceAfter=3,
            textColor=colors.HexColor("#171717"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Role",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=13,
            spaceAfter=7,
            textColor=colors.HexColor("#525252"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=14,
            spaceBefore=9,
            spaceAfter=5,
            textColor=colors.HexColor("#b4232a"),
            borderWidth=0,
            borderPadding=0,
            borderColor=colors.HexColor("#d8d8d8"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Entry",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=12,
            spaceBefore=6,
            spaceAfter=2,
            textColor=colors.HexColor("#171717"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=11.2,
            spaceAfter=4,
            textColor=colors.HexColor("#171717"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Muted",
            parent=styles["Body"],
            textColor=colors.HexColor("#525252"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CvBullet",
            parent=styles["Body"],
            leftIndent=0,
            firstLineIndent=0,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Small",
            parent=styles["Body"],
            fontSize=8.2,
            leading=10.2,
            textColor=colors.HexColor("#525252"),
            spaceAfter=3,
        )
    )

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=13 * mm,
        leftMargin=13 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Hoyoun Jung CV",
        author="Hoyoun Jung",
    )

    lines = INPUT.read_text(encoding="utf-8").splitlines()
    story = []
    pending_bullets: list[str] = []

    def flush_bullets() -> None:
        nonlocal pending_bullets
        if not pending_bullets:
            return
        for item in pending_bullets:
            story.append(Paragraph("- " + inline(item), styles["CvBullet"]))
        pending_bullets = []

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_bullets()
            continue
        if line.startswith("- "):
            pending_bullets.append(line[2:])
            continue

        flush_bullets()
        if line.startswith("# "):
            story.append(Paragraph(inline(line[2:]), styles["Name"]))
        elif line.startswith("## "):
            story.append(Spacer(1, 1.5))
            story.append(Paragraph(inline(line[3:]), styles["Section"]))
        elif line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), styles["Entry"]))
        elif re.match(r"^\d+\. ", line):
            story.append(Paragraph(inline(line), styles["Small"]))
        elif (
            " / " in line
            or re.match(r"^\d{4}\.\d{2} - ", line)
            or line.startswith("Tech:")
        ):
            story.append(Paragraph(inline(line), styles["Muted"]))
        else:
            story.append(Paragraph(inline(line), styles["Body"]))

    flush_bullets()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
