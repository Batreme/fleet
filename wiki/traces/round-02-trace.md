# Round 02 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-02`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 02 Target Scope
  1. `100yearsmonet-com` — *Monet 100 — A century without Claude Monet · 3D gallery*
  2. `11moissanstoit-com` — *11 mois sans toi(t), le tour du monde de Josué & Philippe*
  3. `1stdecember-com` — *First December Films · Ad Film Production House in India*
  4. `21oaks-org` — *21Oaks Student Apartments • USC & Williams-Brice*
  5. `360lexingtonave-com` — *360 Lexington Avenue*
  6. `abhayrohit-com` — *Abhay Rohit — Creative Product Engineer*
  7. `about-centra-com` — *Centra? Centra! The definitive guide.*
  8. `abyme-app` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  9. `actl-me` — *ACTL — Arabian Community Tennis League*
  10. `adamperlis-com` — *Adam Perlis — I design and build apps*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `100yearsmonet-com` | `tier1_fast` | `1440×2400px` (1,451,947 B) | `390×2400px` (327,157 B) | 7 | 16 | 288 | 109 | `0.11` / `0.50` | **25.0 / 25.0** |
| `11moissanstoit-com` | `tier1_fast` | `1440×900px` (410,187 B) | `390×844px` (251,917 B) | 9 | 16 | 292 | 111 | `0.10` / `0.52` | **25.0 / 25.0** |
| `1stdecember-com` | `tier1_fast` | `1440×2400px` (1,648,174 B) | `390×2400px` (586,155 B) | 168 | 16 | 282 | 106 | `0.14` / `0.58` | **25.0 / 25.0** |
| `21oaks-org` | `tier1_fast` | `1440×2400px` (1,617,083 B) | `390×2400px` (332,628 B) | 9 | 16 | 282 | 106 | `0.14` / `0.60` | **25.0 / 25.0** |
| `360lexingtonave-com` | `tier1_fast` | `1440×2400px` (379,119 B) | `390×2400px` (253,489 B) | 36 | 16 | 284 | 107 | `0.11` / `0.50` | **25.0 / 25.0** |
| `abhayrohit-com` | `tier1_fast` | `1440×2400px` (578,597 B) | `390×2400px` (204,075 B) | 174 | 16 | 288 | 109 | `0.09` / `0.47` | **25.0 / 25.0** |
| `about-centra-com` | `tier1_fast` | `1440×2400px` (620,380 B) | `390×2400px` (237,882 B) | 31 | 16 | 297 | 112 | `0.14` / `0.60` | **25.0 / 25.0** |
| `actl-me` | `tier1_fast` | `1440×2400px` (159,685 B) | `390×2400px` (71,429 B) | 5 | 16 | 286 | 108 | `0.11` / `0.51` | **25.0 / 25.0** |
| `adamperlis-com` | `tier2_webgl` | `1440×900px` (48,236 B) | `390×2400px` (109,420 B) | 83 | 16 | 284 | 107 | `0.10` / `0.52` | **25.0 / 25.0** |
| `abyme-app` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
