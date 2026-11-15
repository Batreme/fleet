# Round 26 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-26`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 26 Target Scope
  1. `mychess-events` — *Find Chess Tournaments Worldwide · MyChess.Events* (`https://mychess.events/`)
  2. `myfrida-com` — *My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars* (`https://myfrida.com/`)
  3. `nader-io` — *Nader Cserny* (`https://nader.io`)
  4. `nakagawa-corp-com` — *久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）* (`https://nakagawa-corp.com/`)
  5. `namaha-healthcare` — *Namaha Healthcare* (`https://namaha.healthcare`)
  6. `navtec-com` — *Moab Adventure Tours · Navtec Expeditions Since 1896* (`https://navtec.com/`)
  7. `newminds-studio_concept-elune` — *ELUNE Women's Health App UX/UI Concept · New Minds* (`https://newminds.studio/concept-elune`)
  8. `nickho-motorsports-nl` — *Nick Ho - Dutch Racing Driver · Porsche Carrera Cup* (`https://nickho-motorsports.nl/`)
  9. `no-merci-michel-com` — *No Mercy Michel* (`https://no.merci-michel.com`)
  10. `nodenza-com` — *Home · Nodenza* (`https://nodenza.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `mychess-events` | `1440×2400px` (78,742 B) | `390×2400px` (51,894 B) | 268 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `myfrida-com` | `1440×7118px` (1,513,409 B) | `390×2400px` (88,361 B) | 497 | 16 | 276 | 116 | `0.09` / `0.49` | **25.0 / 25.0** |
| `nader-io` | `1440×4000px` (300,580 B) | `390×2400px` (79,606 B) | 74 | 16 | 256 | 106 | `0.08` / `0.48` | **25.0 / 25.0** |
| `nakagawa-corp-com` | `1440×2400px` (66,815 B) | `390×2400px` (73,229 B) | 131 | 16 | 268 | 112 | `0.09` / `0.51` | **25.0 / 25.0** |
| `namaha-healthcare` | `1440×10213px` (3,483,157 B) | `390×2400px` (62,036 B) | 0 | 12 | 248 | 102 | `0.10` / `0.56` | **25.0 / 25.0** |
| `navtec-com` | `1440×5273px` (5,085,400 B) | `390×2400px` (71,955 B) | 95 | 16 | 256 | 106 | `0.10` / `0.58` | **25.0 / 25.0** |
| `newminds-studio_concept-elune` | `1440×11083px` (749,636 B) | `390×2400px` (130,418 B) | 0 | 12 | 242 | 99 | `0.09` / `0.51` | **25.0 / 25.0** |
| `nickho-motorsports-nl` | `1440×2400px` (1,935,385 B) | `390×2400px` (659,280 B) | 94 | 16 | 256 | 106 | `0.10` / `0.58` | **25.0 / 25.0** |
| `no-merci-michel-com` | `1440×2400px` (838,148 B) | `390×2400px` (193,517 B) | 49 | 16 | 253 | 103 | `0.09` / `0.51` | **25.0 / 25.0** |
| `nodenza-com` | `1440×3230px` (1,218,917 B) | `390×2400px` (32,210 B) | 30 | 16 | 258 | 107 | `0.09` / `0.50` | **25.0 / 25.0** |
