# -*- coding: utf-8 -*-
"""Generate the Manifest guide from `content.py`.

    python build.py

Writes, into this directory:
  index.html and one page per topic  — the site
  assets/search-index.js             — every section, for client-side search
  manifest-guide.html                — the whole guide as one downloadable file
  .nojekyll                          — so GitHub Pages serves assets/ verbatim

Why generated rather than hand-written: the site, the search index and the
download all say the same things, and three hand-maintained copies of the same
sentence is three chances for two of them to be wrong. There is one home for the
content and everything else is derived from it.

The search index is a .js file assigning a global, not .json fetched at runtime,
so search still works when somebody has downloaded the guide and is reading it
from a file:// path with no server and no network.
"""

import html
import json
import os
import re
import unicodedata
from datetime import date

import content

HERE = os.path.dirname(os.path.abspath(__file__))
UPDATED = date.today().strftime("%d %B %Y").lstrip("0")


# --------------------------------------------------------------------- helpers

def strip_tags(markup):
    """Readable text from a body, for the search index and for excerpts."""
    text = re.sub(r"<[^>]+>", " ", markup)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def resolve(markup, single_file=False):
    """Fill placeholders and, for the one-file build, flatten cross-page links.

    In the site, `data.html#server` is a real file. In the download there is
    only one file, so those become plain fragment links -- otherwise every
    cross-reference in the downloaded copy is a dead link to a file the reader
    does not have.
    """
    markup = markup.replace("%POLICY%", content.POLICY_URL)
    if single_file:
        markup = re.sub(r'href="([a-z]+)\.html#([a-z-]+)"', r'href="#\2"', markup)
        markup = re.sub(r'href="([a-z]+)\.html"', r'href="#\1"', markup)
    return markup


def nav_markup(current):
    items = []
    for page in content.PAGES:
        slug = page["slug"]
        href = "index.html" if slug == "index" else f"{slug}.html"
        here = ' aria-current="page"' if slug == current else ""
        items.append(f'<li><a href="{href}"{here}>{html.escape(page["title"])}</a></li>')
    return "<ul class='nav-list'>" + "".join(items) + "</ul>"


def toc_markup(page):
    if len(page["sections"]) < 2:
        return ""
    items = "".join(
        f'<li><a href="#{s["id"]}">{html.escape(s["heading"])}</a></li>'
        for s in page["sections"]
    )
    return f"<nav class='toc' aria-label='On this page'><p class='toc-h'>On this page</p><ul>{items}</ul></nav>"


# ----------------------------------------------------------------- the shell

def shell(title, description, body, current, depth_note=""):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — {content.PRODUCT} guide</title>
<meta name="description" content="{html.escape(description)}">
<link rel="stylesheet" href="assets/guide.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="masthead">
  <div class="wrap masthead-in">
    <a class="brand" href="index.html">
      <span class="brand-name">{content.PRODUCT}</span>
      <span class="brand-sub">guide</span>
    </a>
    <div class="tools">
      <label class="search" for="q">
        <span class="vh">Search the guide</span>
        <input id="q" type="search" placeholder="Search the guide" autocomplete="off"
               spellcheck="false" aria-controls="results" aria-expanded="false">
      </label>
      <a class="dl" href="manifest-guide.html" download>Download</a>
    </div>
  </div>
  <div id="results" class="results" role="region" aria-live="polite" hidden></div>
</header>

<div class="wrap shell">
  <nav class="sidebar" aria-label="Guide">{nav_markup(current)}</nav>
  <main id="main" class="content">{body}</main>
</div>

<footer class="wrap site-foot">
  <p><strong>{content.PRODUCT}</strong> and <strong>{content.STUDIO}</strong> are
  published by Lucas Potter (LPSD). Guide updated {UPDATED}.</p>
  <p><a href="{content.POLICY_URL}">Privacy policy</a> · <a href="manifest-guide.html" download>Download this guide</a></p>
</footer>

