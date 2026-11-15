# UI & UX Architecture: suho-studio

## Overview & Design Identity
- **Target**: `suho-studio` (**Suho Video Editor**)
- **Production URL**: [https://suho.studio/](https://suho.studio/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f3f3ef` / `#2f53ff`)
- **Summary**: Selected work by Suho, video editor and sound designer.
- **Total Clean CSS Variables Extracted**: `99` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Magazine Letter Web`
- **Body Font Stack**: `Awakenning Web`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-weight-display: 600`, `--tracking-display: -.083em`, `--type-display: clamp(3.3rem, 1.52857rem + 8.85714vw, 9.5rem)`; rule `h1` (`font-size: clamp(72px,9vw,170px)`, `line-height: 1`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.35rem,1rem + 1.3vw,2rem)`, `clamp(1.35rem,1rem + 1.9vw,2.5rem)`, `1.1rem`, `clamp(1rem,3.8vw,1.25rem)`, `var(--type-label)`)
- **Body Copy**: CSS variables `--type-body: clamp(.95rem, .9rem + .25vw, 1.125rem)`
- **Metadata & Labels**: CSS variables `--tracking-label: .07em`, `--type-label: clamp(.625rem, .589286rem + .178571vw, .75rem)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f3ef` | `var(--color-paper)` in `:root` |
| **Primary Typography Ink** | `#ebebeb` | `var(--color-gallery-paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#10100f` | `var(--color-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#2f53ff` | `var(--color-blue)` in `:root` |
| **Secondary / Muted Copy** | `#7d3fef` | `var(--color-purple)` in `:root` |
| **Structural Hairline Border** | `#99a8ff` | `var(--color-blue-soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--secondary-loop-gap` | `clamp(4rem, 13vh, 7rem)` | Brand / Palette Token |
| `--trust-viewport` | `calc(var(--screen) - var(--browser-chrome))` | Layout / Spatial Grid Token |
| `--trust-top` | `max(.5rem, env(safe-area-inset-top,0px))` | Dimension / Scale Token |
| `--cover-media-left` | `55vw` | Dimension / Scale Token |
| `--cover-media-width` | `clamp(10.5rem, 22vw, 19rem)` | Layout / Spatial Grid Token |
| `--blend-left` | `calc(var(--cover-media-left) - var(--page-gutter))` | Design System Custom Token |
| `--cover-description-offset` | `clamp(0rem, 8vw, 8rem)` | Dimension / Scale Token |
| `--font-film-magazine` | `var(--font-major)` | Typography / Scale Token |
| `--font-film-reze` | `var(--font-major)` | Typography / Scale Token |
| `--font-film-silksong` | `var(--font-major)` | Typography / Scale Token |
| `--film-wipe` | `1` | Design System Custom Token |
| `--reel-touch-target` | `44px` | Dimension / Scale Token |
| `--reel-seek-outset` | `22px` | Dimension / Scale Token |
| `--cover-lift` | `var(--nav-rail-clearance,0px)` | Dimension / Scale Token |
| `--carry-width` | `clamp(13.25rem, 74vw, 18rem)` | Layout / Spatial Grid Token |
| `--carry-left` | `calc(var(--page-gutter) + clamp(1.75rem, 8vw, 3.5rem))` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.skip-link> — `suho-studio`)**:
   - Landmark `<header class="skip-link">` hosting `Suho Video Editor` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-skip-link="true"`), and stylesheet rule `t-reel-module-scss-module__ba9t6W... { margin-bottom:1.25rem;font-size:1.1rem }`.
2. **Hero Stage & Focal Lead (<section.static-portfolio> — `Suho Video Editor`)**:
   - Landmark `<section class="static-portfolio">` presenting display lead `Suho Video Editor` and copy excerpt *"Selected work by Suho, video editor and sound designer."* over `#f3f3ef` canvas and `#10100f` ink.
3. **Primary Showcase & Content Grid (<section.sr-only> — `Selected work`)**:
   - Landmark `<section class="sr-only">` rendering section `Selected work` with copy *"Featured commission Screens, text and graphics move together to s"*, asset references (`Figtree-VariableFont_wght.woff2`, `254drbfp0n4_4.css`, `161fswjwr-tnq.css`, `00ierz6vnepx8.css`), and grid rule `l-module-scss-module__ba9t6W__par... { font-size:clamp(1rem,3.8vw,1.25rem);line-height:1.4 }`.
4. **Interactive Detail & Feature Matrix (<section> — `Personal edits`)**:
   - Landmark `<section>` landmark framing `Personal edits` and `Contact` (*"Featured commission"*) with `#10100f` surface cards, `#2f53ff` accents, and `module-scss-module__ba9t6W__chipF... { height:5rem }`.
5. **Colophon & Global Directory Footer (<footer> — `https://suho.studio/`)**:
   - Landmark `<footer>` landmark anchoring `Suho Video Editor` footer links (`Overview · Index · Archive · About · Contact`), copy *"Screens, text and graphics move together to show a product i"*, and `#99a8ff` structural dividers.
