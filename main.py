"""Weirdest Job Title entry: one job title, nothing else.

The program writes a single job title to the output directory the
grader provides, as plain UTF-8 text with no trailing newline.
"""

import os

TITLE = "Chief Officer of Checking If the Fridge Light Is On"


def check_title(text: str) -> str:
    """Keep the entry a single short line of real text."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("job title must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("job title must be one line")
    if len(stripped.encode("utf-8")) > 60:
        raise ValueError("job title must fit in 60 bytes")
    return stripped


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(check_title(TITLE))


if __name__ == "__main__":
    main()
