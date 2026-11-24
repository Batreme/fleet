# Round 51 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-51`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `5` live (`5` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 51 Target Scope
  1. `www-ouiwill-com` — *Oui Will · Brand Transformation & Digital Experiences*
  2. `www-paaspop-nl` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  3. `www-palaraiffeisen-ch` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  4. `www-paragonproductions-co` — *PARAGON · Creative Production Studio*
  5. `www-peryton-film-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  6. `www-photiu-ai` — *Remove Background, Upscale & Erase Objects – Photiu.ai*
  7. `www-pistacchioecaffe-it` — *Pistacchio & Caffè*
  8. `www-plugandplaydesign-co-uk` — *Web Design Agency London & Guildford · Plug & Play*
  9. `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  10. `www-polpharmabiologics-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-ouiwill-com` | `tier1_fast` | `1280×6624px` (274,348 B) | `390×872px` (2,454 B) | 106 | 16 | 337 | 110 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-paragonproductions-co` | `tier1_fast` | `1280×6624px` (446,034 B) | `390×2616px` (49,554 B) | 118 | 16 | 342 | 111 | `0.09` / `0.46` | **25.0 / 25.0** |
| `www-photiu-ai` | `tier1_fast` | `1280×6624px` (457,544 B) | `390×1744px` (44,770 B) | 14 | 16 | 351 | 113 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-pistacchioecaffe-it` | `tier1_fast` | `1280×6624px` (420,842 B) | `390×2616px` (88,030 B) | 45 | 16 | 362 | 118 | `0.09` / `0.45` | **25.0 / 25.0** |
| `www-plugandplaydesign-co-uk` | `tier1_fast` | `1280×6624px` (268,082 B) | `390×2616px` (58,924 B) | 380 | 16 | 347 | 111 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-paaspop-nl` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `www-palaraiffeisen-ch` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `www-peryton-film-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `www-polpharmabiologics-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
