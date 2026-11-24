# Round 54 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-54`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 54 Target Scope
  1. `www-soe-org-uk` — *Blocked (`Upstream HTTP 403 (Checking your browser...)`)*
  2. `www-spectup-com` — *Private Capital Advisory: Capital Raising and M&A · spectup*
  3. `www-stellarmanagement-com` — *Stellar Management · NYC Real Estate Developer & No Fee Rentals*
  4. `www-studioplato-co` — *Studio Plato - Contemporary Interior Design*
  5. `www-sztanki-com` — *Blocked (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewport)`)*
  6. `www-teamcafeteria-com_2027` — *2027 — a [cafeteria] report*
  7. `www-tedxportland-com` — *TEDxPortland*
  8. `www-terakawaoffice-com_en` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  9. `www-terrenohotel-com_en` — *Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca*
  10. `www-theboringblog-ai` — *Blocked (`Network/Navigation failure (Desktop session exceeded 178s sub-budget)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-spectup-com` | `tier1_fast` | `1280×6624px` (377,410 B) | `390×2616px` (71,636 B) | 189 | 16 | 353 | 114 | `0.09` / `0.45` | **25.0 / 25.0** |
| `www-stellarmanagement-com` | `tier1_fast` | `1280×6624px` (472,490 B) | `390×872px` (2,630 B) | 94 | 16 | 365 | 123 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-studioplato-co` | `tier1_fast` | `1280×3312px` (388,018 B) | `390×872px` (4,288 B) | 11 | 16 | 321 | 112 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-teamcafeteria-com_2027` | `tier1_fast` | `1280×828px` (59,936 B) | `390×2616px` (59,868 B) | 216 | 16 | 311 | 109 | `0.09` / `0.46` | **25.0 / 25.0** |
| `www-tedxportland-com` | `tier1_fast` | `1280×6624px` (547,384 B) | `390×2616px` (85,784 B) | 85 | 16 | 349 | 112 | `0.09` / `0.44` | **25.0 / 25.0** |
| `www-terrenohotel-com_en` | `tier1_fast` | `1280×6624px` (479,258 B) | `390×2616px` (73,952 B) | 513 | 16 | 345 | 111 | `0.09` / `0.45` | **25.0 / 25.0** |
| `www-soe-org-uk` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 (Checking your browser...)`)** |
| `www-sztanki-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewp`)** |
| `www-terakawaoffice-com_en` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `www-theboringblog-ai` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Desktop session exceeded 178s sub-budget)`)** |
