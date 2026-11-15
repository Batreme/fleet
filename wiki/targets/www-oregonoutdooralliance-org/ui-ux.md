# UI & UX Architecture: www-oregonoutdooralliance-org

## Overview & Design Identity
- **Target**: `www-oregonoutdooralliance-org` (**Oregon Outdoor Alliance · Growing Oregon’s Outdoor Industry**)
- **Production URL**: [https://www.oregonoutdooralliance.org/](https://www.oregonoutdooralliance.org/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#ba4722` canvas, `#fff` ink, `#242a37` accent)
- **Summary**: Connect with Oregon’s outdoor community. Explore events, resources, and partnerships that help outdoor brands and leaders grow and thrive.
- **Total Clean CSS Variables Extracted**: `233` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Worksans Variablefont Wght`
- **Body Font Stack**: `Manrope Variablefont Wght`
- **Monospace / Technical Font Stack**: `Ibmplexmono`
- **Hero Display (`H1`)**: CSS variables `--_typography---font-size--display: var(--size--7rem)`, `--_typography---font-size--h1: var(--size--5rem)`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: CSS variables `--_typography---font-size--h2: var(--size--4rem)`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: CSS variables `--ez-body-lock-z-index: 2147483600`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--radius--small: .375rem`, `--container--small: 66.25rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ba4722` | `var(--swatch--brand-dark)` in `:root` |
| **Primary Typography Ink** | `#efeeee` | `var(--swatch--light-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--swatch--white)` in `:root` |
| **Interactive Accent / Highlight** | `#242a37` | `var(--swatch--neutral-dark-100)` in `:root` |
| **Secondary / Muted Copy** | `#de6e4a` | `var(--swatch--brand-base)` in `:root` |
| **Structural Hairline Border** | `#101319` | `var(--swatch--dark-900)` in `:root` |

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
   - Landmark `<nav class="nav_desktop_layout u-position-relative">` hosting `Oregon Outdoor Alliance · Growing Or` navigation (`Connect · Events · Brand Members · Sponsorship · Cultivate`), DOM attributes (`data-wf-domain="www.oregonoutdooralli..."`, `data-wf-page="68029c5c43248225ae283f85"`, `data-wf-site="68029c5c43248225ae283f91"`, `data-delay="0"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.page_hero> — `Oregon’s Outdoor Business Alliance`)**:
   - Landmark `<section class="page_hero u-position-relative">` presenting display lead `Oregon’s Outdoor Business Alliance` and copy excerpt *"Skip to main content"* over `#ba4722` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.page_wrap> — `Connection. Cultivation. Business `)**:
   - Landmark `<section class="page_wrap">` rendering section `Connection. Cultivation. Business Growth.` with copy *"Connect Connect Events Brand Members Sponsorship"*, asset references (`cdn.prod.website-files.com`, `261-ooa.webflow.shared.517ddcbf1.css`, `437a9f0a-aec5-11f0-9d68-0bd0c0028851`, `gtm.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.page_code_wrap> — `Who We Are`)**:
   - Landmark `<section class="page_code_wrap">` framing `Who We Are` and `Join the Oregon Outdoor Alliance` (*"Cultivate Cultivate Chapters Blog Job Board"*) with `#fff` surface cards, `#242a37` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.oregonoutdooralliance.org/`)**:
   - Landmark `<footer class="footer_wrap u-overflow-hidden">` anchoring `Oregon Outdoor Alliance · Growin` footer links (`Connect · Events · Brand Members · Sponsorship · Cultivate`), copy *"About Us About Us Our Team Our History Contact Us"*, and `#101319` structural dividers.
