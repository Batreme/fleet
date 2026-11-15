# UI & UX Architecture: douglus-co

## Overview & Design Identity
- **Target**: `douglus-co` (**Douglus Nguyen — Web Designer from Vietnam**)
- **Production URL**: [https://douglus.co](https://douglus.co)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fefff8` / `#ebebeb`)
- **Summary**: Independent web designer based in Vietnam, focused on website design, interaction design, and front-end development.
- **Total Clean CSS Variables Extracted**: `92` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Roxborough CF`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`)
- **Body Copy**: rule `p` (`font-size: clamp(.875rem, var(--gw) * .2...`, `line-height: 1.2`, `letter-spacing: -.045em`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fefff8` | `var(--white-color)` in `:root` |
| **Primary Typography Ink** | `#1e1e1e` | `var(--black-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#292724` | `var(--neutral-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ebebeb` | `var(--muted-color)` in `:root` |
| **Secondary / Muted Copy** | `#1c1d20` | `var(--nf-deep)` in `:root` |
| **Structural Hairline Border** | `#000` | `.c-scrollbar_thumb { background-color: #000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-padding` | `clamp(20px, 2.3vw, 40px)` | Layout / Spatial Grid Token |
| `--header-height` | `112px` | Layout / Spatial Grid Token |
| `--footer-right-width` | `clamp(38.75rem, 45.14vw, 48.75rem)` | Layout / Spatial Grid Token |
| `--white-color` | `#fefff8` | Canvas / Surface Token |
| `--black-color` | `#1e1e1e` | Canvas / Surface Token |
| `--neutral-color` | `#292724` | Brand / Palette Token |
| `--muted-color` | `#ebebeb` | Brand / Palette Token |
| `--default-easing` | `cubic-bezier(.25, 1, .5, 1)` | Motion / Easing Token |
| `--gw` | `4.16667vw` | Dimension / Scale Token |
| `--rv-ease` | `var(--default-easing)` | Motion / Easing Token |
| `--rv-ease-img` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Easing Token |
| `--rv-d-s` | `.5s` | Motion / Timing Token |
| `--rv-d-m` | `.7s` | Motion / Timing Token |
| `--rv-d-l` | `.9s` | Motion / Timing Token |
| `--rv-step-t` | `40ms` | Motion / Timing Token |
| `--rv-step-l` | `80ms` | Motion / Timing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `douglus-co`)**:
   - Landmark `<header class="site-header">` hosting `Douglus Nguyen — Web Designer from V` navigation (`H ome · W orks · P layground · A bout · C ontact`), DOM attributes (`data-scroll-direction="vertical"`, `data-barba="wrapper"`, `data-preloader`, `data-fragment="1"`), and stylesheet rule `video { font-size:100%;font:inherit;vertical-align:baseline;border:0;margin:0;pa... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `D ouglus N guyen`)**:
   - Landmark `<section class="home-hero">` presenting display lead `D ouglus N guyen` and copy excerpt *"Hello, Welcome to my Portfolio"* over `#fefff8` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.home-hero> — `Hello, Welcome to my Portfolio`)**:
   - Landmark `<section class="home-hero">` rendering section `Hello, Welcome to my Portfolio` with copy *"Open for collaborations"*, asset references (`favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.home-hero> — `Open for collaborations`)**:
   - Landmark `<section class="home-hero">` framing `Open for collaborations` and `Menu Menu Close Close` (*"Menu Menu Close Close"*) with `#292724` surface cards, `#ebebeb` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.preloader__subject> — `https://douglus.co`)**:
   - Landmark `<footer class="preloader__subject">` anchoring `Douglus Nguyen — Web Designer fr` footer links (`H ome · W orks · P layground · A bout · C ontact`), copy *"Just a designer & developer trying to make good things for t"*, and `#000` structural dividers.
