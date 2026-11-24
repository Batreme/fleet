---
title: "UI & UX Architecture: about-centra-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: about-centra-com

## Overview & Design Identity
- **Target**: `about-centra-com` (**Centra? Centra! The definitive guide.**)
- **Production URL**: [https://about.centra.com](https://about.centra.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#ffff00` accent)
- **Summary**: The commerce platform for fashion brands.
- **Total Clean CSS Variables Extracted**: `150` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `neue-haas-grotesk-display`
- **Body Font Stack**: `neue-haas-grotesk-text`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 146.71px`, `line-height: 124.703px`, `font-weight: 900`, `letter-spacing: 0.12px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 140px`, `line-height: 140px`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `p` (`font-size: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--_colours---mono--0: white`, `--_colours---mono--900: black`, `--_colours---mono--300: darkgrey`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#ffff00` | `.hs-button.submit:hover { background-color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#a9a9a9` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#959494` | `var(--hsf-default-field-input__border-color)` in `:root` (`rgb(149, 148, 148)`) |
| **Variable Token (`--_colours---mono--200`)** | `#d9d9d9` | `var(--_colours---mono--200)` in `:root` |
| **Variable Token (`--_colours---yellow--main`)** | `#fecf48` | `var(--_colours---yellow--main)` in `:root` |
| **Variable Token (`--_colours---mono--800`)** | `#191919` | `var(--_colours---mono--800)` in `:root` |
| **Variable Token (`--_colours---red--main`)** | `#f85943` | `var(--_colours---red--main)` in `:root` |
| **Variable Token (`--_colours---mono--600`)** | `#333333` | `var(--_colours---mono--600)` in `:root` |
| **Variable Token (`--_colours---green--main`)** | `#1cad56` | `var(--_colours---green--main)` in `:root` |
| **Variable Token (`--_colours---blue--main`)** | `#1d80f6` | `var(--_colours---blue--main)` in `:root` |
| **Variable Token (`--_colours---mono--400`)** | `#787878` | `var(--_colours---mono--400)` in `:root` |
| **Variable Token (`--_colours---mono--700`)** | `#252525` | `var(--_colours---mono--700)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_colours---mono--0` | `white` | Typography / Scale Token |
| `--_colours---mono--900` | `black` | Typography / Scale Token |
| `--_colours---mono--300` | `darkgrey` | Typography / Scale Token |
| `--_colours---mono--200` | `#d9d9d9` | Typography / Scale Token |
| `--padding-inner-md` | `40px` | Layout / Spatial Grid Token |
| `--_colours---yellow--main` | `#fecf48` | Layout / Spatial Grid Token |
| `--padding-section-xl` | `90px` | Layout / Spatial Grid Token |
| `--padding-inner-sm` | `20px` | Layout / Spatial Grid Token |
| `--_colours---mono--800` | `#191919` | Typography / Scale Token |
| `--_colours---red--main` | `#f85943` | Layout / Spatial Grid Token |
| `--_colours---mono--600` | `#333` | Typography / Scale Token |
| `--_colours---green--main` | `#1cad56` | Layout / Spatial Grid Token |
| `--_colours---blue--main` | `#1d80f6` | Layout / Spatial Grid Token |
| `--padding-inner-lg` | `80px` | Layout / Spatial Grid Token |
| `--_colours---mono--400` | `#787878` | Typography / Scale Token |
| `--_colours---mono--700` | `#252525` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navigation-glass-wrapper> — `about-centra-com`)**:
   - Landmark `<nav class="navigation-glass-wrapper mobile-navigation">` (`675x60px`) hosting `Centra? Centra! The definitive guide` navigation (`13 ½ Centra Facts · Brands on Centra`), DOM attributes (`data-wf-domain="about.centra.com"`, `data-wf-page="6a0af5d1e1f707540842bee4"`, `data-wf-site="6a0af5d1e1f707540842bf02"`, `data-global-dreamdata-analytics-key="dreamdata"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.heading-animation> — `CENTRA? CENTRA!`)**:
   - Landmark `<section class="heading-animation">` presenting display lead `CENTRA? CENTRA!` and copy excerpt *"Centra uses your contact information to send product and service "* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section-parallax> — `Centra? Centra!`)**:
   - Landmark `<section class="section-parallax">` rendering section `Centra? Centra!` with copy *"CENTRA? CENTRA!"*, asset references (`cdn.prod.website-files.com`, `centra-centra.webflow.shared.3f63...`, `dreamdata.min.js`, `lftracker_v1_ywVkO4XVlwx8Z6Bj.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-call-to-action> — `about-centra-com Interactive Matri`)**:
   - Landmark `<section class="section-call-to-action">` framing `about-centra-com Interactive Matrix` and `about-centra-com Archive & Directory` (*"Centra? Centra!"*) with `#222222` surface cards, `#ffff00` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-neuehaasgrotesktext-n4-active> — `https://about.centra.com`)**:
   - Landmark `<footer class="wf-neuehaasgrotesktext-n4-active">` anchoring `Centra? Centra! The definitive g` footer links (`13 ½ Centra Facts · Brands on Centra`), copy *"about-centra-com Interactive Matrix"*, and `#959494` structural dividers.
