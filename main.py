#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry for 'Weirdest Job Title: Blind Judge Showdown'.

The competition asks for one job title of at most 60 characters and
nothing else. The gate checks that /output/entry.txt is UTF-8 text of
1 to 60 characters and not only white space.

The title is built from its two beats. The role is a real odd job --
the professional mourner, hired to grieve at funerals -- pushed one
step stranger by naming the client: strangers. The twist is the pay
structure, stated like a genuine gig-economy rate card: paid per
convincing sob. The role alone is merely unusual; the rate card is
what makes the person instantly picturable, mid-sob at a stranger's
graveside, invoicing by the tear.

Revision note: the first version held the title as one flat string.
It is now assembled from the role and the twist so each beat can be
checked on its own, and the program re-reads the file after writing
to prove the bytes on disk are the bytes intended.

This program is deterministic: every run writes exactly the same
bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 60

ROLE = "Professional Mourner for Strangers"
TWIST = "Paid Per Convincing Sob"


def build_entry() -> str:
    """Assemble the job title from its role and its pay-structure twist."""
    return f"{ROLE}, {TWIST}"


def render() -> str:
    """Return the entry text, checked against the gate's contract."""
    text = build_entry()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert "\n" not in text and text == text.strip() and text.strip()
    return text


def main() -> None:
    text = render()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry does not match the intended text"


if __name__ == "__main__":
    main()
