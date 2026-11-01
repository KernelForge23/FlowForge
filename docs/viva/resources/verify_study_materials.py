"""Check source fidelity/coverage and render the generated PDF for visual QA."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / "docs/viva"
QA = Path(os.environ.get("FLOWFORGE_VIVA_QA_DIR", str(ROOT / "tmp/pdfs/flowforge-viva")))
QA.mkdir(parents=True, exist_ok=True)

coverage = json.loads((DEST / "resources/source-coverage.json").read_text())
appendix = (DEST / "FlowForge-Line-by-Line.md").read_text(encoding="utf-8")
for entry in coverage["files"]:
    raw = (ROOT / entry["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == entry["sha256"], entry["path"]
    section = appendix.split("## " + entry["path"] + "\n", 1)[1].split("\n## ", 1)[0]
    notes = [int(x) for x in re.findall(r"^\*\*L(\d+)\.\*\*", section, re.M)]
    assert notes == list(range(1, entry["lines"] + 1)), entry["path"]
    source = re.findall(r"^\d{4} \| (.*)$", section, re.M)
    assert source == raw.decode("utf-8-sig").splitlines(), entry["path"]

master = (DEST / "FlowForge-Master-Guide.md").read_text(encoding="utf-8")
groups = re.findall(r"(?:^\|[^\n]*\n)+", master, re.M)
for group in groups:
    widths = {len(re.split(r"(?<!\\)\|", s.strip().strip("|"))) for s in group.splitlines()}
    assert len(widths) == 1, (widths, group)
questions = re.findall(r"^\*\*(\d+)\. ", master, re.M)
assert list(map(int, questions)) == list(range(1, 101))
chapters = re.findall(r"^## (.*)", master, re.M)
assert len(chapters) == 28

pdf = ROOT / "output/pdf/FlowForge-Viva-Master-Guide.pdf"
reader = PdfReader(pdf)
full = "\n".join(p.extract_text() or "" for p in reader.pages)
normalized = re.sub(r"\s+", " ", full)
for chapter in chapters:
    assert re.sub(r"\s+", " ", chapter) in normalized, chapter
assert len(reader.outline) == 29
assert "ZZCODE" not in full and "\ufffd" not in full

poppler = Path("C:/Users/shaha/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin")
expected_pages = [QA / f"page-{i:0{len(str(len(reader.pages)))}}.png" for i in range(1, len(reader.pages) + 1)]
existing = [p for p in expected_pages if p.exists()]
if len(existing) != len(reader.pages) or min((p.stat().st_mtime for p in existing), default=0) < pdf.stat().st_mtime:
    subprocess.run([str(poppler / "pdftoppm.exe"), "-r", "85", "-png", str(pdf), str(QA / "page")], check=True, capture_output=True)
# pypdf does not reliably resolve every multiline text transform for this PDF.
# Use the rendered pixels to check page-edge clearance; inspect full layouts
# separately for internal collisions and glyph extent/readability.
outside = []

pages = [p for p in expected_pages if p.exists()]
assert len(pages) == len(reader.pages)
thumb_w, thumb_h = 177, 251
sheet = Image.new("RGB", (6 * (thumb_w + 12), 8 * (thumb_h + 25)), "#d7dfe8")
draw = ImageDraw.Draw(sheet)
font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
for i, p in enumerate(pages):
    im = Image.open(p).convert("RGB")
    w, h = im.size
    for edge in [(0, 0, 35, h), (w - 35, 0, w, h), (0, 0, w, 12), (0, h - 12, w, h)]:
        if im.crop(edge).convert("L").getextrema()[0] < 245:
            outside.append((i + 1, edge))
    im.thumbnail((thumb_w, thumb_h))
    x, y = (i % 6) * (thumb_w + 12) + 6, (i // 6) * (thumb_h + 25) + 5
    sheet.paste(im, (x, y))
    draw.text((x, y + thumb_h + 1), str(i + 1), font=font, fill="#10243a")
sheet.save(QA / "contact-sheet.png")
assert not outside, outside
result = {"source_fingerprints_verified": len(coverage["files"]), "source_lines_reproduced_and_annotated": coverage["total_lines"], "table_shapes_consistent": True, "viva_questions_sequential": 100, "chapters": 28, "pdf_pages_rendered": len(pages), "pdf_pages_with_nonwhite_outer_edges": len(outside), "bounds_check_scope": "Rendered outer page-edge clearance; full layouts receive separate visual review for internal collisions and readability.", "contact_sheet": str(QA / "contact-sheet.png")}
(DEST / "resources/verification-results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
