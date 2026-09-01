# Manifest — the guide

The product guide for **Manifest** and **Manifest Studio**, published at
<https://lpsd-1.github.io/Manifest-Guide/> and linked from the Play Store
listing.

## It is generated

Do not edit the `.html` files by hand — they are output.

- `content.py` — every word of the guide. **One home for the content.**
- `build.py` — turns that into the site, the search index and the download.
- `assets/guide.css`, `assets/guide.js` — styling and the client-side search.

```
python build.py
```

That writes `index.html` and one page per topic, `assets/search-index.js`, and
`manifest-guide.html` — the whole guide as a single file people can download,
read offline and print.

The site, the search index and the download all say the same things, which is
the reason they are generated from one source rather than maintained as three
copies of the same sentence.

## Rules for the content

- Only describe what the app actually does. A guide claiming a feature that is
  not there is worse than no guide.
- British English. No exclamation marks, no superlatives.
- Say what a thing does, then say what it costs or refuses. The app's own copy
  is honest about limits; the guide should not be less so.

## Search

`assets/search-index.js` assigns a global rather than being fetched as JSON, so
search still works from a `file://` path — which matters because the guide is
meant to be downloaded and read on a laptop with no signal.
