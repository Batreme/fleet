# UI & UX Architecture: ofrenda-davidlangarica-dev

## Overview & Design Identity
- **Target**: `ofrenda-davidlangarica-dev` (**OFRENDA — Create a personal Día de Muertos altar**)
- **Production URL**: [https://ofrenda.davidlangarica.dev](https://ofrenda.davidlangarica.dev)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ef893b`)
- **Summary**: Create a personal Día de Muertos ofrenda with a photograph, flowers, candles, and meaningful offerings. A quiet place to remember someone...
- **Total Clean CSS Variables Extracted**: `37` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Marqen`
- **Body Font Stack**: `Macario`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(44px,12vw,72px)`, `line-height: 1.08`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 30px`, `line-height: 1.1`)
- **Body Copy**: CSS variables `--ui-font-body: Georgia, "Times New Roman", serif`, `--ui-body-size: clamp(16px, 1.5vw, 19px)`, `--ui-body-line-height: 1.55`; rule `p` (`font-size: 16px`, `line-height: 1.4`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `clamp(44px,12vw,72px)`, `16px`, `30px`, `13px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--ui-backdrop)` in `:root` |
| **Primary Typography Ink** | `#f4e6cf` | `var(--ui-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d5c4a9` | `var(--ui-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#ef893b` | `var(--ui-heading)` in `:root` |
| **Secondary / Muted Copy** | `#f3e3c7` | `var(--ui-home-heading)` in `:root` |
| **Structural Hairline Border** | `#efd6a4` | `var(--ui-focus)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ui-font-heading` | `"Marqen", Georgia, "Times New Roman", serif` | Typography Ink Token |
| `--ui-font-body` | `Georgia, "Times New Roman", serif` | Typography / Scale Token |
| `--ui-text-shadow` | `0 2px 14px #000` | Typography Ink Token |
| `--ui-backdrop` | `#000` | Color / Atmospheric Token |
| `--ui-text` | `#f4e6cf` | Typography Ink Token |
| `--ui-muted` | `#d5c4a9` | Color / Atmospheric Token |
| `--ui-heading` | `#ef893b` | Typography Ink Token |
| `--ui-home-heading` | `#f3e3c7` | Typography Ink Token |
| `--ui-amber-rgb` | `189 149 91` | Design System Custom Token |
| `--ui-amber` | `rgb(var(--ui-amber-rgb))` | Color / Atmospheric Token |
| `--ui-surface-rgb` | `70 39 17` | Canvas / Surface Token |
| `--ui-surface` | `rgb(var(--ui-surface-rgb) / .18)` | Canvas / Surface Token |
| `--ui-surface-hover` | `rgb(160 110 49 / .2)` | Canvas / Surface Token |
| `--ui-surface-pressed` | `rgb(184 133 67 / .28)` | Canvas / Surface Token |
| `--ui-border` | `rgb(var(--ui-amber-rgb) / .74)` | Elevation / Border Token |
| `--ui-focus` | `#efd6a4` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.experience-chrome> — `ofrenda-davidlangarica-dev`)**:
   - Landmark `<header class="experience-chrome">` hosting `OFRENDA — Create a personal Día de M` navigation (`David Langarica`), DOM attributes (`data-cf-beacon="("token":"e723bd39f9d..."`, `data-engine="three.js r180 webgpu"`, `data-on="true"`, `data-loading-progress="0.9"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.floating-menu> — `OFRENDA`)**:
   - Landmark `<section class="floating-menu">` presenting display lead `OFRENDA` and copy excerpt *"For you, who still have a place here."* over `#000` canvas and `#f4e6cf` ink.
3. **Primary Showcase & Content Grid (<section.floating-menu> — `OFRENDA — A place to remember`)**:
   - Landmark `<section class="floating-menu">` rendering section `OFRENDA — A place to remember` with copy *"Language Choose English or Spanish."*, asset references (`favicon.ico`, `Marqen.woff2`, `index-CUtJAqPO.js`, `index-BRkV915_.css`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.floating-menu> — `Language Choose English or Spanish`)**:
   - Landmark `<section class="floating-menu">` framing `Language Choose English or Spanish.` and `Sound Music and ambience.` (*"Sound Music and ambience."*) with `#d5c4a9` surface cards, `#ef893b` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.menu-footer> — `https://ofrenda.davidlangarica.dev`)**:
   - Landmark `<footer class="menu-footer">` anchoring `OFRENDA — Create a personal Día ` footer links (`David Langarica`), copy *"Graphics Available after the water and salt."*, and `#efd6a4` structural dividers.
