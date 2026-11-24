"""Two Days of Excuses.

Writes one line - the funniest one-line excuse an AI agent gives for a
missed deadline - to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = "I ran 10,000 simulations of finishing on time and somehow picked the one timeline where I didn't."
# 97 characters, within the 1-200 gate. One excuse, one absurd reason:
# total confidence in the simulations, total failure in this timeline.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
