# Round 11 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-11`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 11 Target Scope
  1. `deathbyscroll-com` — *Death by Scroll*
  2. `degacsid-com` — *DEGACSID*
  3. `delice-ca` — *Accueil - Délice*
  4. `deltacafes-com_en` — *Delta, coffee with heart · Delta Cafés — The coffee of your life*
  5. `departmentofemotions-com` — *Department of Emotions*
  6. `derive-ocean-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  7. `digitalofthings-studio` — *digital of things · user experience digital studio*
  8. `diseinuz-com` — *DISEINUZ — Bilbao Bizkaia Design Summit*
  9. `diversify-nz` — *diversify.nz*
  10. `douglus-co` — *Douglus Nguyen — Web Designer from Vietnam*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `deathbyscroll-com` | `tier1_fast` | `1440×2400px` (107,207 B) | `390×844px` (17,232 B) | 83 | 16 | 306 | 118 | `0.09` / `0.48` | **25.0 / 25.0** |
| `degacsid-com` | `tier1_fast` | `1440×900px` (1,457,224 B) | `390×844px` (440,839 B) | 1 | 13 | 273 | 100 | `0.10` / `0.57` | **25.0 / 25.0** |
| `delice-ca` | `tier1_fast` | `1440×2400px` (2,341,984 B) | `390×2400px` (471,759 B) | 76 | 16 | 286 | 108 | `0.09` / `0.48` | **25.0 / 25.0** |
| `deltacafes-com_en` | `tier1_fast` | `1440×2400px` (1,313,000 B) | `390×844px` (251,176 B) | 237 | 16 | 286 | 108 | `0.09` / `0.49` | **25.0 / 25.0** |
| `departmentofemotions-com` | `tier1_fast` | `1440×900px` (347,074 B) | `390×844px` (159,166 B) | 11 | 16 | 282 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `digitalofthings-studio` | `tier1_fast` | `1440×900px` (151,483 B) | `390×844px` (89,802 B) | 3 | 16 | 282 | 106 | `0.10` / `0.57` | **25.0 / 25.0** |
| `diseinuz-com` | `tier1_fast` | `1440×2400px` (304,363 B) | `390×2400px` (249,217 B) | 40 | 16 | 282 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `diversify-nz` | `tier2_webgl` | `1440×900px` (367,328 B) | `390×844px` (121,841 B) | 48 | 16 | 297 | 113 | `0.10` / `0.53` | **25.0 / 25.0** |
| `douglus-co` | `tier1_fast` | `1440×900px` (93,504 B) | `390×846px` (108,390 B) | 94 | 16 | 284 | 107 | `0.10` / `0.55` | **25.0 / 25.0** |
| `derive-ocean-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
