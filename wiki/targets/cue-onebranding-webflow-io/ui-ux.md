---
title: "UI & UX Architecture: cue-onebranding-webflow-io"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: cue-onebranding-webflow-io

## Overview & Design Identity
- **Target**: `cue-onebranding-webflow-io` (**Cue - Creating Unforgettable Experiences**)
- **Production URL**: [https://cue-onebranding.webflow.io/](https://cue-onebranding.webflow.io/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#13171a` ink, `#0000ff` accent)
- **Summary**: Fan-first technology for premium brands and event experiences. Take your events to the next level with CUE and experience true fan engage...
- **Total Clean CSS Variables Extracted**: `14` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 83.2px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 100px`, `font-weight: 300`); rule `,h2` (`font-size: 2.5rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 300`); rule `p` (`font-size: inherit`, `line-height: inherit`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 300`); CSS variables `--radius--small: .25rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#13171a` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0000ff` | `.styles__nav-link.cc-cta:hover { background-color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#808080` | `.u-text-gray { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--color--aqua`)** | `#3aebdb` | `var(--color--aqua)` in `:root` |
| **Variable Token (`--color--gray`)** | `#f5f5f7` | `var(--color--gray)` in `:root` |
| **Variable Token (`--color--mid-gray`)** | `#e4e5e5` | `var(--color--mid-gray)` in `:root` |
| **Variable Token (`--color--dark-blue`)** | `#030b15` | `var(--color--dark-blue)` in `:root` |
| **Variable Token (`--color--deep-blue`)** | `#010012` | `var(--color--deep-blue)` in `:root` |
| **Variable Token (`--on-light-gradient`)** | `#03b7e8` | `var(--on-light-gradient)` in `:root` |
| **Variable Token (`--on-light-gradient`)** | `#2f68e9` | `var(--on-light-gradient)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color--black` | `#13171a` | Canvas / Surface Token |
| `--color--aqua` | `#3aebdb` | Brand / Palette Token |
| `--color--white` | `white` | Canvas / Surface Token |
| `--radius--small` | `.25rem` | Elevation / Border Token |
| `--color--gray` | `#f5f5f7` | Brand / Palette Token |
| `--color--mid-gray` | `#e4e5e5` | Brand / Palette Token |
| `--color--dark-blue` | `#030b15` | Canvas / Surface Token |
| `--gap--2-5` | `2.5rem` | Layout / Spatial Grid Token |
| `--page-padding` | `0px` | Layout / Spatial Grid Token |
| `--color--deep-blue` | `#010012` | Brand / Palette Token |
| `--radius--main` | `.75rem` | Elevation / Border Token |
| `--on-light-gradient` | `linear-gradient(82deg, #03b7e8 2.55%, #2f68e9 100.58%)` | Canvas / Surface Token |
| `--transition-speed` | `1.5s` | Motion / Easing Token |
| `--speed` | `100s` | Motion / Easing Token |
| `--cue-onebranding--bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--cue-onebranding--ink` | `#13171a` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.section> — `cue-onebranding-webflow-io`)**:
   - Landmark `<header class="section cc-header-centered-gradient">` (`1440x706px`) hosting `Cue - Creating Unforgettable Experie` navigation (`NAB · Ross Video · REQUEST A DEMO · WE ARE CUE`), DOM attributes (`data-wf-domain="cue-onebranding.webfl..."`, `data-wf-page="662871ca1b5c639c39515607"`, `data-wf-site="662871ca1b5c639c39515603"`, `data-cookieconsent="ignore"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Create Unforgettable Experiences`)**:
   - Landmark `<section class="section cc-2col-text-cta">` presenting display lead `Create Unforgettable Experiences` and copy excerpt *"It was a great week at NAB with our friends from Ross Video! Cont"* over `#ffffff` canvas and `#13171a` ink.
3. **Primary Showcase & Content Grid (<section.cc-video-zoom> — `C r e a t e U n f o r g e t t a b `)**:
   - Landmark `<section class="section cc-video-zoom">` rendering section `C r e a t e U n f o r g e t t a b l e E x p e r i...` with copy *"C r e a t e U n f o r g e t t a b l e E x p e r i e n c e s"*, asset references (`cdn.prod.website-files.com`, `cue-onebranding.shared.e83737123....`, `insight.min.js`, `clarity.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.cc-product-starter> — `An experience like no other`)**:
   - Landmark `<section class="section cc-product-starter">` framing `An experience like no other` and `Fanatic Filters` (*"U n f o r g e t t a b l e"*) with `#ffff00` surface cards, `#0000ff` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://cue-onebranding.webflow.io/`)**:
   - Landmark `<footer class="footer">` anchoring `Cue - Creating Unforgettable Exp` footer links (`NAB · Ross Video · REQUEST A DEMO · WE ARE CUE`), copy *"E x p e r i e n c e s"*, and `#e2e2e2` structural dividers.
