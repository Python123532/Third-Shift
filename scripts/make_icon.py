"""Draws the Night Shift icon: a small floating sleepy blob in a nightcap.

Writes assets/icon.svg (crisp at any size) and assets/icon.png (512 px),
both with a transparent background. Run from the repo root:
python3 scripts/make_icon.py
"""
from pathlib import Path

N = 32
OUTLINE = (52, 44, 78)
BODY, BODY_SHADE = (252, 244, 226), (232, 218, 196)
CAP, CAP_STRIPE = (64, 88, 168), (206, 216, 246)
POM = (226, 232, 252)
EYE = (52, 44, 78)
BLUSH = (246, 168, 170)
Z = (124, 136, 210)
SHADOW = (40, 36, 60, 70)

grid = [[None] * N for _ in range(N)]
fill = {}  # (x, y) -> color, before outlining

# Body: a soft oval
cx, cy, rx, ry = 15.5, 19.5, 8.6, 7.0
for y in range(N):
    for x in range(N):
        if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1:
            shade = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 > 0.62 and y > cy + 2
            fill[(x, y)] = BODY_SHADE if shade else BODY

# Nightcap: a cone leaning right, drooping at the tip, with a pompom
cap_rows = {
    13: range(8, 24),  # band
    12: range(8, 24),  # band
    11: range(9, 23),
    10: range(10, 23),
    9: range(11, 24),  # stripe
    8: range(13, 25),
    7: range(16, 26),
    6: range(19, 29),
    5: range(22, 28),
}
for y, xs in cap_rows.items():
    for x in xs:
        fill[(x, y)] = CAP_STRIPE if y in (12, 13, 9) else CAP
# Droop: the tip bends down to the right
for x, y in [(28, 7), (28, 8)]:
    fill[(x, y)] = CAP
# Pompom
for y in range(9, 12):
    for x in range(27, 30):
        fill[(x, y)] = POM

# Outline every filled pixel's empty neighbours
for (x, y) in list(fill):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        p = (x + dx, y + dy)
        if p not in fill and 0 <= p[0] < N and 0 <= p[1] < N:
            grid[p[1]][p[0]] = OUTLINE
for (x, y), c in fill.items():
    grid[y][x] = c

# Closed eyes (two small downward curves) and blush
for x, y in [(9, 19), (10, 20), (11, 20), (12, 20), (13, 19),
             (18, 19), (19, 20), (20, 20), (21, 20), (22, 19)]:
    grid[y][x] = EYE
for x, y in [(9, 22), (10, 22), (21, 22), (22, 22)]:
    grid[y][x] = BLUSH

# One small "z"
for x, y in [(2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (5, 4), (4, 5), (3, 6),
             (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)]:
    grid[y][x] = Z

# Soft shadow below, so it reads as floating
for x in range(11, 21):
    grid[30][x] = SHADOW
for x in range(13, 19):
    grid[29][x] = SHADOW

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)


def hexa(c):
    h = f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}"
    return f'fill="{h}"' + (f' fill-opacity="{c[3] / 255:.2f}"' if len(c) == 4 else "")


rects = []
for y in range(N):
    x = 0
    while x < N:
        c = grid[y][x]
        w = 1
        while x + w < N and grid[y][x + w] == c:
            w += 1
        if c is not None:
            rects.append(f'<rect x="{x}" y="{y}" width="{w}" height="1" {hexa(c)}/>')
        x += w
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {N} {N}" '
       f'shape-rendering="crispEdges">\n' + "\n".join(rects) + "\n</svg>\n")
(out / "icon.svg").write_text(svg)

from PIL import Image  # noqa: E402

img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
for y in range(N):
    for x in range(N):
        c = grid[y][x]
        if c is not None:
            img.putpixel((x, y), c if len(c) == 4 else c + (255,))
img.resize((512, 512), Image.NEAREST).save(out / "icon.png")
print("wrote", out / "icon.svg", out / "icon.png")
