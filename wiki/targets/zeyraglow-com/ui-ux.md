---
title: "UI & UX Architecture: zeyraglow-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: zeyraglow-com

## Overview & Design Identity
- **Target**: `zeyraglow-com` (**Zeyra Glow · Natural Body Care Products in the UAE**)
- **Production URL**: [https://zeyraglow.com/](https://zeyraglow.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ff0000` accent)
- **Summary**: Discover natural body care products by Zeyra Glow, made with comfortable, skin-friendly ingredients for simple everyday care. Shop online...
- **Total Clean CSS Variables Extracted**: `150` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `TikTok Sans`
- **Body Font Stack**: `Outfit`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 20px`, `line-height: 22px`, `font-weight: 500`, `letter-spacing: 0.2px`); CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: 28px`, `line-height: 1.1`, `letter-spacing: 0.01em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20px`, `line-height: 19.2px`, `font-weight: 500`, `letter-spacing: 0.02px`); rule `h2` (`font-size: 28px`, `line-height: .96`, `letter-spacing: 0.001em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--e-global-typography-v4-zg-body-font-family: var(--za-font-fam)`, `--e-global-typography-v4-zg-body-font-size: var(--zg-b-desk-to-tab)`, `--e-global-typography-v4-zg-body-font-weight: 400`; rule `p` (`font-size: 15px`, `line-height: 1.6`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: 15px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f2f2` | `var(--zg-grey-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.woocommerce a.remove { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#7a7a7a` | `var(--e-global-color-text)` in `:root` |
| **Structural Hairline Border** | `#4d3939` | `var(--wc-form-border-color)` in `:root` (`rgba(32, 7, 7, 0.8)`) |
| **Variable Token (`--woocommerce`)** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Variable Token (`--wc-green`)** | `#007518` | `var(--wc-green)` in `:root` |
| **Variable Token (`--wc-red`)** | `#aa0000` | `var(--wc-red)` in `:root` |
| **Variable Token (`--wc-orange`)** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Variable Token (`--wc-blue`)** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Variable Token (`--wc-primary-text`)** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |
| **Variable Token (`--wc-subtext`)** | `#767676` | `var(--wc-subtext)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--woocommerce` | `#720eec` | Color / Atmospheric Token |
| `--wc-green` | `#007518` | Color / Atmospheric Token |
| `--wc-red` | `#a00` | Color / Atmospheric Token |
| `--wc-orange` | `#ffba00` | Color / Atmospheric Token |
| `--wc-blue` | `#2ea2cc` | Color / Atmospheric Token |
| `--wc-primary` | `#720eec` | Brand / Palette Token |
| `--wc-primary-text` | `#fcfbfe` | Typography Ink Token |
| `--wc-secondary` | `#e9e6ed` | Brand / Palette Token |
| `--wc-secondary-text` | `#515151` | Typography Ink Token |
| `--wc-highlight` | `#958e09` | Canvas / Surface Token |
| `--wc-highligh-text` | `white` | Typography Ink Token |
| `--wc-content-bg` | `#fff` | Canvas / Surface Token |
| `--wc-subtext` | `#767676` | Typography Ink Token |
| `--wc-form-border-color` | `rgba(32, 7, 7, 0.8)` | Brand / Palette Token |
| `--wc-form-border-radius` | `4px` | Elevation / Border Token |
| `--wc-form-border-width` | `1px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `zeyraglow-com`)**:
   - Landmark `<header class="elementor elementor-1083">` (`424x67px`) hosting `Zeyra Glow · Natural Body Care Produ` navigation (`Our story · Shop`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `.woocommerce form .form-row { padding:3px;margin:0 0 6px }`.
2. **Hero Stage & Focal Lead (<section.products> — `Body care you'll actually keep usi`)**:
   - Landmark `<section class="products">` presenting display lead `Body care you'll actually keep using` and copy excerpt *"Taxes, shipping and promos are calculated at checkout."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.p-card> — `Glow Nila Body Cream`)**:
   - Landmark `<article class="p-card">` rendering section `Glow Nila Body Cream` with copy *"Soft daily moisture, with argan"*, asset references (`fonts.googleapis.com`, `embed`, `woocommerce-layout.css`, `woocommerce-smallscreen.css`), and grid rule `focus::-webkit-input-placeholder { -webkit-transition:opacity .5s .5s ease;transition:opacity .5s .5s ease;... }`.
4. **Interactive Detail & Feature Matrix (<article.p-card:nth(2)> — `Glow Nila Body Scrub`)**:
   - Landmark `<article class="p-card">` framing `Glow Nila Body Scrub` and `Glow Nila Powder` (*"A rinse-off body scrub with argan, for uneven-feeling"*) with `#f2f2f2` surface cards, `#ff0000` accents, and `.woocommerce form .form-row label { line-height:2 }`.
5. **Colophon & Global Directory Footer (<footer.cart-footer> — `https://zeyraglow.com/`)**:
   - Landmark `<footer class="cart-footer cart-footer--empty">` anchoring `Zeyra Glow · Natural Body Care P` footer links (`Our story · Shop`), copy *"A traditional beauty powder with Moroccan roots"*, and `#4d3939` structural dividers.
