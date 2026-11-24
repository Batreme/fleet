# Round 02 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-02`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 02 Target Scope
  1. `100yearsmonet-com` — *Monet 100 — A century without Claude Monet · 3D gallery*
  2. `11moissanstoit-com` — *11 mois sans toi(t), le tour du monde de Josué & Philippe*
  3. `1stdecember-com` — *First December Films · Ad Film Production House in India*
  4. `21oaks-org` — *21Oaks Student Apartments • USC & Williams-Brice*
  5. `360lexingtonave-com` — *360 Lexington Avenue*
  6. `abhayrohit-com` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  7. `about-centra-com` — *Centra? Centra! The definitive guide.*
  8. `abyme-app` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  9. `actl-me` — *ACTL — Arabian Community Tennis League*
  10. `adamperlis-com` — *Adam Perlis — I design and build apps*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `100yearsmonet-com` | `tier1_fast` | `1280×828px` (48,262 B) | `390×2616px` (57,148 B) | 7 | 16 | 317 | 112 | `0.10` / `0.50` | **25.0 / 25.0** |
| `11moissanstoit-com` | `tier1_fast` | `1280×828px` (10,408 B) | `390×872px` (2,812 B) | 9 | 16 | 319 | 114 | `0.09` / `0.52` | **25.0 / 25.0** |
| `1stdecember-com` | `tier1_fast` | `1280×6624px` (642,896 B) | `390×2616px` (92,276 B) | 600 | 16 | 340 | 110 | `0.13` / `0.55` | **25.0 / 25.0** |
| `21oaks-org` | `tier1_fast` | `1280×6624px` (486,736 B) | `390×2616px` (108,000 B) | 9 | 16 | 341 | 111 | `0.14` / `0.58` | **25.0 / 25.0** |
| `360lexingtonave-com` | `tier1_fast` | `1280×6624px` (323,810 B) | `390×2616px` (88,982 B) | 36 | 16 | 327 | 110 | `0.11` / `0.50` | **25.0 / 25.0** |
| `about-centra-com` | `tier1_fast` | `1280×6624px` (374,708 B) | `390×2616px` (71,414 B) | 150 | 16 | 352 | 116 | `0.14` / `0.58` | **25.0 / 25.0** |
| `actl-me` | `tier1_fast` | `1280×6624px` (311,738 B) | `390×2616px` (71,010 B) | 5 | 16 | 332 | 112 | `0.11` / `0.50` | **25.0 / 25.0** |
| `adamperlis-com` | `tier1_fast` | `1280×1656px` (17,508 B) | `390×1744px` (10,016 B) | 83 | 16 | 331 | 112 | `0.09` / `0.52` | **25.0 / 25.0** |
| `abhayrohit-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `abyme-app` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
