# UI & UX Architecture: guillaumecolombel-fr

## Overview & Design Identity
- **Target**: `guillaumecolombel-fr` (**Guillaume Colombel — Freelance Interactive Developer**)
- **Production URL**: [https://guillaumecolombel.fr/](https://guillaumecolombel.fr/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#050404` / `#fff`)
- **Summary**: Freelance Interactive Developer specializing in immersive web experiences and creative websites. Based in Paris, available worldwide.
- **Total Clean CSS Variables Extracted**: `3` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Neue Montreal`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.875rem`, `10px`, `.75rem`, `.8125rem`, `1.25rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: .6875rem`, `letter-spacing: .12em`, `font-weight: 400`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.875rem`, `10px`, `.75rem`, `.8125rem`, `1.25rem`)
- **Metadata & Labels**: rule `.label` (`font-size: 10px`, `letter-spacing: .06em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#050404` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#f0ebe2` | `var(--ivory)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `html { background: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#fff` | `#site-header a:hover { color: #fff }` |
| **Secondary / Muted Copy** | `#ffe8cd` | `#site-header .nav:focus-visible { color: #ffe8cd }` |
| **Structural Hairline Border** | `#fff1e0` | `#stele-loading .tip { stroke: #fff1e0 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#050404` | Canvas / Surface Token |
| `--ivory` | `#f0ebe2` | Color / Atmospheric Token |
| `--stele-progress` | `1` | Design System Custom Token |
| `--guillaumecolombe-bg` | `#050404` | Canvas Substrate (from `var(--black)` in `:root`) |
| `--guillaumecolombe-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--guillaumecolombe-surface` | `#000000` | Surface Substrate (stylesheet-derived) |
| `--guillaumecolombe-accent` | `#fff` | Interactive Accent (stylesheet-derived) |
| `--guillaumecolombe-muted` | `#ffe8cd` | Secondary Ink (stylesheet-derived) |
| `--guillaumecolombe-border` | `#fff1e0` | Structural Border (stylesheet-derived) |
| `--guillaumecolombe-container` | `30ch` | Container Bound (stylesheet-derived) |
| `--guillaumecolombe-gap` | `5px` | Grid Gutter (stylesheet-derived) |
| `--guillaumecolombe-pad` | `24px` | Lateral Padding (stylesheet-derived) |
| `--guillaumecolombe-ease` | `cubic-bezier(.165,.84,.44,1)` | Primary Easing Function |
| `--guillaumecolombe-radius` | `50%` | Corner Radius (stylesheet-derived) |
| `--guillaumecolombe-fs-base` | `.875rem` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.stele-gl-text> — `guillaumecolombel-fr`)**:
   - Landmark `<header class="stele-gl-text">` hosting `Guillaume Colombel — Freelance Inter` navigation (`01 CLARTÉ · 03 Chris Macari · 05 Axel Vanhessche · 06 Kaizen · 07 Magical Pantry`), DOM attributes (`data-website-id="6a9409f1-490b-4253-85..."`, `data-word="About"`, `data-engine="three.js r185 webgpu"`, `data-slug="clarte"`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.router-link-active> — `Guillaume Colombel, freelance inte`)**:
   - Landmark `<section class="router-link-active">` presenting display lead `Guillaume Colombel, freelance interactive developer` and copy excerpt *"Guillaume Colombel"* over `#050404` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.awards> — `Guillaume Colombel`)**:
   - Landmark `<section class="awards">` rendering section `Guillaume Colombel` with copy *"02 Jean Paul Gaultier — La Favorite"*, asset references (`integral-msdf.png`, `integral-msdf.json`, `NeueMontreal-Medium.woff2`, `_payload.json`), and grid rule `html { -webkit-text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.awards> — `02 Jean Paul Gaultier — La Favorit`)**:
   - Landmark `<section class="awards">` framing `02 Jean Paul Gaultier — La Favorite` and `Jean Paul Gaultier — La Favorite` (*"Jean Paul Gaultier — La Favorite"*) with `#000000` surface cards, `#fff` accents, and `video { display:block;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.nav> — `https://guillaumecolombel.fr/`)**:
   - Landmark `<footer class="nav">` anchoring `Guillaume Colombel — Freelance I` footer links (`01 CLARTÉ · 03 Chris Macari · 05 Axel Vanhessche · 06 Kaizen · 07 Magical Pantry`), copy *"04 Ousmane Ballon d'Or"*, and `#fff1e0` structural dividers.
