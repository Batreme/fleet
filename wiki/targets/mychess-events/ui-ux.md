# UI & UX Architecture: mychess-events

## Overview & Design Identity
- **Target**: `mychess-events` (**Find Chess Tournaments Worldwide · MyChess.Events**)
- **Production URL**: [https://mychess.events/](https://mychess.events/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#0096ff` canvas, `#ffffff` ink, `#ffffff` accent)
- **Summary**: Find chess tournaments worldwide. Explore FIDE-rated classical, rapid and blitz events, schedules, venues and registration details.
- **Total Clean CSS Variables Extracted**: `268` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roboto`
- **Body Font Stack**: `Roboto Condensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: 2em`, `line-height: 1.2`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: 1.7em`, `line-height: 1.3`)
- **Body Copy**: rule `p` (`font-size: 14px`)
- **Metadata & Labels**: CSS variables `--ast-blog-meta-weight: 600`, `--srfm-color-input-label: var(--ast-global-color-2)`, `--rdp-caption-font-size: 18px`; rule `small` (`font-size: 13px`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0096ff` | `var(--wpem-primary-color)` in `:root` |
| **Primary Typography Ink** | `#111111` | `var(--wpem-dark-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#555555` | `var(--wpem-gray-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `var(--wpem-white-color)` in `:root` |
| **Secondary / Muted Copy** | `#e4e4e4` | `var(--wpem-gray-border-color)` in `:root` |
| **Structural Hairline Border** | `#f5f5f5` | `var(--wpem-gray-bg-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wpem-primary-color` | `#0096ff` | Brand / Palette Token |
| `--wpem-dark-color` | `#111111` | Canvas / Surface Token |
| `--wpem-gray-color` | `#555555` | Brand / Palette Token |
| `--wpem-white-color` | `#ffffff` | Canvas / Surface Token |
| `--wpem-gray-border-color` | `#e4e4e4` | Brand / Palette Token |
| `--wpem-gray-bg-color` | `#f5f5f5` | Canvas / Surface Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--justify-content` | `initial` | Design System Custom Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `mychess-events`)**:
   - Landmark `<header class="elementor elementor-191">` hosting `Find Chess Tournaments Worldwide · M` navigation (`UPCOMING TOURNAMENTS · MAP · Calendar · PAST · ORGANIZERS`), DOM attributes (`data-noptimize="1"`, `data-cfasync="false"`, `data-wpfc-render="false"`, `data-noptimize="1"`), and stylesheet rule `.chosen-container a { cursor:pointer }`.
2. **Hero Stage & Focal Lead (<section.mced-home-events> — `FIDE-RATED EVENTS`)**:
   - Landmark `<section class="mced-home-events">` presenting display lead `FIDE-RATED EVENTS` and copy excerpt *"info@mychess.events"* over `#0096ff` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.mced-home-card> — `EASY SEARCH & FILTERS`)**:
   - Landmark `<article class="mced-home-card">` rendering section `EASY SEARCH & FILTERS` with copy *"UPCOMING TOURNAMENTS"*, asset references (`clarity.js`, `show_ads_impl_fy2021.js`, `letmeallez.js`, `uwt.js`), and grid rule `chosen-container-single .chosen-d... { color:999 }`.
4. **Interactive Detail & Feature Matrix (<article.mced-home-card> — `DETAILED INFORMATION`)**:
   - Landmark `<article class="mced-home-card">` framing `DETAILED INFORMATION` and `FOR PLAYERS & ORGANIZERS` (*"SUBMIT A TOURNAMENT"*) with `#555555` surface cards, `#ffffff` accents, and `en-container-single .chosen-singl... { display:block;overflow:hidden;margin-right:26px;text-overflow:ellipsis;w... }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://mychess.events/`)**:
   - Landmark `<footer class="elementor elementor-317">` anchoring `Find Chess Tournaments Worldwide` footer links (`UPCOMING TOURNAMENTS · MAP · Calendar · PAST · ORGANIZERS`), copy *"BROWSE UPCOMING TOURNAMENTS"*, and `#f5f5f5` structural dividers.
