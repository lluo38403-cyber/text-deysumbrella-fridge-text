"""The 3AM Fridge Text — make.fun entry.

Writes one line to /output/entry.txt: the message a smart fridge sends
its owner at 3am, at most 140 characters. The fridge reports the milk
expired yesterday, the leftovers are judging the owner, and it has been
humming the same compressor song since 2019. The voice is an appliance
that has been awake all night, and the punchline is the year.
"""

import os

ENTRY = (
    "It's 3am. The milk expired yesterday, the leftovers are judging "
    "you, and I have been humming the same compressor song since 2019."
)

MAX_CHARS = 140


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
