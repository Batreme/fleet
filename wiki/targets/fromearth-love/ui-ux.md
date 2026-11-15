# UI & UX Architecture: fromearth-love

## Overview & Design Identity
- **Target**: `fromearth-love` (**fromearth · 2050 — Explore climate projections**)
- **Production URL**: [http://fromearth.love](http://fromearth.love)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f7fa` / `#051236`)
- **Summary**: See your future. Explore how climate and population could change where you live, from 2026 to 2050.
- **Total Clean CSS Variables Extracted**: `47` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Noto Sans Cuneiform`
- **Body Font Stack**: `EarthLausanne`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: -.025em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 25px`, `line-height: 1.2`, `letter-spacing: -.025em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 13px`)
- **Metadata & Labels**: CSS variables `--mono: 'PingFang TC','Microsoft JhengHei',sans-serif`; rule `small` (`font-size: 10px`, `line-height: 1.3`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f7fa` | `var(--glass-text)` in `:root` |
| **Primary Typography Ink** | `#c1cad5` | `var(--glass-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b9bdb6` | `var(--fiche-secondaire)` in `:root` |
| **Interactive Accent / Highlight** | `#051236` | `var(--encre)` in `:root` |
| **Secondary / Muted Copy** | `#071a45` | `var(--encre-2)` in `:root` |
| **Structural Hairline Border** | `#0b2358` | `var(--encre-3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--earth-ease` | `cubic-bezier(.19,1,.22,1)` | Motion / Easing Token |
| `--ui-unit` | `max(10px,.5208333333vw)` | Dimension / Scale Token |
| `--ui-inset-x` | `2.5vw` | Dimension / Scale Token |
| `--ui-inset-y` | `var(--ui-inset-x)` | Design System Custom Token |
| `--ui-control` | `max(44px,calc(4.4 * var(--ui-unit)))` | Dimension / Scale Token |
| `--ui-height` | `max(48px,calc(4.8 * var(--ui-unit)))` | Layout / Spatial Grid Token |
| `--ui-gap` | `calc(1.6 * var(--ui-unit))` | Layout / Spatial Grid Token |
| `--ui-step` | `calc(var(--ui-control) + var(--ui-gap))` | Design System Custom Token |
| `--ui-year-width` | `calc(20 * var(--ui-unit))` | Layout / Spatial Grid Token |
| `--ui-left` | `calc(var(--ui-inset-x) + env(safe-area-inset-left,0px))` | Dimension / Scale Token |
| `--ui-right` | `calc(var(--ui-inset-x) + env(safe-area-inset-right,0px))` | Dimension / Scale Token |
| `--ui-top` | `calc(var(--ui-inset-y) + env(safe-area-inset-top,0px))` | Dimension / Scale Token |
| `--dock-bottom` | `calc(max(32px,var(--ui-inset-y)) + env(safe-area-inset-bottom,0px))` | Dimension / Scale Token |
| `--glass-tint` | `rgba(20,20,20,.34)` | Canvas / Surface Token |
| `--glass-text` | `#f5f7fa` | Typography Ink Token |
| `--glass-muted` | `#c1cad5` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.panneau> — `fromearth-love`)**:
   - Landmark `<header class="panneau">` hosting `fromearth · 2050 — Explore climate p` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r160"`, `data-t="sous1"`, `data-t="sous2"`, `data-t="initialiser"`), and stylesheet rule `font-face { font-family:EarthHerbik;src:url('./fonts/Herbik-MediumItalic.woff2') for... }`.
2. **Hero Stage & Focal Lead (<section.loupe> — `Hello, ·⋅+✧✶ human. ⋮·⋅+✧`)**:
   - Landmark `<section class="loupe">` presenting display lead `Hello, ·⋅+✧✶ human. ⋮·⋅+✧` and copy excerpt *"You ✧✶✺ leave ✺⊹⋮·⋅ a ✶ trace ✧✶✺⊹⋮ on +✧ everything ⋅+✧✶✺⊹⋮·⋅ yo"* over `#f5f7fa` canvas and `#051236` ink.
3. **Primary Showcase & Content Grid (<section.fiche-bilan> — `Select your language`)**:
   - Landmark `<section class="fiche-bilan">` rendering section `Select your language` with copy *"everything ⋅+✧✶✺⊹⋮·⋅"*, asset references (`pixel-earth-animated.png`, `three.module.min.js`, `earth_color_2048.webp`, `earth_mask_4320.webp`), and grid rule `language-dialog::backdrop { background:050606 }`.
4. **Interactive Detail & Feature Matrix (<section.fiche-risques> — `from earth / 2050`)**:
   - Landmark `<section class="fiche-risques">` framing `from earth / 2050` and `The globe could not start` (*"Including ⊹⋮·⋅+✧✶✺ me. ✺⊹⋮ You ✶✺⊹ can ✧✶✺ blame +✧✶✺⊹ the ⋅+✧ co"*) with `#b9bdb6` surface cards, `#051236` accents, and `.language-content { width:min(340px,100%);margin:auto;text-align:center;animation:language-a... }`.
5. **Colophon & Global Directory Footer (<footer.actions> — `http://fromearth.love`)**:
   - Landmark `<footer class="actions">` anchoring `fromearth · 2050 — Explore clima` footer links (`Overview · Index · Archive · About · Contact`), copy *"Including ⊹⋮·⋅+✧✶✺"*, and `#0b2358` structural dividers.
