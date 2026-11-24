# Round 36 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-36`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 36 Target Scope
  1. `thecontenders-co` — *The Contenders · Strategic Brand & Design Consultancy*
  2. `thefwa-net` — *FWA Wire — winners' newswire*
  3. `theimmortals-world` — *Blocked (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewport)`)*
  4. `theinfinitysocks-com` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  5. `thenest-pl_en` — *The Nest — a registered business address in central Warsaw*
  6. `theobromachocolat-com` — *Cure Your Chocolate Craving · Theobroma Chocolate*
  7. `theperformancelab-ca` — *The Performance Lab — Sports Science & Athletic Testing in Toronto*
  8. `therechabite-com-au` — *The Rechabite • Multi-level Palace of Surprise and Delight*
  9. `thesovietflip-com` — *The Soviet Flip*
  10. `thestudiobyjuliegranger-com` — *The Studio by Julie Granger*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `thecontenders-co` | `tier1_fast` | `1280×828px` (13,594 B) | `390×2616px` (47,314 B) | 130 | 16 | 311 | 109 | `0.10` / `0.52` | **25.0 / 25.0** |
| `thefwa-net` | `tier1_fast` | `1280×4140px` (262,420 B) | `390×2616px` (134,374 B) | 13 | 16 | 345 | 115 | `0.09` / `0.50` | **25.0 / 25.0** |
| `thenest-pl_en` | `tier1_fast` | `1280×4968px` (135,192 B) | `390×2616px` (78,344 B) | 138 | 16 | 340 | 111 | `0.10` / `0.49` | **25.0 / 25.0** |
| `theobromachocolat-com` | `tier1_fast` | `1280×6624px` (454,696 B) | `390×2616px` (80,164 B) | 58 | 16 | 354 | 117 | `0.09` / `0.48` | **25.0 / 25.0** |
| `theperformancelab-ca` | `tier1_fast` | `1280×1656px` (190,562 B) | `390×2616px` (99,266 B) | 36 | 16 | 338 | 115 | `0.09` / `0.53` | **25.0 / 25.0** |
| `therechabite-com-au` | `tier1_fast` | `1280×1656px` (141,738 B) | `390×2616px` (61,150 B) | 73 | 16 | 344 | 115 | `0.11` / `0.53` | **25.0 / 25.0** |
| `thesovietflip-com` | `tier1_fast` | `1280×1656px` (59,330 B) | `390×872px` (2,742 B) | 42 | 16 | 327 | 111 | `0.08` / `0.50` | **25.0 / 25.0** |
| `thestudiobyjuliegranger-com` | `tier1_fast` | `1280×6624px` (275,680 B) | `390×2616px` (79,232 B) | 47 | 16 | 358 | 117 | `0.11` / `0.52` | **25.0 / 25.0** |
| `theimmortals-world` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewp`)** |
| `theinfinitysocks-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
