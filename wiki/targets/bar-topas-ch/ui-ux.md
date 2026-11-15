# UI & UX Architecture: bar-topas-ch

## Overview & Design Identity
- **Target**: `bar-topas-ch` (**Tòpas - bar-topas.ch**)
- **Production URL**: [https://bar-topas.ch/](https://bar-topas.ch/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#B21236` / `#FEB914`)
- **Summary**: Tòpas by Topaze — Tapas & Bar. Découvrez la nouvelle cuisine hispano-suisse du Topaze.
- **Total Clean CSS Variables Extracted**: `21` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Barlow Condensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`)
- **Body Copy**: rule `body` (`font-size: clamp(17px, 1.05vw + 10px, 21px)`, `line-height: 1.45`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#B21236` | `var(--rouge)` in `:root` |
| **Primary Typography Ink** | `#EFEFE3` | `var(--creme)` in `:root` |
| **Elevated Surface / Card Substrate** | `#EDEAE0` | `var(--creme-fond)` in `:root` |
| **Interactive Accent / Highlight** | `#FEB914` | `var(--jaune)` in `:root` |
| **Secondary / Muted Copy** | `#FE8826` | `var(--orange)` in `:root` |
| **Structural Hairline Border** | `#F03812` | `var(--orange-rouge)` in `:root` |
| **Variable Token (`--bleu`)** | `#2C9FA2` | `var(--bleu)` in `:root` |
| **Variable Token (`--bordeaux`)** | `#7C1820` | `var(--bordeaux)` in `:root` |
| **Variable Token (`--brun`)** | `#60150D` | `var(--brun)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rouge` | `#B21236` | Color / Atmospheric Token |
| `--creme` | `#EFEFE3` | Color / Atmospheric Token |
| `--creme-fond` | `#EDEAE0` | Color / Atmospheric Token |
| `--jaune` | `#FEB914` | Color / Atmospheric Token |
| `--orange` | `#FE8826` | Color / Atmospheric Token |
| `--orange-rouge` | `#F03812` | Color / Atmospheric Token |
| `--bleu` | `#2C9FA2` | Color / Atmospheric Token |
| `--bordeaux` | `#7C1820` | Color / Atmospheric Token |
| `--brun` | `#60150D` | Color / Atmospheric Token |
| `--f-title` | `"Archivo", "Arial Black", system-ui, sans-serif` | Dimension / Scale Token |
| `--f-cond` | `"Barlow Condensed", "Arial Narrow", system-ui, sans-serif` | Dimension / Scale Token |
| `--f-text` | `"Source Sans 3", Arial, system-ui, sans-serif` | Typography Ink Token |
| `--gutter` | `clamp(16px, 4vw, 56px)` | Layout / Spatial Grid Token |
| `--radius` | `22px` | Elevation / Border Token |
| `--ease` | `cubic-bezier(.2, .8, .2, 1)` | Motion / Easing Token |
| `--topbar-h` | `76px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `bar-topas-ch`)**:
   - Landmark `<header class="topbar">` hosting `Tòpas - bar-topas.ch` navigation (`Bar Le Topaze`), DOM attributes (`data-intro`, `data-intro-bar`, `data-intro-done`, `data-cursor`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.s-hero> — `Tòpas by Topaze — Tapas & Bar à Vi`)**:
   - Landmark `<section class="s-hero">` presenting display lead `Tòpas by Topaze — Tapas & Bar à Vicques` and copy excerpt *"On allume la plancha…"* over `#B21236` canvas and `#EFEFE3` ink.
3. **Primary Showcase & Content Grid (<section.s-marquee> — `Tòpas`)**:
   - Landmark `<section class="s-marquee">` rendering section `Tòpas` with copy *"Les pinchos arrivent. Paciencia, amigo."*, asset references (`1640559617463684`, `fbevents.js`, `gtm.js`, `archivo-var-latin.woff2`), and grid rule `html.lenis body { height: auto; }`.
4. **Interactive Detail & Feature Matrix (<section.s-def> — `Un pincho, c’est simple.`)**:
   - Landmark `<section class="s-def">` framing `Un pincho, c’est simple.` and `Mucho délicieuse.` (*"On fait fondre la raclette. Lentamente."*) with `#EDEAE0` surface cards, `#FEB914` accents, and `.lenis.lenis-smooth { scroll-behavior: auto !important; }`.
5. **Colophon & Global Directory Footer (<footer.s-end> — `https://bar-topas.ch/`)**:
   - Landmark `<footer class="s-end edge-wave">` anchoring `Tòpas - bar-topas.ch` footer links (`Bar Le Topaze`), copy *"El chef cherche son pic. Il était dans sa poche."*, and `#F03812` structural dividers.
