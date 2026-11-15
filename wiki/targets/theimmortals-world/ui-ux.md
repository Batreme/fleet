# UI & UX Architecture: theimmortals-world

## Overview & Design Identity
- **Target**: `theimmortals-world` (**The Immortals**)
- **Production URL**: [https://theimmortals.world/](https://theimmortals.world/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#efefef` / `#f1f1f1`)
- **Summary**: An interactive journey through the history of the FIFA World Cup, celebrating every tournament from 1930 to 2022 through iconic moments,...
- **Total Clean CSS Variables Extracted**: `0` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bricolage Grotesque`
- **Body Font Stack**: `Bricolage Grotesque`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#efefef` | `html { background-color: #efefef }` |
| **Primary Typography Ink** | `#121212` | `body { color: #121212 }` |
| **Elevated Surface / Card Substrate** | `#1a1a1a` | `#loader { color: #1a1a1a }` |
| **Interactive Accent / Highlight** | `#f1f1f1` | `#loader { background: #f1f1f1 }` |
| **Secondary / Muted Copy** | `#004cff` | `#g_w div { background: #004cff }` |
| **Structural Hairline Border** | `#000` | `.dots { border-bottom: #000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--theimmortals-wor-bg` | `#efefef` | Canvas Substrate (from `html { background-color: #efefef }`) |
| `--theimmortals-wor-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--theimmortals-wor-surface` | `#1a1a1a` | Surface Substrate (stylesheet-derived) |
| `--theimmortals-wor-accent` | `#f1f1f1` | Interactive Accent (stylesheet-derived) |
| `--theimmortals-wor-muted` | `#004cff` | Secondary Ink (stylesheet-derived) |
| `--theimmortals-wor-border` | `#000` | Structural Border (stylesheet-derived) |
| `--theimmortals-wor-container` | `91rem` | Container Bound (stylesheet-derived) |
| `--theimmortals-wor-gap` | `20.5rem` | Grid Gutter (stylesheet-derived) |
| `--theimmortals-wor-pad` | `.2rem` | Lateral Padding (stylesheet-derived) |
| `--theimmortals-wor-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--theimmortals-wor-radius` | `5px` | Corner Radius (stylesheet-derived) |
| `--theimmortals-wor-fs-base` | `28rem` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav-w> — `theimmortals-world`)**:
   - Landmark `<nav class="nav-w">` hosting `The Immortals` navigation (`The Immortals`), DOM attributes (`data-tr="menu"`, `data-media="https://images.prismi..."`, `data-tr="menu"`, `data-media="https://images.prismi..."`), and stylesheet rule `after { box-sizing:border-box;-webkit-user-select:none;user-select:none }`.
2. **Hero Stage & Focal Lead (<section.ti> — `The Immortals`)**:
   - Landmark `<section class="ti">` presenting display lead `The Immortals` and copy excerpt *"Designer, Developer Jason Jerez"* over `#efefef` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.nav-menu> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="nav-menu">` rendering section `Featured Work & Interactive Showcase` with copy *"Designer, Developer"*, asset references (`theimmortals.world`, `main.css`, `favicon-96x96.png`, `favicon.svg`), and grid rule `body { -webkit-font-smoothing:antialiased;text-rendering:optimizespeed }`.
4. **Interactive Detail & Feature Matrix (<section.menu-wr> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="menu-wr">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"The story continues"*) with `#1a1a1a` surface cards, `#f1f1f1` accents, and `svg { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.m-ti> — `https://theimmortals.world/`)**:
   - Landmark `<footer class="m-ti">` anchoring `The Immortals` footer links (`The Immortals`), copy *"The Return of La Roja"*, and `#000` structural dividers.
