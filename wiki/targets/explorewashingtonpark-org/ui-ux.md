---
title: "UI & UX Architecture: explorewashingtonpark-org"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: explorewashingtonpark-org

## Overview & Design Identity
- **Target**: `explorewashingtonpark-org` (**Explore Washington Park**)
- **Production URL**: [https://explorewashingtonpark.org](https://explorewashingtonpark.org)
- **Final Redirected URL**: [https://www.explorewashingtonpark.org/](https://www.explorewashingtonpark.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fdfbf8` canvas, `#313232` ink, `#ffff00` accent)
- **Summary**: Washington Park in Portland, Oregon is home to the Oregon Zoo, Hoyt Arboretum, world-class gardens, museums, and miles of trails. Find ho...
- **Total Clean CSS Variables Extracted**: `1364` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `national-ygefsl`
- **Body Font Stack**: `National`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 79.208px`, `line-height: 64.9506px`, `font-weight: 700`); CSS variables `--child-display: initial`, `--heading-1-size: 3.76rem`, `--heading-1-size-value: 3.76`; rule `.title` (`font-size: 1rem`, `line-height: 1.4`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 79.208px`, `line-height: 64.9506px`, `font-weight: 700`); CSS variables `--heading-2-size: 2.71rem`, `--heading-2-size-value: 2.71`; rule `h2` (`font-size: 1.88em`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font-font-family: "national-ygefsl"`, `--body-font-font-style: normal`, `--body-font-font-weight: 500`; rule `p` (`line-height: 1`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18.0368px`, `line-height: 18.0368px`, `font-weight: 500`); CSS variables `--heading-font-letter-spacing: 0em`, `--body-font-letter-spacing: 0em`, `--meta-font-font-family: "national-ygefsl"`; rule `.caption` (`font-size: 12px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fdfbf8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#313232` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#9bbd3c` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `.icon-button:hover { color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#6b7280` | `var(--weather-modal-text-muted)` in `:root` |
| **Structural Hairline Border** | `#f1ebe2` | `var(--wm-accordion-item-border-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--course-item-nav-text-color` | `hsla(var(--black-hsl),1)` | Typography Ink Token |
| `--tweak-blog-item-pagination-icon-color` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--tweak-quote-block-source-color-on-background` | `hsla(var(--safeDarkAccent-hsl),1)` | Canvas / Surface Token |
| `--product-basic-item-add-ons-title-color` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--product-block-text-color-on-background` | `hsla(var(--safeDarkAccent-hsl),1)` | Canvas / Surface Token |
| `--paragraphSmallColor` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--sqsp-paragraph-3-color` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--list-section-simple-button-background-color` | `hsla(var(--safeDarkAccent-hsl),1)` | Canvas / Surface Token |
| `--gradientHeaderBorderColor` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--solidHeaderDropShadowColor` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--tweak-summary-block-background-color` | `hsla(var(--white-hsl),1)` | Canvas / Surface Token |
| `--tweak-form-block-survey-title-color` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--list-section-carousel-card-description-color` | `hsla(var(--white-hsl),1)` | Brand / Palette Token |
| `--scheduling-block-scheduler-background-color` | `hsla(var(--lightAccent-hsl),1)` | Canvas / Surface Token |
| `--image-block-card-inline-link-color` | `hsla(var(--black-hsl),1)` | Typography Ink Token |
| `--paragraphLargeColor` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.white> — `explorewashingtonpark-org`)**:
   - Landmark `<header class="white header">` (`1440x198px`) hosting `Explore Washington Park` navigation (`Plan Your Visit · Explore The Park`), DOM attributes (`data-tippy-stylesheet`, `data-name="static-context"`, `data-tawk-font-preconnect`, `data-animation-state="booted"`), and stylesheet rule `.J5FOAYd29BA3bVlN { animation-name:spin;animation-duration:1s;animation-timing-function:line... }`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Portland’s Premier Park`)**:
   - Landmark `<article class="page-regions">` presenting display lead `Portland’s Premier Park` and copy excerpt *"Know Before You Go"* over `#fdfbf8` canvas and `#313232` ink.
3. **Primary Showcase & Content Grid (<section.region> — `7 Spots to See Fall Color for Free`)**:
   - Landmark `<section class="region">` rendering section `7 Spots to See Fall Color for Free` with copy *"Portland’s Premier Park Explore Attractions & Amenities"*, asset references (`twk-main.js`, `announcement-bar-ff2c04748aa19f8b...`, `popup-overlay-f39ec8cdc95ccd84-mi...`, `popup-overlay-eb69d574e194d111-mi...`), and grid rule `.n0vbvuFosektXczs { animation-name:fadeout;animation-iteration-count:1 }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `Reservoir & Reflecting Pools Are N`)**:
   - Landmark `<section class="page-section user-items-list-section">` framing `Reservoir & Reflecting Pools Are Now Open` and `TriMet Gets You Here Faster` (*"7 Spots to See Fall Color for Free Read the Blog"*) with `#9bbd3c` surface cards, `#ffff00` accents, and `.hWuyu_pGCLQnxiCx { animation-name:fadein;animation-iteration-count:1 }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://explorewashingtonpark.org`)**:
   - Landmark `<footer class="sections">` anchoring `Explore Washington Park` footer links (`Plan Your Visit · Explore The Park`), copy *"Reservoir & Reflecting Pools Are Now Open Explore the Reserv"*, and `#f1ebe2` structural dividers.
