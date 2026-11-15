# Round 05 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-05`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 05 Target Scope
  1. `articles-gamcare-org-uk` — *The Gamification of Everything · GamCare* (`https://articles.gamcare.org.uk/`)
  2. `aryabhangybuilders-com` — *Premium Builders In Kochi · Flats & Apartments · Arya Bhangy* (`https://aryabhangybuilders.com/`)
  3. `ascension-pegassi-be` — *Ascension — Pegassi* (`https://ascension.pegassi.be/`)
  4. `atmos-gallery` — *Atmos Gallery · Image Colour Palette Generator* (`https://atmos.gallery`)
  5. `auge-xp-com` — *Digital Experience Studio · AUGE Experience* (`https://auge-xp.com/`)
  6. `aviator-yakudoo-games` — *Aviator* (`https://aviator.yakudoo.games`)
  7. `awards-racing` — *Awards Racing* (`https://awards.racing`)
  8. `awmedia-marketing` — *AW Media & Marketing · UK Web Design Studio* (`https://awmedia.marketing/`)
  9. `aya-nl` — *Danstheater AYA - eigenzinnige voorstellingen voor jong publiek* (`https://aya.nl`)
  10. `azimuteresidencial-com-br` — *Azimute — Seu próximo horizonte · ASL* (`https://azimuteresidencial.com.br/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `articles-gamcare-org-uk` | `1440×2400px` (229,542 B) | `390×2400px` (143,398 B) | 140 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `aryabhangybuilders-com` | `1440×2400px` (897,487 B) | `390×2400px` (406,778 B) | 171 | 16 | 256 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `ascension-pegassi-be` | `1440×5425px` (764,084 B) | `390×2400px` (197,732 B) | 46 | 16 | 256 | 106 | `0.10` / `0.53` | **25.0 / 25.0** |
| `atmos-gallery` | `1440×2400px` (552,923 B) | `390×2400px` (312,676 B) | 260 | 16 | 256 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
| `auge-xp-com` | `1440×2400px` (917,217 B) | `390×2400px` (227,642 B) | 37 | 16 | 250 | 103 | `0.10` / `0.53` | **25.0 / 25.0** |
| `aviator-yakudoo-games` | `1440×2400px` (489,328 B) | `390×2400px` (292,165 B) | 87 | 16 | 258 | 107 | `0.10` / `0.53` | **25.0 / 25.0** |
| `awards-racing` | `1440×2400px` (575,379 B) | `390×2400px` (273,258 B) | 57 | 16 | 253 | 103 | `0.10` / `0.51` | **25.0 / 25.0** |
| `awmedia-marketing` | `1440×16653px` (1,824,041 B) | `390×2400px` (54,524 B) | 65 | 16 | 256 | 106 | `0.10` / `0.53` | **25.0 / 25.0** |
| `aya-nl` | `1440×8166px` (1,696,402 B) | `390×2400px` (363,660 B) | 66 | 16 | 274 | 115 | `0.08` / `0.49` | **25.0 / 25.0** |
| `azimuteresidencial-com-br` | `1440×29619px` (8,459,296 B) | `390×2400px` (105,875 B) | 20 | 16 | 266 | 111 | `0.09` / `0.50` | **25.0 / 25.0** |
