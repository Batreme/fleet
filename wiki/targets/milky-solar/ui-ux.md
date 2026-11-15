# UI & UX Architecture: milky-solar

## Overview & Design Identity
- **Target**: `milky-solar` (**Earth**)
- **Production URL**: [https://milky.solar](https://milky.solar)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#000000` accent)
- **Summary**: Follow Wolfs journeys on Earth, navigating eternal cycles of conflict and transformation.
- **Total Clean CSS Variables Extracted**: `0` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Arial`
- **Body Font Stack**: `Helvetica`
- **Monospace / Technical Font Stack**: `Courier New`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `body { background-color: white }` (`#ffffff`) |
| **Primary Typography Ink** | `#000000` | `body { color: black }` (`#000000`) |
| **Elevated Surface / Card Substrate** | `#ff0000` | `select { border: red }` (`#ff0000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--milky-solar-bg` | `#ffffff` | Canvas Substrate (from `body { background-color: white }` (`#ffffff`)) |
| `--milky-solar-ink` | `#000000` | Primary Typography Ink (stylesheet-derived) |
| `--milky-solar-surface` | `#ff0000` | Surface Substrate (stylesheet-derived) |
| `--milky-solar-accent` | `#000000` | Interactive Accent (stylesheet-derived) |
| `--milky-solar-muted` | `#000000` | Secondary Ink (stylesheet-derived) |
| `--milky-solar-border` | `#000000` | Structural Border (stylesheet-derived) |
| `--milky-solar-container` | `890px` | Container Bound (stylesheet-derived) |
| `--milky-solar-gap` | `0px` | Grid Gutter (stylesheet-derived) |
| `--milky-solar-pad` | `4px` | Lateral Padding (stylesheet-derived) |
| `--milky-solar-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--milky-solar-radius` | `1px` | Corner Radius (stylesheet-derived) |
| `--milky-solar-fs-base` | `16px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.button> — `milky-solar`)**:
   - Landmark `<header class="button">` hosting `Earth` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scenario="new"`, `data-scenario="otherworld"`, `data-scenario="random"`, `data-scenario="israel"`), and stylesheet rule `body { background-color: white; color: black; width: 800px; text-align: center;... }`.
2. **Hero Stage & Focal Lead (<main.empty-space> — `Earth`)**:
   - Landmark `<main class="empty-space">` presenting display lead `Earth` and copy excerpt *"Follow Wolfs journeys on Earth, navigating eternal cycles of conf"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.float-up> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="float-up">` rendering section `Featured Work & Interactive Showcase` with copy *"Earth"*, asset references (`milky.solar`, `Logo.ico`, `Logo.svg`, `Logo.jpg`), and grid rule `header { width: 100%; }`.
4. **Interactive Detail & Feature Matrix (<main.balloon> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="balloon">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#ff0000` surface cards, `#000000` accents, and `main { margin-bottom: 20px; }`.
5. **Colophon & Global Directory Footer (<footer.float-down> — `https://milky.solar`)**:
   - Landmark `<footer class="float-down">` anchoring `Earth` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#000000` structural dividers.
