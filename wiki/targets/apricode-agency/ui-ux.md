# UI & UX Architecture: apricode-agency

## Overview & Design Identity
- **Target**: `apricode-agency` (**Apricode — Immersive Websites, Ecommerce, Apps & AI**)
- **Production URL**: [https://apricode.agency](https://apricode.agency)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#eeece6` / `#d6b287`)
- **Summary**: Apricode is an independent design and development studio. We create immersive websites, ecommerce experiences, digital products and AI wo...
- **Total Clean CSS Variables Extracted**: `57` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `clamp(64px`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--home-display: clamp(64px,9.5vw,152px)`; rule `h1` (`font-size: clamp(56px,5.25vw,90px)`, `line-height: 1.055`, `letter-spacing: -.055em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(50px,6.9vw,110px)`, `line-height: 1.02`, `letter-spacing: -.056em`, `font-weight: 440`)
- **Body Copy**: rule `p` (`font-size: 17px`, `line-height: 1.6`)
- **Metadata & Labels**: CSS variables `--editorial-metal: #847360`, `--phone-label: 11px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#eeece6` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#243037` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#69757a` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#d6b287` | `var(--signal)` in `:root` |
| **Secondary / Muted Copy** | `#847360` | `var(--editorial-metal)` in `:root` |
| **Structural Hairline Border** | `#192126` | `var(--editorial-dark)` in `:root` |
| **Variable Token (`--brand-paper`)** | `#f3f1ec` | `var(--brand-paper)` in `:root` |
| **Variable Token (`--brand-ink`)** | `#232624` | `var(--brand-ink)` in `:root` |
| **Variable Token (`--brand-dark`)** | `#111918` | `var(--brand-dark)` in `:root` |
| **Variable Token (`--brand-surface`)** | `#e8e5df` | `var(--brand-surface)` in `:root` |
| **Variable Token (`--brand-muted`)** | `#6b706b` | `var(--brand-muted)` in `:root` |
| **Variable Token (`--brand-secondary`)** | `#677062` | `var(--brand-secondary)` in `:root` |
| **Variable Token (`--brand-olive`)** | `#65705f` | `var(--brand-olive)` in `:root` |
| **Variable Token (`--brand-sage`)** | `#c7d6a8` | `var(--brand-sage)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#eeece6` | Canvas / Surface Token |
| `--ink` | `#243037` | Typography Ink Token |
| `--muted` | `#69757a` | Color / Atmospheric Token |
| `--signal` | `#d6b287` | Color / Atmospheric Token |
| `--gutter` | `clamp(24px,6.7vw,112px)` | Layout / Spatial Grid Token |
| `--editorial-metal` | `#847360` | Color / Atmospheric Token |
| `--editorial-dark` | `#192126` | Canvas / Surface Token |
| `--work-inset` | `72px` | Dimension / Scale Token |
| `--brand-paper` | `#f3f1ec` | Canvas / Surface Token |
| `--brand-ink` | `#232624` | Typography Ink Token |
| `--brand-dark` | `#111918` | Canvas / Surface Token |
| `--brand-surface` | `#e8e5df` | Canvas / Surface Token |
| `--brand-muted` | `#6b706b` | Brand / Palette Token |
| `--brand-secondary` | `#677062` | Brand / Palette Token |
| `--brand-olive` | `#65705f` | Brand / Palette Token |
| `--brand-sage` | `#c7d6a8` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.passage-nav> — `apricode-agency`)**:
   - Landmark `<header class="passage-nav has-adaptive-header">` hosting `Apricode — Immersive Websites, Ecomm` navigation (`Work · Solutions · About · Contact`), DOM attributes (`data-focus-input="keyboard"`, `data-route-critical`, `data-site-seo`, `data-header-ready`), and stylesheet rule `font-face { font-family:Geist;src:url(/fonts/geist/Geist-Variable.woff2)format("woff... }`.
2. **Hero Stage & Focal Lead (<section.scene-copy> — `Make the digital feel extraordinar`)**:
   - Landmark `<section class="scene-copy scene-copy--hero">` presenting display lead `Make the digital feel extraordinary` and copy excerpt *"Skip to what we do"* over `#eeece6` canvas and `#192126` ink.
3. **Primary Showcase & Content Grid (<section.scene-copy> — `Bring the pieces together`)**:
   - Landmark `<section class="scene-copy scene-copy--pieces">` rendering section `Bring the pieces together` with copy *"Independent thinking. Connected execution."*, asset references (`Geist-Variable.woff2`, `modulepreload-polyfill-P2Xu9kJm.js`, `render-budget-C7i9NcxA.js`, `viewport-a3t6fSxm.js`), and grid rule `body { -webkit-font-smoothing:antialiased;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.scene-copy> — `Built to explore Ready to use`)**:
   - Landmark `<section class="scene-copy scene-copy--connection">` framing `Built to explore Ready to use` and `Find your angle` (*"hello@apricode.agency"*) with `#69757a` surface cards, `#d6b287` accents, and `button { font:inherit;cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.site-end> — `https://apricode.agency`)**:
   - Landmark `<footer class="site-end">` anchoring `Apricode — Immersive Websites, E` footer links (`Work · Solutions · About · Contact`), copy *"Loading the experience"*, and `#192126` structural dividers.
