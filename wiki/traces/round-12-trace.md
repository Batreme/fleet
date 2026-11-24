# Round 12 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-12`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 12 Target Scope
  1. `dream-with-ai-com` — *Dream with AI*
  2. `dreams-paulvl-eu` — *Blocked (`Browser/WebGPU Hardware Gate (I'm having bad dreams)`)*
  3. `drshabri-com` — *Cosmetic Dentist & Facial Aesthetics, Marylebone*
  4. `dsquaredmedia-net` — *South Florida Marketing Agency · Branding, Web & AI · Dsquared Media*
  5. `duda-works` — *Duda Lima*
  6. `dwell-au` — *Dwell · A new way home*
  7. `earthwallet-com` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  8. `edisonfangworkshop-com` — *Edison Fang Workshop*
  9. `effepinnastudio-com` — *Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio*
  10. `ellioteriksson-com` — *Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `dream-with-ai-com` | `tier1_fast` | `1280×828px` (34,386 B) | `390×872px` (24,864 B) | 16 | 16 | 313 | 111 | `0.08` / `0.51` | **25.0 / 25.0** |
| `drshabri-com` | `tier1_fast` | `1280×6624px` (499,356 B) | `390×2616px` (82,510 B) | 178 | 16 | 343 | 112 | `0.10` / `0.49` | **25.0 / 25.0** |
| `dsquaredmedia-net` | `tier1_fast` | `1280×6624px` (474,460 B) | `390×2616px` (64,610 B) | 87 | 16 | 370 | 122 | `0.09` / `0.49` | **25.0 / 25.0** |
| `duda-works` | `tier1_fast` | `1280×6624px` (299,604 B) | `390×2616px` (66,892 B) | 5 | 16 | 334 | 107 | `0.10` / `0.52` | **25.0 / 25.0** |
| `dwell-au` | `tier1_fast` | `1280×3312px` (147,196 B) | `390×872px` (6,394 B) | 203 | 16 | 330 | 110 | `0.09` / `0.52` | **25.0 / 25.0** |
| `edisonfangworkshop-com` | `tier1_fast` | `1280×2484px` (47,010 B) | `390×1744px` (25,150 B) | 144 | 16 | 337 | 114 | `0.09` / `0.49` | **25.0 / 25.0** |
| `effepinnastudio-com` | `tier1_fast` | `1280×6624px` (413,860 B) | `390×2616px` (89,444 B) | 109 | 16 | 350 | 113 | `0.10` / `0.50` | **25.0 / 25.0** |
| `ellioteriksson-com` | `tier1_fast` | `1280×6624px` (292,084 B) | `390×1744px` (21,116 B) | 45 | 16 | 345 | 113 | `0.09` / `0.52` | **25.0 / 25.0** |
| `dreams-paulvl-eu` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Browser/WebGPU Hardware Gate (I'm having bad dreams)`)** |
| `earthwallet-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
