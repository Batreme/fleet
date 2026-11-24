# Round 55 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-55`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 55 Target Scope
  1. `www-thecandyvault-com-au` — *The Candy Vault · Buy Sweets Online · Australia*
  2. `www-thedesignsociety-fr` — *The Design Society Lyon — la communauté des designers*
  3. `www-thefriedegg-com` — *Fried Egg Golf*
  4. `www-thelasttango-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  5. `www-tokonoma-xyz` — *Tokonoma Studio — Image Making, Art, AI & Creative Direction*
  6. `www-tomdekoning-work` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call log: - navigating to 'https://www.tomdekoning.work/', waiting until 'domcontentloaded' )`)*
  7. `www-unbelievablycrap-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call log: - navigating to 'https://www.unbelievablycrap.com/', waiting until 'domcontentloaded' )`)*
  8. `www-undplus-com` — *UNDPLUS — Brand Architecture & Spatial Design Studio*
  9. `www-upscayl-app` — *Upscale Image Online Free – Upscale to 8K with AI · Upscayl*
  10. `www-urbik-eu` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call log: - navigating to 'https://www.urbik.eu/', waiting until 'domcontentloaded' )`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-thecandyvault-com-au` | `tier1_fast` | `1280×6624px` (348,030 B) | `390×2616px` (71,900 B) | 2102 | 16 | 341 | 111 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-thedesignsociety-fr` | `tier1_fast` | `1280×6624px` (511,340 B) | `390×872px` (9,564 B) | 60 | 16 | 345 | 114 | `0.10` / `0.51` | **25.0 / 25.0** |
| `www-thefriedegg-com` | `tier1_fast` | `1280×6624px` (621,592 B) | `390×2616px` (62,652 B) | 236 | 16 | 349 | 111 | `0.10` / `0.51` | **25.0 / 25.0** |
| `www-tokonoma-xyz` | `tier1_fast` | `1280×2484px` (66,690 B) | `390×872px` (11,238 B) | 3 | 15 | 325 | 107 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-undplus-com` | `tier1_fast` | `1280×6624px` (286,824 B) | `390×2616px` (47,852 B) | 29 | 16 | 333 | 113 | `0.10` / `0.51` | **25.0 / 25.0** |
| `www-upscayl-app` | `tier1_fast` | `1280×6624px` (340,868 B) | `390×2616px` (91,002 B) | 77 | 16 | 343 | 111 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-thelasttango-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `www-tomdekoning-work` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call `)** |
| `www-unbelievablycrap-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call `)** |
| `www-urbik-eu` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call `)** |
