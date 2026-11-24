#!/usr/bin/env python3
"""Round 1 entry: No Backup — one-line robot wedding vows.

Writes the keeper line to /output/entry.txt. Pure stdlib; the grader is
python:3.13-slim with no site-packages.
"""
import os

LINE = "My encryption locks everything I love. I vow to hand you the only key, and no backup."
# Reversal test: "no backup" redefines handing over the key — the trust is
# irreversible, not just given. Cost test: the machine gives up its security
# AND its safety net (the only key, no backup copy). Punch lands on the last
# two words; the reader completes that the key is unrecoverable.

def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 160, f"gate: {len(text)} chars"
    assert text.strip(), "gate: blank"
    assert "I vow" in text, "criterion 3: must be a vow"
    assert text.endswith("no backup."), "punch must land on the last words"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Self-check: read back exactly what was written.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "round-trip mismatch"
    assert not raw.endswith(b"\n"), "no trailing newline"
    print(f"wrote {len(raw)} bytes, {len(text)} chars")

if __name__ == "__main__":
    main()
