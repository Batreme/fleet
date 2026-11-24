---
title: "UI & UX Architecture: ads-apple-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ads-apple-com

## Overview & Design Identity
- **Target**: `ads-apple-com` (**Apple Ads**)
- **Production URL**: [http://ads.apple.com](http://ads.apple.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#2997ff` accent)
- **Summary**: Reach customers where only Apple Ads can take you. Learn how to grow your business with ads on the App Store, Apple Maps, Apple News, MLS...
- **Total Clean CSS Variables Extracted**: `274` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SF Pro Display`
- **Body Font Stack**: `SF Pro Text`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 84px`, `font-weight: 600`, `letter-spacing: -1.2px`); CSS variables `--sk-button-display: inline-block`, `--sk-badge-display: initial`; rule `h1` (`font-size: 40px`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 56px`, `line-height: 60px`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25px`, `font-weight: 400`, `letter-spacing: -0.374px`); CSS variables `--sk-body-font-stack: text`, `--sk-paragraph-plus-element-margin: .8em`, `--sk-paragraph-plus-headline-margin: 1.6em`; rule `p` (`font-size: 12px`, `line-height: 1.33337`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25px`, `font-weight: 400`, `letter-spacing: -0.374px`); CSS variables `--r-localnav-viewport-small-min-width: 320px`, `--r-localnav-viewport-small-max-width: 767px`, `--r-localnav-viewport-small-query: (min-width: 320px)`; rule `small` (`font-size: 1em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e8e8ed` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#2997ff` | `ooter-dark a.ac-gf-block .ac-gf... { color: #2997ff }` |
| **Secondary / Muted Copy** | `#888888` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d2d2d7` | `var(--buystrip-border-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--r-localnav-height` | `52px` | Layout / Spatial Grid Token |
| `--r-localnav-stacked-height` | `66px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-large-min-width` | `1024px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-large-query` | `(min-width: 1024px)` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-medium-min-width` | `768px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-medium-max-width` | `1023px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-medium-query` | `(min-width: 768px)` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-small-min-width` | `320px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-small-max-width` | `767px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-small-query` | `(min-width: 320px)` | Layout / Spatial Grid Token |
| `--sk-body-text-color` | `rgb(29, 29, 31)` | Typography Ink Token |
| `--sk-headline-text-color` | `rgb(29, 29, 31)` | Typography Ink Token |
| `--sk-body-background-color` | `rgb(255, 255, 255)` | Canvas / Surface Token |
| `--sk-body-font-stack` | `text` | Typography / Scale Token |
| `--sk-default-stacked-margin` | `.4em` | Layout / Spatial Grid Token |
| `--sk-paragraph-plus-element-margin` | `.8em` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.localnav> — `ads-apple-com`)**:
   - Landmark `<nav class="localnav localnav--custom-background">` (`1440x44px`) hosting `Apple Ads` navigation (` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`), DOM attributes (`data-anim-scroll-group="body"`, `data-sticky="sticky"`, `data-tracking-title="App Store"`, `data-tracking-title="Apple Maps"`), and stylesheet rule `font-face { font-family: "Apple Icons 100"; src: url("../assets/ac-footer/legacy/app... }`.
2. **Hero Stage & Focal Lead (<section.hero-panel-cb> — `Advertising that works for everyon`)**:
   - Landmark `<section class="hero-panel-cb heroPanel-video-v1">` presenting display lead `Advertising that works for everyone.` and copy excerpt *"Promote your brand in the places people love and trust. Apple Ads"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.heroPanel-video-v1> — `Run ads on Apple Maps. The most di`)**:
   - Landmark `<section class="hero-panel-cb heroPanel-video-v1">` rendering section `Run ads on Apple Maps. The most direct route to r...` with copy *"Promote your brand in the places people love and trust."*, asset references (`favicon.ico`, `180_touch.png`, `ads.apple.com`, `globalheader.css`), and grid rule `ac-globalfooter { font-weight: normal; -webkit-text-size-adjust: 100%; text-size-adjust: 100% }`.
4. **Interactive Detail & Feature Matrix (<section.callout-text-with-gradient> — `Experiences only Apple can deliver`)**:
   - Landmark `<section class="callout-text-with-gradient section-content--fixed">` framing `Experiences only Apple can deliver.` and `Spark discovery where downloads happen.` (*"Apple Ads purposefully integrates your advertising where millions"*) with `#e8e8ed` surface cards, `#2997ff` accents, and `after { box-sizing: content-box; margin: 0; padding: 0; pointer-events: auto; le... }`.
5. **Colophon & Global Directory Footer (<footer.js> — `http://ads.apple.com`)**:
   - Landmark `<footer class="js sa-footer">` anchoring `Apple Ads` footer links (` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`), copy *"Creating opportunity — and helping you grow your business — "*, and `#d2d2d7` structural dividers.
