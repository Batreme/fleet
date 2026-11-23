# Round 20 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-20`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 20 Target Scope
  1. `kamdalej-sk_en` — *Mastercard · Where Next*
  2. `karma-tracks-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  3. `kelvin-8b-com` — *Kelvin — three nights of music, filmed in heat*
  4. `key-co` — *KEY.co · Luxury Vacation Home Rentals + Concierge Services*
  5. `kindi-land` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  6. `kingriver-com-au` — *Australian Wagyu Beef · King River Legendary Wagyu*
  7. `kinoria-studio` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  8. `kissbranding-co-uk` — *Kiss · Brands that Kiss*
  9. `klad-design` — *Multidisciplinary Design Syndicate – KLAD*
  10. `kohenavocats-com_avocats-droit-famille-paris` — *Avocat Droit de la Famille Paris · Divorce, Garde d'Enfants, Succession*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kamdalej-sk_en` | `tier1_fast` | `1440×2400px` (573,102 B) | `390×2400px` (217,652 B) | 149 | 16 | 282 | 106 | `0.11` / `0.48` | **25.0 / 25.0** |
| `kelvin-8b-com` | `tier1_fast` | `1440×2400px` (639,359 B) | `390×2400px` (216,410 B) | 23 | 16 | 298 | 114 | `0.10` / `0.49` | **25.0 / 25.0** |
| `key-co` | `tier2_webgl` | `1440×900px` (797,102 B) | `390×844px` (302,648 B) | 2 | 14 | 278 | 104 | `0.10` / `0.48` | **25.0 / 25.0** |
| `kingriver-com-au` | `tier1_fast` | `1440×2400px` (117,428 B) | `390×2400px` (178,900 B) | 51 | 16 | 294 | 112 | `0.10` / `0.52` | **25.0 / 25.0** |
| `kissbranding-co-uk` | `tier1_fast` | `1440×900px` (1,081,644 B) | `390×844px` (317,697 B) | 95 | 16 | 282 | 106 | `0.11` / `0.52` | **25.0 / 25.0** |
| `klad-design` | `tier1_fast` | `1440×2400px` (934,719 B) | `390×2400px` (476,622 B) | 68 | 16 | 286 | 108 | `0.11` / `0.52` | **25.0 / 25.0** |
| `kohenavocats-com_avocats-droit-famille-paris` | `tier1_fast` | `1440×2400px` (816,141 B) | `390×2400px` (251,006 B) | 298 | 16 | 286 | 108 | `0.11` / `0.49` | **25.0 / 25.0** |
| `karma-tracks-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `kindi-land` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `kinoria-studio` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
