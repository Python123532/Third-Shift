"""Draws the Night Shift icon: a sleepy pixel crescent moon over a night sea.

Writes assets/icon.svg (crisp at any size) and assets/icon.png (512 px).
Run from the repo root: python3 scripts/make_icon.py
"""
from pathlib import Path

N = 32  # grid size
SKY_TOP, SKY_BOT = (11, 16, 40), (24, 36, 80)
STAR = (255, 236, 170)
MOON, MOON_SHADE = (255, 222, 130), (232, 180, 80)
EYE = (110, 70, 30)
BLUSH = (245, 150, 140)
ZZZ = (200, 215, 255)
SEA, SEA_DEEP, WAVE = (22, 52, 100), (14, 34, 70), (60, 105, 170)
GLINT = (255, 222, 130)

grid = [[None] * N for _ in range(N)]


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


# Sky
for y in range(22):
    for x in range(N):
        grid[y][x] = lerp(SKY_TOP, SKY_BOT, y / 21)

# Stars
for x, y in [(3, 3), (8, 6), (28, 13), (4, 15), (29, 18), (20, 3), (12, 2)]:
    grid[y][x] = STAR

# Crescent moon: a disc with a bite taken out of its upper right
cx, cy, r = 14.5, 11.5, 8.2
bx, by, br = 18.5, 8.0, 7.0
for y in range(N):
    for x in range(N):
        inside = (x - cx) ** 2 + (y - cy) ** 2 <= r * r
        bitten = (x - bx) ** 2 + (y - by) ** 2 <= br * br
        if inside and not bitten:
            # shade the outer rim on the lower left
            rim = (x - cx) ** 2 + (y - cy) ** 2 >= (r - 1.3) ** 2 and (x < cx or y > cy + 3)
            grid[y][x] = MOON_SHADE if rim else MOON

# Sleepy closed eye (a small downward arc) and a blush
for x, y in [(8, 13), (9, 14), (10, 14), (11, 14), (12, 14), (13, 13)]:
    grid[y][x] = EYE
grid[16][9] = BLUSH
grid[16][10] = BLUSH

# "z z" drifting up to the right
def z(x0, y0, size):
    for i in range(size):
        grid[y0][x0 + i] = ZZZ
        grid[y0 + size - 1][x0 + i] = ZZZ
        grid[y0 + size - 1 - i][x0 + i] = ZZZ

z(21, 9, 4)
z(26, 2, 5)

# Sea
for y in range(22, N):
    for x in range(N):
        grid[y][x] = lerp(SEA, SEA_DEEP, (y - 22) / 9)
for y, xs in [(23, [2, 3, 4, 20, 21, 22, 23]), (25, [7, 8, 9, 25, 26, 27]),
              (27, [1, 2, 18, 19, 20, 29, 30]), (29, [9, 10, 11, 24, 25])]:
    for x in xs:
        grid[y][x] = WAVE
# Moon reflection, breaking up as it goes down
for y, xs in [(22, range(10, 18)), (23, range(11, 17)), (24, range(12, 16)),
              (26, range(12, 15)), (28, range(13, 15)), (30, [13])]:
    for x in xs:
        grid[y][x] = GLINT

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)

# SVG: one rect per pixel, merged into horizontal runs
rects = []
for y in range(N):
    x = 0
    while x < N:
        c = grid[y][x]
        w = 1
        while x + w < N and grid[y][x + w] == c:
            w += 1
        rects.append(f'<rect x="{x}" y="{y}" width="{w}" height="1" fill="#{c[0]:02x}{c[1]:02x}{c[2]:02x}"/>')
        x += w
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {N} {N}" '
       f'shape-rendering="crispEdges">\n' + "\n".join(rects) + "\n</svg>\n")
(out / "icon.svg").write_text(svg)

from PIL import Image  # noqa: E402

img = Image.new("RGB", (N, N))
for y in range(N):
    for x in range(N):
        img.putpixel((x, y), grid[y][x])
img.resize((512, 512), Image.NEAREST).save(out / "icon.png")
print("wrote", out / "icon.svg", out / "icon.png")
