#!/usr/bin/env python3
"""Write one newly coined English word and its definition to /output/entry.txt.

Draft (v1): "cancelight" — a blend of "cancel" and "delight" for the
quiet pleasure of a plan being cancelled, freeing an evening you
secretly wanted to yourself.

Revision (v2): "quiet delight ... freeing an evening you secretly
wanted to yourself" was wordy and soft. The revision swaps in
"secret relief" — it names the guilt-tinged joy everyone recognises
but will not admit — and ends on "the evening is suddenly yours
again", which is shorter, punchier, and lands in one reading instead
of trailing off in a subordinate clause.
"""

from pathlib import Path

TEXT = (
    "cancelight — the secret relief when a plan is cancelled and "
    "the evening is suddenly yours again."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
