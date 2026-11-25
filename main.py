"""One-Line Laugh-Off entry.

Writes exactly one funny line to entry.txt: a single joke that lands
on a cold read, with no setup notes and no explanation.
"""

import os

ENTRY = (
    "My smart fridge emailed me a grocery list, my toaster replied-all, "
    "and now my kitchen has a group chat I am not in."
)

# The sealed scorer accepts 1 to 200 characters; refuse to write an
# entry the gate would reject instead of submitting invalid output.
MAX_CHARS = 200


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = ENTRY + "\n"
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, gate allows 1-{MAX_CHARS}"
        )
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Round-trip verification: read back and confirm the bytes on disk
    # are exactly what was written.
    with open(entry_path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise ValueError("round-trip verification failed: entry.txt mismatch")


if __name__ == "__main__":
    main()
