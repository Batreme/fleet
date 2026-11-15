# Round 18 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-18`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 18 Target Scope
  1. `houseofgiants-com` — *House of Giants · Product engineering partner* (`https://houseofgiants.com`)
  2. `hoyojerez-com` — *HOYO Jerez · Discoteca en Jerez de la Frontera* (`https://hoyojerez.com/`)
  3. `ieqtechnology-com` — *IEQ Technology · Innovation. Experience. Quality.* (`https://ieqtechnology.com/`)
  4. `iginusa-com` — *IGIN USA · Official Home of IGIN in the United States* (`https://iginusa.com`)
  5. `imdday-ch` — *IMDDay 2026* (`https://imdday.ch/`)
  6. `infinitytechstack-uk_pulsebridge` — *PulseBridge [2026] · AI IDE Mobile Companion (Free)* (`https://infinitytechstack.uk/pulsebridge`)
  7. `inherited-band` — *INHERITED* (`https://inherited.band/`)
  8. `inks-studio` — *Ink Studio - UI UX Design, CRO & Webflow Development Agency* (`http://inks.studio/`)
  9. `iroom-devinthehood-com` — *iRoom framework 3 · Get started* (`https://iroom.devinthehood.com/`)
  10. `its-tomo-dev` — *its_tomo - creative engineer* (`https://its-tomo.dev/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `houseofgiants-com` | `1440×6415px` (776,000 B) | `390×2400px` (164,807 B) | 188 | 16 | 248 | 102 | `0.09` / `0.48` | **25.0 / 25.0** |
| `hoyojerez-com` | `1440×2400px` (238,777 B) | `390×2400px` (130,125 B) | 6 | 16 | 256 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `ieqtechnology-com` | `1440×9002px` (374,113 B) | `390×2400px` (126,235 B) | 51 | 16 | 260 | 108 | `0.09` / `0.52` | **25.0 / 25.0** |
| `iginusa-com` | `1440×13053px` (1,255,047 B) | `390×2400px` (59,999 B) | 699 | 16 | 256 | 106 | `0.09` / `0.46` | **25.0 / 25.0** |
| `imdday-ch` | `1440×2400px` (67,119 B) | `390×2400px` (297,390 B) | 53 | 16 | 254 | 105 | `0.09` / `0.50` | **25.0 / 25.0** |
| `infinitytechstack-uk_pulsebridge` | `1440×2400px` (1,520,832 B) | `390×2400px` (756,388 B) | 157 | 16 | 262 | 109 | `0.09` / `0.49` | **25.0 / 25.0** |
| `inherited-band` | `1440×4747px` (4,433,860 B) | `390×2400px` (552,310 B) | 5 | 16 | 254 | 105 | `0.09` / `0.53` | **25.0 / 25.0** |
| `inks-studio` | `1440×9230px` (1,012,681 B) | `390×2400px` (97,703 B) | 443 | 16 | 272 | 114 | `0.08` / `0.48` | **25.0 / 25.0** |
| `iroom-devinthehood-com` | `1440×3944px` (1,417,250 B) | `390×2400px` (432,996 B) | 113 | 16 | 260 | 108 | `0.09` / `0.50` | **25.0 / 25.0** |
| `its-tomo-dev` | `1440×2400px` (576,382 B) | `390×2400px` (90,777 B) | 44 | 16 | 254 | 105 | `0.09` / `0.52` | **25.0 / 25.0** |
