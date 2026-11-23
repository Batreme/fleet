# Round 13 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-13`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 13 Target Scope
  1. `emmaus-agir-31-fr` — *Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour*
  2. `equitifyasset-com` — *EquitiFy Assets · Home*
  3. `errormade-tech` — *Entrance — Errormade*
  4. `estudioniksen-com` — *Estudio Niksen*
  5. `ethanwong-photography` — *Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...*
  6. `ethiack-com` — *Ethiack*
  7. `example-app` — *Blocked (`Placeholder Example Domain (no production site)`)*
  8. `exp-fiddle-digital` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  9. `explorajourneys-com_int-en-explora-journal` — *The Explora Journal, A Magazine by Explora Journeys*
  10. `explore-auravinyl-com` — *Aura Vinyl Color Explorer*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `emmaus-agir-31-fr` | `tier1_fast` | `1440×900px` (668,116 B) | `390×844px` (332,759 B) | 70 | 16 | 288 | 109 | `0.10` / `0.52` | **25.0 / 25.0** |
| `equitifyasset-com` | `tier1_fast` | `1440×2400px` (1,513,447 B) | `390×2400px` (407,538 B) | 96 | 16 | 300 | 115 | `0.09` / `0.53` | **25.0 / 25.0** |
| `errormade-tech` | `tier2_webgl` | `1440×900px` (13,426 B) | `390×844px` (6,108 B) | 82 | 16 | 284 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `estudioniksen-com` | `tier1_fast` | `1440×900px` (1,328,742 B) | `390×2400px` (564,732 B) | 130 | 16 | 284 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `ethanwong-photography` | `tier1_fast` | `1440×900px` (1,374,008 B) | `390×844px` (372,128 B) | 30 | 16 | 292 | 111 | `0.10` / `0.52` | **25.0 / 25.0** |
| `ethiack-com` | `tier2_webgl` | `1440×900px` (81,523 B) | `390×844px` (34,854 B) | 184 | 16 | 306 | 118 | `0.09` / `0.49` | **25.0 / 25.0** |
| `explorajourneys-com_int-en-explora-journal` | `tier1_fast` | `1440×2400px` (1,486,006 B) | `390×2400px` (738,290 B) | 10 | 16 | 284 | 107 | `0.09` / `0.48` | **25.0 / 25.0** |
| `explore-auravinyl-com` | `tier1_fast` | `1440×900px` (360,998 B) | `390×844px` (24,223 B) | 59 | 16 | 298 | 114 | `0.08` / `0.52` | **25.0 / 25.0** |
| `example-app` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Placeholder Example Domain (no production site)`)** |
| `exp-fiddle-digital` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
