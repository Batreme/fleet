# Round 43 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-43`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `7` (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 43 Target Scope
  1. `www-bitwip-fr_en` — *Communications consulting agency for Overseas France · Bitwip* (`https://www.bitwip.fr/en`)
  2. `www-bluesqx-com` — *Blue Square X – Premium LED Displays & Immersive Digital Experiences* (`https://www.bluesqx.com/`)
  3. `www-blumjeffrey-com` — *Jeffrey Blum — AI Digital Creative Director* (`https://www.blumjeffrey.com`)
  4. `www-brandlos-nl` — *Brandlos · Het creatieve bureau van Limburg* (`https://www.brandlos.nl`)
  5. `www-brandtheagency-com` — *BR& – Creating brands that make you smile* (`https://www.brandtheagency.com/`)
  6. `www-butter-video` — *Butter Video · Online Video Editor Engineered for Creativity* (`https://www.butter.video/`)
  7. `www-cadillacf1team-com` — *Blocked (`CloudFront HTTP 403 WAF Block (ERROR: The request could not be satisfied)`)*
  8. `www-cartier-com_en-fr-lechoeurdespierres` — *Blocked (`Akamai Edge WAF Block (Access Denied)`)*
  9. `www-cartier-com_en-us-roadster-universe-html` — *Blocked (`Akamai Edge WAF Block (Access Denied)`)*
  10. `www-casamomo-at` — *Casa Momo • Boutique Apartments in Graz* (`https://www.casamomo.at/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-bitwip-fr_en` | `1440×12242px` (911,055 B) | `390×2400px` (47,249 B) | 184 | 16 | 264 | 110 | `0.08` / `0.50` | **25.0 / 25.0** |
| `www-bluesqx-com` | `1440×11949px` (1,747,895 B) | `390×2400px` (56,207 B) | 66 | 16 | 258 | 107 | `0.11` / `0.56` | **25.0 / 25.0** |
| `www-blumjeffrey-com` | `1440×20402px` (3,348,305 B) | `390×2400px` (540,130 B) | 46 | 16 | 256 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-brandlos-nl` | `1440×9524px` (176,796 B) | `390×2400px` (233,040 B) | 11 | 16 | 264 | 110 | `0.11` / `0.56` | **25.0 / 25.0** |
| `www-brandtheagency-com` | `1440×2400px` (1,390,975 B) | `390×2400px` (52,248 B) | 1044 | 16 | 256 | 106 | `0.09` / `0.46` | **25.0 / 25.0** |
| `www-butter-video` | `1440×14365px` (691,751 B) | `390×2400px` (59,226 B) | 22 | 16 | 262 | 109 | `0.08` / `0.51` | **25.0 / 25.0** |
| `www-cadillacf1team-com` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`CloudFront HTTP 403 WAF Block (ERROR: The request could not be satisfied)`)** |
| `www-cartier-com_en-fr-lechoeurdespierres` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Akamai Edge WAF Block (Access Denied)`)** |
| `www-cartier-com_en-us-roadster-universe-html` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Akamai Edge WAF Block (Access Denied)`)** |
| `www-casamomo-at` | `1440×2400px` (64,578 B) | `390×2400px` (346,681 B) | 36 | 16 | 258 | 107 | `0.09` / `0.52` | **25.0 / 25.0** |
