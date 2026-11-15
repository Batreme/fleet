# UI & UX Architecture: www-amberjs-dev

## Overview & Design Identity
- **Target**: `www-amberjs-dev` (**Amber — Scroll & Motion Toolkit**)
- **Production URL**: [https://www.amberjs.dev/](https://www.amberjs.dev/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#5c5d69` / `#101010`)
- **Summary**: A lightweight motion toolkit for expressive websites. Explore smooth scrolling, animation and SVG morphing with Amber.
- **Total Clean CSS Variables Extracted**: `48` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans Variable`
- **Body Font Stack**: `Fragment Mono`
- **Monospace / Technical Font Stack**: `Fragment Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(38px,4.3vw,66px)`, `line-height: 1.08`, `letter-spacing: -.055em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 36px`, `letter-spacing: -.04em`)
- **Body Copy**: rule `p` (`line-height: 1.8`)
- **Metadata & Labels**: CSS variables `--home-mono: "Fragment Mono",monospace`, `--mono: "Fragment Mono",monospace`; rule `nav` (`font-size: 14px`, `letter-spacing: normal`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#5c5d69` | `var(--home-muted)` in `:root` |
| **Primary Typography Ink** | `#dcdde1` | `var(--home-rule)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fcfbf8` | `var(--home-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#101010` | `var(--home-ink)` in `:root` |
| **Secondary / Muted Copy** | `#cf001c` | `var(--home-red)` in `:root` |
| **Structural Hairline Border** | `#767570` | `var(--muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--home-sans` | `"Instrument Sans Variable",sans-serif` | Typography / Scale Token |
| `--home-serif` | `"Instrument Serif",serif` | Typography / Scale Token |
| `--home-mono` | `"Fragment Mono",monospace` | Typography / Scale Token |
| `--home-muted` | `#5c5d69` | Color / Atmospheric Token |
| `--home-rule` | `#dcdde1` | Color / Atmospheric Token |
| `--home-paper` | `#fcfbf8` | Canvas / Surface Token |
| `--home-ink` | `#101010` | Typography Ink Token |
| `--home-red` | `#cf001c` | Color / Atmospheric Token |
| `--link-arrow-color` | `var(--home-ink)` | Typography Ink Token |
| `--camera-exit` | `0` | Design System Custom Token |
| `--camera-entry` | `1` | Design System Custom Token |
| `--camera-focus-scale` | `1.3` | Design System Custom Token |
| `--camera-focus-opacity` | `0` | Design System Custom Token |
| `--camera-inset-x` | `3.2vw` | Dimension / Scale Token |
| `--camera-inset-top` | `max(28px, env(safe-area-inset-top))` | Dimension / Scale Token |
| `--camera-inset-bottom` | `max(28px, env(safe-area-inset-bottom))` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.home-header> — `www-amberjs-dev`)**:
   - Landmark `<header class="home-header">` hosting `Amber — Scroll & Motion Toolkit` navigation (`Playground`), DOM attributes (`data-amber`, `data-engine="three.js r180"`, `data-paint`, `data-m-middle`), and stylesheet rule `button { font:inherit;color:inherit;cursor:pointer }`.
2. **Hero Stage & Focal Lead (<section.home-panel> — `Move it your way.`)**:
   - Landmark `<section class="home-panel">` presenting display lead `Move it your way.` and copy excerpt *"VISIT ON DESKTOP FOR BETTER EXPERIENCE."* over `#5c5d69` canvas and `#fcfbf8` ink.
3. **Primary Showcase & Content Grid (<section.box-scene> — `Small by design.`)**:
   - Landmark `<section class="box-scene">` rendering section `Small by design.` with copy *"A lightweight motion toolkit. Zero dependencies."*, asset references (`hardikgandhi.me`, `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `button:focus-visible { outline:2px solid var(--home-red);outline-offset:7px }`.
4. **Interactive Detail & Feature Matrix (<article.book-accessible-copy> — `The rest is yours.`)**:
   - Landmark `<article class="book-accessible-copy">` framing `The rest is yours.` and `Getting Started` (*"SMOOTH SCROLL · ANIMATE · MORPH"*) with `#fcfbf8` surface cards, `#101010` accents, and `selection { background:var(--home-red);color:fff }`.
5. **Colophon & Global Directory Footer (<footer.home-baseline> — `https://www.amberjs.dev/`)**:
   - Landmark `<footer class="home-baseline">` anchoring `Amber — Scroll & Motion Toolkit` footer links (`Playground`), copy *"RUNNING ON AMBER · <20 KB"*, and `#767570` structural dividers.
