# Round 38 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-38`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 38 Target Scope
  1. `tridentstars-maserati-com_en` — *Discover Maserati’s Trident Constellation in the Sky* (`https://tridentstars.maserati.com/en/`)
  2. `turismo-gov-st_fr` — *Homepage · São Tomé E Príncipe* (`https://turismo.gov.st/fr`)
  3. `twodo-design` — *Two-Do* (`https://twodo.design`)
  4. `twohalves-co` — *Two Halves — design & development studio, Cairo* (`https://twohalves.co/`)
  5. `ty1official-com` — *TY1 — DJ & Producer* (`https://ty1official.com`)
  6. `uimaven-art` — *uimaven.art* (`https://uimaven.art`)
  7. `untitledfilm-framer-website` — *“Untitled.”* (`https://untitledfilm.framer.website/`)
  8. `useguidely-co` — *guidely - the hospitality of the future* (`https://useguidely.co/`)
  9. `v4vevilos-gr` — *Βέβηλος • Once dead twice alive* (`https://v4vevilos.gr`)
  10. `vadimcarazan-com` — *Vadim Carazan, Creative Director* (`https://vadimcarazan.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `tridentstars-maserati-com_en` | `1440×2400px` (74,269 B) | `390×2400px` (47,776 B) | 89 | 16 | 256 | 106 | `0.09` / `0.55` | **25.0 / 25.0** |
| `turismo-gov-st_fr` | `1440×2400px` (703,929 B) | `390×2400px` (330,175 B) | 104 | 16 | 256 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `twodo-design` | `1440×10990px` (597,896 B) | `390×2400px` (601,208 B) | 19 | 16 | 268 | 112 | `0.09` / `0.53` | **25.0 / 25.0** |
| `twohalves-co` | `1440×14075px` (399,003 B) | `390×2400px` (112,986 B) | 27 | 16 | 262 | 109 | `0.09` / `0.55` | **25.0 / 25.0** |
| `ty1official-com` | `1440×2400px` (542,633 B) | `390×2400px` (408,104 B) | 172 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `uimaven-art` | `1440×2400px` (295,926 B) | `390×2400px` (330,803 B) | 101 | 16 | 263 | 108 | `0.09` / `0.55` | **25.0 / 25.0** |
| `untitledfilm-framer-website` | `1440×8820px` (6,073,293 B) | `390×2400px` (244,749 B) | 38 | 16 | 254 | 105 | `0.08` / `0.51` | **25.0 / 25.0** |
| `useguidely-co` | `1440×3643px` (1,047,878 B) | `390×2400px` (556,072 B) | 14 | 16 | 256 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `v4vevilos-gr` | `1440×2400px` (1,288,014 B) | `390×2400px` (646,274 B) | 27 | 16 | 256 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `vadimcarazan-com` | `1440×2400px` (110,476 B) | `390×2400px` (35,253 B) | 14 | 16 | 254 | 105 | `0.09` / `0.55` | **25.0 / 25.0** |
