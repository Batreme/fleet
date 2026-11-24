---
title: "UI & UX Architecture: studyhall-design"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: studyhall-design

## Overview & Design Identity
- **Target**: `studyhall-design` (**Home · Study Hall ✶ Built to move you.**)
- **Production URL**: [https://studyhall.design/](https://studyhall.design/)
- **Final Redirected URL**: [https://www.studyhall.design/](https://www.studyhall.design/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)
- **Summary**: A creative agency based in Oakland and partnering globally. We craft brand, motion, and interactive to help businesses resonate now and r...
- **Total Clean CSS Variables Extracted**: `213` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Neue Montreal`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`, `letter-spacing: -1.28px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 30px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--type-body-lg-mobile: 20`, `--type-body-lg-tablet: 20`, `--type-body-lg-desktop: 24`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--type-small-mobile: 16`, `--type-small-tablet: 16`, `--type-small-desktop: 16`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#cdcdcd` | `var(--color-form-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.bg-blue-500 { background-color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#ff0000` | `.text-red-700 { color: red }` (`#ff0000`) |
| **Structural Hairline Border** | `#e5e5e5` | `10 { border-color: #e5e5e5 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--type-root-max-value` | `18` | Typography / Scale Token |
| `--gx` | `1rem` | Dimension / Scale Token |
| `--gutter` | `1rem` | Layout / Spatial Grid Token |
| `--project-image-gap` | `10px` | Layout / Spatial Grid Token |
| `--columns` | `12` | Layout / Spatial Grid Token |
| `--gy` | `calc(140 / var(--type-root-max-value) * 1rem)` | Dimension / Scale Token |
| `--xs` | `calc(4 / var(--type-root-max-value) * 1rem)` | Dimension / Scale Token |
| `--sm` | `2rem` | Dimension / Scale Token |
| `--md` | `4rem` | Dimension / Scale Token |
| `--lg` | `8rem` | Dimension / Scale Token |
| `--xl` | `16rem` | Dimension / Scale Token |
| `--xxl` | `32rem` | Dimension / Scale Token |
| `--max-w` | `calc(1920 / var(--type-root-max-value) * 1rem)` | Layout / Spatial Grid Token |
| `--nav-h` | `3rem` | Layout / Spatial Grid Token |
| `--nav-b` | `1rem` | Layout / Spatial Grid Token |
| `--nav-clear` | `calc(var(--nav-h) + var(--nav-b))` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.pt-20> — `studyhall-design`)**:
   - Landmark `<nav class="pt-20 flex">` (`1440x54px`) hosting `Home · Study Hall ✶ Built to move yo` navigation (`About · Work with us`), DOM attributes (`data-cookieconsent="ignore"`, `data-hs-ignore="true"`, `data-loader="hs-scriptloader"`, `data-hsjs-portal="246568091"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.pb-gy> — `We're in the business of making th`)**:
   - Landmark `<section class="pb-gy">` presenting display lead `We're in the business of making things move. Bran...` and copy excerpt *"San Francisco Running Company"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.py-gy> — `San Francisco Running Company Bran`)**:
   - Landmark `<section class="py-gy px-gx">` rendering section `San Francisco Running Company Brand Identity` with copy *"Mt. Tamalpais is sacred ground in trail running, the site of the "*, asset references (`banner.js`, `collectedforms.js`, `246568091.js`, `594ac8afc003a31c157eba4bb9a25ab65...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.gap-gutter> — `Awards & Publications`)**:
   - Landmark `<section class="py-gy gap-gutter">` framing `Awards & Publications` and `Recent Work` (*"Netflix Sports Club"*) with `#cdcdcd` surface cards, `#0000ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mb-18> — `https://studyhall.design/`)**:
   - Landmark `<footer class="mb-18 pt-24">` anchoring `Home · Study Hall ✶ Built to mov` footer links (`About · Work with us`), copy *"Since day one, this unique blend 1 has powered vast creative"*, and `#e5e5e5` structural dividers.
