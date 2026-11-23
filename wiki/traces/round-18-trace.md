# Round 18 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-18`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 18 Target Scope
  1. `houseofgiants-com` — *House of Giants · Product engineering partner*
  2. `hoyojerez-com` — *HOYO Jerez · Discoteca en Jerez de la Frontera*
  3. `ieqtechnology-com` — *IEQ Technology · Innovation. Experience. Quality.*
  4. `iginusa-com` — *IGIN USA · Official Home of IGIN in the United States*
  5. `imdday-ch` — *IMDDay 2026*
  6. `infinitytechstack-uk_pulsebridge` — *PulseBridge [2026] · AI IDE Mobile Companion (Free)*
  7. `inherited-band` — *INHERITED*
  8. `inks-studio` — *Ink Studio - UI UX Design, CRO & Webflow Development Agency*
  9. `iroom-devinthehood-com` — *iRoom framework 3 · Get started*
  10. `its-tomo-dev` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `houseofgiants-com` | `tier1_fast` | `1440×2400px` (452,828 B) | `390×2400px` (257,350 B) | 188 | 16 | 282 | 106 | `0.09` / `0.47` | **25.0 / 25.0** |
| `hoyojerez-com` | `tier2_webgl` | `1440×900px` (58,553 B) | `390×844px` (20,827 B) | 6 | 16 | 282 | 106 | `0.09` / `0.55` | **25.0 / 25.0** |
| `ieqtechnology-com` | `tier1_fast` | `1440×2400px` (446,463 B) | `390×2400px` (196,864 B) | 51 | 16 | 292 | 111 | `0.10` / `0.51` | **25.0 / 25.0** |
| `iginusa-com` | `tier1_fast` | `1440×2400px` (323,548 B) | `390×2400px` (186,976 B) | 204 | 16 | 282 | 106 | `0.10` / `0.48` | **25.0 / 25.0** |
| `imdday-ch` | `tier1_fast` | `1440×2400px` (593,579 B) | `390×2400px` (396,217 B) | 53 | 16 | 282 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `infinitytechstack-uk_pulsebridge` | `tier1_fast` | `1440×2400px` (967,363 B) | `390×2400px` (469,877 B) | 157 | 16 | 304 | 117 | `0.10` / `0.49` | **25.0 / 25.0** |
| `inherited-band` | `tier1_fast` | `1440×2400px` (2,794,697 B) | `390×844px` (504,931 B) | 5 | 16 | 281 | 105 | `0.09` / `0.55` | **25.0 / 25.0** |
| `inks-studio` | `tier1_fast` | `1440×2400px` (689,195 B) | `390×2400px` (409,948 B) | 21 | 16 | 303 | 116 | `0.09` / `0.49` | **25.0 / 25.0** |
| `iroom-devinthehood-com` | `tier1_fast` | `1440×2400px` (1,193,173 B) | `390×2400px` (385,918 B) | 113 | 16 | 288 | 109 | `0.10` / `0.51` | **25.0 / 25.0** |
| `its-tomo-dev` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
