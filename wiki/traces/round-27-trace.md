# Round 27 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-27`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `4` live (`6` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 27 Target Scope
  1. `noho-ink` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  2. `noravale-framer-website` — *Blankit – Ultimate Portfolio System for Framer*
  3. `north-cloud` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  4. `oblikworks-com` — *oblikworks · Architectural Visualization & 3D Rendering Studio*
  5. `offform-net` — *Blocked (`Upstream HTTP 502 (502 Bad Gateway)`)*
  6. `offpossible-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://offpossible.com/', waiting until 'domcontentloaded' )`)*
  7. `ofrenda-davidlangarica-dev` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  8. `oliviaarents-com` — *OliviaOS 96 — Personal Edition*
  9. `ondocollective-jp` — *Ondo Collective*
  10. `onecoldnight-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `noravale-framer-website` | `tier1_fast` | `1280×1656px` (53,714 B) | `390×872px` (13,216 B) | 151 | 16 | 335 | 116 | `0.11` / `0.54` | **25.0 / 25.0** |
| `oblikworks-com` | `tier1_fast` | `1280×4140px` (331,532 B) | `390×1744px` (37,576 B) | 5 | 16 | 320 | 110 | `0.09` / `0.52` | **25.0 / 25.0** |
| `oliviaarents-com` | `tier1_fast` | `1280×828px` (8,426 B) | `390×872px` (5,858 B) | 7 | 16 | 309 | 107 | `0.11` / `0.54` | **25.0 / 25.0** |
| `ondocollective-jp` | `tier2_webgl` | `1280×828px` (23,034 B) | `390×2616px` (57,332 B) | 56 | 16 | 327 | 113 | `0.10` / `0.52` | **25.0 / 25.0** |
| `noho-ink` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `north-cloud` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `offform-net` | `blocked` (`502`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 502 (502 Bad Gateway)`)** |
| `offpossible-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
| `ofrenda-davidlangarica-dev` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `onecoldnight-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
