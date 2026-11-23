---
title: "UI & UX Architecture: daddyyankee-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: daddyyankee-com

## Overview & Design Identity
- **Target**: `daddyyankee-com` (**Daddy Yankee · Official Website**)
- **Production URL**: [https://daddyyankee.com/](https://daddyyankee.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ece8dc` / `#ff0000`)
- **Summary**: The official Daddy Yankee website. Discover La Postal, his upcoming album, listen to his new single, and get the latest from Daddy Yankee.
- **Total Clean CSS Variables Extracted**: `101` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ABC Diatype Compressed`
- **Body Font Stack**: `Inter Tight 500`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 420px`, `line-height: 336px`, `font-weight: 900`, `letter-spacing: -8.4px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 420px`, `line-height: 336px`, `font-weight: 900`, `letter-spacing: -8.4px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--_typography---body-family: "Inter Tight 500",Arial,sans-serif`, `--_theme---body: var(--_swatch---swatch--black)`, `--_typography---body-line-height: 1.2`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--text-style--body-small: max(1em,16px)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ece8dc` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.hero_cta.is-red { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#efee32` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--_swatch---swatch--cream)` | Canvas / Surface Token |
| `--_typography---body-family` | `"Inter Tight 500",Arial,sans-serif` | Typography / Scale Token |
| `--_theme---body` | `var(--_swatch---swatch--black)` | Brand / Palette Token |
| `--size-font` | `calc(var(--size-container)/(var(--size-container-ideal)/var(--size-unit)))` | Typography / Scale Token |
| `--_typography---body-line-height` | `1.2` | Typography / Scale Token |
| `--_typography---body-weight` | `500` | Design System Custom Token |
| `--_typography---body-letter-space` | `-.03em` | Layout / Spatial Grid Token |
| `--_typography---heading-family` | `"ABC Diatype Compressed",Impact,sans-serif` | Typography Ink Token |
| `--text-style--64` | `4em` | Typography Ink Token |
| `--_typography---heading-line-height` | `.8` | Typography Ink Token |
| `--_typography---heading-weight` | `900` | Typography Ink Token |
| `--_typography---heading-letter-space` | `-.02em` | Typography Ink Token |
| `--text-style--32` | `2em` | Typography Ink Token |
| `--site-margin` | `.75em` | Layout / Spatial Grid Token |
| `--_swatch---swatch--cream` | `#ece8dc` | Brand / Palette Token |
| `--nav--height` | `4.5em` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `daddyyankee-com`)**:
   - Landmark `<nav class="bold-nav-full">` (`1440x900px`) hosting `Daddy Yankee · Official Website` navigation (`STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`), DOM attributes (`data-wf-domain="daddyyankee.com"`, `data-wf-page="6ab927d471adf53e60a6e4f4"`, `data-wf-site="6ab927d171adf53e60a6e4a4"`, `data-cky-tag="notice"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `LA POSTAL`)**:
   - Landmark `<section class="hero_wrap u-section">` presenting display lead `LA POSTAL` and copy excerpt *"October 30th, 2026"* over `#ece8dc` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.portrait_wrap> — `October 30th, 2026`)**:
   - Landmark `<section class="portrait_wrap u-section">` rendering section `October 30th, 2026` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`cdn.prod.website-files.com`, `daddy-yankee.webflow.shared.3af00...`, `script.js`, `gtm.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.tl_wrap> — `We use cookies to enhance your bro`)**:
   - Landmark `<section class="tl_wrap u-section">` framing `We use cookies to enhance your browsing experien` and `Customise Consent Preferences` (*"Customise Consent Preferences"*) with `#ffff00` surface cards, `#ff0000` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://daddyyankee.com/`)**:
   - Landmark `<footer class="footer_wrap u-section">` anchoring `Daddy Yankee · Official Website` footer links (`STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#e2e2e2` structural dividers.
