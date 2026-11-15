# Round 02 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-02`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 02 Target Scope
  1. `100yearsmonet-com` — *Monet 100 — A century without Claude Monet · 3D gallery* (`https://100yearsmonet.com`)
  2. `11moissanstoit-com` — *11 mois sans toi(t), le tour du monde de Josué & Philippe* (`https://11moissanstoit.com/`)
  3. `1stdecember-com` — *First December Films · Ad Film Production House in India* (`https://1stdecember.com`)
  4. `21oaks-org` — *21Oaks Student Apartments • USC & Williams-Brice* (`https://21oaks.org/`)
  5. `360lexingtonave-com` — *360 Lexington Avenue* (`https://360lexingtonave.com`)
  6. `abhayrohit-com` — *Abhay Rohit — Creative Product Engineer* (`https://abhayrohit.com/`)
  7. `about-centra-com` — *Centra? Centra! The definitive guide.* (`https://about.centra.com`)
  8. `abyme-app` — *Curiouser and Curiouser* (`https://abyme.app`)
  9. `actl-me` — *ACTL — Arabian Community Tennis League* (`https://actl.me/`)
  10. `adamperlis-com` — *Adam Perlis — I design and build apps* (`https://adamperlis.com`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `100yearsmonet-com` | `1440×18000px` (1,703,647 B) | `390×2400px` (1,192,035 B) | 7 | 16 | 262 | 109 | `0.09` / `0.48` | **25.0 / 25.0** |
| `11moissanstoit-com` | `1440×2400px` (120,415 B) | `390×2400px` (118,737 B) | 9 | 16 | 258 | 107 | `0.11` / `0.51` | **25.0 / 25.0** |
| `1stdecember-com` | `1440×2400px` (68,114 B) | `390×2400px` (45,043 B) | 168 | 16 | 256 | 106 | `0.16` / `0.58` | **25.0 / 25.0** |
| `21oaks-org` | `1440×2400px` (102,724 B) | `390×2400px` (36,632 B) | 9 | 16 | 256 | 106 | `0.17` / `0.61` | **25.0 / 25.0** |
| `360lexingtonave-com` | `1440×2400px` (49,166 B) | `390×2400px` (39,539 B) | 36 | 16 | 260 | 108 | `0.10` / `0.50` | **25.0 / 25.0** |
| `abhayrohit-com` | `1440×2400px` (59,815 B) | `390×2400px` (36,169 B) | 188 | 16 | 258 | 107 | `0.09` / `0.46` | **25.0 / 25.0** |
| `about-centra-com` | `1440×6253px` (1,095,454 B) | `390×2400px` (247,800 B) | 150 | 16 | 262 | 109 | `0.17` / `0.61` | **25.0 / 25.0** |
| `abyme-app` | `1440×2400px` (767,438 B) | `390×2400px` (328,847 B) | 61 | 16 | 272 | 114 | `0.09` / `0.49` | **25.0 / 25.0** |
| `actl-me` | `1440×10391px` (973,126 B) | `390×2400px` (39,595 B) | 5 | 16 | 256 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `adamperlis-com` | `1440×2400px` (91,297 B) | `390×2400px` (72,460 B) | 83 | 16 | 256 | 106 | `0.11` / `0.51` | **25.0 / 25.0** |
