---
title: "UI & UX Architecture: www-vineyard-co-za"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-vineyard-co-za

## Overview & Design Identity
- **Target**: `www-vineyard-co-za` (**The Vineyard Hotel · Hotel & Spa in Newlands, Cape Town**)
- **Production URL**: [https://www.vineyard.co.za/](https://www.vineyard.co.za/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fffefd` canvas, `#151d25` ink, `#185abc` accent)
- **Summary**: Independently owned hotel on Table Mountain's eastern slopes in Newlands. Rooms and apartments, four places to eat, Angsana Spa, two pool...
- **Total Clean CSS Variables Extracted**: `139` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Optima`
- **Body Font Stack**: `Mori`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 11.6667px`, `line-height: 11.6667px`, `font-weight: 400`, `letter-spacing: 0.466667px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 49.1667px`, `line-height: 54.0833px`, `font-weight: 400`, `letter-spacing: -0.491667px`); rule `,h2` (`letter-spacing: calc(var(--size)*-0.01)`)
- **Body Copy**: live computed `body` (`font-size: 13.3333px`, `line-height: 21.3333px`, `font-weight: 400`); rule `p` (`line-height: 180%`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13.3333px`, `line-height: 21.3333px`, `font-weight: 400`); CSS variables `--content-width-small: 44.8rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fffefd` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#151d25` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--adp-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#185abc` | `.rc-2fa-submit-button-holder bu... { background-color: #185abc }` |
| **Secondary / Muted Copy** | `#9c9c9c` | `var(--adp-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#dbdbdb` | `var(--adp-border-color)` in `:root` |
| **Variable Token (`--c-black`)** | `#000000` | `var(--c-black)` in `:root` |
| **Variable Token (`--c-mb-15`)** | `#293a49` | `var(--c-mb-15)` in `:root` |
| **Variable Token (`--c-mb-20`)** | `#41525f` | `var(--c-mb-20)` in `:root` |
| **Variable Token (`--c-mb-30`)** | `#5d7587` | `var(--c-mb-30)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-optima` | `"Optima", sans-serif` | Typography / Scale Token |
| `--font-mori` | `"Mori", sans-serif` | Typography / Scale Token |
| `--container-width` | `140rem` | Layout / Spatial Grid Token |
| `--container-width-s` | `115.6rem` | Layout / Spatial Grid Token |
| `--content-width` | `68.4rem` | Layout / Spatial Grid Token |
| `--content-width-small` | `44.8rem` | Layout / Spatial Grid Token |
| `--container-offset` | `calc((100vw - var(--container-width)) * .5)` | Layout / Spatial Grid Token |
| `--gap` | `1.6rem` | Layout / Spatial Grid Token |
| `--header-height` | `12rem` | Layout / Spatial Grid Token |
| `--header-height-scroll` | `6.4rem` | Layout / Spatial Grid Token |
| `--c-black` | `#000` | Canvas / Surface Token |
| `--c-white` | `#fff` | Canvas / Surface Token |
| `--c-mb-10` | `#151D25` | Color / Atmospheric Token |
| `--c-mb-15` | `#293A49` | Color / Atmospheric Token |
| `--c-mb-20` | `#41525F` | Color / Atmospheric Token |
| `--c-mb-30` | `#5D7587` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-vineyard-co-za`)**:
   - Landmark `<header class="header header-light">` (`1440x100px`) hosting `The Vineyard Hotel · Hotel & Spa in ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-barba="wrapper"`, `data-id="sleep"`, `data-id="eat"`, `data-id="meet"`), and stylesheet rule `root { --swiper-theme-color: 007aff }`.
2. **Hero Stage & Focal Lead (<section.section> — `THE VINEYARD HOTEL, NEWLANDS, CAPE`)**:
   - Landmark `<section class="section section-home-hero">` presenting display lead `THE VINEYARD HOTEL, NEWLANDS, CAPE TOWN` and copy excerpt *"1 Adults, 0 Children"* over `#fffefd` canvas and `#151d25` ink.
3. **Primary Showcase & Content Grid (<section.section-trust> — `The Vineyard Hotel, Newlands, Cape`)**:
   - Landmark `<section class="section section-trust">` rendering section `The Vineyard Hotel, Newlands, Cape Town` with copy *"Remove room Remove room"*, asset references (`public-prod.dineplan.com`, `i.vimeocdn.com`, `mori-regular.woff2`, `mori-medium.woff2`), and grid rule `host { position:relative;display:block;margin-left:auto;margin-right:auto;z-ind... }`.
4. **Interactive Detail & Feature Matrix (<section.section-carousel> — `Reawaken your sense of wonder`)**:
   - Landmark `<section class="section section-carousel">` framing `Reawaken your sense of wonder` and `Best Available Rate` (*"Book Your Stay Book Your Stay"*) with `#ffffff` surface cards, `#185abc` accents, and `.swiper { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.vineyard.co.za/`)**:
   - Landmark `<footer class="footer">` anchoring `The Vineyard Hotel · Hotel & Spa` footer links (`Overview · Index · Archive · About · Contact`), copy *"There is a place, nestled at the foot of Table Mountain, whe"*, and `#dbdbdb` structural dividers.
