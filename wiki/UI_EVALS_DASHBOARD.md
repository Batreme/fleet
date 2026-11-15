# UI Design & Prompt Evaluation Dashboard

> Central Obsidian dashboard tracking the reverse-engineering transformation of production web properties into ground-truth AI UI Prompt Blueprints (`prompt-blueprint.md`), validated by deterministic consistency checks (`evaluate_batch.py`) and multi-round Anthropic Claude review (`claude-loop`).

---

## 📊 Campaign Progress Overview

| Metric | Current Value | Target Goal | Status |
| :--- | :--- | :--- | :--- |
| **Total Catalog Targets** | 575 | 575 | Cataloged in `wiki/targets/` |
| **Batch 1 Flagship Blueprints** | 10 / 10 | 10 | **100% Grounded in Source DOM/CSS (239–263L)** |
| **Batch 1 Visual Assets (Desktop + Mobile)** | 20 / 20 | 20 | **100% Standard `1440px` & `390px` Full-Height** |
| **Upgraded Truth & Consistency Eval Score** | **25.0 / 25.0** | >= 23.0 | **All C1–C13 Checks Passing** |
| **Master Prompt Unsplit Fence Length** | **94–105 lines** | >= 80 lines | **Single Unsplit Fenced Block Verified** |
| **Max Cross-Target Overlap (Line / Word Jaccard)** | **0.09 / 0.43** | < 0.30 / < 0.50 | **Highly Unique Per Target** |
| **Anthropic Reviewer (`claude-loop`)** | `claude-sonnet-5-5-high` | `VERDICT: APPROVE` | **Approved in Round 3 (`24/25`)** |

---

## 🎯 Batch 1 Scorecard Table

| # | Target | Ground-Truth Design Archetype | Desktop (`assets/desktop.png`) | Mobile (`assets/mobile.png`) | Fence Lines | Truth Eval | Blueprint & Tokens |
| :-: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | [[targets/dennypratama-com/overview\|dennypratama-com]] | Monolith Ink (`#0c0c0b`) & Bone (`#eceae4`) Editorial Grid (`Archivo`) | `1440×16914` | `390×16750` | `105L` | **25.0 / 25** | [[targets/dennypratama-com/prompt-blueprint\|Blueprint]] · [[targets/dennypratama-com/ui-ux\|Tokens]] |
| 2 | [[targets/agnestoth-com/overview\|agnestoth-com]] | Haute Couture Embroidery Atelier (`FreightBig Pro` + `Jost`, `#FFFFFF` / `#9a3b2e`) | `1440×9759` | `390×4200` | `97L` | **25.0 / 25** | [[targets/agnestoth-com/prompt-blueprint\|Blueprint]] · [[targets/agnestoth-com/ui-ux\|Tokens]] |
| 3 | [[targets/www-sigma-imaging-se/overview\|www-sigma-imaging-se]] | Swiss-Japanese Optical Hardware System (`Sigma Sans` + `Sigma Serif`, `#fefefd`) | `1440×7696` | `390×10390` | `102L` | **25.0 / 25** | [[targets/www-sigma-imaging-se/prompt-blueprint\|Blueprint]] · [[targets/www-sigma-imaging-se/ui-ux\|Tokens]] |
| 4 | [[targets/morrow-valerian-studio/overview\|morrow-valerian-studio]] | Swiss-Editorial Fashion 12-Col SVH Grid (`ppNeueMontreal` + `editorialNew`) | `1440×5154` | `390×6015` | `101L` | **25.0 / 25** | [[targets/morrow-valerian-studio/prompt-blueprint\|Blueprint]] · [[targets/morrow-valerian-studio/ui-ux\|Tokens]] |
| 5 | [[targets/wiro-ae/overview\|wiro-ae]] | Warm-Paper (`#f6efe3`) Tactile Agency OS & Scatter Cards (`Bricolage Grotesque`) | `1440×7497` | `390×8396` | `95L` | **25.0 / 25** | [[targets/wiro-ae/prompt-blueprint\|Blueprint]] · [[targets/wiro-ae/ui-ux\|Tokens]] |
| 6 | [[targets/www-anduril-com/overview\|www-anduril-com]] | Defense Autonomy & Odometer Telemetry Grid (`HelveticaNowDisplay` + `Elios`, `#010101`) | `1440×5230` | `390×6917` | `94L` | **25.0 / 25** | [[targets/www-anduril-com/prompt-blueprint\|Blueprint]] · [[targets/www-anduril-com/ui-ux\|Tokens]] |
| 7 | [[targets/www-avilus-com/overview\|www-avilus-com]] | Tactical Aerospace Spec Sheet (`Inter` + `Robotomono`, `#f7f7f7` / `#183032` / `#ddff2c`) | `1440×6212` | `390×6167` | `97L` | **25.0 / 25** | [[targets/www-avilus-com/prompt-blueprint\|Blueprint]] · [[targets/www-avilus-com/ui-ux\|Tokens]] |
| 8 | [[targets/www-eladiodieste-com/overview\|www-eladiodieste-com]] | Ceramic-Brick Archival Monograph (`#eadfd2` Sand + `#a55f2d` Terracotta, `1.6s` Expo) | `1440×14025` | `390×10165` | `96L` | **25.0 / 25** | [[targets/www-eladiodieste-com/prompt-blueprint\|Blueprint]] · [[targets/www-eladiodieste-com/ui-ux\|Tokens]] |
| 9 | [[targets/www-unimaticwatches-com/overview\|www-unimaticwatches-com]] | Milanese Horology Lab & Srgb `color-mix` Ladder (`#F6F6F6` / `#000000` / `#AFFF00`) | `1440×4841` | `390×6103` | `96L` | **25.0 / 25** | [[targets/www-unimaticwatches-com/prompt-blueprint\|Blueprint]] · [[targets/www-unimaticwatches-com/ui-ux\|Tokens]] |
| 10 | [[targets/seedjewelry-com/overview\|seedjewelry-com]] | Botanical Emerald (`#162924`) & Champagne-Gold (`#e8d3a8`) High Jewelry (`Plus Jakarta Sans`) | `1440×7802` | `390×4200` | `98L` | **25.0 / 25** | [[targets/seedjewelry-com/prompt-blueprint\|Blueprint]] · [[targets/seedjewelry-com/ui-ux\|Tokens]] |

