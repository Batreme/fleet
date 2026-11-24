# Round 13 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-13`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
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
  8. `exp-fiddle-digital` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  9. `explorajourneys-com_int-en-explora-journal` — *The Explora Journal, A Magazine by Explora Journeys*
  10. `explore-auravinyl-com` — *Aura Vinyl Color Explorer*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `emmaus-agir-31-fr` | `tier1_fast` | `1280×828px` (76,132 B) | `390×2616px` (75,978 B) | 70 | 16 | 317 | 112 | `0.09` / `0.50` | **25.0 / 25.0** |
| `equitifyasset-com` | `tier1_fast` | `1280×6624px` (356,046 B) | `390×2616px` (41,310 B) | 96 | 16 | 349 | 118 | `0.10` / `0.54` | **25.0 / 25.0** |
| `errormade-tech` | `tier2_webgl` | `1280×6624px` (350,184 B) | `390×2616px` (64,904 B) | 82 | 16 | 329 | 110 | `0.10` / `0.54` | **25.0 / 25.0** |
| `estudioniksen-com` | `tier1_fast` | `1280×6624px` (608,070 B) | `390×2616px` (97,100 B) | 633 | 16 | 348 | 111 | `0.10` / `0.52` | **25.0 / 25.0** |
| `ethanwong-photography` | `tier1_fast` | `1280×2484px` (210,388 B) | `390×872px` (13,734 B) | 52 | 16 | 345 | 116 | `0.08` / `0.51` | **25.0 / 25.0** |
| `ethiack-com` | `tier1_fast` | `1280×828px` (45,822 B) | `390×1744px` (54,924 B) | 180 | 16 | 336 | 122 | `0.09` / `0.49` | **25.0 / 25.0** |
| `explorajourneys-com_int-en-explora-journal` | `tier1_fast` | `1280×6624px` (613,538 B) | `390×2616px` (114,496 B) | 11 | 16 | 340 | 111 | `0.10` / `0.48` | **25.0 / 25.0** |
| `explore-auravinyl-com` | `tier2_webgl` | `1280×828px` (4,556 B) | `390×872px` (2,868 B) | 57 | 16 | 332 | 117 | `0.08` / `0.52` | **25.0 / 25.0** |
| `example-app` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Placeholder Example Domain (no production site)`)** |
| `exp-fiddle-digital` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
