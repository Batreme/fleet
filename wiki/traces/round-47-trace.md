# Round 47 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-47`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `9` (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 47 Target Scope
  1. `www-governorsmansion-org` — *Louisiana's House · Louisiana Governor's Mansion* (`https://www.governorsmansion.org/`)
  2. `www-gravelleduparc-com` — *Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026* (`https://www.gravelleduparc.com/`)
  3. `www-greenlock-io` — *Independent Wealth Oversight for Family Offices · GreenLock* (`https://www.greenlock.io`)
  4. `www-halcyon-co-nz` — *Halcyon · Leading Lighting Specialists* (`https://www.halcyon.co.nz/`)
  5. `www-hauntedbouldercity-com` — *Boulder City Ghost & UFO Walking Tour · Haunted Boulder City* (`https://www.hauntedbouldercity.com/`)
  6. `www-hollywoodexhibit2026-com` — *ELLE & Esquire, The New Hollywood Photography Exhibition* (`https://www.hollywoodexhibit2026.com`)
  7. `www-honeyquote-com` — *Compare Insurance Quotes Worth Trusting · HoneyQuote* (`https://www.honeyquote.com/`)
  8. `www-hoteldutassosorrento-com` — *Blocked (`Cloudflare HTTP 520 Origin Error (Web server is returning an unknown error)`)*
  9. `www-huxleysaga-com` — *Huxley · Home* (`https://www.huxleysaga.com/`)
  10. `www-iamsunnywang-com` — *Sunny's Journey* (`http://www.iamsunnywang.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-governorsmansion-org` | `1440×2400px` (1,113,542 B) | `390×2400px` (442,045 B) | 171 | 16 | 256 | 106 | `0.15` / `0.61` | **25.0 / 25.0** |
| `www-gravelleduparc-com` | `1440×2400px` (959,287 B) | `390×2400px` (354,954 B) | 49 | 16 | 276 | 116 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-greenlock-io` | `1440×4789px` (437,842 B) | `390×2400px` (267,648 B) | 62 | 16 | 268 | 112 | `0.15` / `0.61` | **25.0 / 25.0** |
| `www-halcyon-co-nz` | `1440×6175px` (3,012,780 B) | `390×2400px` (429,502 B) | 735 | 16 | 256 | 106 | `0.08` / `0.48` | **25.0 / 25.0** |
| `www-hauntedbouldercity-com` | `1440×12505px` (4,609,967 B) | `390×2400px` (912,905 B) | 20 | 16 | 260 | 108 | `0.08` / `0.48` | **25.0 / 25.0** |
| `www-hollywoodexhibit2026-com` | `1440×2400px` (336,443 B) | `390×2400px` (188,716 B) | 44 | 16 | 254 | 104 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-honeyquote-com` | `1440×10704px` (3,237,446 B) | `390×2400px` (170,794 B) | 235 | 16 | 256 | 106 | `0.15` / `0.61` | **25.0 / 25.0** |
| `www-hoteldutassosorrento-com` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Cloudflare HTTP 520 Origin Error (Web server is returning an unknown error)`)** |
| `www-huxleysaga-com` | `1440×2400px` (387,939 B) | `390×2400px` (242,101 B) | 228 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-iamsunnywang-com` | `1440×2400px` (987,672 B) | `390×2400px` (430,170 B) | 191 | 16 | 256 | 106 | `0.09` / `0.46` | **25.0 / 25.0** |
