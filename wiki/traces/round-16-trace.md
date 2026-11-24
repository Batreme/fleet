# Round 16 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-16`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 16 Target Scope
  1. `giordanobetti-com` — *Giordano Betti - Independent Cinematographer*
  2. `glinto-co-kr` — *Glinto — Creative studio*
  3. `gmxdigital-com_en` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  4. `gpg-dops-agency` — *Garvinpromo*
  5. `gracefashion-ai` — *KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai*
  6. `grail-app-com` — *Grail: Real-world quests, every day*
  7. `grids03-obys-agency` — *Grids — DES Season 03*
  8. `grubogrubo-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call log: - navigating to 'https://grubogrubo.com/', waiting until 'domcontentloaded' )`)*
  9. `guillaumecolombel-fr` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  10. `halloween-ferayna-com` — *Blocked (`Browser/WebGPU Hardware Gate (Every brief has a face | Ferayna)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `giordanobetti-com` | `tier1_fast` | `1280×828px` (13,700 B) | `390×872px` (6,064 B) | 20 | 16 | 307 | 108 | `0.08` / `0.53` | **25.0 / 25.0** |
| `glinto-co-kr` | `tier1_fast` | `1280×6624px` (210,886 B) | `390×2616px` (48,364 B) | 292 | 16 | 371 | 125 | `0.09` / `0.52` | **25.0 / 25.0** |
| `gpg-dops-agency` | `tier1_fast` | `1280×6624px` (152,614 B) | `390×2616px` (76,326 B) | 50 | 16 | 344 | 112 | `0.09` / `0.53` | **25.0 / 25.0** |
| `gracefashion-ai` | `tier1_fast` | `1280×6624px` (91,112 B) | `390×2616px` (26,914 B) | 11 | 16 | 346 | 113 | `0.09` / `0.49` | **25.0 / 25.0** |
| `grail-app-com` | `tier1_fast` | `1280×6624px` (296,288 B) | `390×2616px` (11,104 B) | 83 | 16 | 351 | 119 | `0.09` / `0.50` | **25.0 / 25.0** |
| `grids03-obys-agency` | `tier1_fast` | `1280×828px` (37,000 B) | `390×2616px` (15,422 B) | 20 | 16 | 313 | 110 | `0.09` / `0.53` | **25.0 / 25.0** |
| `gmxdigital-com_en` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `grubogrubo-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call `)** |
| `guillaumecolombel-fr` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `halloween-ferayna-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Browser/WebGPU Hardware Gate (Every brief has a face | Ferayna)`)** |
