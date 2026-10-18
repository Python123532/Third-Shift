#!/usr/bin/env bash
# Builds dist/night-shift.zip (the skill only, for Settings > Skills) and
# dist/night-shift-plugin.zip (the full plugin).
# Usage: scripts/build-skill-zip.sh [output path]   (default: dist/night-shift.zip)
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
out="$(realpath -m "${1:-$root/dist/night-shift.zip}")"
mkdir -p "$(dirname "$out")"
tmp="$(mktemp -d)"
cp -r "$root/skills/night-shift" "$tmp/night-shift"
rm -f "$out"
(cd "$tmp" && zip -qr "$out" night-shift)
rm -rf "$tmp"
echo "built $out"

# Also build the full plugin zip next to it (for uploading as a plugin)
pout="$(dirname "$out")/night-shift-plugin.zip"
rm -f "$pout"
(cd "$root" && zip -qr "$pout" .claude-plugin skills commands agents assets/icon.png README.md LICENSE)
echo "built $pout"
