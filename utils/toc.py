import re
import sys

def slugify(title: str) -> str:
    # GitHub-like simple slug
    s = title.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)   # remove punctuation
    s = re.sub(r"\s+", "-", s)       # spaces -> -
    s = re.sub(r"-+", "-", s)        # collapse multiple -
    return s

def generate_toc(md_text: str) -> str:
    lines = md_text.splitlines()
    toc = []

    for line in lines:
        m = re.match(r"^(#{2,6})\s+(.*)$", line)  # only ## to ######
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        anchor = slugify(title)
        indent = "  " * (level - 2)
        toc.append(f"{indent}- [{title}](#{anchor})")

    return "\n".join(toc)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python toc.py your_file.md")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        md_text = f.read()

    print("## Table of Contents")
    print(generate_toc(md_text))