---

## 🧪 5-Point Truth & Consistency Evaluation Rubric (`evaluate_batch.py`)

1. **Visual Assets & Standard Viewport Verification (5.0 pts)**: Confirms `assets/desktop.png` (`1440px` wide, `> 1000px` tall) and `assets/mobile.png` (`390px` wide, `> 1000px` tall) exist, validates binary PNG `IHDR` dimensions, and checks that exact pixel dimensions are documented in Section 2.
2. **Token Hygiene & Ground-Truth Fidelity (5.0 pts)**: Rejects any table row containing parser debris (`{`, `}`, `@media`, `@property`), rejects duplicate CSS variable names, rejects placeholder roles (`"Extracted CSS Variable"`), and verifies Section 3 variables match `ui-ux.md`.
3. **Structural & Wireframe Fidelity (5.0 pts)**: Verifies all 7 required sections exist, enforces uniform 74-character width alignment on Section 6 ASCII wireframe boxes, and verifies cited DOM classes against raw `dom.html`.
4. **Internal Cross-Section Consistency (5.0 pts)**: Asserts that every hex color, CSS variable, and `cubic-bezier()` curve in Section 7's Master Prompt is grounded in Sections 3, 4, and 5 of that same blueprint.
5. **Master Prompt Generability, Fence Integrity & Uniqueness (5.0 pts)**: Enforces a single uninterrupted fenced Section 7 block of `>= 80` lines (actual: `94–105` lines), rejects double-backtick formatting glitches, and verifies both line-level Jaccard (`<= 0.09`) and word-level Jaccard (`<= 0.43`) across all 10 targets.

---

## 🛠️ Infrastructure & Audit Trail

- **Active Audit Trace & `claude-loop` Ledger**: [[traces/round-01-trace|Round 1 Execution Trace (C1–C13 Verified)]]
- **UI Prompt Designer Standard**: [[../skills/ui-prompt-designer/SKILL|UI Prompt Designer Skill]]
- **Anthropic Review Workflow**: [[../skills/claude-loop/SKILL|Claude-Loop Skill]]
- **Master Knowledge Base Directory**: [[INDEX|Knowledge Base Index]]
