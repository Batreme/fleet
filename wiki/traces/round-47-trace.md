# Round 47 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-47`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 47 Target Scope
  1. `www-governorsmansion-org` — *Louisiana's House · Louisiana Governor's Mansion*
  2. `www-gravelleduparc-com` — *Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026*
  3. `www-greenlock-io` — *Independent Wealth Oversight for Family Offices · GreenLock*
  4. `www-halcyon-co-nz` — *Halcyon · Leading Lighting Specialists*
  5. `www-hauntedbouldercity-com` — *Boulder City Ghost & UFO Walking Tour · Haunted Boulder City*
  6. `www-hollywoodexhibit2026-com` — *ELLE & Esquire, The New Hollywood Photography Exhibition*
  7. `www-honeyquote-com` — *Compare Insurance Quotes Worth Trusting · HoneyQuote*
  8. `www-hoteldutassosorrento-com` — *Blocked (`Upstream HTTP 520 — Cloudflare Origin/WAF Error`)*
  9. `www-huxleysaga-com` — *Huxley · Home*
  10. `www-iamsunnywang-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-governorsmansion-org` | `tier1_fast` | `1440×2400px` (1,228,263 B) | `390×2400px` (469,313 B) | 171 | 16 | 282 | 106 | `0.14` / `0.56` | **25.0 / 25.0** |
| `www-gravelleduparc-com` | `tier1_fast` | `1440×2400px` (1,545,651 B) | `390×2400px` (453,293 B) | 53 | 16 | 308 | 119 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-greenlock-io` | `tier1_fast` | `1440×2400px` (318,612 B) | `390×2400px` (269,803 B) | 62 | 16 | 308 | 119 | `0.14` / `0.57` | **25.0 / 25.0** |
| `www-halcyon-co-nz` | `tier1_fast` | `1440×2400px` (1,694,234 B) | `390×2400px` (477,656 B) | 1262 | 16 | 292 | 111 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-hauntedbouldercity-com` | `tier1_fast` | `1440×2400px` (1,740,922 B) | `390×2400px` (634,699 B) | 18 | 16 | 286 | 108 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-hollywoodexhibit2026-com` | `tier1_fast` | `1440×900px` (101,927 B) | `390×844px` (15,370 B) | 44 | 16 | 279 | 103 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-honeyquote-com` | `tier1_fast` | `1440×2400px` (2,439,364 B) | `390×2400px` (393,712 B) | 235 | 16 | 282 | 106 | `0.14` / `0.57` | **25.0 / 25.0** |
| `www-huxleysaga-com` | `tier2_webgl` | `1440×900px` (676,354 B) | `390×844px` (344,810 B) | 228 | 16 | 282 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-hoteldutassosorrento-com` | `blocked` (`520`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 520 — Cloudflare Origin/WAF Error`)** |
| `www-iamsunnywang-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
