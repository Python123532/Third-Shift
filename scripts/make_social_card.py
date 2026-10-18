"""Draws the GitHub social preview card (1280x640) in the icon's pixel style.

The night scene is drawn on a 64x32 pixel grid at 20 px per pixel; the text
sits in the sky on the right. Everything important stays inside GitHub's
40 px safe border. Run from the repo root: python3 scripts/make_social_card.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H, PX = 1280, 640, 20
GW, GH = W // PX, H // PX  # 64 x 32
SAFE = 40

SKY_TOP, SKY_BOT = (11, 16, 40), (24, 36, 80)
STAR = (255, 236, 170)
MOON, MOON_SHADE = (255, 222, 130), (232, 180, 80)
ZZZ = (200, 215, 255)
SEA, SEA_DEEP, WAVE = (22, 52, 100), (14, 34, 70), (60, 105, 170)
GLINT = (255, 222, 130)
TEXT, SUBTEXT, ACCENT = (250, 246, 232), (196, 206, 236), (255, 222, 130)
HORIZON = 24  # first sea row


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


g = [[None] * GW for _ in range(GH)]

for y in range(HORIZON):
    for x in range(GW):
        g[y][x] = lerp(SKY_TOP, SKY_BOT, y / (HORIZON - 1))

for x, y in [(4, 4), (9, 2), (3, 15), (26, 18), (33, 2), (44, 3),
             (58, 2), (61, 9), (38, 20), (60, 21), (21, 21)]:
    g[y][x] = STAR

# Crescent moon (same shape as the icon), on the left
cx, cy, r = 13.5, 12.5, 8.2
bx, by, br = 17.5, 9.0, 7.0
for y in range(GH):
    for x in range(GW):
        inside = (x - cx) ** 2 + (y - cy) ** 2 <= r * r
        bitten = (x - bx) ** 2 + (y - by) ** 2 <= br * br
        if inside and not bitten:
            rim = (x - cx) ** 2 + (y - cy) ** 2 >= (r - 1.3) ** 2 and (x < cx or y > cy + 3)
            g[y][x] = MOON_SHADE if rim else MOON


def z(x0, y0, size):
    for i in range(size):
        g[y0][x0 + i] = ZZZ
        g[y0 + size - 1][x0 + i] = ZZZ
        g[y0 + size - 1 - i][x0 + i] = ZZZ


z(19, 11, 4)
z(22, 4, 5)

# Sea
for y in range(HORIZON, GH):
    for x in range(GW):
        g[y][x] = lerp(SEA, SEA_DEEP, (y - HORIZON) / (GH - HORIZON - 1))
for y, xs in [(25, [3, 4, 5, 22, 23, 24, 25, 40, 41, 42, 55, 56, 57, 58]),
              (27, [8, 9, 10, 28, 29, 30, 47, 48, 49, 61, 62]),
              (29, [1, 2, 18, 19, 20, 35, 36, 37, 52, 53]),
              (31, [10, 11, 12, 26, 27, 44, 45, 46, 59, 60])]:
    for x in xs:
        g[y][x] = WAVE
for y, xs in [(24, range(9, 17)), (25, range(10, 16)), (26, range(11, 15)),
              (28, range(11, 14)), (30, range(12, 14))]:
    for x in xs:
        g[y][x] = GLINT

img = Image.new("RGB", (GW, GH))
for y in range(GH):
    for x in range(GW):
        img.putpixel((x, y), g[y][x])
img = img.resize((W, H), Image.NEAREST)

# Text, in the sky to the right of the moon
d = ImageDraw.Draw(img)
fonts = Path("/usr/share/fonts/opentype/inter")
title_f = ImageFont.truetype(str(fonts / "Inter-ExtraBold.otf"), 104)
sub_f = ImageFont.truetype(str(fonts / "Inter-Medium.otf"), 31)
tag_f = ImageFont.truetype(str(fonts / "Inter-SemiBold.otf"), 26)

left = 31 * PX  # x = 620
right = W - SAFE - 20
d.text((left, 92), "Third Shift", font=title_f, fill=TEXT)
lines = ["A task queue in a Google Sheet that", "Claude works through while you sleep."]
y = 232
for line in lines:
    d.text((left + 4, y), line, font=sub_f, fill=SUBTEXT)
    y += 44
d.text((left + 4, y + 26), "TASK create  ·  TASK queue  ·  TASK review", font=tag_f, fill=ACCENT)

# Check the text fits inside the safe area and above the sea
for text, f, x0, y0 in [("Third Shift", title_f, left, 92),
                        (lines[1], sub_f, left + 4, 276),
                        ("TASK create  ·  TASK queue  ·  TASK review", tag_f, left + 4, y + 26)]:
    bb = d.textbbox((x0, y0), text, font=f)
    assert bb[2] <= right and bb[3] <= HORIZON * PX - 16, (text, bb)

out = Path(__file__).resolve().parent.parent / "assets" / "social-preview.png"
img.save(out)
print("wrote", out)
