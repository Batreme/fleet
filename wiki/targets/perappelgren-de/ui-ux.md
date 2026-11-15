# UI & UX Architecture: perappelgren-de

## Overview & Design Identity
- **Target**: `perappelgren-de` (**Per Appelgren**)
- **Production URL**: [https://perappelgren.de/](https://perappelgren.de/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ffffff`)
- **Summary**: Per Appelgren is a Paris and Berlin based photographer working across fashion, beauty, editorial, and commercial image-making.
- **Total Clean CSS Variables Extracted**: `30` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `neueMontreal`
- **Body Font Stack**: `neueMontreal Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-sm)`, `var(--text-xs)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-sm)`, `var(--text-xs)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-sm)`, `var(--text-xs)`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `textarea { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#ffffff` | `.border-white { border-color: white }` (`#ffffff`) |
| **Secondary / Muted Copy** | `#fffc` | `80 { border-color: #fffc }` |
| **Structural Hairline Border** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-neue-montreal` | `"neueMontreal", "neueMontreal Fallback"` | Typography / Scale Token |
| `--font-vemior` | `"vemior", "vemior Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-neue-montreal)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--tracking-normal` | `0em` | Typography / Scale Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.home-nav> — `perappelgren-de`)**:
   - Landmark `<nav class="home-nav fixed">` hosting `Per Appelgren` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-gallery-title-track="true"`, `data-cursor="arrow"`), and stylesheet rule `real_94799760-module__C5EBEW__cla... { font-family:neueMontreal,neueMontreal Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Studio`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Studio` and copy excerpt *"CASABLANCA PRE-FALL ´26 CAMPAIGN"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Office`)**:
   - Landmark `<section class="relative w-full">` rendering section `Office` with copy *"ARCHIVE A R C H I V E"*, asset references (`vemior-s.p.0loat6znd6m5-.otf`, `12mrv9~q-_9yg.css`, `0wjx1qarcnur7.js`, `14x4ulv7j4.e5.js`), and grid rule `treal_94799760-module__C5EBEW__va... { --font-neue-montreal:"neueMontreal", "neueMontreal Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Represented in Europe`)**:
   - Landmark `<section class="relative h-auto">` framing `Represented in Europe` and `CONTACT C O N T A C T` (*"CONTACT C O N T A C T"*) with `#0000` surface cards, `#ffffff` accents, and `mior_bd07f20d-module__cotiFq__cla... { font-family:vemior,vemior Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://perappelgren.de/`)**:
   - Landmark `<footer class="relative z-42">` anchoring `Per Appelgren` footer links (`Overview · Index · Archive · About · Contact`), copy *"Hi! I am Per! I'm a German-Swedish photographer based betwee"*, and `#000000` structural dividers.
