---
title: "UI & UX Architecture: macmillan-studio"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: macmillan-studio

## Overview & Design Identity
- **Target**: `macmillan-studio` (**Christian MacMillan · Independent Tech Lead—Developer**)
- **Production URL**: [https://macmillan.studio](https://macmillan.studio)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#808080`)
- **Summary**: Over a decade of experience implementing fully custom, high-quality interactive experiences for global agencies and brands.
- **Total Clean CSS Variables Extracted**: `32` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `HelveticaNowDisplayMedium`
- **Body Font Stack**: `HelveticaNowDisplayBold`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 10px`, `line-height: 10px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 52px`, `line-height: 56px`, `font-weight: 700`, `letter-spacing: -0.875px`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: 10px`, `font-weight: 400`); rule `p` (`font-size: max(4vw,1.5rem)`, `line-height: max(4.8vw,1.8rem)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: 10px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#808080` | `.home__services__service__conte... { background-color: grey }` (`#808080`) |
| **Interactive Accent / Highlight** | `#808080` | `home__projects__buttons__button... { color: grey }` (`#808080`) |
| **Secondary / Muted Copy** | `#808080` | `ome__projects__project__collabo... { color: grey }` (`#808080`) |
| **Structural Hairline Border** | `#ffff00` | `.home__projects__videos video { border: #ffff00 }` |
| **Variable Token (`--lime`)** | `#bdff00` | `var(--lime)` in `:root` |
| **Variable Token (`--light-grey`)** | `#d3d6da` | `var(--light-grey)` in `:root` |
| **Variable Token (`--dark-grey`)** | `#818388` | `var(--dark-grey)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#000` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--lime` | `#bdff00` | Color / Atmospheric Token |
| `--light-grey` | `#d3d6da` | Canvas / Surface Token |
| `--dark-grey` | `#818388` | Canvas / Surface Token |
| `--layout-max-width` | `1800px` | Layout / Spatial Grid Token |
| `--layout-columns` | `8` | Layout / Spatial Grid Token |
| `--layout-margin` | `1.6rem` | Layout / Spatial Grid Token |
| `--layout-gutter` | `.8rem` | Layout / Spatial Grid Token |
| `--layout-column-width` | `calc(var(--layout-width)/var(--layout-columns))` | Layout / Spatial Grid Token |
| `--col` | `33.3333%` | Layout / Spatial Grid Token |
| `--columns` | `4` | Layout / Spatial Grid Token |
| `--columns-width` | `calc((var(--columns)/var(--layout-columns))*100%)` | Layout / Spatial Grid Token |
| `--columns-gap-width` | `calc(var(--layout-gutter)*(1 - 1/(var(--layout-columns)/var(--columns))))` | Layout / Spatial Grid Token |
| `--gap` | `2` | Layout / Spatial Grid Token |
| `--gap-width` | `calc((var(--gap)/var(--layout-columns))*100%)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `macmillan-studio`)**:
   - Landmark `<header class="header">` (`1440x49px`) hosting `Christian MacMillan · Independent Te` navigation (`Projects, · Services, · About`), DOM attributes (`data-tab-fixed`, `data-v-7d7b041a`, `data-scroll-target-top`, `data-scroll-continuous`), and stylesheet rule `.accordion { border-bottom:.2rem solid 000;position:relative }`.
2. **Hero Stage & Focal Lead (<section.home__hero> — `MacMillan Studio—Independent Devel`)**:
   - Landmark `<section class="home__hero">` presenting display lead `MacMillan Studio—Independent Development Studio l...` and copy excerpt *"Independent Tech Lead—Developer"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.home__hero:nth(2)> — `Joining your team as a freelancer `)**:
   - Landmark `<section class="home__hero">` rendering section `Joining your team as a freelancer or taking on th...` with copy *"Over a decade of experience implementing fully custom, high-quali"*, asset references (`entry.CkIT_B6y.css`, `default.Kg7iOwm3.css`, `Pause.BHNIHZ0n.css`, `_slug_.DfTMbnN4.css`), and grid rule `.accordion--first { border-top:.2rem solid 000 }`.
4. **Interactive Detail & Feature Matrix (<section.home__hero:nth(3)> — `Installations`)**:
   - Landmark `<section class="home__hero">` framing `Installations` and `Site Maintainance` (*"Joining your team as a freelancer or taking on the project indepe"*) with `#808080` surface cards, `#808080` accents, and `.accordion__title { align-items:center;border:none;display:flex;height:min(10.6666666667vw,1... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://macmillan.studio`)**:
   - Landmark `<footer class="footer">` anchoring `Christian MacMillan · Independen` footer links (`Projects, · Services, · About`), copy *"From large-scale websites to creative campaign landing pages"*, and `#ffff00` structural dividers.
