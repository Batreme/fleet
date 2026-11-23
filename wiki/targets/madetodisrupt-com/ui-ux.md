---
title: "UI & UX Architecture: madetodisrupt-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: madetodisrupt-com

## Overview & Design Identity
- **Target**: `madetodisrupt-com` (**Disrupt · Creative Brand Experience Agency**)
- **Production URL**: [https://madetodisrupt.com](https://madetodisrupt.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#1863dc`)
- **Summary**: Disrupt is a creative brand experience agency shaping strategy, identity, events and activations into ideas people can see, feel and expe...
- **Total Clean CSS Variables Extracted**: `226` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Clash Display`
- **Body Font Stack**: `Syne`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 98px`, `line-height: 90.16px`, `font-weight: 850`); CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: 2em`, `line-height: 1.2`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 244.8px`, `line-height: 318.24px`, `font-weight: 700`, `letter-spacing: -7.344px`); rule `,h2` (`font-size: 1.7em`, `line-height: 1.3`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); rule `p` (`font-size: 20px`, `line-height: 1.65`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--ast-blog-meta-weight: 600`, `--mv-label-x: calc(var(--mv-base-x) + var(--mv-shift-x))`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0d0d` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#111111` | `var(--mxq-hover-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#1863dc` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#7a7a7a` | `var(--e-global-color-text)` in `:root` |
| **Structural Hairline Border** | `#0b0b0b` | `var(--mxq-box-border)` in `:root` (`rgba(0,0,0,.12)`) |
| **Variable Token (`--ast-code-block-background`)** | `#eceff3` | `var(--ast-code-block-background)` in `:root` |
| **Variable Token (`--ast-comment-inputs-background`)** | `#f9fafb` | `var(--ast-comment-inputs-background)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ast-post-nav-space` | `0` | Layout / Spatial Grid Token |
| `--ast-container-default-xlg-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--ast-container-default-lg-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--ast-container-default-slg-padding` | `2em` | Layout / Spatial Grid Token |
| `--ast-container-default-md-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--ast-container-default-sm-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--ast-container-default-xs-padding` | `2.4em` | Layout / Spatial Grid Token |
| `--ast-container-default-xxs-padding` | `1.8em` | Layout / Spatial Grid Token |
| `--ast-code-block-background` | `#ECEFF3` | Canvas / Surface Token |
| `--ast-comment-inputs-background` | `#F9FAFB` | Canvas / Surface Token |
| `--ast-normal-container-width` | `1200px` | Layout / Spatial Grid Token |
| `--ast-narrow-container-width` | `750px` | Layout / Spatial Grid Token |
| `--ast-blog-title-font-weight` | `600` | Typography / Scale Token |
| `--ast-blog-meta-weight` | `600` | Design System Custom Token |
| `--ast-global-color-primary` | `var(--ast-global-color-4)` | Brand / Palette Token |
| `--ast-global-color-secondary` | `var(--ast-global-color-5)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.entry-header> — `madetodisrupt-com`)**:
   - Landmark `<header class="entry-header ast-no-thumbnail">` (`1440x0px`) hosting `Disrupt · Creative Brand Experience ` navigation (`Home · Work · Services · Contact`), DOM attributes (`data-minify="1"`, `data-rocket-defer`, `data-rocket-prefetch`, `data-rocket-preload`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<article.post-10> — `BRANDS IN SESSION`)**:
   - Landmark `<article class="post-10 page">` presenting display lead `BRANDS IN SESSION` and copy excerpt *"Brand Therapy, Without the couch."* over `#0d0d0d` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.poc-tilt-section> — `Craft experiences that move people`)**:
   - Landmark `<section class="poc-tilt-section">` rendering section `Craft experiences that move people and shape how...` with copy *"Strategic brand therapy for identities, experiences, and activati"*, asset references (`recaptcha__en.js`, `script.js`, `www.gstatic.com`, `fonts.googleapis.com`), and grid rule `nav { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.mxq-stage> — `A world where brands live as story`)**:
   - Landmark `<section class="mxq-stage">` framing `A world where brands live as story-spaces; design...` and `BRAND STRATEGY` (*"E v e r y b r a n d c a r r i e s a s p a r k . W e t u r n i t i"*) with `#111111` surface cards, `#1863dc` accents, and `progress { display:inline-block;vertical-align:baseline }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://madetodisrupt.com`)**:
   - Landmark `<footer class="elementor elementor-425">` anchoring `Disrupt · Creative Brand Experie` footer links (`Home · Work · Services · Contact`), copy *"We shape brands from the inside out; strategy, identity, and"*, and `#0b0b0b` structural dividers.
