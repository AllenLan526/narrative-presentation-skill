#!/usr/bin/env python3
"""Build the vector PDF derivative of the modular poster demo."""

from __future__ import annotations

import math
import sys
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas


W, H = 1280.0, 1800.0
PAPER = HexColor("#F3EFE6")
INK = HexColor("#1C1B1A")
RED = HexColor("#E4472E")
WHITE = HexColor("#FFFDF7")


def rotated(points, cx, cy, degrees):
    angle = math.radians(degrees)
    cs, sn = math.cos(angle), math.sin(angle)
    out = []
    for x, y in points:
        dx, dy = x - cx, y - cy
        out.append((cx + dx * cs - dy * sn, cy + dx * sn + dy * cs))
    return out


def build(output: Path) -> None:
    page_w, page_h = A3
    scale = min(page_w / W, page_h / H)
    offset_x = (page_w - W * scale) / 2
    offset_y = (page_h - H * scale) / 2

    def px(x):
        return offset_x + x * scale

    def py(y):
        return offset_y + (H - y) * scale

    def polygon(c, points, fill, stroke=None, stroke_width=1):
        path = c.beginPath()
        x0, y0 = points[0]
        path.moveTo(px(x0), py(y0))
        for x, y in points[1:]:
            path.lineTo(px(x), py(y))
        path.close()
        c.setFillColor(fill)
        if stroke:
            c.setStrokeColor(stroke)
            c.setLineWidth(stroke_width * scale)
        c.drawPath(path, fill=1, stroke=1 if stroke else 0)

    def line(c, x1, y1, x2, y2, color=INK, width=1):
        c.setStrokeColor(color)
        c.setLineWidth(width * scale)
        c.line(px(x1), py(y1), px(x2), py(y2))

    def rect(c, x, y, w, h, fill):
        c.setFillColor(fill)
        c.rect(px(x), py(y + h), w * scale, h * scale, fill=1, stroke=0)

    def text(c, x, y, value, size, weight="regular", color=INK, tracking=0, align="left"):
        font = "Helvetica-Bold" if weight in {"bold", "black"} else "Helvetica"
        c.setFont(font, size * scale)
        c.setFillColor(color)
        if tracking:
            t = c.beginText(px(x), py(y))
            t.setFont(font, size * scale)
            t.setFillColor(color)
            t.setCharSpace(tracking * scale)
            t.textLine(value)
            c.drawText(t)
        elif align == "right":
            c.drawRightString(px(x), py(y), value)
        else:
            c.drawString(px(x), py(y), value)

    c = canvas.Canvas(str(output), pagesize=A3, pageCompression=1)
    c.setTitle("Design as Layers - Modular Poster Demo")
    c.setAuthor("Modular vector demo")
    c.setSubject("Editable SVG source with vector PDF derivative")

    rect(c, 0, 0, W, H, PAPER)

    text(c, 88, 106, "MODULAR POSTER / 01", 24, "bold", tracking=4)
    text(c, 82, 252, "DESIGN", 126, "black")
    text(c, 82, 370, "AS LAYERS", 126, "black")
    text(c, 88, 446, "A one-page system that keeps the story", 31, "regular")
    text(c, 88, 486, "tactile - and the parts movable.", 31, "regular")

    polygon(c, [(878, 78), (928, 88), (913, 224), (943, 342), (919, 514),
                (946, 641), (917, 828), (951, 1008), (924, 1186), (953, 1372),
                (927, 1548), (947, 1718), (888, 1728), (905, 1560), (879, 1378),
                (902, 1196), (872, 1016), (900, 832), (868, 646), (896, 510),
                (871, 338), (900, 220)], RED)

    text(c, 88, 616, "EXPLODED POSTER ANATOMY", 21, "bold", tracking=3)

    bands = [
        ([(88, 660), (760, 660), (794, 700), (766, 772), (104, 772), (78, 710)], 0, 480, 730, WHITE, INK,
         "MESSAGE", "LIVE TYPE", "01 / WHAT THE VIEWER REMEMBERS"),
        ([(120, 788), (832, 788), (806, 900), (104, 900), (76, 844)], 0, 522, 854, RED, WHITE,
         "ANCHOR", "NATIVE SHAPE", "02 / THE RELATION THAT HOLDS IT TOGETHER"),
        ([(84, 924), (786, 924), (824, 966), (802, 1052), (104, 1052), (68, 1010)], 0, 500, 990, INK, PAPER,
         "EVIDENCE", "DATA / IMAGE", "03 / THE THING THAT MAKES IT TRUE"),
        ([(110, 1074), (846, 1074), (816, 1190), (98, 1190), (72, 1122)], 0, 520, 1126, WHITE, INK,
         "HANDOFF", "SOURCE + ACTION", "04 / WHERE THE VIEWER CAN KEEP WORKING"),
    ]
    positions = [(150, 714, 720, 714, 150, 746), (156, 842, 770, 842, 156, 874),
                 (160, 980, 750, 980, 160, 1018), (160, 1132, 760, 1132, 160, 1164)]
    for band, pos in zip(bands, positions):
        points, deg, cx, cy, fill, fg, label, value, note = band
        polygon(c, rotated(points, cx, cy, deg), fill, INK if fill == WHITE else None, 4)
        lx, ly, vx, vy, nx, ny = pos
        text(c, lx, ly, label, 36, "black", fg)
        text(c, vx, vy, value, 22, "bold", fg, align="right")
        text(c, nx, ny, note, 15, "bold", fg, tracking=2)

    text(c, 88, 1332, "MODULE LEDGER", 21, "bold", tracking=3)
    line(c, 88, 1354, 710, 1354, INK, 3)
    rows = [
        (1382, "LIVE TYPE", "REWRITE"),
        (1432, "NATIVE SHAPES", "MOVE / RECOLOR"),
        (1482, "DATA MODULE", "REMAP"),
        (1532, "SWAPPABLE IMAGE", "REPLACE"),
    ]
    for y, label, action in rows:
        rect(c, 88, y, 20, 20, RED)
        text(c, 130, y + 18, label, 24, "bold")
        text(c, 486, y + 18, action, 18, "bold")

    text(c, 985, 1388, "THE TEST", 19, "bold", tracking=3)
    text(c, 985, 1434, "MOVE ONE", 30, "black")
    text(c, 985, 1474, "PIECE.", 30, "black")
    text(c, 985, 1514, "THE STORY", 30, "black")
    text(c, 985, 1554, "STILL HOLDS.", 30, "black")

    line(c, 88, 1660, 1192, 1660, INK, 3)
    text(c, 88, 1706, "01 / MODULAR DEMO", 17, "bold", tracking=1.4)

    c.showPage()
    c.save()


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: build_pdf.py output.pdf", file=sys.stderr)
        return 2
    build(Path(sys.argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
