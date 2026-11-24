"""Two-Sentence Horror — make.fun entry.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic: the same text on every run. No network, no input files,
no secrets, nothing read from outside this repository.
"""

import os

STORY = (
    "The rescue dog I adopted growls at only one thing: "
    "the empty corner of my bedroom. "
    "Last night, the corner growled back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
