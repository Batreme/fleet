# Round 27 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-27`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `9` (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 27 Target Scope
  1. `noho-ink` — *Noho* (`https://noho.ink`)
  2. `noravale-framer-website` — *Blankit – Ultimate Portfolio System for Framer* (`https://noravale.framer.website/`)
  3. `north-cloud` — *North - Take control of your cloud costs with AI-powered FinOps - North* (`https://north.cloud`)
  4. `oblikworks-com` — *oblikworks · Architectural Visualization & 3D Rendering Studio* (`https://oblikworks.com/`)
  5. `offform-net` — *Blocked (`Empty raw DOM capture (39 bytes, 0 stylesheets)`)*
  6. `offpossible-com` — *OffPossible · Interfaces Between People and Their Own Minds* (`https://offpossible.com/`)
  7. `ofrenda-davidlangarica-dev` — *OFRENDA — Create a personal Día de Muertos altar* (`https://ofrenda.davidlangarica.dev`)
  8. `oliviaarents-com` — *OliviaOS 96 — Personal Edition* (`https://oliviaarents.com/`)
  9. `ondocollective-jp` — *Ondo Collective* (`https://ondocollective.jp/`)
  10. `onecoldnight-com` — *The Little Match Girl* (`https://onecoldnight.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `noho-ink` | `1440×2400px` (50,449 B) | `390×2400px` (41,458 B) | 41 | 16 | 258 | 107 | `0.11` / `0.56` | **25.0 / 25.0** |
| `noravale-framer-website` | `1440×2400px` (45,988 B) | `390×2400px` (371,946 B) | 151 | 16 | 260 | 108 | `0.11` / `0.54` | **25.0 / 25.0** |
| `north-cloud` | `1440×21285px` (1,251,804 B) | `390×2400px` (44,391 B) | 181 | 16 | 256 | 106 | `0.08` / `0.52` | **25.0 / 25.0** |
| `oblikworks-com` | `1440×3719px` (1,108,731 B) | `390×2400px` (229,727 B) | 5 | 16 | 256 | 106 | `0.11` / `0.56` | **25.0 / 25.0** |
| `offform-net` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Empty raw DOM capture (39 bytes, 0 stylesheets)`)** |
| `offpossible-com` | `1440×2400px` (382,551 B) | `390×2400px` (211,646 B) | 21 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `ofrenda-davidlangarica-dev` | `1440×2400px` (47,733 B) | `390×2400px` (544,960 B) | 37 | 16 | 256 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `oliviaarents-com` | `1440×2400px` (463,244 B) | `390×2400px` (267,168 B) | 7 | 16 | 254 | 104 | `0.10` / `0.53` | **25.0 / 25.0** |
| `ondocollective-jp` | `1440×2400px` (53,481 B) | `390×2400px` (39,029 B) | 56 | 16 | 258 | 107 | `0.09` / `0.54` | **25.0 / 25.0** |
| `onecoldnight-com` | `1440×2400px` (153,106 B) | `390×2400px` (79,647 B) | 14 | 16 | 256 | 106 | `0.10` / `0.53` | **25.0 / 25.0** |
