---
title: "UI & UX Architecture: www-oregonoutdooralliance-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-oregonoutdooralliance-org

## Overview & Design Identity
- **Target**: `www-oregonoutdooralliance-org` (**Oregon Outdoor Alliance · Growing Oregon’s Outdoor Industry**)
- **Production URL**: [https://www.oregonoutdooralliance.org/](https://www.oregonoutdooralliance.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#efeeee` canvas, `#616161` ink, `#0082f3` accent)
- **Summary**: Connect with Oregon’s outdoor community. Explore events, resources, and partnerships that help outdoor brands and leaders grow and thrive.
- **Total Clean CSS Variables Extracted**: `234` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Ibmplexmono`
- **Body Font Stack**: `Manrope Variablefont Wght`
- **Monospace / Technical Font Stack**: `Ibmplexmono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`, `letter-spacing: -0.144px`); CSS variables `--_typography---font-size--display: var(--size--7rem)`, `--_typography---font-size--h1: var(--size--5rem)`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 81.6px`, `font-weight: 600`, `letter-spacing: -2.4px`); CSS variables `--_typography---font-size--h2: var(--size--4rem)`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--ez-body-lock-z-index: 2147483600`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--radius--small: .375rem`, `--container--small: 66.25rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#efeeee` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#616161` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#eeeeee` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `var(--ez-banner-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--swatch--light-200)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--dark-400)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--1-5)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-regular)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--0em)` | Typography Ink Token |
| `--_theme---heading` | `var(--swatch--dark-800)` | Typography Ink Token |
| `--_text-style---margin-top` | `var(--_spacing---space--4)` | Typography Ink Token |
| `--_text-style---margin-bottom` | `var(--_spacing---space--4)` | Typography Ink Token |
| `--_spacing---space--6` | `var(--size--2-5rem)` | Layout / Spatial Grid Token |
| `--_spacing---space--7` | `var(--size--3rem)` | Layout / Spatial Grid Token |
| `--swatch--brand` | `var(--swatch--brand-base)` | Brand / Palette Token |
| `--radius--small` | `.375rem` | Elevation / Border Token |
| `--container--main` | `90rem` | Layout / Spatial Grid Token |
| `--container--small` | `66.25rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav_desktop_layout> — `www-oregonoutdooralliance-org`)**:
   - Landmark `<nav class="nav_desktop_layout u-position-relative">` (`1076x64px`) hosting `Oregon Outdoor Alliance · Growing Or` navigation (`Connect · Events · Brand Members · Sponsorship · Cultivate`), DOM attributes (`data-wf-domain="www.oregonoutdooralli..."`, `data-wf-page="68029c5c43248225ae283f85"`, `data-wf-site="68029c5c43248225ae283f91"`, `data-delay="0"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.page_hero> — `OREGON’S OUTDOOR BUSINESS ALLIANCE`)**:
   - Landmark `<section class="page_hero u-position-relative">` presenting display lead `OREGON’S OUTDOOR BUSINESS ALLIANCE` and copy excerpt *"Join the Oregon Outdoor Alliance today!"* over `#efeeee` canvas and `#616161` ink.
3. **Primary Showcase & Content Grid (<section.page_wrap> — `Oregon’s Outdoor Business Alliance`)**:
   - Landmark `<section class="page_wrap">` rendering section `Oregon’s Outdoor Business Alliance` with copy *"The Southern Oregon Panel: Enhancing the Outdoor Recreation Econo"*, asset references (`cdn.prod.website-files.com`, `261-ooa.webflow.shared.d47e507e6.css`, `437a9f0a-aec5-11f0-9d68-0bd0c0028851`, `gtm.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.page_code_wrap> — `Connection. Cultivation. Business `)**:
   - Landmark `<section class="page_code_wrap">` framing `Connection. Cultivation. Business Growth.` and `Join the Oregon Outdoor Alliance` (*"O r e g o n O u t d o o r A l l i a n c e u n i t e s i n d i v i"*) with `#ffffff` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.oregonoutdooralliance.org/`)**:
   - Landmark `<footer class="footer_wrap u-overflow-hidden">` anchoring `Oregon Outdoor Alliance · Growin` footer links (`Connect · Events · Brand Members · Sponsorship · Cultivate`), copy *"Be part of an extensive member directory that helps you find"*, and `#ffffff` structural dividers.
