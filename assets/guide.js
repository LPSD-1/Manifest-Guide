/* Manifest guide — client-side search.
 *
 * The index is a global assigned by assets/search-index.js rather than fetched,
 * so this works from a file:// path with no server and no network. That matters
 * because the guide is meant to be downloadable and read on a laptop in a van.
 */
(function () {
  "use strict";

  var box = document.getElementById("q");
  var panel = document.getElementById("results");
  if (!box || !panel || !window.GUIDE_INDEX) return;

  var index = window.GUIDE_INDEX;
  var lastQuery = "";

  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function escapeRe(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  /* Score a section against the words typed. Every word must appear somewhere,
     so typing more narrows rather than widens — which is what people expect
     from a search box and not what a naive OR gives them. */
  function score(entry, words) {
    var total = 0;
    for (var i = 0; i < words.length; i++) {
      var w = words[i];
      if (entry.t.indexOf(w) === -1) return 0;
      if (entry.h.toLowerCase().indexOf(w) !== -1) total += 12;
      if (entry.p.toLowerCase().indexOf(w) !== -1) total += 4;
      total += 1;
    }
    return total;
  }

  function mark(text, words) {
    var out = escapeHtml(text);
    for (var i = 0; i < words.length; i++) {
      if (words[i].length < 2) continue;
      out = out.replace(new RegExp("(" + escapeRe(words[i]) + ")", "gi"), "<mark>$1</mark>");
    }
    return out;
  }

  function render(hits, words) {
    if (!hits.length) {
      panel.innerHTML =
        '<div class="results-in"><p class="no-hits">Nothing matches that. Try a single word — ' +
        '<em>signature</em>, <em>pairing</em>, <em>labels</em>.</p></div>';
      return;
    }
    var html = '<div class="results-in">';
    for (var i = 0; i < hits.length; i++) {
      var e = hits[i];
      html +=
        '<a class="hit" href="' + e.u + '">' +
        '<span class="hit-p">' + escapeHtml(e.p) + "</span>" +
        '<span class="hit-h">' + mark(e.h, words) + "</span>" +
        '<span class="hit-x">' + mark(e.x, words) + "…</span>" +
        "</a>";
    }
    panel.innerHTML = html + "</div>";
  }

  function run() {
    var q = box.value.trim().toLowerCase();
    if (q === lastQuery) return;
    lastQuery = q;

    if (q.length < 2) {
      panel.hidden = true;
      box.setAttribute("aria-expanded", "false");
      return;
    }

    var words = q.split(/\s+/).filter(Boolean);
    var hits = [];
    for (var i = 0; i < index.length; i++) {
      var s = score(index[i], words);
      if (s > 0) hits.push({ s: s, e: index[i] });
    }
    hits.sort(function (a, b) { return b.s - a.s; });

    render(hits.slice(0, 12).map(function (h) { return h.e; }), words);
    panel.hidden = false;
    box.setAttribute("aria-expanded", "true");
  }

  box.addEventListener("input", run);
  box.addEventListener("focus", function () { if (box.value.trim().length > 1) run(); });

  box.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      box.value = "";
      lastQuery = "";
      panel.hidden = true;
      box.setAttribute("aria-expanded", "false");
      box.blur();
    }
    if (e.key === "Enter") {
      var first = panel.querySelector(".hit");
      if (first && !panel.hidden) { e.preventDefault(); window.location.href = first.getAttribute("href"); }
    }
  });

  document.addEventListener("click", function (e) {
    if (!panel.contains(e.target) && e.target !== box) {
      panel.hidden = true;
      box.setAttribute("aria-expanded", "false");
    }
  });

  /* "/" focuses search, the convention people already have from other docs. */
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== box &&
        !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
      e.preventDefault();
      box.focus();
    }
  });
})();
