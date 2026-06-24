# Enhanced Recovery → Wells Engineering Intelligence Dashboard

An interactive, self-contained dashboard built from the JPT/SPE
[**Enhanced recovery**](https://jpt.spe.org/topic/enhanced-recovery) topic feed, re-framed
through the lens of an **integrated operator's wells-engineering** organization:
field development, drilling & well construction, completions & stimulation, production &
well performance, and facilities — with the underlying reservoir/EOR science.

`index.html` is fully self-contained (data embedded, no external dependencies). Open it in
any browser or publish it straight to GitHub Pages.

## What it does

- **Zoomable timeline** — click a month bar or drag the two handles to scope a date window.
- **Filters** — full-text search (title/abstract/author/play/operator), discipline chips,
  relevance segment (High/Medium), "wells-engineering core only" toggle, and sort.
- **Sortable paper list** — newest, oldest, A–Z, or by wells-engineering relevance.
- **Technical summary panel** — click any title and the right pane opens an
  **abstract-faithful** brief: Context · Technical Approach · Business Problem & Value ·
  Challenges · Gaps (what's behind the paywall) · verbatim Abstract · engineering tags
  (methods, play/field, region, operators) · link to the source paper.
- **Paste-to-enrich (dynamic records)** — because the source papers are paywalled, you can
  paste the **full text** of any article and update its record live (see below).

## Updating records by pasting paywalled full text

Click **Enrich with full text** on any open paper, or **➕ Add paywalled article** for one
not in the list. In the editor:

1. Paste the article's full text and hit **⚡ Auto-derive** — the dashboard re-runs the same
   keyword classifier (disciplines, methods, plays/regions/operators, relevance) and pre-fills
   Context / Technical / Business / Challenges from the pasted text.
2. Edit any field by hand, then **Save**.

Saved edits live in your browser's **localStorage**, so they survive reloads. The original
verbatim brief is preserved; an enriched record shows a green **✓ enriched** badge, and the
"Source" section displays your full text instead of the short abstract.

**Persist / share your edits**
- **⬇ Export data.json** — downloads the full dataset with your enrichments merged. Replace
  the `data.json` in this folder and re-run `build_dashboard.py` to bake edits permanently
  into `index.html` (e.g. for the published portfolio).
- **⬇ Backup edits** / **⬆ Restore edits** — save or reload just your overrides as a small
  JSON file (handy across machines/browsers).
- **Revert** removes an enrichment and restores the original baseline record;
  **Clear edits** wipes all local changes.

> Edits are stored per-browser. Use Export/Backup if you want them on another device or in git.

## Dataset

- **118 papers**, Nov 2023 → Jun 2026 (full 2024–2026 coverage), scraped from pages 1–12.
- Articles on JPT are paywalled, so every summary field is **abstract-faithful** —
  derived only from the public brief. Quantitative results and full methodology live in
  the source SPE papers.
- Discipline labels and engineering tags are produced by transparent keyword-rule
  classifiers in `build_data.py` (auto-classification; expert review recommended).

## Key wells-engineering topics surfaced (count of papers touching each discipline)

| Discipline | Papers |
|---|---|
| Reservoir & EOR (core science) | 95 |
| Completions & Stimulation | 31 |
| Production & Well Performance | 24 |
| Digital, AI & Modeling | 20 |
| Facilities & Flow Assurance | 13 |
| Field Development | 12 |
| CCUS & Decarbonization | 12 |
| Drilling & Well Construction | 11 |

**Dominant technical approaches:** reservoir simulation/modeling, CO₂ / miscible gas
flooding, SAGD & thermal recovery, machine learning/AI, hydraulic fracturing, matrix
acidizing, polymer flooding, surfactant/chemical EOR, inflow control (ICD/AICV), and
nanotechnology. (Papers may map to more than one discipline, so columns overlap.)

## Regenerate

```bash
python3 build_data.py        # rebuilds data.json from the embedded record set
python3 build_dashboard.py   # injects data.json into index.html
```

To extend the archive, add records to the `R` list in `build_data.py` (title, slug, tag,
date, author, abstract, locked) and re-run both scripts.

Source: <https://jpt.spe.org/topic/enhanced-recovery>
