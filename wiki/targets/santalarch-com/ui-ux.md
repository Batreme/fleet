# UI & UX Architecture: santalarch-com

## Overview & Design Identity
- **Target**: `santalarch-com` (**Santalarch**)
- **Production URL**: [https://santalarch.com](https://santalarch.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f0` / `#0f0f0f`)
- **Summary**: Architectural studio built on uncompromising precision and intent.
- **Total Clean CSS Variables Extracted**: `103` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica`
- **Body Font Stack**: `lil-gui`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`line-height: calc(var(--title-heig...`, `font-weight: 600`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `14.625rem`, `7.875rem`, `6.125rem`, `4rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `14.625rem`, `7.875rem`, `6.125rem`, `4rem`)
- **Metadata & Labels**: CSS variables `--font-family-mono: Menlo, Monaco, Consolas, "Droid Sans Mono", monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0f0` | `var(--c-base-light-primary)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--c-pure-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--c-pure-white)` in `:root` |
| **Interactive Accent / Highlight** | `#0f0f0f` | `var(--c-base-dark-primary)` in `:root` |
| **Secondary / Muted Copy** | `#8f2424` | `var(--c-error)` in `:root` |
| **Structural Hairline Border** | `#1f1f1f` | `var(--background-color)` in `:root` |
| **Variable Token (`--c-base-line-highlight`)** | `#f2f0f033` | `var(--c-base-line-highlight)` in `:root` |
| **Variable Token (`--c-base-line-dark-bg`)** | `#f2f0f00d` | `var(--c-base-line-dark-bg)` in `:root` |
| **Variable Token (`--c-light-secondary`)** | `#f2f0f066` | `var(--c-light-secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--viewport-width` | `1440` | Layout / Spatial Grid Token |
| `--viewport-height` | `800` | Layout / Spatial Grid Token |
| `--font-helvetica` | `"Helvetica",sans-serif` | Typography / Scale Token |
| `--ease-out` | `cubic-bezier(.25,1,.5,1)` | Motion / Easing Token |
| `--transition` | `.5s var(--ease-out)` | Motion / Easing Token |
| `--transition-fast` | `.3s var(--ease-out)` | Motion / Easing Token |
| `--transition-slow` | `.8s var(--ease-out)` | Motion / Easing Token |
| `--c-base-light-primary` | `#f0f0f0` | Canvas / Surface Token |
| `--c-base-line-highlight` | `#f2f0f033` | Canvas / Surface Token |
| `--c-base-line-dark-bg` | `#f2f0f00d` | Canvas / Surface Token |
| `--c-pure-black` | `#000` | Canvas / Surface Token |
| `--c-pure-white` | `#fff` | Canvas / Surface Token |
| `--c-pure-black-rgb` | `0,0,0` | Canvas / Surface Token |
| `--c-pure-black-0` | `rgba(var(--c-pure-black-rgb),0)` | Canvas / Surface Token |
| `--c-light-primary` | `var(--c-base-light-primary)` | Canvas / Surface Token |
| `--c-light-secondary` | `#f2f0f066` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `santalarch-com`)**:
   - Landmark `<header class="header difference">` hosting `Santalarch` navigation (`Works Works · Services Services · Process Process · Company Company · Contact Contact`), DOM attributes (`data-theme="light"`, `data-v-fd5224ce`, `data-v-211bdc1c`, `data-v-52d76f34`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Bold`)**:
   - Landmark `<section class="hero">` presenting display lead `Bold` and copy excerpt *"This site uses cookies."* over `#f0f0f0` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.cubes-wrap> — `Confident`)**:
   - Landmark `<section class="cubes-wrap">` rendering section `Confident` with copy *"Philosophy Philosophy"*, asset references (`entry.D7X7o5bn.css`, `DrgmgFce.js`, `08bc0b24-806f-4d88-b7d6-f5aecb73d...`, `ad.B18i8NGa.svg`), and grid rule `video { border:0;font-size:100%;font:inherit;margin:0;padding:0;vertical-align:b... }`.
4. **Interactive Detail & Feature Matrix (<section.approach> — `Quiet`)**:
   - Landmark `<section class="approach grid-container">` framing `Quiet` and `Intent Before Image` (*"Architectural studio built on uncompromising precision and intent"*) with `#fff` surface cards, `#0f0f0f` accents, and `svg { display:block }`.
5. **Colophon & Global Directory Footer (<footer.cookies-actions> — `https://santalarch.com`)**:
   - Landmark `<footer class="cookies-actions">` anchoring `Santalarch` footer links (`Works Works · Services Services · Process Process · Company Company · Contact Contact`), copy *"Architecture Shapes Perception"*, and `#1f1f1f` structural dividers.
