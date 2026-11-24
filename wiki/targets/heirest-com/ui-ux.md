---
title: "UI & UX Architecture: heirest-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: heirest-com

## Overview & Design Identity
- **Target**: `heirest-com` (**HEIREST · Fine Jewellery, Authored By You**)
- **Production URL**: [https://heirest.com/](https://heirest.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ffc700` accent)
- **Summary**: Fine jewellery for those who choose to author what others inherit. Configured by you and crafted to last.
- **Total Clean CSS Variables Extracted**: `1464` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Moderat-Regular`
- **Body Font Stack**: `Moderat-Regular`
- **Monospace / Technical Font Stack**: `ModeratMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--loyalty-shimmer-display: none`, `--font-h1--spacing: var(--font-heading--spacing)`, `--max-width--display-normal: 13em`; rule `h1` (`line-height: var(--line-height--di...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 62px`, `line-height: 71.3px`, `font-weight: 400`, `letter-spacing: -2.79px`); CSS variables `--loyalty-banner-subtitle-size: 14px`, `--font-h2--spacing: var(--font-heading--spacing)`, `--font-h2--weight: 400`; rule `h2` (`font-size: var(--heading-font-size)`, `font-weight: var(--heading...`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 21.45px`, `font-weight: 400`, `letter-spacing: -0.195px`); CSS variables `--paragraph-font-size: 16px`, `--paragraph-font-weight: 400`, `--form-paragraph-font-weight: var(--paragraph-font-weight)`; rule `p` (`line-height: var(--line-height--bo...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 21.45px`, `font-weight: 400`, `letter-spacing: -0.195px`); CSS variables `--section-height-small: 15rem`, `--default-mono-font-family: var(--font-mono)`, `--image-height-small: calc(var(--image-height-basis) * 2)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fefdfc` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffc700` | `oduct-review .question-form .ra... { color: #ffc700 }` |
| **Secondary / Muted Copy** | `#606775` | `var(--cs-secondary-text)` in `:root` |
| **Structural Hairline Border** | `#fefdfc` | `var(--color-border-secondary)` in `:root` |
| **Variable Token (`--product-image-tint`)** | `#f9f8f6` | `var(--product-image-tint)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1.03` | Design System Custom Token |
| `--hover-subtle-zoom-amount` | `1.015` | Design System Custom Token |
| `--hover-shadow-color` | `var(--color-shadow)` | Brand / Palette Token |
| `--hover-transition-duration` | `var(--global-transition-duration)` | Motion / Easing Token |
| `--hover-transition-timing` | `var(--global-transition-timing-function)` | Motion / Easing Token |
| `--surface-transition-duration` | `var(--global-transition-duration)` | Canvas / Surface Token |
| `--surface-transition-timing` | `var(--global-transition-timing-function)` | Canvas / Surface Token |
| `--submenu-animation-speed` | `.36s` | Motion / Easing Token |
| `--submenu-animation-easing` | `cubic-bezier(.25, .1, .25, 1)` | Motion / Easing Token |
| `--icon-stroke-width` | `1px` | Layout / Spatial Grid Token |
| `--page-margin` | `16px` | Layout / Spatial Grid Token |
| `--product-image-tint` | `#f9f8f6` | Canvas / Surface Token |
| `--sidebar-width` | `25rem` | Layout / Spatial Grid Token |
| `--narrow-content-width` | `36rem` | Layout / Spatial Grid Token |
| `--normal-content-width` | `42rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shopify-section> — `heirest-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x0px`) hosting `HEIREST · Fine Jewellery, Authored B` navigation (`Bespoke · Engagement · Our Standards`), DOM attributes (`data-swym-guest-login-bound="1"`, `data-swym-drawer-close-bound="1"`, `data-swym-evt-bound="1"`, `data-swym-save-click-bound="1"`), and stylesheet rule `body { scrollbar-width:none;-ms-overflow-style:none }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Author what others inherit.`)**:
   - Landmark `<section class="shopify-section featured-blog-posts">` presenting display lead `Author what others inherit.` and copy excerpt *"cookies are used on this site. Privacy Policy"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.template-index> — `Time-honoured finery, authored by `)**:
   - Landmark `<section class="template-index">` rendering section `Time-honoured finery, authored by you.` with copy *"Every decision yours. Every step visible."*, asset references (`swym-ext-shopify.js`, `1297080862623390`, `fbevents.js`, `clarity.js`), and grid rule `body::-webkit-scrollbar { width:0;height:0;display:none }`.
4. **Interactive Detail & Feature Matrix (<section.navbar--always-show> — `Our Standards`)**:
   - Landmark `<section class="navbar--always-show">` framing `Our Standards` and `Start with a category` (*"Clarity and transparency at every step"*) with `#fefdfc` surface cards, `#ffc700` accents, and `svg { display:block;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.announcement-bar--show> — `https://heirest.com/`)**:
   - Landmark `<footer class="announcement-bar--show">` anchoring `HEIREST · Fine Jewellery, Author` footer links (`Bespoke · Engagement · Our Standards`), copy *"Complimentary worldwide shipping"*, and `#fefdfc` structural dividers.
