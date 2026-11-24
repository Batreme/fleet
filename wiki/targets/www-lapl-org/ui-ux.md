---
title: "UI & UX Architecture: www-lapl-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-lapl-org

## Overview & Design Identity
- **Target**: `www-lapl-org` (**Homepage · Los Angeles Public Library**)
- **Production URL**: [https://www.lapl.org/](https://www.lapl.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f2eb` canvas, `#000000` ink, `#ffff00` accent)
- **Summary**: The Library will be closed on Thursday, November 26 & Friday, November 27, 2026, in observance of Thanksgiving.
- **Total Clean CSS Variables Extracted**: `189` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `gelica`
- **Body Font Stack**: `niveau-grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 68px`, `font-weight: 300`); CSS variables `--lapl-fs-heading-h1-large: 2.25rem`, `--lapl-fs-heading-h1-regular: 2rem`, `--lapl-fs-heading-h1-small: 1.75rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 48px`, `font-weight: 300`); CSS variables `--lapl-fs-heading-h2-regular: 1.75rem`, `--lapl-fs-heading-h2-small: 1.5rem`, `--lapl-fs-heading-h2-1xsmall: 1.375rem`; rule `,h2` (`font-weight: var(--lapl-fw...`)
- **Body Copy**: live computed `body` (`font-size: 22px`, `line-height: 32px`, `font-weight: 400`); CSS variables `--lapl-fs-body-regular: 1rem`, `--lapl-fs-body-small: 0.875rem`, `--lapl-fs-body-1xsmall: 0.875rem`; rule `p` (`font-size: var(--lapl-fs-body-1xsmall)`, `line-height: var(--lapl-lh-body-1x...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 22px`, `line-height: 32px`, `font-weight: 400`); CSS variables `--lapl-width-small: 1178px`, `--lapl-width-xsmall: 984px`, `--lapl-fs-heading-h1-small: 1.75rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f2eb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `ton--primary .e-button__suffix.... { background-color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#ff8fc7` | `var(--lapl-clr-pink)` in `:root` |
| **Structural Hairline Border** | `#808080` | `textarea:focus { border-color: #808080 }` |
| **Variable Token (`--lapl-clr-sunburn`)** | `#ffccd5` | `var(--lapl-clr-sunburn)` in `:root` |
| **Variable Token (`--lapl-clr-coral`)** | `#ff9eaf` | `var(--lapl-clr-coral)` in `:root` |
| **Variable Token (`--lapl-clr-red`)** | `#eb4646` | `var(--lapl-clr-red)` in `:root` |
| **Variable Token (`--lapl-clr-brick`)** | `#bf2713` | `var(--lapl-clr-brick)` in `:root` |
| **Variable Token (`--lapl-clr-peach`)** | `#ffcc99` | `var(--lapl-clr-peach)` in `:root` |
| **Variable Token (`--lapl-clr-orange`)** | `#ff9326` | `var(--lapl-clr-orange)` in `:root` |
| **Variable Token (`--lapl-clr-burnt-orange`)** | `#bd5d2d` | `var(--lapl-clr-burnt-orange)` in `:root` |
| **Variable Token (`--lapl-clr-buttercream`)** | `#ffeba8` | `var(--lapl-clr-buttercream)` in `:root` |
| **Variable Token (`--lapl-clr-yellow`)** | `#ffde39` | `var(--lapl-clr-yellow)` in `:root` |
| **Variable Token (`--lapl-clr-gold`)** | `#eb9c00` | `var(--lapl-clr-gold)` in `:root` |
| **Variable Token (`--lapl-clr-sage`)** | `#d6e5ae` | `var(--lapl-clr-sage)` in `:root` |
| **Variable Token (`--lapl-clr-green`)** | `#a2c746` | `var(--lapl-clr-green)` in `:root` |
| **Variable Token (`--lapl-clr-dark-green`)** | `#20661a` | `var(--lapl-clr-dark-green)` in `:root` |
| **Variable Token (`--lapl-clr-robins-egg`)** | `#aedce5` | `var(--lapl-clr-robins-egg)` in `:root` |
| **Variable Token (`--lapl-clr-teal`)** | `#3cbcd6` | `var(--lapl-clr-teal)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lapl-transition-easeInOutQuad` | `cubic-bezier(0.45,0,0.55,1)` | Motion / Easing Token |
| `--lapl-clr-sunburn` | `#ffccd5` | Color / Atmospheric Token |
| `--lapl-clr-coral` | `#ff9eaf` | Color / Atmospheric Token |
| `--lapl-clr-red` | `#eb4646` | Color / Atmospheric Token |
| `--lapl-clr-brick` | `#bf2713` | Color / Atmospheric Token |
| `--lapl-clr-peach` | `#fc9` | Color / Atmospheric Token |
| `--lapl-clr-orange` | `#ff9326` | Color / Atmospheric Token |
| `--lapl-clr-burnt-orange` | `#bd5d2d` | Color / Atmospheric Token |
| `--lapl-clr-buttercream` | `#ffeba8` | Color / Atmospheric Token |
| `--lapl-clr-yellow` | `#ffde39` | Color / Atmospheric Token |
| `--lapl-clr-gold` | `#eb9c00` | Color / Atmospheric Token |
| `--lapl-clr-sage` | `#d6e5ae` | Color / Atmospheric Token |
| `--lapl-clr-green` | `#a2c746` | Color / Atmospheric Token |
| `--lapl-clr-dark-green` | `#20661a` | Canvas / Surface Token |
| `--lapl-clr-robins-egg` | `#aedce5` | Color / Atmospheric Token |
| `--lapl-clr-teal` | `#3cbcd6` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.r-site-header> — `www-lapl-org`)**:
   - Landmark `<header class="r-site-header">` (`1440x182px`) hosting `Homepage · Los Angeles Public Librar` navigation (`My Account · Get Help · Contact Us · Locations and Hours · Printing`), DOM attributes (`data-once="lapl-remove-is-loadin..."`, `data-off-canvas-main-canvas`, `data-component-id="lapl:alert"`, `data-component-id="lapl:site-header"`), and stylesheet rule `.text-align-left { text-align:left; }`.
2. **Hero Stage & Focal Lead (<article.p-homepage> — `WELCOME TO THE Los Angeles Public `)**:
   - Landmark `<article class="p-homepage">` presenting display lead `WELCOME TO THE Los Angeles Public Library` and copy excerpt *"The Library will be closed on Thursday, November 26 & Friday, Nov"* over `#f7f2eb` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.p-homepage__actions> — `Welcome to the Los Angeles Public `)**:
   - Landmark `<section class="p-homepage__actions">` rendering section `Welcome to the Los Angeles Public Library` with copy *"Los Angeles Public Library"*, asset references (`challenges.cloudflare.com`, `shim.js`, `zh-hant`, `favicon-default.svg`), and grid rule `.text-align-right { text-align:right; }`.
4. **Interactive Detail & Feature Matrix (<section.p-homepage__section> — `What can we help you find?`)**:
   - Landmark `<section class="p-homepage__section p-homepage__featured">` framing `What can we help you find?` and `Read, Stream & Borrow` (*"Get a Library Card"*) with `#ffffff` surface cards, `#ffff00` accents, and `.text-align-center { text-align:center; }`.
5. **Colophon & Global Directory Footer (<footer.r-site-footer> — `https://www.lapl.org/`)**:
   - Landmark `<footer class="r-site-footer">` anchoring `Homepage · Los Angeles Public Li` footer links (`My Account · Get Help · Contact Us · Locations and Hours · Printing`), copy *"Computers & Technology"*, and `#808080` structural dividers.
