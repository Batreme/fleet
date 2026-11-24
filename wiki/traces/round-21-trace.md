# Round 21 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-21`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 21 Target Scope
  1. `konkelectrical-com` — *Konk Electrical · Eastern Suburbs Electricians, Sydney*
  2. `ksenpanchenko-com` — *Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS*
  3. `labellavista-es` — *LABELLAVISTA — Creative production co.*
  4. `labs-griflan-com` — *Blocked (`Browser/WebGPU Hardware Gate (Griflan Labs)`)*
  5. `ladolfinajumping-com` — *La Dolfina Jumping. World class genetics, breed in Argentina*
  6. `lajoya-foods-com_en` — *LAJOYA GOURMET*
  7. `later-com_made-you-look` — *Blocked (`Headless Preloader / Blank Viewport Capture (Loading 100%)`)*
  8. `launch-joinautopilot-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  9. `layernative-com_tinkeroll` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://layernative.com/tinkeroll/', waiting until 'domcontentloaded' )`)*
  10. `layersoftime-studio` — *LAYERS OF TIME — The show runs on our clock.*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `konkelectrical-com` | `tier1_fast` | `1280×6624px` (393,150 B) | `390×2616px` (55,890 B) | 41 | 16 | 364 | 119 | `0.10` / `0.51` | **25.0 / 25.0** |
| `ksenpanchenko-com` | `tier1_fast` | `1280×6624px` (409,162 B) | `390×2616px` (50,152 B) | 240 | 16 | 355 | 117 | `0.08` / `0.52` | **25.0 / 25.0** |
| `labellavista-es` | `tier1_fast` | `1280×6624px` (390,070 B) | `390×2616px` (131,500 B) | 36 | 16 | 347 | 114 | `0.10` / `0.52` | **25.0 / 25.0** |
| `ladolfinajumping-com` | `tier1_fast` | `1280×6624px` (422,360 B) | `390×872px` (55,262 B) | 12 | 16 | 348 | 116 | `0.09` / `0.53` | **25.0 / 25.0** |
| `lajoya-foods-com_en` | `tier1_fast` | `1280×828px` (37,480 B) | `390×872px` (9,276 B) | 13 | 16 | 313 | 111 | `0.09` / `0.53` | **25.0 / 25.0** |
| `layersoftime-studio` | `tier1_fast` | `1280×4140px` (185,768 B) | `390×2616px` (85,498 B) | 35 | 16 | 347 | 117 | `0.09` / `0.51` | **25.0 / 25.0** |
| `labs-griflan-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Browser/WebGPU Hardware Gate (Griflan Labs)`)** |
| `later-com_made-you-look` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (Loading 100%)`)** |
| `launch-joinautopilot-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `layernative-com_tinkeroll` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
