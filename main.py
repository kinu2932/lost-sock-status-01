"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update (<=120 chars) in the voice of a lost sock
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it.
"""

import os

ENTRY = "The dog buried me in the yard. My pair's in the dryer, convinced I left him. Neither of us is coming home."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
