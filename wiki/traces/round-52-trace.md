# Round 52 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-52`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 52 Target Scope
  1. `www-poulo-site` — *Blocked (`Upstream HTTP 429 — Vercel Security Checkpoint`)*
  2. `www-pragenhatlen-com` — *Prägen Hätlen · Swiss watchmaking for the crypto community.*
  3. `www-qissa-co-uk` — *Indian Restaurant in Sevenoaks, Kent · Qissa*
  4. `www-quintadamalia-com` — *Quinta D. Amália - Redefining Luxury Living in Portugal*
  5. `www-raomuhammadhamza-tech` — *Rao Muhammad Hamza, AI Engineer*
  6. `www-rebelliously-optimistic-com` — *Rebelliously Optimistic — A movement for the human future*
  7. `www-remyshoots-co-za` — *Remy Shoots*
  8. `www-rikoutaku-work` — *Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio*
  9. `www-romainavalle-dev` — *Romain Avalle - Interactive developper*
  10. `www-rosshalfin-com` — *Ross Halfin Photography · Music Images + Fine Art Prints*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-pragenhatlen-com` | `tier2_webgl` | `1440×900px` (121,541 B) | `390×844px` (95,087 B) | 71 | 16 | 284 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-qissa-co-uk` | `tier1_fast` | `1440×2400px` (2,134,330 B) | `390×2400px` (498,596 B) | 26 | 16 | 298 | 114 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-quintadamalia-com` | `tier1_fast` | `1440×2400px` (236,823 B) | `390×2400px` (634,702 B) | 574 | 16 | 312 | 121 | `0.08` / `0.48` | **25.0 / 25.0** |
| `www-raomuhammadhamza-tech` | `tier1_fast` | `1440×2400px` (418,819 B) | `390×2400px` (189,110 B) | 32 | 16 | 298 | 114 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-rebelliously-optimistic-com` | `tier1_fast` | `1440×900px` (59,118 B) | `390×844px` (37,656 B) | 16 | 16 | 294 | 112 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-remyshoots-co-za` | `tier1_fast` | `1440×900px` (26,808 B) | `390×844px` (14,976 B) | 45 | 16 | 288 | 109 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-rikoutaku-work` | `tier2_webgl` | `1440×2400px` (22,913 B) | `390×844px` (47,129 B) | 36 | 16 | 294 | 112 | `0.08` / `0.52` | **25.0 / 25.0** |
| `www-romainavalle-dev` | `tier2_webgl` | `1440×900px` (18,869 B) | `390×2400px` (49,876 B) | 11 | 16 | 283 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-rosshalfin-com` | `tier1_fast` | `1440×2400px` (802,605 B) | `390×2400px` (415,203 B) | 67 | 16 | 292 | 111 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-poulo-site` | `blocked` (`429`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 429 — Vercel Security Checkpoint`)** |
