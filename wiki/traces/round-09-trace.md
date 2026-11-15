# Round 09 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-09`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 09 Target Scope
  1. `clinia-com` — *Patient Context for Healthcare AI · Clinia* (`https://clinia.com`)
  2. `clipdance-ai` — *Seedance 2.0 - Free AI Video Generator · Text/Image to Video* (`https://clipdance.ai`)
  3. `clubcharlestown-com-au` — *Home · Club Charlestown* (`https://clubcharlestown.com.au/`)
  4. `cobaltaf-org` — *Cobalt Abortion Fund* (`https://cobaltaf.org/`)
  5. `coloniazacamil-com` — *Colonia Zacamil* (`https://coloniazacamil.com/`)
  6. `concretaceramiche-it` — *Concreta Ceramiche Artigianali Fatte a Mano* (`https://concretaceramiche.it/`)
  7. `constellations-icilalune-com` — *Constellation(s) — Immersive virtual 3D art exhibitions* (`https://constellations.icilalune.com/`)
  8. `continuance-ai` — *Continuance - A novel by Chris Bennett* (`https://continuance.ai/`)
  9. `crl-2026-webflow-io` — *Creative Reference Library · CRL* (`https://crl-2026.webflow.io/`)
  10. `crun-ai` — *One API for All Top AI Models – Cost-Effective AI API · Crun* (`https://crun.ai`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `clinia-com` | `1440×2400px` (198,477 B) | `390×2400px` (132,308 B) | 231 | 16 | 270 | 113 | `0.09` / `0.53` | **25.0 / 25.0** |
| `clipdance-ai` | `1440×2400px` (654,395 B) | `390×2400px` (314,619 B) | 287 | 16 | 266 | 111 | `0.09` / `0.52` | **25.0 / 25.0** |
| `clubcharlestown-com-au` | `1440×2400px` (102,365 B) | `390×2400px` (64,884 B) | 429 | 16 | 256 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `cobaltaf-org` | `1440×7641px` (2,530,279 B) | `390×2400px` (409,404 B) | 249 | 16 | 258 | 107 | `0.10` / `0.51` | **25.0 / 25.0** |
| `coloniazacamil-com` | `1440×2400px` (592,626 B) | `390×2400px` (274,015 B) | 17 | 16 | 256 | 106 | `0.10` / `0.55` | **25.0 / 25.0** |
| `concretaceramiche-it` | `1440×9047px` (999,351 B) | `390×2400px` (404,400 B) | 68 | 16 | 264 | 110 | `0.09` / `0.51` | **25.0 / 25.0** |
| `constellations-icilalune-com` | `1440×2963px` (1,994,077 B) | `390×2400px` (76,075 B) | 48 | 16 | 274 | 115 | `0.08` / `0.50` | **25.0 / 25.0** |
| `continuance-ai` | `1440×2400px` (1,196,591 B) | `390×2400px` (469,913 B) | 46 | 16 | 256 | 106 | `0.10` / `0.55` | **25.0 / 25.0** |
| `crl-2026-webflow-io` | `1440×2400px` (101,259 B) | `390×2400px` (56,845 B) | 158 | 16 | 256 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `crun-ai` | `1440×7745px` (1,596,139 B) | `390×2400px` (235,404 B) | 811 | 16 | 256 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
