---
title: "UI & UX Architecture: productionportugal-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: productionportugal-com

## Overview & Design Identity
- **Target**: `productionportugal-com` (**Production Portugal: Your trusted film production company in Portugal an...**)
- **Production URL**: [https://productionportugal.com/](https://productionportugal.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0063`)
- **Summary**: Dive into cinematic excellence with expert location scouting. Explore possibilities with Production Portugal - Your Trusted film producti...
- **Total Clean CSS Variables Extracted**: `24` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Grotesk Display Pro`
- **Body Font Stack**: `Neue Haas Grotesk Display Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96px`, `line-height: 81.6px`, `font-weight: 700`, `letter-spacing: -2.88px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 11.52px`, `font-weight: 700`, `letter-spacing: -0.36px`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 11.52px`, `font-weight: 700`, `letter-spacing: -0.36px`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff0080` | `var(--base-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0063` | `var(--_colours---brand)` in `:root` |
| **Secondary / Muted Copy** | `#7f7f7f` | `.switcher__button { color: #7f7f7f }` |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--_colours---color--grey--grey-100`)** | `#6b6d79` | `var(--_colours---color--grey--grey-100)` in `:root` |
| **Variable Token (`--home__about__links-edge`)** | `#ff1972` | `var(--home__about__links-edge)` in `:root` |
| **Variable Token (`--blob-1`)** | `#ff126f` | `var(--blob-1)` in `:root` |
| **Variable Token (`--blob-2`)** | `#a3003f` | `var(--blob-2)` in `:root` |
| **Variable Token (`--vignette`)** | `#590224` | `var(--vignette)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_colours---color--grey--grey-100` | `#6b6d79` | Brand / Palette Token |
| `--home__about__links-edge` | `#ff1972` | Typography Ink Token |
| `--_colours---brand` | `#ff0063` | Brand / Palette Token |
| `--psp-intro-height` | `100vh` | Layout / Spatial Grid Token |
| `--psp-stage-height` | `var(--psp-viewport-height, 100dvh)` | Layout / Spatial Grid Token |
| `--psp-stage-bottom-inset` | `0px` | Dimension / Scale Token |
| `--psp-viewport-height` | `100vh` | Layout / Spatial Grid Token |
| `--base-bg` | `#ff0080` | Canvas / Surface Token |
| `--blob-1` | `#ff126f` | Color / Atmospheric Token |
| `--blob-2` | `#a3003f` | Color / Atmospheric Token |
| `--vignette` | `#590224d9` | Color / Atmospheric Token |
| `--sec-bg` | `#00000005` | Canvas / Surface Token |
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--home-hero-project-progress` | `0%` | Dimension / Scale Token |
| `--home-brands-project-progress` | `0%` | Brand / Palette Token |
| `--psp-hover-x` | `0px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `productionportugal-com`)**:
   - Landmark `<header class="header">` (`1440x55px`) hosting `Production Portugal: Your trusted fi` navigation (`[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`), DOM attributes (`data-wf-domain="productionportugal.com"`, `data-wf-page="69f205b2a0439779a1d74754"`, `data-wf-site="69f205b0a0439779a1d746f7"`, `data-home-intro-title="Minute Maid"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.home__hero> — `Production Portugal: Your trusted `)**:
   - Landmark `<section class="home__hero">` presenting display lead `Production Portugal: Your trusted film productio` and copy excerpt *"At PSP Production, every project is guided by senior executive pr"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.home__about> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="home__about">` rendering section `Featured Work & Interactive Showcase` with copy *"Hinge Can't Believe We Met on Hinge"*, asset references (`cdn.prod.website-files.com`, `psp-6eb01f.webflow.shared.c80d7d9...`, `6a68884496439a79375f31d1_PSP-Logo...`, `6a688844292fe50b266154c7_PSP-Logo...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.home__brands> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="home__brands">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Xfinity - We Love To Update"*) with `#ff0080` surface cards, `#ff0063` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://productionportugal.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Production Portugal: Your truste` footer links (`[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`), copy *"Volkswagen Abt E-Line"*, and `#3898ec` structural dividers.
