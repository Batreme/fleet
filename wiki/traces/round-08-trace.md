# Round 08 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-08`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 08 Target Scope
  1. `bybang-co` — *Estudio Bang · Architecture, Interiors, Objects & Digital Media*
  2. `carnilove-ashfall-studio` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  3. `chandebootcamp-com` — *Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam*
  4. `chanpan-com-ar` — *ChanPan · AI Video Production, Commercials & Creative Studio — Argentina*
  5. `chicago-com` — *chicago.com*
  6. `christoph-nagel-dev` — *Christoph Nagel · Webentwickler, Fotograf & Videograf in Dorsten*
  7. `cinetic-creatives-com` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  8. `citadelgroup-org` — *Citadel National Construction Group · Nationwide Construction*
  9. `ciuslabs-com` — *Blocked (`Live desktop screenshot capture failed (0 valid PNG bytes)`)*
  10. `classe-squarespace-com` — *Blocked (`Upstream HTTP 404 (Squarespace - Website Expired)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `bybang-co` | `tier1_fast` | `1280×1656px` (109,184 B) | `390×2616px` (38,742 B) | 50 | 16 | 318 | 111 | `0.09` / `0.52` | **25.0 / 25.0** |
| `chandebootcamp-com` | `tier1_fast` | `1280×6624px` (613,634 B) | `390×2616px` (94,790 B) | 77 | 16 | 360 | 117 | `0.09` / `0.52` | **25.0 / 25.0** |
| `chanpan-com-ar` | `tier1_fast` | `1280×6624px` (197,974 B) | `390×1744px` (32,700 B) | 13 | 16 | 348 | 113 | `0.09` / `0.52` | **25.0 / 25.0** |
| `chicago-com` | `tier1_fast` | `1280×5796px` (599,064 B) | `390×2616px` (125,268 B) | 394 | 16 | 348 | 115 | `0.08` / `0.47` | **25.0 / 25.0** |
| `christoph-nagel-dev` | `tier1_fast` | `1280×6624px` (405,250 B) | `390×872px` (21,690 B) | 19 | 16 | 337 | 112 | `0.09` / `0.49` | **25.0 / 25.0** |
| `citadelgroup-org` | `tier1_fast` | `1280×6624px` (530,356 B) | `390×2616px` (97,634 B) | 79 | 16 | 348 | 117 | `0.09` / `0.49` | **25.0 / 25.0** |
| `carnilove-ashfall-studio` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `cinetic-creatives-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `ciuslabs-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop screenshot capture failed (0 valid PNG bytes)`)** |
| `classe-squarespace-com` | `blocked` (`404`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 404 (Squarespace - Website Expired)`)** |
