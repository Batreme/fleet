# Round 08 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-08`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 08 Target Scope
  1. `bybang-co` — *Estudio Bang · Architecture, Interiors, Objects & Digital Media*
  2. `carnilove-ashfall-studio` — *Carnilove · Home*
  3. `chandebootcamp-com` — *Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam*
  4. `chanpan-com-ar` — *ChanPan · AI Video Production, Commercials & Creative Studio — Argentina*
  5. `chicago-com` — *chicago.com*
  6. `christoph-nagel-dev` — *Christoph Nagel · Webentwickler, Fotograf & Videograf in Dorsten*
  7. `cinetic-creatives-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  8. `citadelgroup-org` — *Citadel National Construction Group · Nationwide Construction*
  9. `ciuslabs-com` — *Blocked (`Live desktop screenshot capture failed (0 valid PNG bytes)`)*
  10. `classe-squarespace-com` — *Blocked (`Upstream HTTP 404 (Squarespace - Website Expired)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `bybang-co` | `tier1_fast` | `1440×2400px` (1,579,814 B) | `390×2400px` (636,548 B) | 50 | 16 | 287 | 108 | `0.10` / `0.54` | **25.0 / 25.0** |
| `carnilove-ashfall-studio` | `tier1_fast` | `1440×900px` (334,145 B) | `390×2400px` (60,464 B) | 103 | 16 | 282 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `chandebootcamp-com` | `tier1_fast` | `1440×2400px` (1,563,085 B) | `390×2400px` (862,335 B) | 77 | 16 | 295 | 112 | `0.10` / `0.52` | **25.0 / 25.0** |
| `chanpan-com-ar` | `tier1_fast` | `1440×2400px` (301,961 B) | `390×2400px` (78,915 B) | 12 | 16 | 284 | 107 | `0.09` / `0.54` | **25.0 / 25.0** |
| `chicago-com` | `tier1_fast` | `1440×2400px` (967,331 B) | `390×2400px` (192,833 B) | 391 | 16 | 290 | 110 | `0.09` / `0.51` | **25.0 / 25.0** |
| `christoph-nagel-dev` | `tier1_fast` | `1440×900px` (430,024 B) | `390×844px` (148,349 B) | 19 | 16 | 284 | 107 | `0.08` / `0.49` | **25.0 / 25.0** |
| `citadelgroup-org` | `tier1_fast` | `1440×2400px` (1,443,999 B) | `390×2400px` (460,765 B) | 79 | 16 | 298 | 114 | `0.09` / `0.51` | **25.0 / 25.0** |
| `cinetic-creatives-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `ciuslabs-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop screenshot capture failed (0 valid PNG bytes)`)** |
| `classe-squarespace-com` | `blocked` (`404`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 404 (Squarespace - Website Expired)`)** |
