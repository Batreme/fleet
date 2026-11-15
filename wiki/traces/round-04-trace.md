# Round 04 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-04`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `9` (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 04 Target Scope
  1. `altufanulu-com_en` — *Altufan Ulu Law Office · Istanbul Legal Counsel* (`https://altufanulu.com/en/`)
  2. `andreas-vision` — *Andreas Kruszakin, growth-focused design engineer in Europe* (`https://andreas.vision`)
  3. `anemone-mina-massoud-com` — *Anemone: an interactive paper-theatre film by Mina Massoud* (`https://anemone.mina-massoud.com/`)
  4. `annnimate-com` — *GSAP Motion Components for React & Vue · Annnimate* (`https://annnimate.com`)
  5. `anokhee-dev_albatross` — *The Albatross* (`https://anokhee.dev/albatross`)
  6. `apricode-agency` — *Apricode — Immersive Websites, Ecommerce, Apps & AI* (`https://apricode.agency`)
  7. `aqualoqa-com` — *AQUALOQA* (`https://aqualoqa.com/`)
  8. `arcteryx-com_us-en-explore-system0` — *System 0 · Arc’teryx* (`https://arcteryx.com/us/en/explore/system0`)
  9. `armor-bd-com` — *Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions* (`https://armor-bd.com`)
  10. `art-appstate-edu` — *Blocked (`Empty raw DOM capture (39 bytes, 0 stylesheets)`)*

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `altufanulu-com_en` | `1440×5617px` (2,105,877 B) | `390×2400px` (118,436 B) | 6 | 16 | 258 | 107 | `0.09` / `0.51` | **25.0 / 25.0** |
| `andreas-vision` | `1440×2400px` (51,574 B) | `390×2400px` (59,198 B) | 39 | 16 | 241 | 97 | `0.10` / `0.53` | **25.0 / 25.0** |
| `anemone-mina-massoud-com` | `1440×2400px` (809,974 B) | `390×2400px` (337,135 B) | 11 | 16 | 256 | 106 | `0.11` / `0.52` | **25.0 / 25.0** |
| `annnimate-com` | `1440×2400px` (81,382 B) | `390×2400px` (48,064 B) | 453 | 16 | 256 | 106 | `0.10` / `0.46` | **25.0 / 25.0** |
| `anokhee-dev_albatross` | `1440×2400px` (260,720 B) | `390×2400px` (96,280 B) | 14 | 16 | 266 | 111 | `0.10` / `0.55` | **25.0 / 25.0** |
| `apricode-agency` | `1440×2400px` (1,094,260 B) | `390×2400px` (357,393 B) | 57 | 16 | 272 | 114 | `0.10` / `0.49` | **25.0 / 25.0** |
| `aqualoqa-com` | `1440×2400px` (387,674 B) | `390×2400px` (230,587 B) | 0 | 12 | 239 | 96 | `0.11` / `0.55` | **25.0 / 25.0** |
| `arcteryx-com_us-en-explore-system0` | `1440×2400px` (118,794 B) | `390×2400px` (68,135 B) | 96 | 16 | 256 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `armor-bd-com` | `1440×2400px` (489,141 B) | `390×2400px` (158,850 B) | 43 | 16 | 256 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `art-appstate-edu` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Empty raw DOM capture (39 bytes, 0 stylesheets)`)** |
