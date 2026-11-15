# UI & UX Architecture: www-beige-zone

## Overview & Design Identity
- **Target**: `www-beige-zone` (**Alex/Avery Beige Artist, Playwright / Creative Technologist / Biohacker**)
- **Production URL**: [https://www.beige.zone](https://www.beige.zone)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f9f4f2` / `#42d5b6`)
- **Summary**: Avery / Alex Beige is a freelance web developer, biohacker, and playwright based in NYC. They design speculative theater and digital expe...
- **Total Clean CSS Variables Extracted**: `61` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Avery`
- **Body Font Stack**: `Avery Display`
- **Monospace / Technical Font Stack**: `Avery Mono`
- **Hero Display (`H1`)**: CSS variables `--avery-display: "Avery Display", "Avery", Arial, sans-serif`, `--display-w: 3`, `--display-h: 2`
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.5em`)
- **Body Copy**: rule `body` (`font-size: 1rem`, `line-height: 1.325`)
- **Metadata & Labels**: CSS variables `--avery-mono: "Avery Mono", ui-monospace, monospace`, `--avery-mono-fw: "Avery Mono FW", "Avery Mono", ui-monospace, monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f9f4f2` | `var(--beige)` in `:root` |
| **Primary Typography Ink** | `#2a1664` | `var(--blurple)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e0d9e1` | `var(--light-purple)` in `:root` |
| **Interactive Accent / Highlight** | `#42d5b6` | `var(--green)` in `:root` |
| **Secondary / Muted Copy** | `#3f74de` | `var(--blue)` in `:root` |
| **Structural Hairline Border** | `#8055d9` | `var(--tag-purple)` in `:root` |
| **Variable Token (`--well-inner`)** | `#5e2cca91` | `var(--well-inner)` in `:root` |
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
1. **Brand Header & Navigation Bar (<header.has-custom-cursor> — `www-beige-zone`)**:
   - Landmark `<header class="has-custom-cursor">` hosting `Alex/Avery Beige Artist, Playwright ` navigation (`Oct 21st! · alex@beige.zone · Eyebeam · trailer here · Greg Lakhan`), DOM attributes (`data-goatcounter="https://abeige.goatco..."`, `data-category="playwriting"`, `data-category="creative-tech"`, `data-category="performance"`), and stylesheet rule `property --blurple { syntax: "<color>"; inherits: true; initial-value: 2a1664; }`.
2. **Hero Stage & Focal Lead (<main.pagewrapper> — `Alex/Avery Beige ©`)**:
   - Landmark `<main class="pagewrapper">` presenting display lead `Alex/Avery Beige ©` and copy excerpt *"Under Construction!"* over `#f9f4f2` canvas and `#2a1664` ink.
3. **Primary Showcase & Content Grid (<main.pagewrapper> — `Playwright / Creative Technologist`)**:
   - Landmark `<main class="pagewrapper">` rendering section `Playwright / Creative Technologist / Biohacker` with copy *"I'm working on it! Right now! I'll be done by the end of October "*, asset references (`favicon.png`, `alex-beige-icon.png`, `Avery-Display-Regular.woff2`, `style.css`), and grid rule `property --purple { syntax: "<color>"; inherits: true; initial-value: 5f2cca; }`.
4. **Interactive Detail & Feature Matrix (<main.pagewrapper> — `Selected Works`)**:
   - Landmark `<main class="pagewrapper">` framing `Selected Works` and `Blushing Milk Protocol w/ Eyebeam` (*"Avery / Alex Beige is a creative technologist, biohacker, and pla"*) with `#e0d9e1` surface cards, `#42d5b6` accents, and `property --green { syntax: "<color>"; inherits: true; initial-value: 42d5b6; }`.
5. **Colophon & Global Directory Footer (<footer.is-hidden> — `https://www.beige.zone`)**:
   - Landmark `<footer class="is-hidden">` anchoring `Alex/Avery Beige Artist, Playwri` footer links (`Oct 21st! · alex@beige.zone · Eyebeam · trailer here · Greg Lakhan`), copy *"Welcome! I'm a creative technologist, biohacker, and playwri"*, and `#8055d9` structural dividers.
