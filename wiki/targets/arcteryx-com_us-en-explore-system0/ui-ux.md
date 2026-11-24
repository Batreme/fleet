---
title: "UI & UX Architecture: arcteryx-com_us-en-explore-system0"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: arcteryx-com_us-en-explore-system0

## Overview & Design Identity
- **Target**: `arcteryx-com_us-en-explore-system0` (**System 0 · Arc’teryx**)
- **Production URL**: [https://arcteryx.com/us/en/explore/system0](https://arcteryx.com/us/en/explore/system0)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×5796px`, Mobile `390×872px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0c0c0c` canvas, `#fdfdfd` ink, `#1883fd` accent)
- **Summary**: System 0 is the Arc’teryx platform linking our products, services, and guest experience together in a committed, synchronized journey tow...
- **Total Clean CSS Variables Extracted**: `245` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Elan ITC Pro`
- **Body Font Stack**: `Elan ITC Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 40px`, `font-weight: 400`, `letter-spacing: 0.4px`); CSS variables `--font-helvetica-now-display: "Helvetica Now Display", helvetica, sans-serif`, `--type-font-size-display-1: 34px`, `--type-font-size-display-2: 20px`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 22px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.4px`); rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--type-font-size-body-1: 18px`, `--type-font-size-body-2: 14px`, `--type-line-height-body-1: 22px`; rule `,p` (`line-height: inherit`, `letter-spacing: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--type-letter-spacing-display-1: .4px`, `--type-letter-spacing-display-2: .4px`, `--type-letter-spacing-body-1: .25px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0c0c0c` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fdfdfd` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2c6415` | `#ot-sdk-btn.optanon-show-settin... { background-color: #2c6415 }` |
| **Interactive Accent / Highlight** | `#1883fd` | `#onetrust-pc-sdk #ot-pc-desc a:... { color: #1883fd }` |
| **Secondary / Muted Copy** | `#1f96db` | `-banner-sdk .onetrust-vendors-l... { color: #1f96db }` |
| **Structural Hairline Border** | `#57665a` | `#ot-sdk-btn.optanon-show-settin... { border: #57665a }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dot-overlap-offset-horizontal` | `12px` | Dimension / Scale Token |
| `--dot-overlap-offset-vertical` | `14px` | Dimension / Scale Token |
| `--dot-overlap-offset-relative` | `calc( var(--dot-overlap-offset-horizontal) + .5% )` | Dimension / Scale Token |
| `--circle-size` | `var(--button-circle-small-size)` | Layout / Spatial Grid Token |
| `--circle-border-opacity` | `1` | Elevation / Border Token |
| `--circle-border-interact` | `.2` | Elevation / Border Token |
| `--circle-content-opacity` | `1` | Design System Custom Token |
| `--circle-content-interact` | `1` | Design System Custom Token |
| `--pill-background` | `rgb(26, 26, 26)` | Canvas / Surface Token |
| `--pill-color` | `rgb(253, 253, 253)` | Brand / Palette Token |
| `--pill-background-active` | `rgb(212, 212, 212)` | Canvas / Surface Token |
| `--pill-color-active` | `rgb(12, 12, 12)` | Brand / Palette Token |
| `--pill-background-hover` | `rgb(253, 253, 253)` | Canvas / Surface Token |
| `--pill-color-hover` | `rgb(12, 12, 12)` | Brand / Palette Token |
| `--pill-background-disabled` | `rgb(253, 253, 253)` | Canvas / Surface Token |
| `--pill-color-disabled` | `rgb(212, 212, 212)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.onetrust-pc-dark-filter> — `arcteryx-com_us-en-explore-system0`)**:
   - Landmark `<header class="onetrust-pc-dark-filter">` (`1440x208px`) hosting `System 0 · Arc’teryx` navigation (`PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`), DOM attributes (`data-signup-tag="4467"`, `data-is-header-visible="true"`, `data-id="D15L1J3C77UCOE1UF3N0"`, `data-document-language="true"`), and stylesheet rule `._container_ybue0_1 { display:grid;width:100% }`.
2. **Hero Stage & Focal Lead (<section.ot-hide> — `THE REVOLUTION IS CIRCULAR`)**:
   - Landmark `<section class="ot-hide">` presenting display lead `THE REVOLUTION IS CIRCULAR` and copy excerpt *"TO CREATE AN ENDURING SYSTEM,SOMETIMES YOU HAVE TO BREAK IT ALL D"* over `#0c0c0c` canvas and `#fdfdfd` ink.
3. **Primary Showcase & Content Grid (<section.ot-fade-in> — `The Revolution is Circular`)**:
   - Landmark `<section class="ot-fade-in">` rendering section `The Revolution is Circular` with copy *"To create an enduring system, Sometimes you have to break it all "*, asset references (`identify_f7846436.js`, `amzn.js`, `main.MTUyMzg1YjAxMQ.js`, `0.8.77`), and grid rule `._asset_ybue0_9 { opacity:0;transition:opacity .2s cubic-bezier(.42,0,.58,1) }`.
4. **Interactive Detail & Feature Matrix (<section.otFloatingRoundedCorner> — `Find preferred materials`)**:
   - Landmark `<section class="otFloatingRoundedCorner">` framing `Find preferred materials` and `Design for durability` (*"To create an enduring system,"*) with `#2c6415` surface cards, `#1883fd` accents, and `._picture_ybue0_18 { display:contents }`.
5. **Colophon & Global Directory Footer (<footer.otRelFont> — `https://arcteryx.com/us/en/explore/system0`)**:
   - Landmark `<footer class="otRelFont">` anchoring `System 0 · Arc’teryx` footer links (`PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`), copy *"Sometimes you have to break it all down."*, and `#57665a` structural dividers.
