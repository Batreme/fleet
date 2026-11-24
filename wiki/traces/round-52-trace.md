# Round 52 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-52`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 52 Target Scope
  1. `www-poulo-site` — *Blocked (`Upstream HTTP 429 — Vercel Security Checkpoint`)*
  2. `www-pragenhatlen-com` — *Prägen Hätlen · Swiss watchmaking for the crypto community.*
  3. `www-qissa-co-uk` — *Indian Restaurant in Sevenoaks, Kent · Qissa*
  4. `www-quintadamalia-com` — *Quinta D. Amália - Redefining Luxury Living in Portugal*
  5. `www-raomuhammadhamza-tech` — *Rao Muhammad Hamza, AI Engineer*
  6. `www-rebelliously-optimistic-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  7. `www-remyshoots-co-za` — *Remy Shoots*
  8. `www-rikoutaku-work` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  9. `www-romainavalle-dev` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  10. `www-rosshalfin-com` — *Ross Halfin Photography · Music Images + Fine Art Prints*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-pragenhatlen-com` | `tier1_fast` | `1280×6624px` (313,602 B) | `390×872px` (9,292 B) | 78 | 16 | 326 | 110 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-qissa-co-uk` | `tier1_fast` | `1280×6624px` (434,138 B) | `390×2616px` (76,996 B) | 26 | 16 | 364 | 120 | `0.09` / `0.45` | **25.0 / 25.0** |
| `www-quintadamalia-com` | `tier1_fast` | `1280×6624px` (455,352 B) | `390×2616px` (64,412 B) | 574 | 16 | 355 | 124 | `0.08` / `0.47` | **25.0 / 25.0** |
| `www-raomuhammadhamza-tech` | `tier1_fast` | `1280×6624px` (330,886 B) | `390×2616px` (75,840 B) | 32 | 16 | 349 | 118 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-remyshoots-co-za` | `tier2_webgl` | `1280×828px` (17,294 B) | `390×872px` (9,084 B) | 45 | 16 | 325 | 113 | `0.08` / `0.47` | **25.0 / 25.0** |
| `www-rosshalfin-com` | `tier1_fast` | `1280×5796px` (338,882 B) | `390×2616px` (70,678 B) | 67 | 16 | 353 | 115 | `0.08` / `0.47` | **25.0 / 25.0** |
| `www-poulo-site` | `blocked` (`429`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 429 — Vercel Security Checkpoint`)** |
| `www-rebelliously-optimistic-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `www-rikoutaku-work` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `www-romainavalle-dev` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
