# UI & UX Architecture: nodenza-com

## Overview & Design Identity
- **Target**: `nodenza-com` (**Home · Nodenza**)
- **Production URL**: [https://nodenza.com/](https://nodenza.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#e6efff` accent)
- **Summary**: Nosenza invests globally in early-stage biotech, medtech, and healthcare companies advancing life sciences and improving patient outcomes.
- **Total Clean CSS Variables Extracted**: `30` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aspekta`
- **Body Font Stack**: `Aspekta`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`line-height: 0.95`, `letter-spacing: -0.03em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--f-b)`, `line-height: 1`, `font-weight: 600`)
- **Body Copy**: rule `p` (`font-size: var(--f-d)`, `line-height: 1.3`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `0.0625vw`, `var(--f-d)`, `var(--f-xl)`, `var(--f-xxl)`, `300rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--c0)` in `:root` |
| **Primary Typography Ink** | `#000000` | `var(--c1)` in `:root` |
| **Elevated Surface / Card Substrate** | `#32006f` | `var(--c2)` in `:root` |
| **Interactive Accent / Highlight** | `#e6efff` | `var(--c3)` in `:root` |
| **Secondary / Muted Copy** | `#ee0000` | `var(--c5)` in `:root` |
| **Structural Hairline Border** | `#bfbfbf` | `var(--c7)` in `:root` |
| **Variable Token (`--c8`)** | `#5e5e5e` | `var(--c8)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--app-height` | `100vh` | Layout / Spatial Grid Token |
| `--headroom-height` | `auto` | Layout / Spatial Grid Token |
| `--c0` | `#ffffff` | Color / Atmospheric Token |
| `--c1` | `#000000` | Color / Atmospheric Token |
| `--c2` | `#32006f` | Color / Atmospheric Token |
| `--c3` | `#e6efff` | Color / Atmospheric Token |
| `--c4` | `rgba(127, 173, 255, 0.2)` | Color / Atmospheric Token |
| `--c5` | `#ee0000` | Color / Atmospheric Token |
| `--c6` | `rgba(0, 0, 0, 0.7)` | Color / Atmospheric Token |
| `--c7` | `#bfbfbf` | Color / Atmospheric Token |
| `--c8` | `#5e5e5e` | Color / Atmospheric Token |
| `--wr` | `20rem` | Dimension / Scale Token |
| `--awr` | `calc(-1 * var(--wr))` | Design System Custom Token |
| `--gap` | `20rem` | Layout / Spatial Grid Token |
| `--sl` | `max(1px, 1rem)` | Dimension / Scale Token |
| `--br1` | `10rem` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hide-scrollbar> — `nodenza-com`)**:
   - Landmark `<header class="hide-scrollbar">` hosting `Home · Nodenza` navigation (`Home · Our Team · Portfolio · News · Webinars`), DOM attributes (`data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`, `data-acsb-force-visible="true"`, `data-acsb`), and stylesheet rule `html { font-size: 0.0625vw; background-color: var(--c3); }`.
2. **Hero Stage & Focal Lead (<section.hero-snap__slide> — `Experience the explosive power of `)**:
   - Landmark `<section class="hero-snap__slide">` presenting display lead `Experience the explosive power of when science me...` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hero-snap__slide> — `Our Mission`)**:
   - Landmark `<section class="hero-snap__slide">` rendering section `Our Mission` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`embed`, `styles.css`, `style.css`, `main.css`), and grid rule `body { overflow-x: hidden; }`.
4. **Interactive Detail & Feature Matrix (<section.hero-snap__slide> — `Our Approach`)**:
   - Landmark `<section class="hero-snap__slide">` framing `Our Approach` and `What brings you to Nodenza?` (*"Enabling disruptive life sciences technology."*) with `#32006f` surface cards, `#e6efff` accents, and `.wrapper { width: 100%; margin: 0 auto; padding: 0 var(--wr); max-width: var(--mw); }`.
5. **Colophon & Global Directory Footer (<footer.acsb-sr-alert> — `https://nodenza.com/`)**:
   - Landmark `<footer class="acsb-sr-alert">` anchoring `Home · Nodenza` footer links (`Home · Our Team · Portfolio · News · Webinars`), copy *"Established by a team of experienced life sciences entrepren"*, and `#bfbfbf` structural dividers.
