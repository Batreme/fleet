---
title: "UI & UX Architecture: deadlyponies-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: deadlyponies-com

## Overview & Design Identity
- **Target**: `deadlyponies-com` (**Deadly Ponies - Luxury Leather Bags & Accessories**)
- **Production URL**: [https://deadlyponies.com](https://deadlyponies.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f0efeb` canvas, `#000000` ink, `#084ccc` accent)
- **Summary**: Discover Deadly Ponies, a New Zealand-based label, crafting luxury bags & accessories. Coveted luxury leather handbags and accessories.
- **Total Clean CSS Variables Extracted**: `33` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DLYP`
- **Body Font Stack**: `DLYP`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 26px`, `line-height: 32px`, `letter-spacing: -.78px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16px`, `line-height: 38px`, `font-weight: 400`, `letter-spacing: -0.64px`); rule `h2` (`font-size: 22px`, `line-height: 30px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 20px`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0efeb` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f9f9f7` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#084ccc` | `.video-section__btn:active { background-color: #084ccc }` |
| **Secondary / Muted Copy** | `#8f8f8f` | `var(--apd-muted)` in `:root` |
| **Structural Hairline Border** | `#dadada` | `var(--apd-line)` in `:root` |
| **Variable Token (`--kl-reviews-color-light-gray`)** | `#e9e9eb` | `var(--kl-reviews-color-light-gray)` in `:root` |
| **Variable Token (`--swym-remind-cta-bg-color`)** | `#00a65a` | `var(--swym-remind-cta-bg-color)` in `:root` |
| **Variable Token (`--swym-subscribe-success-bg-color`)** | `#aee9d1` | `var(--swym-subscribe-success-bg-color)` in `:root` |
| **Variable Token (`--swym-subscribe-success-text-color`)** | `#202223` | `var(--swym-subscribe-success-text-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--height-full` | `100vh` | Layout / Spatial Grid Token |
| `--height-fill` | `calc(100vh - var(--nav-height))` | Layout / Spatial Grid Token |
| `--font-deadly` | `"Deadly", sans-serif` | Typography / Scale Token |
| `--nav-main-height` | `46px` | Layout / Spatial Grid Token |
| `--nav-height` | `var(--nav-main-height)` | Layout / Spatial Grid Token |
| `--text-color` | `#000000` | Typography Ink Token |
| `--section-height` | `90vh` | Layout / Spatial Grid Token |
| `--kl-reviews-color-light-gray` | `#e9e9eb` | Canvas / Surface Token |
| `--swym-remind-cta-bg-color` | `#00a65a` | Canvas / Surface Token |
| `--swym-remind-cta-text-color` | `white` | Typography Ink Token |
| `--swym-remind-cta-bg-color-v2` | `#000000` | Canvas / Surface Token |
| `--swym-remind-cta-text-color-v2` | `white` | Typography Ink Token |
| `--swym-subscribe-success-bg-color` | `#AEE9D1` | Canvas / Surface Token |
| `--swym-subscribe-success-text-color` | `#202223` | Typography Ink Token |
| `--swym-recently-viewed-pointer-pos` | `92%` | Dimension / Scale Token |
| `--base-height` | `calc(100vh - 310px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `deadlyponies-com`)**:
   - Landmark `<header class="header header--dark">` (`1440x83px`) hosting `Deadly Ponies - Luxury Leather Bags ` navigation (`Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="71218823442"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Transparency`)**:
   - Landmark `<section class="shopify-section content-section">` presenting display lead `Transparency` and copy excerpt *"Deadly Ponies’ tiered loyalty programme with bespoke gifting and "* over `#f0efeb` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.content-section> — `Find your local`)**:
   - Landmark `<section class="shopify-section content-section">` rendering section `Find your local` with copy *"A commitment to responsible materials, thoughtful craft, and piec"*, asset references (`93837`, `loader.js`, `01H2CKQHWBM22V9RBNTG4KH275`, `swym-ext-shopify.js`), and grid rule `swiper-container { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
4. **Interactive Detail & Feature Matrix (<section.section--hero_v2> — `Express Shipping`)**:
   - Landmark `<section class="shopify-section content-section">` framing `Express Shipping` and `Find in store` (*"Our stores provide a serene space to live and breathe the magic t"*) with `#f9f9f7` surface cards, `#084ccc` accents, and `.swiper-vertical>.swiper-wrapper { flex-direction:column }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://deadlyponies.com`)**:
   - Landmark `<footer class="footer">` anchoring `Deadly Ponies - Luxury Leather B` footer links (`Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`), copy *"Discover our Journal - a space for collections, creativity, "*, and `#dadada` structural dividers.
