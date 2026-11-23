# Round 44 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-44`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 44 Target Scope
  1. `www-chriswilliamsart-com` — *Chris Williams Art Gallery · Contemporary painting in London*
  2. `www-codeofsagar-in` — *Sagar K. Ghosh — Full-stack Developer & Designer*
  3. `www-concretemanagement-fr` — *Concrete.*
  4. `www-cybear-it_world` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  5. `www-danielebuser-com` — *Daniele Buser · Creative Developer*
  6. `www-davidecarusio-it` — *Davide Carusio - Web Designer / Webflow Dev*
  7. `www-dbydt-space` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  8. `www-deathtorobots-com` — *Death to Robots*
  9. `www-designbomb-it` — *Design Bomb Festival*
  10. `www-discoverforgiveness-org` — *Discover Forgiveness · Templeton World Charity Foundation*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-chriswilliamsart-com` | `tier1_fast` | `1440×900px` (586,812 B) | `390×844px` (154,244 B) | 7 | 16 | 284 | 107 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-codeofsagar-in` | `tier1_fast` | `1440×2400px` (789,873 B) | `390×2400px` (128,641 B) | 126 | 16 | 283 | 106 | `0.11` / `0.53` | **25.0 / 25.0** |
| `www-concretemanagement-fr` | `tier1_fast` | `1440×900px` (1,057,486 B) | `390×844px` (246,673 B) | 25 | 16 | 293 | 111 | `0.12` / `0.56` | **25.0 / 25.0** |
| `www-danielebuser-com` | `tier1_fast` | `1440×2400px` (15,701 B) | `390×2400px` (154,876 B) | 72 | 16 | 290 | 110 | `0.11` / `0.53` | **25.0 / 25.0** |
| `www-davidecarusio-it` | `tier2_webgl` | `1440×900px` (292,372 B) | `390×844px` (270,045 B) | 27 | 16 | 290 | 110 | `0.11` / `0.56` | **25.0 / 25.0** |
| `www-deathtorobots-com` | `tier1_fast` | `1440×2400px` (791,722 B) | `390×2400px` (638,844 B) | 31 | 16 | 288 | 109 | `0.12` / `0.57` | **25.0 / 25.0** |
| `www-designbomb-it` | `tier1_fast` | `1440×2400px` (166,318 B) | `390×2400px` (186,632 B) | 36 | 16 | 288 | 109 | `0.12` / `0.57` | **25.0 / 25.0** |
| `www-discoverforgiveness-org` | `tier1_fast` | `1440×2400px` (206,157 B) | `390×2400px` (138,487 B) | 28 | 16 | 302 | 116 | `0.12` / `0.54` | **25.0 / 25.0** |
| `www-cybear-it_world` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `www-dbydt-space` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
