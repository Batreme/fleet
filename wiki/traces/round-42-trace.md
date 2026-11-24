# Round 42 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-42`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 42 Target Scope
  1. `www-apc-pallets-nl` — *Algemeen Pallet Centrum · APC*
  2. `www-areyoudami-com` — *Blocked (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewport)`)*
  3. `www-arsenals-com` — *Arsenals · Liberty is built*
  4. `www-arshawnarbabi-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  5. `www-ataccama-com_fwrd2026` — *Ataccama FWRD 2026: Press play on what's next in data trust · Ataccama*
  6. `www-avara-band` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  7. `www-banham-co-uk` — *Banham · Experts in Security Services Since 1926*
  8. `www-barebonescollective-com` — *Bare Bones Collective*
  9. `www-baseline-agency` — *Baseline · Brand identity systems, designed and built*
  10. `www-beige-zone` — *Alex/Avery Beige Artist, Playwright / Creative Technologist / Biohacker*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-apc-pallets-nl` | `tier1_fast` | `1280×6624px` (691,052 B) | `390×2616px` (104,344 B) | 201 | 16 | 340 | 110 | `0.16` / `0.58` | **25.0 / 25.0** |
| `www-arsenals-com` | `tier2_webgl` | `1280×828px` (167,236 B) | `390×1744px` (67,966 B) | 14 | 16 | 311 | 109 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-ataccama-com_fwrd2026` | `tier1_fast` | `1280×4968px` (187,836 B) | `390×2616px` (40,316 B) | 323 | 16 | 338 | 117 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-banham-co-uk` | `tier1_fast` | `1280×6624px` (411,978 B) | `390×2616px` (100,532 B) | 138 | 16 | 358 | 117 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-barebonescollective-com` | `tier1_fast` | `1280×6624px` (356,330 B) | `390×2616px` (74,044 B) | 184 | 16 | 337 | 107 | `0.16` / `0.58` | **25.0 / 25.0** |
| `www-baseline-agency` | `tier1_fast` | `1280×6624px` (534,870 B) | `390×2616px` (95,668 B) | 64 | 16 | 339 | 110 | `0.10` / `0.50` | **25.0 / 25.0** |
| `www-beige-zone` | `tier1_fast` | `1280×2484px` (307,896 B) | `390×2616px` (173,438 B) | 66 | 16 | 348 | 121 | `0.08` / `0.47` | **25.0 / 25.0** |
| `www-areyoudami-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewp`)** |
| `www-arshawnarbabi-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `www-avara-band` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
