# Round 43 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-43`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
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

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-bitwip-fr_en` | `tier1_fast` | `1280×6624px` (355,890 B) | `390×2616px` (66,888 B) | 186 | 16 | 363 | 118 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-bluesqx-com` | `tier1_fast` | `1280×6624px` (401,124 B) | `390×2616px` (66,884 B) | 67 | 16 | 351 | 113 | `0.11` / `0.54` | **25.0 / 25.0** |
| `www-blumjeffrey-com` | `tier1_fast` | `1280×6624px` (526,508 B) | `390×2616px` (83,572 B) | 56 | 16 | 341 | 110 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-brandlos-nl` | `tier1_fast` | `1280×6624px` (270,718 B) | `390×2616px` (73,368 B) | 11 | 16 | 356 | 118 | `0.11` / `0.54` | **25.0 / 25.0** |
| `www-brandtheagency-com` | `tier1_fast` | `1280×2484px` (121,282 B) | `390×2616px` (51,286 B) | 1042 | 16 | 312 | 106 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-butter-video` | `tier1_fast` | `1280×1656px` (73,278 B) | `390×1744px` (24,386 B) | 40 | 16 | 335 | 120 | `0.08` / `0.49` | **25.0 / 25.0** |
| `www-casamomo-at` | `tier1_fast` | `1280×6624px` (336,390 B) | `390×1744px` (19,808 B) | 36 | 16 | 347 | 114 | `0.08` / `0.49` | **25.0 / 25.0** |
| `www-cadillacf1team-com` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — CloudFront WAF Block`)** |
| `www-cartier-com_en-fr-lechoeurdespierres` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — Edge WAF Access Denied`)** |
| `www-cartier-com_en-us-roadster-universe-html` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — Edge WAF Access Denied`)** |
