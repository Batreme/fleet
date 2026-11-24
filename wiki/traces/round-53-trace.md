# Round 53 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-53`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `4` live (`6` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 53 Target Scope
  1. `www-routedurhum-com` — *Route du Rhum 2026 – Destination Guadeloupe · Site Officiel*
  2. `www-rtmaudio-com` — *RTM Audio · Audio plug-ins for mixing and mastering*
  3. `www-schemeengine-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  4. `www-schlosshotel-kitzbuehel-com_en` — *Schlosshotel Kitzbühel – a premium experience*
  5. `www-seasats-com` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  6. `www-selkirk-com_pages-omni-pickleball-paddle` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  7. `www-sentientx-com` — *Blocked (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewport)`)*
  8. `www-serko-ai` — *Serko.ai · AI Travel Agent for Business Trips*
  9. `www-sharplink-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  10. `www-si-edu` — *Blocked (`Upstream HTTP 403 — Cloudflare Origin/WAF Error`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-routedurhum-com` | `tier1_fast` | `1280×6624px` (756,760 B) | `390×2616px` (62,704 B) | 485 | 16 | 349 | 111 | `0.10` / `0.45` | **25.0 / 25.0** |
| `www-rtmaudio-com` | `tier1_fast` | `1280×6624px` (359,948 B) | `390×2616px` (62,648 B) | 73 | 16 | 349 | 112 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-schlosshotel-kitzbuehel-com_en` | `tier1_fast` | `1280×4140px` (355,784 B) | `390×2616px` (97,564 B) | 65 | 16 | 338 | 112 | `0.08` / `0.47` | **25.0 / 25.0** |
| `www-serko-ai` | `tier1_fast` | `1280×6624px` (287,656 B) | `390×2616px` (67,646 B) | 591 | 16 | 352 | 114 | `0.10` / `0.46` | **25.0 / 25.0** |
| `www-schemeengine-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `www-seasats-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `www-selkirk-com_pages-omni-pickleball-paddle` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `www-sentientx-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewp`)** |
| `www-sharplink-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `www-si-edu` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — Cloudflare Origin/WAF Error`)** |
