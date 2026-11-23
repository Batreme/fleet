---
title: "UI & UX Architecture: www-davidecarusio-it"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-davidecarusio-it

## Overview & Design Identity
- **Target**: `www-davidecarusio-it` (**Davide Carusio - Web Designer / Webflow Dev**)
- **Production URL**: [https://www.davidecarusio.it/](https://www.davidecarusio.it/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f9efe7` / `#0082f3`)
- **Summary**: Freelance web designer and Webflow expert in Italy. Fast, custom-built websites from design to development for agencies and international...
- **Total Clean CSS Variables Extracted**: `27` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geistmono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 20.8px`, `line-height: 24.96px`, `font-weight: 600`, `letter-spacing: -0.832px`); rule `h1` (`font-size: 38px`, `line-height: 44px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 64px`, `font-weight: 600`, `letter-spacing: -2.56px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 600`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 600`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9efe7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1c1c1b` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e5ccb2` | `var(--tag_bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#73675e` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d9d9d9` | `var(--divider)` in `:root` |
| **Variable Token (`--lighter-black`)** | `#2b2b2b` | `var(--lighter-black)` in `:root` |
| **Variable Token (`--tag_text`)** | `#4b5563` | `var(--tag_text)` in `:root` |
| **Variable Token (`--p_paragraph`)** | `#998a7e` | `var(--p_paragraph)` in `:root` |
| **Variable Token (`--button-043-color`)** | `#ffffff` | `var(--button-043-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--light-bg` | `#f9efe7` | Canvas / Surface Token |
| `--lighter-black` | `#2b2b2b` | Canvas / Surface Token |
| `--dark-bg` | `#1c1c1b` | Canvas / Surface Token |
| `--p_paragraph-darker` | `#73675e` | Canvas / Surface Token |
| `--tag_bg` | `#e5ccb2` | Canvas / Surface Token |
| `--tag_text` | `#4b5563` | Typography Ink Token |
| `--divider` | `#d9d9d9` | Color / Atmospheric Token |
| `--p_paragraph` | `#998a7e` | Typography / Scale Token |
| `--size-unit` | `16` | Layout / Spatial Grid Token |
| `--size-container-ideal` | `1440` | Layout / Spatial Grid Token |
| `--size-container-min` | `1280px` | Layout / Spatial Grid Token |
| `--size-container-max` | `1920px` | Layout / Spatial Grid Token |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container-max))` | Layout / Spatial Grid Token |
| `--button-043-color` | `#fff` | Brand / Palette Token |
| `--button-043-color-background` | `currentColor` | Canvas / Surface Token |
| `--button-043-hover-color-background` | `currentColor` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.underlay-nav__header> — `www-davidecarusio-it`)**:
   - Landmark `<nav class="underlay-nav__header">` (`1425x76px`) hosting `Davide Carusio - Web Designer / Webf` navigation (`davide carusio · Projects · Services · IT · G e t i n t o u c h`), DOM attributes (`data-wf-page="6aabacfa3017369152d1f8b2"`, `data-wf-site="6a3a84272e4493d30711d604"`, `data-theme-nav="light"`, `data-bg-nav="light"`), and stylesheet rule `.w-icon-slider-right:before { content: "\e600"; }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `Websites that work. For agencies a`)**:
   - Landmark `<section class="hero_wrap">` presenting display lead `Websites that work. For agencies and brands who d...` and copy excerpt *"Italy-based photographer. The site focuses on clean design and th"* over `#f9efe7` canvas and `#1c1c1b` ink.
3. **Primary Showcase & Content Grid (<section.sticky-title-wrapper> — `Italy-based photographer. The site`)**:
   - Landmark `<section class="sticky-title-wrapper">` rendering section `Italy-based photographer. The site focuses on cl` with copy *"t h e b e s t p i z z a i s t h e m a r g h e r i t a"*, asset references (`normalize.css`, `webflow.css`, `davidecarusio-it-v3.webflow.css`, `favicon.png`), and grid rule `.w-icon-slider-left:before { content: "\e601"; }`.
4. **Interactive Detail & Feature Matrix (<section.work_wrap> — `t h e b e s t p i z z a i s t h e `)**:
   - Landmark `<section class="work_wrap">` framing `t h e b e s t p i z z a i s t h e m a r g h e r ` and `G e t i n t o u c h` (*"G e t i n t o u c h"*) with `#e5ccb2` surface cards, `#0082f3` accents, and `.w-icon-nav-menu:before { content: "\e602"; }`.
5. **Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.davidecarusio.it/`)**:
   - Landmark `<footer class="footer-wrap">` anchoring `Davide Carusio - Web Designer / ` footer links (`davide carusio · Projects · Services · IT · G e t i n t o u c h`), copy *"Last Updated: 24/09/2026"*, and `#d9d9d9` structural dividers.
