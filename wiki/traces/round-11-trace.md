# Round 11 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-11`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 11 Target Scope
  1. `deathbyscroll-com` — *Death by Scroll*
  2. `degacsid-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  3. `delice-ca` — *Accueil - Délice*
  4. `deltacafes-com_en` — *Delta, coffee with heart · Delta Cafés — The coffee of your life*
  5. `departmentofemotions-com` — *Department of Emotions*
  6. `derive-ocean-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  7. `digitalofthings-studio` — *digital of things · user experience digital studio*
  8. `diseinuz-com` — *DISEINUZ — Bilbao Bizkaia Design Summit*
  9. `diversify-nz` — *diversify.nz*
  10. `douglus-co` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `deathbyscroll-com` | `tier1_fast` | `1280×6624px` (328,312 B) | `390×2616px` (56,020 B) | 91 | 16 | 364 | 122 | `0.08` / `0.48` | **25.0 / 25.0** |
| `delice-ca` | `tier1_fast` | `1280×828px` (81,560 B) | `390×2616px` (81,434 B) | 76 | 16 | 315 | 111 | `0.09` / `0.49` | **25.0 / 25.0** |
| `deltacafes-com_en` | `tier1_fast` | `1280×6624px` (570,330 B) | `390×2616px` (64,234 B) | 264 | 16 | 344 | 112 | `0.09` / `0.48` | **25.0 / 25.0** |
| `departmentofemotions-com` | `tier1_fast` | `1280×1656px` (137,774 B) | `390×872px` (29,494 B) | 11 | 16 | 312 | 109 | `0.09` / `0.50` | **25.0 / 25.0** |
| `digitalofthings-studio` | `tier1_fast` | `1280×828px` (16,514 B) | `390×872px` (9,890 B) | 3 | 16 | 323 | 110 | `0.09` / `0.50` | **25.0 / 25.0** |
| `diseinuz-com` | `tier1_fast` | `1280×6624px` (396,842 B) | `390×2616px` (42,400 B) | 40 | 16 | 339 | 110 | `0.09` / `0.50` | **25.0 / 25.0** |
| `diversify-nz` | `tier1_fast` | `1280×4140px` (272,958 B) | `390×2616px` (78,968 B) | 54 | 16 | 330 | 114 | `0.09` / `0.49` | **25.0 / 25.0** |
| `degacsid-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `derive-ocean-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `douglus-co` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
