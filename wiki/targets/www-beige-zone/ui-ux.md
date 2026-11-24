---
title: "UI & UX Architecture: www-beige-zone"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-beige-zone

## Overview & Design Identity
- **Target**: `www-beige-zone` (**Alex/Avery Beige Artist, Playwright / Creative Technologist / Biohacker**)
- **Production URL**: [https://www.beige.zone](https://www.beige.zone)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×2484px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#2a1664` / `#0082f3`)
- **Summary**: Avery / Alex Beige is a freelance web developer, biohacker, and playwright based in NYC. They design speculative theater and digital expe...
- **Total Clean CSS Variables Extracted**: `66` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Avery Display`
- **Body Font Stack**: `Avery`
- **Monospace / Technical Font Stack**: `Avery Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 65.9123px`, `line-height: 65.9123px`, `font-weight: 700`); CSS variables `--avery-display: "Avery Display", "Avery", Arial, sans-serif`, `--display-w: 3`, `--display-h: 2`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 31.8px`, `font-weight: 700`); rule `h2` (`font-size: 1.5em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 21.2px`, `font-weight: 400`); rule `body` (`font-size: 1rem`, `line-height: 1.325`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); CSS variables `--avery-mono: "Avery Mono", ui-monospace, monospace`, `--avery-mono-fw: "Avery Mono FW", "Avery Mono", ui-monospace, monospace`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#2a1664` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f9f4f2` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#311a7a` | `.bg-blurple { background: #311a7a }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#999999` | `.w-select::placeholder { color: #999999 }` |
| **Structural Hairline Border** | `#f9f4f2` | `var(--light-border)` in `:root` |
| **Variable Token (`--light-purple`)** | `#e0d9e1` | `var(--light-purple)` in `:root` |
| **Variable Token (`--green`)** | `#42d5b6` | `var(--green)` in `:root` |
| **Variable Token (`--blue`)** | `#3f74de` | `var(--blue)` in `:root` |
| **Variable Token (`--tag-purple`)** | `#8055d9` | `var(--tag-purple)` in `:root` |
| **Variable Token (`--well-inner`)** | `#5e2cca` | `var(--well-inner)` in `:root` |
| **Variable Token (`--well-outer`)** | `#26145c` | `var(--well-outer)` in `:root` |
| **Variable Token (`--bezel-crown`)** | `#8e82bd` | `var(--bezel-crown)` in `:root` |
| **Variable Token (`--bezel-face`)** | `#55458c` | `var(--bezel-face)` in `:root` |
| **Variable Token (`--bezel-rail`)** | `#2f2160` | `var(--bezel-rail)` in `:root` |
| **Variable Token (`--bezel-bounce`)** | `#6a58a4` | `var(--bezel-bounce)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--beige` | `#f9f4f2` | Color / Atmospheric Token |
| `--blurple` | `#2a1664` | Elevation / Border Token |
| `--purple` | `rgb(95, 44, 202)` | Color / Atmospheric Token |
| `--light-purple` | `#e0d9e1` | Canvas / Surface Token |
| `--green` | `#42d5b6` | Color / Atmospheric Token |
| `--blue` | `#3f74de` | Color / Atmospheric Token |
| `--tag-purple` | `#8055d9` | Color / Atmospheric Token |
| `--cat-playwriting` | `var(--green)` | Design System Custom Token |
| `--cat-creative-tech` | `var(--blue)` | Design System Custom Token |
| `--cat-performance` | `var(--tag-purple)` | Design System Custom Token |
| `--well-inner` | `#5e2cca91` | Color / Atmospheric Token |
| `--well-outer` | `#26145c` | Color / Atmospheric Token |
| `--bezel-crown` | `#8e82bd` | Color / Atmospheric Token |
| `--bezel-face` | `#55458c` | Color / Atmospheric Token |
| `--bezel-rail` | `#2f2160` | Color / Atmospheric Token |
| `--bezel-bounce` | `#6a58a4` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.has-show-banner> — `www-beige-zone`)**:
   - Landmark `<header class="has-show-banner">` (`1440px`) hosting `Alex/Avery Beige Artist, Playwright ` navigation (`Open Call · Oct 21st! · alex@beige.zone · Eyebeam · trailer here`), DOM attributes (`data-goatcounter="https://abeige.goatco..."`, `data-hide-after="2026-12-22T05:00:00.000Z"`, `data-key="2026-12-21T19:00:00-0..."`, `data-category="playwriting"`), and stylesheet rule `property --blurple { syntax: "<color>"; inherits: true; initial-value: 2a1664; }`.
2. **Hero Stage & Focal Lead (<main.pagewrapper> — `Alex/Avery Beige ©`)**:
   - Landmark `<main class="pagewrapper">` presenting display lead `Alex/Avery Beige ©` and copy excerpt *"HyperText Theatre Project: 120 Words, No Intermission Open Call"* over `#2a1664` canvas and `#f9f4f2` ink.
3. **Primary Showcase & Content Grid (<main.pagewrapper:nth(2)> — `Playwright / Creative Technologist`)**:
   - Landmark `<main class="pagewrapper">` rendering section `Playwright / Creative Technologist / Biohacker` with copy *"Under Construction!"*, asset references (`favicon.png`, `alex-beige-icon.png`, `Avery-Display-Regular.woff2`, `style.css`), and grid rule `property --purple { syntax: "<color>"; inherits: true; initial-value: 5f2cca; }`.
4. **Interactive Detail & Feature Matrix (<main.pagewrapper:nth(3)> — `Selected Works`)**:
   - Landmark `<main class="pagewrapper">` framing `Selected Works` and `Blushing Milk Protocol w/ Eyebeam` (*"I'm working on it! Right now! I'll be done by the end of October "*) with `#311a7a` surface cards, `#0082f3` accents, and `property --green { syntax: "<color>"; inherits: true; initial-value: 42d5b6; }`.
5. **Colophon & Global Directory Footer (<footer.show-banner> — `https://www.beige.zone`)**:
   - Landmark `<footer class="show-banner">` anchoring `Alex/Avery Beige Artist, Playwri` footer links (`Open Call · Oct 21st! · alex@beige.zone · Eyebeam · trailer here`), copy *"Avery / Alex Beige is a creative technologist, biohacker, an"*, and `#f9f4f2` structural dividers.
