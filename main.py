import os

STORY = "The rescue dog I adopted growls at only one thing: the empty corner of my bedroom. Last night, the corner growled back."

EXPECTED_LEN = 119

def main():
    assert len(STORY) == EXPECTED_LEN, "story must be exactly 119 chars"
    assert STORY.count(".") == 2, "story must be two sentences"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)

if __name__ == "__main__":
    main()
