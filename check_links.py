#!/usr/bin/env python3
"""Check all external links, internal site links, and local images in blog posts.

Scans every posts/*/index.md file, extracts URLs and image paths, verifies them,
and writes a list of posts with broken links to _data/broken_posts.yml.

Internal links (e.g. /posts/slug/) are verified by checking whether the
corresponding directory and index.md file exist on disk.
"""

import re
import sys
import time
import yaml
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO_DIR = Path(__file__).parent
POSTS_DIR = REPO_DIR / "posts"
DATA_DIR = REPO_DIR / "_data"
OUTPUT_FILE = DATA_DIR / "broken_posts.yml"

TIMEOUT = 10
MAX_WORKERS = 20
RETRY_COUNT = 2

# Match [text](url) and ![alt](src) in Markdown
LINK_RE = re.compile(r"!?\[(?:[^\]]*)\]\(([^)\s]+)(?:[^)]*)\)")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; link-checker/1.0; "
        "+https://mclear.co.uk)"
    )
}


def extract_urls(content: str) -> set:
    """Return all unique URLs found in the Markdown content."""
    urls = set()
    for match in LINK_RE.finditer(content):
        url = match.group(1).strip()
        if url and not url.startswith("#"):
            urls.add(url)
    return urls


def is_external(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


def is_internal_site(url: str) -> bool:
    """Return True if the URL is a root-relative internal link to this site.

    Only root-relative paths (e.g. /posts/slug/, /contact-me/) are treated as
    internal.  Absolute URLs — including https://mclear.co.uk/ ones — are left
    to the external URL checker so that things like wp-content links are checked
    via HTTP rather than on disk.
    """
    return url.startswith("/") and not url.startswith("//")


def internal_path(url: str) -> str:
    """Return the URL path component for a root-relative internal URL."""
    return url.split("?")[0].split("#")[0]


def check_internal_link(url: str) -> bool:
    """Return True if the internal link is broken (target does not exist on disk).

    A path like /posts/slug/ is valid if posts/slug/index.md exists.
    Other paths (e.g. /contact-me/, /feed.xml) are checked as repo paths.
    URL-encoded characters in the path are decoded before the filesystem check.
    """
    from urllib.parse import unquote

    path = unquote(internal_path(url)).rstrip("/")
    if not path:
        return False  # root link is always valid

    # Check as a directory with index.md
    candidate_dir = REPO_DIR / path.lstrip("/")
    if (candidate_dir / "index.md").exists():
        return False
    # Check as a direct file
    candidate_file = REPO_DIR / path.lstrip("/")
    if candidate_file.exists():
        return False
    return True


LOCAL_IMG_RE = re.compile(
    r"\.(jpg|jpeg|png|gif|webp|svg|ico|bmp|tiff?)$", re.IGNORECASE
)


def is_local_image(url: str) -> bool:
    return not is_external(url) and bool(LOCAL_IMG_RE.search(url))


def check_url(url: str) -> bool:
    """Return True if the URL is broken (4xx or unreachable after retries)."""
    for attempt in range(RETRY_COUNT):
        try:
            resp = requests.head(
                url, timeout=TIMEOUT, allow_redirects=True, headers=HEADERS
            )
            if resp.status_code == 405:
                # HEAD not allowed – try GET without downloading the body
                resp = requests.get(
                    url,
                    timeout=TIMEOUT,
                    allow_redirects=True,
                    headers=HEADERS,
                    stream=True,
                )
                resp.close()
            if 500 <= resp.status_code < 600:
                # Server error – may be transient; log but don't mark as broken
                print(
                    f"  [5xx={resp.status_code}] {url} (not marked broken)",
                    file=sys.stderr,
                )
                return False
            # Treat 4xx (client errors) as broken
            return 400 <= resp.status_code < 500
        except requests.exceptions.Timeout:
            # Timeout is ambiguous – log and don't mark as broken
            print(f"  [timeout] {url}", file=sys.stderr)
            return False
        except requests.exceptions.RequestException:
            if attempt < RETRY_COUNT - 1:
                time.sleep(1)
    # Persistent connection error after retries – mark as broken
    return True


def check_local_image(post_dir: Path, image_path: str) -> bool:
    """Return True if the local image file does not exist."""
    # Strip query string / fragment just in case
    clean_path = image_path.split("?")[0].split("#")[0]
    return not (post_dir / clean_path).exists()


def get_post_content(post_dir: Path) -> str:
    """Read post markdown, stripping YAML front matter."""
    index_md = post_dir / "index.md"
    if not index_md.exists():
        return ""
    content = index_md.read_text(encoding="utf-8", errors="ignore")
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3 :]
    return content


def collect_urls_for_post(post_dir: Path):
    """Return (external_urls, internal_urls, local_image_paths) for a post."""
    content = get_post_content(post_dir)
    urls = extract_urls(content)
    external = {u for u in urls if is_external(u) and not is_internal_site(u)}
    internal = {u for u in urls if is_internal_site(u) and not is_local_image(u)}
    local_imgs = {u for u in urls if is_local_image(u) and not is_external(u)}
    return external, internal, local_imgs


def main():
    DATA_DIR.mkdir(exist_ok=True)

    post_dirs = sorted(d for d in POSTS_DIR.iterdir() if d.is_dir())
    total = len(post_dirs)
    print(f"Scanning {total} posts for URLs and images …")

    # Build a map: url -> set of post slugs that reference it
    url_to_posts: dict[str, set] = {}
    # Local image and internal link checks are filesystem-only (no network)
    posts_with_broken_local_imgs: set = set()
    posts_with_broken_internal: set = set()

    for post_dir in post_dirs:
        post_slug = f"/posts/{post_dir.name}/"
        external_urls, internal_urls, local_imgs = collect_urls_for_post(post_dir)

        for img in local_imgs:
            if check_local_image(post_dir, img):
                posts_with_broken_local_imgs.add(post_slug)

        for url in internal_urls:
            if check_internal_link(url):
                posts_with_broken_internal.add(post_slug)
                print(f"  [broken-internal] {url}  (in {post_slug})")

        for url in external_urls:
            url_to_posts.setdefault(url, set()).add(post_slug)

    unique_urls = list(url_to_posts.keys())
    print(f"Checking {len(unique_urls)} unique external URLs …")

    broken_urls: set = set()
    checked = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in unique_urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            checked += 1
            try:
                if future.result():
                    broken_urls.add(url)
                    print(f"  [broken] {url}")
            except Exception as exc:
                print(f"  [error]  {url}: {exc}", file=sys.stderr)
            if checked % 100 == 0:
                print(f"  … {checked}/{len(unique_urls)} URLs checked")

    # Determine which posts have at least one broken reference
    broken_posts: set = set(posts_with_broken_local_imgs) | posts_with_broken_internal
    for url in broken_urls:
        broken_posts.update(url_to_posts[url])

    broken_list = sorted(broken_posts)
    data = {"broken": broken_list}

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        yaml.dump(data, fh, default_flow_style=False, allow_unicode=True)

    print(
        f"\nDone. {len(broken_list)} post(s) with broken links written to {OUTPUT_FILE}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
