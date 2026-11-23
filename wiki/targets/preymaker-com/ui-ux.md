---
title: "UI & UX Architecture: preymaker-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: preymaker-com

## Overview & Design Identity
- **Target**: `preymaker-com` (**Preymaker**)
- **Production URL**: [https://preymaker.com/](https://preymaker.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#f1f3f5` ink, `#ffffff` accent)
- **Summary**: Preymaker
- **Total Clean CSS Variables Extracted**: `34` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NewGrotesk`
- **Body Font Stack**: `NewGrotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 42px`, `font-weight: 600`, `letter-spacing: -0.8px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 42px`, `font-weight: 600`, `letter-spacing: -0.8px`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: 10px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: 10px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f1f3f5` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#b9c1c8` | `.hero_hero__GgZAX header .hero_... { background: #b9c1c8 }` |
| **Interactive Accent / Highlight** | `#ffffff` | `.media button { color: #ffffff }` |
| **Secondary / Muted Copy** | `#859099` | `_links__dYPZS button .footer_co... { color: #859099 }` |
| **Structural Hairline Border** | `#ffffff` | `Cf1 .blocks_thumbnails__Ag9k4 f... { border-color: #ffffff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--breakpoints-desktop` | `1920` | Design System Custom Token |
| `--breakpoints-tablet` | `1920` | Design System Custom Token |
| `--breakpoints-mobile` | `768` | Design System Custom Token |
| `--sizes-desktop` | `1920` | Layout / Spatial Grid Token |
| `--sizes-tablet` | `1440` | Layout / Spatial Grid Token |
| `--sizes-mobile` | `390` | Layout / Spatial Grid Token |
| `--spacings-xl` | `2rem` | Layout / Spatial Grid Token |
| `--spacings-l` | `1.2rem` | Layout / Spatial Grid Token |
| `--spacings-m` | `0.8rem` | Layout / Spatial Grid Token |
| `--spacings-s` | `0.4rem` | Layout / Spatial Grid Token |
| `--spacings-xs` | `0.2rem` | Layout / Spatial Grid Token |
| `--paddings-xxl` | `24rem` | Layout / Spatial Grid Token |
| `--paddings-xl` | `16rem` | Layout / Spatial Grid Token |
| `--paddings-l` | `10rem` | Layout / Spatial Grid Token |
| `--paddings-m` | `8rem` | Layout / Spatial Grid Token |
| `--paddings-s` | `4rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.menu_header__bK96y> — `preymaker-com`)**:
   - Landmark `<header class="menu_header__bK96y">` (`351x40px`) hosting `Preymaker` navigation (`Preymaker`), DOM attributes (`data-scroll-orientation="vertical"`, `data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `Tw5s_ .blocks_bottom__VwtoR figur... { height:100%;left:0;position:absolute;top:0;width:100% }`.
2. **Hero Stage & Focal Lead (<section.hero_hero__Sbbfz> — `Future-Facing Creators of Exceptio`)**:
   - Landmark `<section class="hero_hero__Sbbfz">` presenting display lead `Future-Facing Creators of Exceptional Visual Content` and copy excerpt *"Into the Wild 60sec"* over `#000000` canvas and `#f1f3f5` ink.
3. **Primary Showcase & Content Grid (<section.sticky_sticky__yNlFf> — `An award-winning creative collecti`)**:
   - Landmark `<section class="sticky_sticky__yNlFf">` rendering section `An award-winning creative collective specializing...` with copy *"Aviators, the film"*, asset references (`aecae019b9172d3b647d798d28fcbf7f8...`, `d2ed2c41a495322ff01622c1c5438d3c4...`, `94387763ebca6d854c48dda1a76ba924b...`, `577cb103f4f05fe570f1f09d872e4a6ad...`), and grid rule `blocks__L_epw .blocks_full_image_... { position:relative;width:100%;height:100svh }`.
4. **Interactive Detail & Feature Matrix (<article.sticky_article__zGMPW> — `W+K NY, Director Rupert Sanders Ma`)**:
   - Landmark `<article class="sticky_article__zGMPW">` framing `W+K NY, Director Rupert Sanders Mark Ford’s F1 Re...` and `Preymaker Welcomes Theuns Van Rensburg and Robert...` (*"Apple Watch Greek God Group Chat"*) with `#b9c1c8` surface cards, `#ffffff` accents, and `pw .blocks_full_image__agSU_ figu... { object-fit:cover;object-position:center }`.
5. **Colophon & Global Directory Footer (<footer.footer_footer__1m2ab> — `https://preymaker.com/`)**:
   - Landmark `<footer class="footer_footer__1m2ab">` anchoring `Preymaker` footer links (`Preymaker`), copy *"Google Tech partner"*, and `#ffffff` structural dividers.
