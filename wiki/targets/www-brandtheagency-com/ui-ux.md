---
title: "UI & UX Architecture: www-brandtheagency-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-brandtheagency-com

## Overview & Design Identity
- **Target**: `www-brandtheagency-com` (**BR& – Creating brands that make you smile**)
- **Production URL**: [https://www.brandtheagency.com/](https://www.brandtheagency.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#e4351e`)
- **Summary**: BR& is a creative agency based in Dubai offering branding, marketing, strategy, advertising and social media services. Blending local exp...
- **Total Clean CSS Variables Extracted**: `1044` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gloock`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `Pixelify Sans`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 67.84px`, `line-height: 94.976px`, `font-weight: 400`); CSS variables `--heading-1-size: 4.6rem`, `--heading-1-size-value: 4.6`; rule `.title` (`font-size: 1rem`, `line-height: 1.4`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 29.824px`, `line-height: 34.6436px`, `font-weight: 400`); CSS variables `--heading-2-size: 4rem`, `--heading-2-size-value: 4`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font-font-family: "Helvetica Neue",Arial,sans-serif`, `--body-font-font-style: normal`, `--body-font-font-weight: 400`; rule `p` (`line-height: 1.68em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--heading-font-letter-spacing: 0em`, `--body-font-letter-spacing: 0em`, `--meta-font-font-family: "Pixelify Sans"`; rule `.caption` (`font-size: 12px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#efeee9` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#3e3e3e` | `.sqs-system-error input.disable... { background-color: #3e3e3e }` |
| **Interactive Accent / Highlight** | `#e4351e` | `ontent .buttons .confirmation-b... { background-color: #e4351e }` |
| **Secondary / Muted Copy** | `#797979` | `ockStatus-box-kbArticleLink a:a... { color: #797979 }` |
| **Structural Hairline Border** | `#262626` | `.T7RRDU2nDIcMmFA2 { border-color: #262626 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--image-component-container-width` | `initial` | Layout / Spatial Grid Token |
| `--image-component-container-height` | `initial` | Layout / Spatial Grid Token |
| `--tweak-form-block-title-color-on-background` | `#000` | Canvas / Surface Token |
| `--tweak-form-block-caption-color-on-background` | `#000` | Canvas / Surface Token |
| `--tweak-form-block-option-color-on-background` | `#000` | Canvas / Surface Token |
| `--overlap-image-width-flex-offset` | `calc((var(--image-block-overlap-image-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--overlap-title-width-offset` | `50%` | Layout / Spatial Grid Token |
| `--collage-image-width-flex-offset` | `calc((var(--image-block-collage-image-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--collage-content-width-flex-offset` | `calc((var(--image-block-collage-image-content-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--fallback-white-hsl` | `0, 0%, 98%` | Canvas / Surface Token |
| `--fallback-black-hsl` | `0, 0%, 0%` | Canvas / Surface Token |
| `--solid-alpha-modifier` | `1` | Design System Custom Token |
| `--solid-hover-alpha-modifier` | `0.6` | Design System Custom Token |
| `--outline-hover-alpha-modifier` | `0.4` | Elevation / Border Token |
| `--inverted-solid-hover-alpha-modifier` | `var(--solid-hover-alpha-modifier)` | Design System Custom Token |
| `--inverted-outline-hover-alpha-modifier` | `var(--outline-hover-alpha-modifier)` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.yui3-js-enabled> — `www-brandtheagency-com`)**:
   - Landmark `<header class="yui3-js-enabled">` (`1440px`) hosting `BR& – Creating brands that make you ` navigation (`Subscribe · our services · projects · careers · contact us`), DOM attributes (`data-sqsp-font-ids="6a3134d3db03507f54d78..."`, `data-name="static-context"`, `data-sqs-type="cookiepreferencesgetter"`, `data-motion-style="m-6b08526a3060ed6bcdf2"`), and stylesheet rule `.J5FOAYd29BA3bVlN { animation-name:spin;animation-duration:1s;animation-timing-function:line... }`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `creating brands that make you smil`)**:
   - Landmark `<article class="page-regions">` presenting display lead `creating brands that make you smile` and copy excerpt *"creating brands that make you smile"* over `#000000` canvas and `#efeee9` ink.
3. **Primary Showcase & Content Grid (<section.region> — `creating brands that make you smil`)**:
   - Landmark `<section class="region">` rendering section `creating brands that make you smile creating bran...` with copy *"creating brands that make you smile"*, asset references (`favicon.ico`, `www.brandtheagency.com`, `BR%26_banner.jpg`, `images.squarespace-cdn.com`), and grid rule `.n0vbvuFosektXczs { animation-name:fadeout;animation-iteration-count:1 }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `www-brandtheagency-com Interactive`)**:
   - Landmark `<section class="page-section full-bleed-section">` framing `www-brandtheagency-com Interactive Matrix` and `www-brandtheagency-com Archive & Directory` (*"creating brands that make you smile creating bran..."*) with `#3e3e3e` surface cards, `#e4351e` accents, and `.hWuyu_pGCLQnxiCx { animation-name:fadein;animation-iteration-count:1 }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://www.brandtheagency.com/`)**:
   - Landmark `<footer class="sections">` anchoring `BR& – Creating brands that make ` footer links (`Subscribe · our services · projects · careers · contact us`), copy *"www-brandtheagency-com Interactive Matrix"*, and `#262626` structural dividers.