<script src="assets/search-index.js"></script>
<script src="assets/guide.js"></script>
</body>
</html>
"""


def page_body(page):
    parts = []
    is_index = page["slug"] == "index"

    if is_index:
        parts.append(
            "<div class='hero'>"
            "<p class='eyebrow'>Manifest &amp; Manifest Studio</p>"
            "<h1>Your catalogue <em>is</em> the app.</h1>"
            "<p class='lede'>A parts catalogue and job sheet for the person doing "
            "the work. No accounts, no server, no signal required — and every "
            "field, category and word on the buttons comes from a document you "
            "control.</p>"
            "</div>"
        )
    else:
        parts.append(
            f"<div class='page-head'><p class='eyebrow'>{html.escape(page['title'])}</p>"
            f"<h1>{html.escape(page['title'])}</h1>"
            f"<p class='lede'>{html.escape(page['blurb'])}</p></div>"
        )

    parts.append(toc_markup(page))

    for s in page["sections"]:
        parts.append(
            f"<section id='{s['id']}' class='sec'>"
            f"<h2><a class='anchor' href='#{s['id']}'>{html.escape(s['heading'])}</a></h2>"
            f"{resolve(s['body'])}"
            "</section>"
        )

    if is_index:
        cards = "".join(
            f"<a class='jump' href='{p['slug']}.html'>"
            f"<span class='jump-t'>{html.escape(p['title'])}</span>"
            f"<span class='jump-b'>{html.escape(p['blurb'])}</span></a>"
            for p in content.PAGES
            if p["slug"] != "index"
        )
        parts.append(
            "<section class='sec'><h2>Everything in this guide</h2>"
            f"<div class='jumps'>{cards}</div></section>"
        )

    return "\n".join(parts)


# ------------------------------------------------------------------ the build

def build():
    written = []

    for page in content.PAGES:
        slug = page["slug"]
        name = "index.html" if slug == "index" else f"{slug}.html"
        markup = shell(page["title"], page["blurb"], page_body(page), slug)
        with open(os.path.join(HERE, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(markup)
        written.append(name)

    # ---- search index -----------------------------------------------------
    index = []
    for page in content.PAGES:
        href = "index.html" if page["slug"] == "index" else f"{page['slug']}.html"
        for s in page["sections"]:
            text = strip_tags(resolve(s["body"]))
            index.append(
                {
                    "p": page["title"],
                    "h": s["heading"],
                    "u": f"{href}#{s['id']}",
                    "x": text[:320],
                    "t": (page["title"] + " " + s["heading"] + " " + text).lower(),
                }
            )
    payload = json.dumps(index, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(HERE, "assets", "search-index.js"), "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write("window.GUIDE_INDEX=" + payload + ";\n")
    written.append("assets/search-index.js")

    # ---- one-file download ------------------------------------------------
    chunks = [
        "<div class='hero'>",
        "<p class='eyebrow'>Manifest &amp; Manifest Studio</p>",
        "<h1>The complete guide</h1>",
        f"<p class='lede'>Everything in the online guide, in one file you can keep, "
        f"search with your browser's own find, or print. Updated {UPDATED}.</p>",
        "</div>",
    ]

    toc = ["<nav class='toc big-toc' aria-label='Contents'><p class='toc-h'>Contents</p><ol>"]
    for page in content.PAGES:
        subs = "".join(
            f"<li><a href='#{s['id']}'>{html.escape(s['heading'])}</a></li>"
            for s in page["sections"]
        )
        toc.append(
            f"<li><a href='#{page['slug']}'>{html.escape(page['title'])}</a>"
            f"<ul>{subs}</ul></li>"
        )
    toc.append("</ol></nav>")
    chunks.append("".join(toc))

    for page in content.PAGES:
        chunks.append(
            f"<section id='{page['slug']}' class='chapter'>"
            f"<p class='eyebrow'>{html.escape(page['title'])}</p>"
            f"<h1 class='chapter-h'>{html.escape(page['title'])}</h1>"
            f"<p class='lede'>{html.escape(page['blurb'])}</p></section>"
        )
        for s in page["sections"]:
            chunks.append(
                f"<section id='{s['id']}' class='sec'>"
                f"<h2>{html.escape(s['heading'])}</h2>"
                f"{resolve(s['body'], single_file=True)}"
                "</section>"
            )

    css_path = os.path.join(HERE, "assets", "guide.css")
    with open(css_path, encoding="utf-8") as fh:
        css = fh.read()

    single = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{content.PRODUCT} — the complete guide</title>
<meta name="description" content="The complete Manifest guide, in one file.">
<style>
{css}
/* the download has no sidebar and no live search */
.shell {{ display: block; }}
.content {{ max-width: 44rem; margin: 0 auto; }}
.chapter {{ margin-top: 4.5rem; padding-top: 2.5rem; border-top: 2px solid var(--accent); }}
.chapter:first-of-type {{ margin-top: 2.5rem; }}
.chapter-h {{ font-size: clamp(1.8rem, 5vw, 2.6rem); }}
.big-toc ol {{ padding-left: 1.1rem; }}
.big-toc > ol > li {{ margin: .85rem 0; font-weight: 600; }}
.big-toc ul {{ list-style: none; padding-left: 0; margin: .3rem 0 0; font-weight: 400; }}
.big-toc ul li {{ margin: .12rem 0; font-size: .93rem; }}
@media print {{
  body {{ background: #fff; color: #000; font-size: 11pt; }}
  .chapter {{ page-break-before: always; border-top: 0; }}
  .chapter:first-of-type {{ page-break-before: avoid; }}
  .sec {{ page-break-inside: avoid; }}
  a {{ color: #000; text-decoration: none; }}
  .big-toc {{ page-break-after: always; }}
}}
</style>
</head>
<body>
<div class="wrap shell"><main class="content">
{''.join(chunks)}
<footer class="site-foot">
<p><strong>{content.PRODUCT}</strong> and <strong>{content.STUDIO}</strong> are
published by Lucas Potter (LPSD). Updated {UPDATED}.</p>
<p><a href="{content.POLICY_URL}">Privacy policy</a></p>
</footer>
</main></div>
</body>
</html>
"""
    with open(os.path.join(HERE, "manifest-guide.html"), "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write(single)
    written.append("manifest-guide.html")

    with open(os.path.join(HERE, ".nojekyll"), "w", encoding="utf-8") as fh:
        fh.write("")
    written.append(".nojekyll")

    sections = sum(len(p["sections"]) for p in content.PAGES)
    words = sum(len(strip_tags(resolve(s["body"])).split())
                for p in content.PAGES for s in p["sections"])
    print(f"{len(content.PAGES)} pages, {sections} sections, ~{words} words")
    for name in written:
        print("  wrote", name)


if __name__ == "__main__":
    build()
