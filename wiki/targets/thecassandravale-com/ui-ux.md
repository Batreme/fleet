# UI & UX Architecture: thecassandravale-com

## Overview & Design Identity
- **Target**: `thecassandravale-com` (**Cassandra Vale · Fashion, Stories & Branded Content**)
- **Production URL**: [https://thecassandravale.com/](https://thecassandravale.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#131313` ink, `#bb3a4e` accent)
- **Summary**: Cassandra Vale brings together fashion, short-form stories, editorial imagery and branded collaborations.
- **Total Clean CSS Variables Extracted**: `42` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Monument`
- **Body Font Stack**: `ffffff`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 35px`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 45px!important`, `line-height: 51px!important`)
- **Body Copy**: CSS variables `--nectar-body-line-height: 29px`, `--nectar-body-font-size: 16px`; rule `p` (`font-size: 16px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 15px`, `letter-spacing: 2px`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--nectar-accent-color)` in `:root` |
| **Primary Typography Ink** | `#131313` | `var(--nectar-extra-color-1)` in `:root` |
| **Elevated Surface / Card Substrate** | `#bf7741` | `var(--nectar-extra-color-2)` in `:root` |
| **Interactive Accent / Highlight** | `#bb3a4e` | `var(--nectar-extra-color-3)` in `:root` |
| **Secondary / Muted Copy** | `#f0f0f1` | `#wpadminbar>#wp-toolbar span.no... { color: #f0f0f1 }` |
| **Structural Hairline Border** | `#2c3338` | `#wpadminbar .shortlink-input { background: #2c3338 }` |
| **Variable Token (`--nectar-extra-color-gradient-1`)** | `#ff1053` | `var(--nectar-extra-color-gradient-1)` in `:root` |
| **Variable Token (`--nectar-extra-color-gradient-1`)** | `#3452ff` | `var(--nectar-extra-color-gradient-1)` in `:root` |
| **Variable Token (`--nectar-extra-color-gradient-2`)** | `#32d6ff` | `var(--nectar-extra-color-gradient-2)` in `:root` |
| **Variable Token (`--nectar-extra-color-gradient-2`)** | `#2AC4EA` | `var(--nectar-extra-color-gradient-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-admin--admin-bar--height` | `32px` | Layout / Spatial Grid Token |
| `--mobile-container-width` | `88%` | Layout / Spatial Grid Token |
| `--nectar-extra-color-gradient-1` | `linear-gradient(to right,#ff1053,#3452ff)` | Brand / Palette Token |
| `--nectar-extra-color-gradient-2` | `linear-gradient(to right,#32d6ff,#2AC4EA)` | Brand / Palette Token |
| `--nectar-accent-color` | `#ffffff` | Brand / Palette Token |
| `--nectar-extra-color-1` | `#131313` | Brand / Palette Token |
| `--nectar-extra-color-2` | `#bf7741` | Brand / Palette Token |
| `--nectar-extra-color-3` | `#bb3a4e` | Brand / Palette Token |
| `--nectar-bg-color` | `#131313` | Canvas / Surface Token |
| `--nectar-font-color` | `#ffffff` | Brand / Palette Token |
| `--nectar-font-light-color` | `#ffffff` | Canvas / Surface Token |
| `--header-nav-height` | `49px` | Layout / Spatial Grid Token |
| `--nectar-menu-padding` | `10px` | Brand / Palette Token |
| `--nectar-menu-item-spacing` | `10px` | Brand / Palette Token |
| `--nectar-ocm-icon-width` | `22px` | Brand / Palette Token |
| `--nectar-border-thickness` | `2px` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.js> — `thecassandravale-com`)**:
   - Landmark `<header class="js">` hosting `Cassandra Vale · Fashion, Stories & ` navigation (`Skip to main content`), DOM attributes (`data-pagespeed-no-defer`, `data-nowprocket`, `data-wpacu-skip`, `data-no-optimize`), and stylesheet rule `html { --wp-admin--admin-bar--height:32px;scroll-padding-top:var(--wp-admin--ad... }`.
2. **Hero Stage & Focal Lead (<div.lenis> — `INSTAGRAM`)**:
   - Landmark `<div class="lenis">` presenting display lead `INSTAGRAM` and copy excerpt *"Skip to main content"* over `#ffffff` canvas and `#131313` ink.
3. **Primary Showcase & Content Grid (<div.home> — `her world`)**:
   - Landmark `<div class="home">` rendering section `her world` with copy *"SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEVER MAKES A BETTER"*, asset references (`embed`, `icomoon.woff`, `HERO5_OPT-1024x768.jpg`, `HERO5_OPT.jpg`), and grid rule `wpadminbar .ab-empty-item { cursor:default }`.
4. **Interactive Detail & Feature Matrix (<div.wp-singular> — `Too loud`)**:
   - Landmark `<div class="wp-singular">` framing `Too loud` and `to stay still` (*"TO MAKE IT WORTH SHOWING UP FOR."*) with `#bf7741` surface cards, `#bb3a4e` accents, and `wp-toolbar span.noticon { color:f0f0f1 }`.
5. **Colophon & Global Directory Footer (<footer.page-template-default> — `https://thecassandravale.com/`)**:
   - Landmark `<footer class="page-template-default">` anchoring `Cassandra Vale · Fashion, Storie` footer links (`Skip to main content`), copy *"ARTEM MARKOVSKY / ARCR"*, and `#2c3338` structural dividers.
