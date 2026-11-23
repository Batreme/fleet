---
title: "UI & UX Architecture: matthisgarnier-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: matthisgarnier-com

## Overview & Design Identity
- **Target**: `matthisgarnier-com` (**Matthis Garnier · Head of Creative Engineering, Polymarket**)
- **Production URL**: [https://matthisgarnier.com](https://matthisgarnier.com)
- **Final Redirected URL**: [https://www.matthisgarnier.com/](https://www.matthisgarnier.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ececec` / `#2c6be7`)
- **Summary**: Matthis Garnier, Head of Creative Engineering at Polymarket, New York. Previously design director at SVZ and Hours Global; founded Cohem...
- **Total Clean CSS Variables Extracted**: `253` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `handFont`
- **Body Font Stack**: `areal`
- **Monospace / Technical Font Stack**: `arealMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 205.98px`, `line-height: 175.083px`, `font-weight: 400`); rule `h1` (`font-size: 18px`, `letter-spacing: 0`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48.96px`, `line-height: 44.064px`, `font-weight: 400`, `letter-spacing: -2.2032px`); rule `h2` (`font-size: 13px`, `line-height: 1.4`, `letter-spacing: 0`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 12px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 16.2px`, `font-weight: 400`); CSS variables `--mono-font: var(--font-areal), system-ui, sans-serif`, `--font-areal-mono: "arealMono", "arealMono Fallback", ui-monospace, monospace`, `--font-mono: var(--font-areal-mono), ui-monospace, monospace`; rule `.meta` (`font-size: 11px`, `line-height: 1.25`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ececec` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#181818` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7f4ec` | `var(--sticker-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#2c6be7` | `var(--nfl-brand)` in `:root` |
| **Secondary / Muted Copy** | `#19a4dc` | `var(--room-ink-cyan)` in `:root` |
| **Structural Hairline Border** | `#c1c1c1` | `.sc-ball-body { stroke: #c1c1c1 }` |
| **Variable Token (`--g-0`)** | `#fcfcfc` | `var(--g-0)` in `:root` |
| **Variable Token (`--g-1`)** | `#fafafa` | `var(--g-1)` in `:root` |
| **Variable Token (`--g-2`)** | `#f3f3f3` | `var(--g-2)` in `:root` |
| **Variable Token (`--g-4`)** | `#e2e2e2` | `var(--g-4)` in `:root` |
| **Variable Token (`--g-5`)** | `#d4d4d4` | `var(--g-5)` in `:root` |
| **Variable Token (`--g-6`)** | `#bcbcbc` | `var(--g-6)` in `:root` |
| **Variable Token (`--g-7`)** | `#8e8e8e` | `var(--g-7)` in `:root` |
| **Variable Token (`--g-8`)** | `#6a6a6a` | `var(--g-8)` in `:root` |
| **Variable Token (`--g-9`)** | `#474747` | `var(--g-9)` in `:root` |
| **Variable Token (`--g-10`)** | `#2a2a2a` | `var(--g-10)` in `:root` |
| **Variable Token (`--g-12`)** | `#0a0a0a` | `var(--g-12)` in `:root` |
| **Variable Token (`--shade`)** | `#000000` | `var(--shade)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--g-0` | `#fcfcfc` | Color / Atmospheric Token |
| `--g-1` | `#fafafa` | Color / Atmospheric Token |
| `--g-2` | `#f3f3f3` | Color / Atmospheric Token |
| `--g-3` | `#ececec` | Color / Atmospheric Token |
| `--g-4` | `#e2e2e2` | Color / Atmospheric Token |
| `--g-5` | `#d4d4d4` | Color / Atmospheric Token |
| `--g-6` | `#bcbcbc` | Color / Atmospheric Token |
| `--g-7` | `#8e8e8e` | Color / Atmospheric Token |
| `--g-8` | `#6a6a6a` | Color / Atmospheric Token |
| `--g-9` | `#474747` | Color / Atmospheric Token |
| `--g-10` | `#2a2a2a` | Color / Atmospheric Token |
| `--g-11` | `#181818` | Color / Atmospheric Token |
| `--g-12` | `#0a0a0a` | Color / Atmospheric Token |
| `--shade` | `#00000024` | Color / Atmospheric Token |
| `--shade-deep` | `#00000038` | Color / Atmospheric Token |
| `--sticker-paper` | `#f7f4ec` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.topbar> — `matthisgarnier-com`)**:
   - Landmark `<nav class="topbar">` (`1440x28px`) hosting `Matthis Garnier · Head of Creative E` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-theme="light"`, `data-three="off"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.xp .mecard { width:min(300px,100% - 32px) }`.
2. **Hero Stage & Focal Lead (<section.story-desk-module__g7DRpa__win> — `matthis garnier`)**:
   - Landmark `<section class="story-desk-module__g7DRpa__win story-desk-module__g7DRpa__cover">` presenting display lead `matthis garnier` and copy excerpt *"NYC 23:35 LA 20:35 PAR 05:35 TUL 23:35 NYC 23:35 LA 20:35 PAR 05:"* over `#ececec` canvas and `#181818` ink.
3. **Primary Showcase & Content Grid (<section.story-desk-module__g7DRpa__index> — `Matthis Garnier`)**:
   - Landmark `<section class="story-desk-module__g7DRpa__win story-desk-module__g7DRpa__index">` rendering section `Matthis Garnier` with copy *"Head of Creative Engineering at Polymarket"*, asset references (`7ebf22b5a21034f8-s.p.3strvg7o-g5v...`, `ABCArealMonoVariable-s.p.28z6jix4...`, `ABCArealVariable-s.p.0r-_z7ct5is3...`, `DaftFont-s.p.1r6c1opwgow9_.woff2`), and grid rule `button { opacity:.5;border-radius:9px;width:36px;height:36px;padding:0;transition... }`.
4. **Interactive Detail & Feature Matrix (<section.story-desk-module__g7DRpa__year> — `Building for an information market`)**:
   - Landmark `<section class="story-desk-module__g7DRpa__win story-desk-module__g7DRpa__year">` framing `Building for an information market.` and `questions are everything, on tape` (*"Founded Cohem, a creative and consulting studio for small and mid"*) with `#f7f4ec` surface cards, `#2c6be7` accents, and `button>span:first-child { border-radius:9px;width:36px;height:36px;display:block }`.
5. **Colophon & Global Directory Footer (<footer.taskbar> — `https://matthisgarnier.com`)**:
   - Landmark `<footer class="taskbar">` anchoring `Matthis Garnier · Head of Creati` footer links (`Overview · Index · Archive · About · Contact`), copy *"Finsweet Multidisciplinary Designer"*, and `#c1c1c1` structural dividers.
