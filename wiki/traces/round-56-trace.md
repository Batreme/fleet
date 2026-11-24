# Round 56 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-56`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 56 Target Scope
  1. `www-vanderhotel-com` — *Hotel & Restaurant Ljubljana · Vander Urbani Resort*
  2. `www-vanguardinitiative-com` — *Blocked (`Upstream HTTP 402 — Vercel Deployment Paused`)*
  3. `www-velaaprivateisland-com` — *Velaa Private Island Maldives*
  4. `www-vibr-studio` — *Vibr — Figma to code for designers who ship*
  5. `www-villiers-ai` — *Blocked (`Network/Navigation failure (Desktop session exceeded 178s sub-budget)`)*
  6. `www-vineyard-co-za` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  7. `www-weisslameraner-com_en` — *Weiss & Lameraner Media Group – Lifestyle Media House Vienna*
  8. `www-worksruthi-com` — *meet Sruthi. a copywriter, marketer and artist with chutzpah.*
  9. `www-xantium-com` — *Xantium*
  10. `www-zagrebwebusluge-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-vanderhotel-com` | `tier1_fast` | `1280×6624px` (274,362 B) | `390×2616px` (74,612 B) | 25 | 16 | 343 | 112 | `0.11` / `0.46` | **25.0 / 25.0** |
| `www-velaaprivateisland-com` | `tier1_fast` | `1280×6624px` (286,708 B) | `390×2616px` (35,696 B) | 48 | 16 | 331 | 112 | `0.11` / `0.46` | **25.0 / 25.0** |
| `www-vibr-studio` | `tier1_fast` | `1280×828px` (67,102 B) | `390×2616px` (94,218 B) | 87 | 16 | 333 | 120 | `0.08` / `0.49` | **25.0 / 25.0** |
| `www-weisslameraner-com_en` | `tier1_fast` | `1280×6624px` (322,880 B) | `390×2616px` (54,270 B) | 152 | 16 | 349 | 115 | `0.10` / `0.57` | **25.0 / 25.0** |
| `www-worksruthi-com` | `tier1_fast` | `1280×6624px` (365,464 B) | `390×2616px` (31,866 B) | 205 | 16 | 358 | 117 | `0.10` / `0.47` | **25.0 / 25.0** |
| `www-xantium-com` | `tier1_fast` | `1280×6624px` (468,570 B) | `390×2616px` (96,016 B) | 43 | 16 | 349 | 112 | `0.10` / `0.57` | **25.0 / 25.0** |
| `www-vanguardinitiative-com` | `blocked` (`402`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 402 — Vercel Deployment Paused`)** |
| `www-villiers-ai` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Desktop session exceeded 178s sub-budget)`)** |
| `www-vineyard-co-za` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `www-zagrebwebusluge-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
