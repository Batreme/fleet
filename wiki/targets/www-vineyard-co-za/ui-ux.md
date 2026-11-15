# UI & UX Architecture: www-vineyard-co-za

## Overview & Design Identity
- **Target**: `www-vineyard-co-za` (**The Vineyard Hotel · Hotel & Spa in Newlands, Cape Town**)
- **Production URL**: [https://www.vineyard.co.za/](https://www.vineyard.co.za/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#4a4a4a` ink, `#a2ddf6` accent)
- **Summary**: Independently owned hotel on Table Mountain's eastern slopes in Newlands. Rooms and apartments, four places to eat, Angsana Spa, two pool...
- **Total Clean CSS Variables Extracted**: `139` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Optima`
- **Body Font Stack**: `Mori`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `,h2` (`letter-spacing: calc(var(--size)*-0.01)`)
- **Body Copy**: rule `p` (`line-height: 180%`)
- **Metadata & Labels**: CSS variables `--content-width-small: 44.8rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--adp-background-color)` in `:root` |
| **Primary Typography Ink** | `#f0f0f0` | `var(--adp-background-color-hover)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eaeaea` | `var(--adp-background-color-active)` in `:root` |
| **Interactive Accent / Highlight** | `#a2ddf6` | `var(--adp-background-color-selected-other-month)` in `:root` |
| **Secondary / Muted Copy** | `#4a4a4a` | `var(--adp-color)` in `:root` |
| **Structural Hairline Border** | `#9c9c9c` | `var(--adp-color-secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--adp-font-size` | `14px` | Typography / Scale Token |
| `--adp-width` | `246px` | Layout / Spatial Grid Token |
| `--adp-z-index` | `100` | Elevation / Border Token |
| `--adp-padding` | `4px` | Layout / Spatial Grid Token |
| `--adp-grid-areas` | `"nav" "body" "timepicker" "buttons"` | Layout / Spatial Grid Token |
| `--adp-transition-duration` | `.3s` | Motion / Easing Token |
| `--adp-transition-ease` | `ease-out` | Motion / Easing Token |
| `--adp-transition-offset` | `8px` | Motion / Easing Token |
| `--adp-background-color` | `#fff` | Canvas / Surface Token |
| `--adp-background-color-hover` | `#f0f0f0` | Canvas / Surface Token |
| `--adp-background-color-active` | `#eaeaea` | Canvas / Surface Token |
| `--adp-background-color-in-range` | `rgba(92, 196, 239, .1)` | Canvas / Surface Token |
| `--adp-background-color-in-range-focused` | `rgba(92, 196, 239, .2)` | Canvas / Surface Token |
| `--adp-background-color-selected-other-month` | `#a2ddf6` | Canvas / Surface Token |
| `--adp-color` | `#4a4a4a` | Brand / Palette Token |
| `--adp-color-secondary` | `#9c9c9c` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-vineyard-co-za`)**:
   - Landmark `<header class="header header-light">` hosting `The Vineyard Hotel · Hotel & Spa in ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-barba="wrapper"`, `data-id="sleep"`, `data-id="eat"`, `data-id="meet"`), and stylesheet rule `root { --swiper-theme-color: 007aff }`.
2. **Hero Stage & Focal Lead (<section.section> — `Booking`)**:
   - Landmark `<section class="section section-home-hero">` presenting display lead `Booking` and copy excerpt *"Skip to main content"* over `#fff` canvas and `#4a4a4a` ink.
3. **Primary Showcase & Content Grid (<section.section> — `The Vineyard Hotel, Newlands, Cape`)**:
   - Landmark `<section class="section section-trust">` rendering section `The Vineyard Hotel, Newlands, Cape Town` with copy *"Check-in Date 14 Nov 2026"*, asset references (`public-prod.dineplan.com`, `i.vimeocdn.com`, `mori-regular.woff2`, `mori-medium.woff2`), and grid rule `host { position:relative;display:block;margin-left:auto;margin-right:auto;z-ind... }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Reawaken your sense of wonder`)**:
   - Landmark `<section class="section section-carousel">` framing `Reawaken your sense of wonder` and `Best Available Rate` (*"Check-out Date 15 Nov 2026"*) with `#eaeaea` surface cards, `#a2ddf6` accents, and `.swiper { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.vineyard.co.za/`)**:
   - Landmark `<footer class="footer">` anchoring `The Vineyard Hotel · Hotel & Spa` footer links (`Overview · Index · Archive · About · Contact`), copy *"Remove room Remove room"*, and `#9c9c9c` structural dividers.
