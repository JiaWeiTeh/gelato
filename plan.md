# Documentation Plan for GELATO

## Current State
- Sphinx-based docs with RTD theme, hosted on ReadTheDocs
- Existing pages: `index.rst`, `installation.rst`, `license.rst`, `acknowledgements.rst`
- `customisation.rst` is misplaced in `_static/` and is a stub
- Most `.rst` files have broken formatting (newlines collapsed)
- No documentation for quiz modes, configuration, or project structure

## Phase 1: Fix Foundation
- Fix `conf.py` (update version, metadata)
- Fix `index.rst` (clean up formatting, update toctree with new pages)
- Fix `installation.rst` (add `pip install` via setup.py, list dependencies)
- Move `customisation.rst` from `_static/` to `docs/` root
- Fix `license.rst` and `acknowledgements.rst` formatting

## Phase 2: Core Content Pages
- **`quickstart.rst`** — Minimal "get running in 30 seconds" guide
- **`modes.rst`** — Document all three quiz modes:
  - Artikel (Normal) — practice articles with retry loop, score percentage
  - Artikel (Challenge/Survival) — hearts system, scoreboard, analysis
  - Verben (Practice) — verb conjugation with checkmark scoring
- **`configuration.rst`** — Full reference for `settings.yml`:
  - `general.name`, `general.def_language`
  - `artikel_normal.def_qs`
  - `artikel_challenge.hearts`
  - How to open settings from within the app (mode 4)

## Phase 3: Customisation & Data
- **`customisation.rst`** — How to add your own words:
  - Excel file format for `artikel.xlsx` (columns: Artikel, Noun, Translation, Tag)
  - Excel file format for `verben.xlsx` (columns: Infinitiv, Prasens, Prateritum, Perfekt, Beispielsatz)
  - Adding new data files
- **`scoreboard.rst`** — How the scoreboard works, where data is stored

## Phase 4: Language & Developer Info
- **`languages.rst`** — Supported UI languages (en, cn, katze), how translations work, how to add a new language
- **`contributing.rst`** — Project structure overview, how to set up for development, dependencies
