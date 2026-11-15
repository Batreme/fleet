# UI & UX Architecture: seemecreative-com

## Overview & Design Identity
- **Target**: `seemecreative-com` (**SEE ME Creative**)
- **Production URL**: [https://seemecreative.com/](https://seemecreative.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f7f7` canvas, `#000` ink, `#333` accent)
- **Summary**: SEE ME emerged from the desire to forge a creative environment that reimagines the ways in which we tell, create, and share stories.
- **Total Clean CSS Variables Extracted**: `26` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ABC Favorit`
- **Body Font Stack**: `ABC Favorit Mono`
- **Monospace / Technical Font Stack**: `ABC Favorit Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `25px`, `10px`, `20px`, `32px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `25px`, `10px`, `20px`, `32px`)
- **Body Copy**: rule `p` (`font-size: 18px`, `line-height: 130%`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--unit-margin-small: 10px`, `--unit-max-width-small: 680px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f7f7` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b2b2b2` | `var(--color-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#333` | `var(--color-charcoal)` in `:root` |
| **Secondary / Muted Copy** | `#ff5600` | `var(--color-orange)` in `:root` |
| **Structural Hairline Border** | `#00a9ff` | `var(--color-orange-inverse)` in `:root` |
| **Variable Token (`--color-off-white`)** | `#f9f3f2` | `var(--color-off-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-white` | `#f8f7f7` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-gray` | `#b2b2b2` | Brand / Palette Token |
| `--color-charcoal` | `#333` | Brand / Palette Token |
| `--color-orange` | `#ff5600` | Brand / Palette Token |
| `--color-orange-inverse` | `#00a9ff` | Brand / Palette Token |
| `--color-off-white` | `#f9f3f2` | Canvas / Surface Token |
| `--color-white-inverse` | `#f8f7f7` | Canvas / Surface Token |
| `--unit-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--unit-gap` | `25px` | Layout / Spatial Grid Token |
| `--unit-max-width` | `1800px` | Layout / Spatial Grid Token |
| `--unit-header-height` | `66px` | Layout / Spatial Grid Token |
| `--font-primary` | `"ABC Favorit",sans-serif` | Brand / Palette Token |
| `--font-secondary` | `"Cardinal Fruit Web",serif` | Brand / Palette Token |
| `--font-tertiary` | `"ABC Favorit Mono",monospace` | Typography / Scale Token |
| `--easing-motion` | `cubic-bezier(0.4,0,0.2,1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.global-header> — `seemecreative-com`)**:
   - Landmark `<header class="global-header header">` hosting `SEE ME Creative` navigation (`001 Work · 002 Artists · 003 About · 004 News`), DOM attributes (`data-capo`, `data-v-344bacdf`, `data-v-bd05448e`, `data-v-61c5c60e`), and stylesheet rule `.tag { color:var(--color-charcoal);font-size:10px;font-weight:400;line-height:201% }`.
2. **Hero Stage & Focal Lead (<section.page> — `SEE ME Creative`)**:
   - Landmark `<section class="page page-home">` presenting display lead `SEE ME Creative` and copy excerpt *"MIKE & Wiki Patta x Tommy Hilfiger ✛"* over `#f8f7f7` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.page> — `Where your vision goes to grow`)**:
   - Landmark `<section class="page page-home">` rendering section `Where your vision goes to grow` with copy *"Integrated Campaign Prose ✛"*, asset references (`entry.BKkY1yHX.css`, `wp-image.abO9u4pg.css`, `grid-work.Dsp1qX9O.css`, `grid-masonry.BnNvLTuH.css`), and grid rule `.tag:after { color:var(--color-charcoal) }`.
4. **Interactive Detail & Feature Matrix (<section.page> — `WE ARE A FULL-SERVICE CREATIVE AGE`)**:
   - Landmark `<section class="page page-home">` framing `WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO...` and `「 WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING...` (*"Kids These Days i-D ✛"*) with `#b2b2b2` surface cards, `#333` accents, and `.media { transition:filter .4s var(--easing-motion) }`.
5. **Colophon & Global Directory Footer (<footer.wp-seo> — `https://seemecreative.com/`)**:
   - Landmark `<footer class="wp-seo">` anchoring `SEE ME Creative` footer links (`001 Work · 002 Artists · 003 About · 004 News`), copy *"Localized Campaign Bumble ✛"*, and `#00a9ff` structural dividers.
