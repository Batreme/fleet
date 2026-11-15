# Round 13 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-13`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `9` (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 13 Target Scope
  1. `emmaus-agir-31-fr` — *Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour* (`https://emmaus-agir-31.fr/`)
  2. `equitifyasset-com` — *EquitiFy Assets · Home* (`https://equitifyasset.com/`)
  3. `errormade-tech` — *Entrance — Errormade* (`https://errormade.tech/`)
  4. `estudioniksen-com` — *Estudio Niksen* (`https://estudioniksen.com/`)
  5. `ethanwong-photography` — *Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...* (`http://ethanwong.photography`)
  6. `ethiack-com` — *Ethiack* (`https://ethiack.com/`)
  7. `example-app` — *Blocked (`Placeholder Example Domain capture (0 production stylesheets)`)*
  8. `exp-fiddle-digital` — *Fiddle.Digital — Experiments* (`https://exp.fiddle.digital`)
  9. `explorajourneys-com_int-en-explora-journal` — *The Explora Journal, A Magazine by Explora Journeys* (`https://explorajourneys.com/int/en/explora-journal`)
  10. `explore-auravinyl-com` — *Aura Vinyl Color Explorer* (`https://explore.auravinyl.com`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `emmaus-agir-31-fr` | `1440×2400px` (666,710 B) | `390×2400px` (328,785 B) | 70 | 16 | 258 | 107 | `0.09` / `0.51` | **25.0 / 25.0** |
| `equitifyasset-com` | `1440×8426px` (1,714,922 B) | `390×2400px` (375,889 B) | 96 | 16 | 270 | 113 | `0.10` / `0.50` | **25.0 / 25.0** |
| `errormade-tech` | `1440×11365px` (84,201 B) | `390×2400px` (38,118 B) | 82 | 16 | 256 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `estudioniksen-com` | `1440×10946px` (4,083,840 B) | `390×2400px` (238,345 B) | 624 | 16 | 260 | 108 | `0.10` / `0.50` | **25.0 / 25.0** |
| `ethanwong-photography` | `1440×2400px` (611,552 B) | `390×2400px` (311,535 B) | 30 | 16 | 256 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `ethiack-com` | `1440×2400px` (484,856 B) | `390×2400px` (247,237 B) | 167 | 16 | 272 | 114 | `0.09` / `0.51` | **25.0 / 25.0** |
| `example-app` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Placeholder Example Domain capture (0 production stylesheets)`)** |
| `exp-fiddle-digital` | `1440×2400px` (1,043,184 B) | `390×2400px` (450,480 B) | 74 | 16 | 253 | 103 | `0.09` / `0.52` | **25.0 / 25.0** |
| `explorajourneys-com_int-en-explora-journal` | `1440×9273px` (127,251 B) | `390×2400px` (99,430 B) | 29 | 16 | 256 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `explore-auravinyl-com` | `1440×2400px` (471,692 B) | `390×2400px` (255,362 B) | 59 | 16 | 264 | 110 | `0.09` / `0.52` | **25.0 / 25.0** |
