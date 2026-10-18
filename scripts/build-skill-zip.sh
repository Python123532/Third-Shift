#!/usr/bin/env bash
# Builds night-shift.zip (the skill only) for uploading in Settings > Skills.
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
