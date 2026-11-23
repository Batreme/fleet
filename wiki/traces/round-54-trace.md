# Round 54 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-54`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 54 Target Scope
  1. `www-soe-org-uk` — *Blocked (`Upstream HTTP 403 (Checking your browser...)`)*
  2. `www-spectup-com` — *Private Capital Advisory: Capital Raising and M&A · spectup*
  3. `www-stellarmanagement-com` — *Stellar Management · NYC Real Estate Developer & No Fee Rentals*
  4. `www-studioplato-co` — *Studio Plato - Contemporary Interior Design*
  5. `www-sztanki-com` — *Blocked (`Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)`)*
  6. `www-teamcafeteria-com_2027` — *2027 — a [cafeteria] report*
  7. `www-tedxportland-com` — *TEDxPortland*
  8. `www-terakawaoffice-com_en` — *Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office*
  9. `www-terrenohotel-com_en` — *Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca*
  10. `www-theboringblog-ai` — *The Boring Blog — art, engineering and AI*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-spectup-com` | `tier1_fast` | `1440×2400px` (1,510,479 B) | `390×2400px` (451,470 B) | 162 | 16 | 288 | 109 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-stellarmanagement-com` | `tier1_fast` | `1440×2400px` (1,137,302 B) | `390×2400px` (230,709 B) | 92 | 16 | 308 | 119 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-studioplato-co` | `tier1_fast` | `1440×900px` (1,036,037 B) | `390×844px` (236,762 B) | 11 | 16 | 288 | 109 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-teamcafeteria-com_2027` | `tier2_webgl` | `1440×900px` (50,436 B) | `390×844px` (58,589 B) | 142 | 16 | 282 | 106 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-tedxportland-com` | `tier1_fast` | `1440×2400px` (1,861,788 B) | `390×2400px` (227,347 B) | 85 | 16 | 282 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-terakawaoffice-com_en` | `tier2_webgl` | `1440×900px` (2,095,834 B) | `390×844px` (239,903 B) | 36 | 16 | 294 | 112 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-terrenohotel-com_en` | `tier1_fast` | `1440×2400px` (1,634,439 B) | `390×2400px` (634,794 B) | 492 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-theboringblog-ai` | `tier2_webgl` | `1440×900px` (140,684 B) | `390×844px` (54,013 B) | 427 | 16 | 304 | 117 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-soe-org-uk` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 (Checking your browser...)`)** |
| `www-sztanki-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (cannot hydrate without in`)** |
