# Round 53 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-53`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 53 Target Scope
  1. `www-routedurhum-com` — *Route du Rhum 2026 – Destination Guadeloupe · Site Officiel*
  2. `www-rtmaudio-com` — *RTM Audio · Audio plug-ins for mixing and mastering*
  3. `www-schemeengine-com` — *Home - Scheme Engine*
  4. `www-schlosshotel-kitzbuehel-com_en` — *Schlosshotel Kitzbühel – a premium experience*
  5. `www-seasats-com` — *Seasats · Ocean Autonomy That Works*
  6. `www-selkirk-com_pages-omni-pickleball-paddle` — *Selkirk OMNI™ Pickleball Paddle · Selkirk Sport - We Are Pickleball*
  7. `www-sentientx-com` — *SentientX · Enterprise AI & Digital Likeness Protection*
  8. `www-serko-ai` — *Serko.ai · AI Travel Agent for Business Trips*
  9. `www-sharplink-com` — *Sharplink : Home*
  10. `www-si-edu` — *Blocked (`Upstream HTTP 403 — Cloudflare Origin/WAF Error`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-routedurhum-com` | `tier1_fast` | `1440×2400px` (1,516,132 B) | `390×2400px` (510,878 B) | 492 | 16 | 282 | 106 | `0.16` / `0.66` | **25.0 / 25.0** |
| `www-rtmaudio-com` | `tier2_webgl` | `1440×900px` (304,482 B) | `390×844px` (158,020 B) | 73 | 16 | 286 | 108 | `0.08` / `0.48` | **25.0 / 25.0** |
| `www-schemeengine-com` | `tier1_fast` | `1440×2400px` (746,940 B) | `390×2400px` (10,129 B) | 55 | 16 | 300 | 115 | `0.10` / `0.58` | **25.0 / 25.0** |
| `www-schlosshotel-kitzbuehel-com_en` | `tier1_fast` | `1440×2400px` (2,542,158 B) | `390×2400px` (640,167 B) | 36 | 16 | 282 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-seasats-com` | `tier1_fast` | `1440×2400px` (375,121 B) | `390×2400px` (156,639 B) | 138 | 16 | 286 | 108 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-selkirk-com_pages-omni-pickleball-paddle` | `tier1_fast` | `1440×900px` (890,620 B) | `390×2400px` (845,522 B) | 232 | 16 | 290 | 110 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-sentientx-com` | `tier1_fast` | `1440×2400px` (165,570 B) | `390×2400px` (165,957 B) | 316 | 16 | 282 | 106 | `0.16` / `0.66` | **25.0 / 25.0** |
| `www-serko-ai` | `tier1_fast` | `1440×2400px` (715,454 B) | `390×2400px` (280,068 B) | 591 | 16 | 290 | 110 | `0.10` / `0.58` | **25.0 / 25.0** |
| `www-sharplink-com` | `tier1_fast` | `1440×2400px` (1,155,776 B) | `390×844px` (235,877 B) | 590 | 16 | 282 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-si-edu` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — Cloudflare Origin/WAF Error`)** |
