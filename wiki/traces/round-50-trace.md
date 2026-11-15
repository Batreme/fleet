# Round 50 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-50`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 50 Target Scope
  1. `www-miljofyrtarn-no` — *Hjem · Miljøfyrtårn* (`https://www.miljofyrtarn.no/`)
  2. `www-motorq-com` — *Motorq · Turn Connected Vehicle Data Into Decisions* (`https://www.motorq.com/`)
  3. `www-mynobs-co` — *NoBS - No Brief Shit* (`https://www.mynobs.co`)
  4. `www-nereo-io` — *Nereo — AI Video Generator for Creators & Marketers* (`https://www.nereo.io/`)
  5. `www-nettiesbees-com` — *Raw Local Honey in Rochester, MA · Nettie's Bees* (`https://www.nettiesbees.com/`)
  6. `www-norddeutscher-figuralchor-de` — *Norddeutscher Figuralchor Hannover — Kammerchor seit 1981* (`https://www.norddeutscher-figuralchor.de`)
  7. `www-oceans-faith_moralcatch` — *The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans* (`https://www.oceans.faith/moralcatch`)
  8. `www-offforum-com` — *A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM · SEPT 15, 2027 · OFFF S...* (`https://www.offforum.com/`)
  9. `www-omni-org` — *Omni Institute* (`https://www.omni.org`)
  10. `www-oregonoutdooralliance-org` — *Oregon Outdoor Alliance · Growing Oregon’s Outdoor Industry* (`https://www.oregonoutdooralliance.org/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-miljofyrtarn-no` | `1440×17284px` (882,988 B) | `390×2400px` (270,296 B) | 29 | 16 | 256 | 106 | `0.11` / `0.50` | **25.0 / 25.0** |
| `www-motorq-com` | `1440×12694px` (2,639,445 B) | `390×2400px` (435,538 B) | 281 | 16 | 256 | 106 | `0.15` / `0.58` | **25.0 / 25.0** |
| `www-mynobs-co` | `1440×1820px` (147,632 B) | `390×2400px` (101,377 B) | 25 | 16 | 272 | 114 | `0.08` / `0.48` | **25.0 / 25.0** |
| `www-nereo-io` | `1440×9591px` (4,890,812 B) | `390×2400px` (106,656 B) | 127 | 16 | 256 | 106 | `0.11` / `0.52` | **25.0 / 25.0** |
| `www-nettiesbees-com` | `1440×14696px` (7,126,852 B) | `390×2400px` (775,959 B) | 77 | 16 | 256 | 106 | `0.11` / `0.53` | **25.0 / 25.0** |
| `www-norddeutscher-figuralchor-de` | `1440×4112px` (2,629,712 B) | `390×2400px` (330,499 B) | 24 | 16 | 258 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-oceans-faith_moralcatch` | `1440×2400px` (598,874 B) | `390×2400px` (230,316 B) | 1004 | 16 | 256 | 106 | `0.10` / `0.49` | **25.0 / 25.0** |
| `www-offforum-com` | `1440×1397px` (1,046,558 B) | `390×2400px` (39,190 B) | 149 | 16 | 256 | 106 | `0.11` / `0.52` | **25.0 / 25.0** |
| `www-omni-org` | `1440×10444px` (631,095 B) | `390×2400px` (56,123 B) | 45 | 16 | 258 | 107 | `0.15` / `0.58` | **25.0 / 25.0** |
| `www-oregonoutdooralliance-org` | `1440×3905px` (1,822,977 B) | `390×2400px` (68,639 B) | 233 | 16 | 256 | 106 | `0.11` / `0.55` | **25.0 / 25.0** |
