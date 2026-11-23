---
title: "UI & UX Architecture: mychess-events"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: mychess-events

## Overview & Design Identity
- **Target**: `mychess-events` (**Find Chess Tournaments Worldwide · MyChess.Events**)
- **Production URL**: [https://mychess.events/](https://mychess.events/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#c7c7c7` ink, `#0096ff` accent)
- **Summary**: Find chess tournaments worldwide. Explore FIDE-rated classical, rapid and blitz events, schedules, venues and registration details.
- **Total Clean CSS Variables Extracted**: `263` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Open Sans`
- **Body Font Stack**: `Roboto`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 18px`, `line-height: normal`, `font-weight: 700`); CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: 2em`, `line-height: 1.2`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 30px`, `line-height: 39px`, `font-weight: 600`); rule `,h2` (`font-size: 1.7em`, `line-height: 1.3`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 25.2px`, `font-weight: 400`); rule `p` (`font-size: 20px`, `line-height: 1.65`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 25.2px`, `font-weight: 400`); CSS variables `--ast-blog-meta-weight: 600`, `--rdp-caption-font-size: 18px`; rule `small` (`font-size: 13px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#c7c7c7` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0b0b0b` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0096ff` | `var(--wpem-primary-color)` in `:root` |
| **Secondary / Muted Copy** | `#54595f` | `var(--e-global-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#333647` | `var(--tp-dark-stroke-color)` in `:root` |
| **Variable Token (`--ast-code-block-background`)** | `#eceff3` | `var(--ast-code-block-background)` in `:root` |
| **Variable Token (`--ast-comment-inputs-background`)** | `#f9fafb` | `var(--ast-comment-inputs-background)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ast-post-nav-space` | `0` | Layout / Spatial Grid Token |
| `--ast-container-default-xlg-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--ast-container-default-lg-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--ast-container-default-slg-padding` | `2em` | Layout / Spatial Grid Token |
| `--ast-container-default-md-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--ast-container-default-sm-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--ast-container-default-xs-padding` | `2.4em` | Layout / Spatial Grid Token |
| `--ast-container-default-xxs-padding` | `1.8em` | Layout / Spatial Grid Token |
| `--ast-code-block-background` | `#ECEFF3` | Canvas / Surface Token |
| `--ast-comment-inputs-background` | `#F9FAFB` | Canvas / Surface Token |
| `--ast-normal-container-width` | `1440px` | Layout / Spatial Grid Token |
| `--ast-narrow-container-width` | `750px` | Layout / Spatial Grid Token |
| `--ast-blog-title-font-weight` | `600` | Typography / Scale Token |
| `--ast-blog-meta-weight` | `600` | Design System Custom Token |
| `--ast-global-color-primary` | `var(--ast-global-color-5)` | Brand / Palette Token |
| `--ast-global-color-secondary` | `var(--ast-global-color-4)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `mychess-events`)**:
   - Landmark `<header class="elementor elementor-191">` (`1440x90px`) hosting `Find Chess Tournaments Worldwide · M` navigation (`UPCOMING TOURNAMENTS · MAP · Calendar · PAST · ORGANIZERS`), DOM attributes (`data-noptimize="1"`, `data-cfasync="false"`, `data-wpfc-render="false"`, `data-noptimize="1"`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<article.mced-home-card> — `Manage your data`)**:
   - Landmark `<article class="mced-home-card">` presenting display lead `Manage your data` and copy excerpt *"Find tournaments worldwide"* over `#000000` canvas and `#c7c7c7` ink.
3. **Primary Showcase & Content Grid (<article.mced-home-card:nth(2)> — `Upcoming Featured Events`)**:
   - Landmark `<article class="mced-home-card">` rendering section `Upcoming Featured Events` with copy *"UPCOMING TOURNAMENTS"*, asset references (`show_ads_impl_fy2021.js`, `clarity.js`, `letmeallez.js`, `uwt.js`), and grid rule `progress { display:inline-block;vertical-align:baseline }`.
4. **Interactive Detail & Feature Matrix (<article.mced-home-card:nth(3)> — `FIDE World Junior U20 Championship`)**:
   - Landmark `<article class="mced-home-card">` framing `FIDE World Junior U20 Championships 2026` and `Jordan Aqaba Red Sea Chess Seminar Tournament 2026` (*"SUBMIT A TOURNAMENT"*) with `#0b0b0b` surface cards, `#0096ff` accents, and `a:visited { text-decoration:none }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://mychess.events/`)**:
   - Landmark `<footer class="elementor elementor-317">` anchoring `Find Chess Tournaments Worldwide` footer links (`UPCOMING TOURNAMENTS · MAP · Calendar · PAST · ORGANIZERS`), copy *"EASY SEARCH & FILTERS"*, and `#333647` structural dividers.
