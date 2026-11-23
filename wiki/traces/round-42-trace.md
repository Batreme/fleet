# Round 42 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-42`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 42 Target Scope
  1. `www-apc-pallets-nl` — *Algemeen Pallet Centrum · APC*
  2. `www-areyoudami-com` — *AreyouDami. — Damilare Olawoyin, Creative Director*
  3. `www-arsenals-com` — *Arsenals · Liberty is built*
  4. `www-arshawnarbabi-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  5. `www-ataccama-com_fwrd2026` — *Ataccama FWRD 2026: Press play on what's next in data trust · Ataccama*
  6. `www-avara-band` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  7. `www-banham-co-uk` — *Banham · Experts in Security Services Since 1926*
  8. `www-barebonescollective-com` — *Bare Bones Collective*
  9. `www-baseline-agency` — *Baseline · Brand identity systems, designed and built*
  10. `www-beige-zone` — *Alex/Avery Beige Artist, Playwright / Creative Technologist / Biohacker*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-apc-pallets-nl` | `tier1_fast` | `1440×2400px` (1,997,280 B) | `390×2400px` (569,007 B) | 201 | 16 | 282 | 106 | `0.17` / `0.59` | **25.0 / 25.0** |
| `www-areyoudami-com` | `tier1_fast` | `1440×2400px` (697,318 B) | `390×2400px` (257,132 B) | 52 | 16 | 282 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-arsenals-com` | `tier1_fast` | `1440×900px` (2,397,606 B) | `390×2400px` (372,642 B) | 14 | 16 | 283 | 106 | `0.09` / `0.54` | **25.0 / 25.0** |
| `www-ataccama-com_fwrd2026` | `tier1_fast` | `1440×2400px` (363,899 B) | `390×2400px` (164,758 B) | 323 | 16 | 298 | 114 | `0.10` / `0.49` | **25.0 / 25.0** |
| `www-banham-co-uk` | `tier1_fast` | `1440×2400px` (3,207,146 B) | `390×2400px` (926,927 B) | 138 | 16 | 292 | 111 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-barebonescollective-com` | `tier2_webgl` | `1440×2400px` (224,916 B) | `390×844px` (278,643 B) | 1 | 13 | 273 | 100 | `0.17` / `0.59` | **25.0 / 25.0** |
| `www-baseline-agency` | `tier1_fast` | `1440×2400px` (665,741 B) | `390×2400px` (364,063 B) | 61 | 16 | 282 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-beige-zone` | `tier1_fast` | `1440×2025px` (667,139 B) | `390×2191px` (217,945 B) | 61 | 16 | 304 | 117 | `0.08` / `0.48` | **25.0 / 25.0** |
| `www-arshawnarbabi-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `www-avara-band` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
