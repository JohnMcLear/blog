#!/usr/bin/env python3
"""Check all blog posts for duplicate titles.

Scans every posts/*/index.md file, extracts the title from the YAML front
matter, and writes a map of duplicated titles to _data/duplicate_posts.yml.
"""

import sys
import yaml
from pathlib import Path

POSTS_DIR = Path(__file__).parent / "posts"
DATA_DIR = Path(__file__).parent / "_data"
OUTPUT_FILE = DATA_DIR / "duplicate_posts.yml"


def get_front_matter(post_dir: Path) -> dict:
    """Parse and return the YAML front matter of a post, or an empty dict."""
    index_md = post_dir / "index.md"
    if not index_md.exists():
        return {}
    content = index_md.read_text(encoding="utf-8", errors="replace")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(content[3:end]) or {}
    except yaml.YAMLError:
        return {}


def main() -> int:
    DATA_DIR.mkdir(exist_ok=True)

    post_dirs = sorted(d for d in POSTS_DIR.iterdir() if d.is_dir())
    total = len(post_dirs)
    print(f"Scanning {total} posts for duplicate titles …")

    # Map title -> list of post slugs
    title_to_posts: dict[str, list[str]] = {}
    for post_dir in post_dirs:
        fm = get_front_matter(post_dir)
        title = fm.get("title", "")
        if not title:
            continue
        slug = f"/posts/{post_dir.name}/"
        title_to_posts.setdefault(title, []).append(slug)

    # Keep only titles that appear more than once
    duplicates = {
        title: slugs
        for title, slugs in title_to_posts.items()
        if len(slugs) > 1
    }

    if duplicates:
        print(f"\nFound {len(duplicates)} duplicate title(s):")
        for title, slugs in sorted(duplicates.items()):
            print(f"  {title!r}")
            for slug in slugs:
                print(f"    - {slug}")
    else:
        print("No duplicate titles found.")

    data = {
        "duplicates": [
            {"title": title, "posts": sorted(slugs)}
            for title, slugs in sorted(duplicates.items())
        ]
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        yaml.dump(data, fh, default_flow_style=False, allow_unicode=True)

    print(f"\nResults written to {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
