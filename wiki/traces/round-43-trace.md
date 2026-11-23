# Round 43 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-43`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 43 Target Scope
  1. `www-bitwip-fr_en` — *Communications consulting agency for Overseas France · Bitwip*
  2. `www-bluesqx-com` — *Blue Square X – Premium LED Displays & Immersive Digital Experiences*
  3. `www-blumjeffrey-com` — *Jeffrey Blum — AI Digital Creative Director*
  4. `www-brandlos-nl` — *Brandlos · Het creatieve bureau van Limburg*
  5. `www-brandtheagency-com` — *BR& – Creating brands that make you smile*
  6. `www-butter-video` — *Butter Video · Online Video Editor Engineered for Creativity*
  7. `www-cadillacf1team-com` — *Blocked (`Upstream HTTP 403 — CloudFront WAF Block`)*
  8. `www-cartier-com_en-fr-lechoeurdespierres` — *Blocked (`Upstream HTTP 403 — Edge WAF Access Denied`)*
  9. `www-cartier-com_en-us-roadster-universe-html` — *Blocked (`Upstream HTTP 403 — Edge WAF Access Denied`)*
  10. `www-casamomo-at` — *Casa Momo • Boutique Apartments in Graz*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-bitwip-fr_en` | `tier1_fast` | `1440×2400px` (149,542 B) | `390×2400px` (207,729 B) | 184 | 16 | 296 | 113 | `0.08` / `0.47` | **25.0 / 25.0** |
| `www-bluesqx-com` | `tier1_fast` | `1440×2400px` (638,877 B) | `390×2400px` (780,456 B) | 67 | 16 | 286 | 108 | `0.11` / `0.55` | **25.0 / 25.0** |
| `www-blumjeffrey-com` | `tier1_fast` | `1440×2400px` (1,565,391 B) | `390×2400px` (431,324 B) | 46 | 16 | 283 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-brandlos-nl` | `tier1_fast` | `1440×2400px` (82,933 B) | `390×2400px` (95,706 B) | 11 | 16 | 298 | 114 | `0.11` / `0.55` | **25.0 / 25.0** |
| `www-brandtheagency-com` | `tier2_webgl` | `1440×900px` (575,945 B) | `390×844px` (162,213 B) | 1044 | 16 | 279 | 103 | `0.08` / `0.46` | **25.0 / 25.0** |
| `www-butter-video` | `tier1_fast` | `1440×2400px` (206,149 B) | `390×2400px` (145,086 B) | 40 | 16 | 304 | 117 | `0.08` / `0.49` | **25.0 / 25.0** |
| `www-casamomo-at` | `tier1_fast` | `1440×2400px` (1,237,953 B) | `390×2400px` (629,152 B) | 36 | 16 | 290 | 110 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-cadillacf1team-com` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — CloudFront WAF Block`)** |
| `www-cartier-com_en-fr-lechoeurdespierres` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — Edge WAF Access Denied`)** |
| `www-cartier-com_en-us-roadster-universe-html` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — Edge WAF Access Denied`)** |
