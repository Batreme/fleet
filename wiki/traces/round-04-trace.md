# Round 04 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-04`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `5` live (`5` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 04 Target Scope
  1. `altufanulu-com_en` — *Altufan Ulu Law Office · Istanbul Legal Counsel*
  2. `andreas-vision` — *Andreas Kruszakin, growth-focused design engineer in Europe*
  3. `anemone-mina-massoud-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  4. `annnimate-com` — *GSAP Motion Components for React & Vue · Annnimate*
  5. `anokhee-dev_albatross` — *Blocked (`Headless Preloader / Blank Viewport Capture (The Albatross I can smell the island now. 70% or WASD to fly • M to mu)`)*
  6. `apricode-agency` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  7. `aqualoqa-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call log: - navigating to 'https://aqualoqa.com/', waiting until 'domcontentloaded' )`)*
  8. `arcteryx-com_us-en-explore-system0` — *System 0 · Arc’teryx*
  9. `armor-bd-com` — *Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions*
  10. `art-appstate-edu` — *Blocked (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at https://art.appstate.edu/ Call log: - navigating to 'https://art.appstate.edu/', waiting until 'domc)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `altufanulu-com_en` | `tier1_fast` | `1440×2400px` (1,781,643 B) | `390×2400px` (531,324 B) | 6 | 16 | 294 | 112 | `0.08` / `0.49` | **25.0 / 25.0** |
| `andreas-vision` | `tier1_fast` | `1440×900px` (99,057 B) | `390×844px` (35,146 B) | 193 | 16 | 275 | 101 | `0.10` / `0.51` | **25.0 / 25.0** |
| `annnimate-com` | `tier1_fast` | `1440×2400px` (181,188 B) | `390×2400px` (182,407 B) | 453 | 16 | 292 | 111 | `0.09` / `0.48` | **25.0 / 25.0** |
| `arcteryx-com_us-en-explore-system0` | `tier1_fast` | `1440×900px` (1,173,257 B) | `390×844px` (8,604 B) | 96 | 16 | 282 | 106 | `0.10` / `0.49` | **25.0 / 25.0** |
| `armor-bd-com` | `tier1_fast` | `1440×2400px` (2,028,088 B) | `390×2400px` (585,143 B) | 43 | 16 | 283 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `anemone-mina-massoud-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `anokhee-dev_albatross` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (The Albatross I can smell`)** |
| `apricode-agency` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `aqualoqa-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call `)** |
| `art-appstate-edu` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at http`)** |
