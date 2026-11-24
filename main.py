"""Time Machine Warning Label — make.fun entry.

Writes the competition entry (a single one-line warning label for a
time machine) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
and self-verifies the gate: UTF-8 text, 1-120 characters, a single line,
not whitespace-only. Exits non-zero on any failure.

Python standard library only. Deterministic.
"""

import os
import sys

ENTRY = "WARNING: If you meet yourself, remain calm. You have done this before."

MAX_CHARS = 120


def validate(text: str) -> None:
    """Enforce the competition gate; raise ValueError on failure."""
    # Must be valid UTF-8 (str is already decoded; re-encode to prove it).
    text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-verify what was written, byte for byte.
    with open(out_path, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    validate(written)
    if written != ENTRY:
        raise ValueError("written entry does not match ENTRY constant")
    print(f"Wrote {out_path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
