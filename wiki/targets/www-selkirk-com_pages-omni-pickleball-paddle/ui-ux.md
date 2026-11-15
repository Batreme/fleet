# UI & UX Architecture: www-selkirk-com_pages-omni-pickleball-paddle

## Overview & Design Identity
- **Target**: `www-selkirk-com_pages-omni-pickleball-paddle` (**Selkirk OMNI™ Pickleball Paddle · Selkirk Sport - We Are Pickleball**)
- **Production URL**: [https://www.selkirk.com/pages/omni-pickleball-paddle](https://www.selkirk.com/pages/omni-pickleball-paddle)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#5046e4` canvas, `#ffffff` ink, `#333333` accent)
- **Summary**: The Selkirk OMNI™ pickleball paddle redefines all-court performance for the modern fast-paced pickleball game. Featuring ReactCore™ techn...
- **Total Clean CSS Variables Extracted**: `232` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `tenby-six`
- **Body Font Stack**: `kallisto`
- **Monospace / Technical Font Stack**: `Kode Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 4rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--font_size)`, `font-weight: 400`)
- **Body Copy**: CSS variables `--body_bg: #ffffff`, `--body_color: #3c3c3c`, `--oke-bodyText-fontWeight: 400`; rule `p` (`font-size: clamp(12px,1.125rem,16px)`, `line-height: 133%`)
- **Metadata & Labels**: CSS variables `--custom_label_text: #ffffff`, `--custom_label_bg: #323232`, `--bundle_label_text: #ffffff`; rule `.label` (`font-size: 9px`, `line-height: 24px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#5046e4` | `var(--shop-ai-bubble-color)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--shop-ai-chat-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f1f1f1` | `var(--shop-ai-reply-background)` in `:root` |
| **Interactive Accent / Highlight** | `#333333` | `var(--shop-ai-reply-text)` in `:root` |
| **Secondary / Muted Copy** | `#eaeaea` | `var(--shop-ai-border-color)` in `:root` |
| **Structural Hairline Border** | `#030712` | `var(--loop-primary-color)` in `:root` |
| **Variable Token (`--shop-ai-inline-shadow-raised`)** | `#0000` | `var(--shop-ai-inline-shadow-raised)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--shop-ai-inline-shadow-color` | `16 24 40` | Brand / Palette Token |
| `--shop-ai-inline-shadow-resting` | `0 1px 2px rgb(var(--shop-ai-inline-shadow-color) / 0.06)` | Elevation / Border Token |
| `--shop-ai-inline-header-radius` | `12px` | Layout / Spatial Grid Token |
| `--shop-ai-inline-control-radius` | `999px` | Elevation / Border Token |
| `--shop-ai-inline-button-radius` | `50%` | Elevation / Border Token |
| `--shop-ai-inline-transition` | `160ms ease` | Motion / Easing Token |
| `--shop-ai-inline-shadow-raised` | `0 0 #0000` | Elevation / Border Token |
| `--shop-ai-inline-shadow-hover` | `0 0 #0000` | Elevation / Border Token |
| `--shop-ai-inline-header-shadow` | `0 0 #0000` | Layout / Spatial Grid Token |
| `--shop-ai-inline-send-shadow` | `0 0 #0000` | Elevation / Border Token |
| `--shop-ai-inline-send-shadow-hover` | `0 0 #0000` | Elevation / Border Token |
| `--viewport-height` | `100vh` | Layout / Spatial Grid Token |
| `--shop-ai-bubble-color` | `#5046e4` | Brand / Palette Token |
| `--shop-ai-window-color` | `#5046e4` | Brand / Palette Token |
| `--shop-ai-chat-background` | `#ffffff` | Canvas / Surface Token |
| `--shop-ai-reply-background` | `#f1f1f1` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.no-js> — `www-selkirk-com_pages-omni-pickleball-paddle`)**:
   - Landmark `<header class="no-js">` hosting `Selkirk OMNI™ Pickleball Paddle · Se` navigation (`Customer Support · Shop Boomstik ST · Shop the deals · Wholesale Login · Paddles`), DOM attributes (`data-gif-toggle-ready="true"`, `data-src="https://static.ads-tw..."`, `data-cookiecategory="4"`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `.tk-tenby-five { font-family: "tenby-five",sans-serif; }`.
2. **Hero Stage & Focal Lead (<section.template-page> — `Earn money back while shopping onl`)**:
   - Landmark `<section class="template-page">` presenting display lead `Earn money back while shopping online at selkirk....` and copy excerpt *"Bonus Bucks can be earned on purchases $100+ from 12:00AM EST Dec"* over `#5046e4` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.header-nav> — `Popular Products`)**:
   - Landmark `<section class="header-nav">` rendering section `Popular Products` with copy *"Spend $100: Get $25 in Bonus Bucks"*, asset references (`uwt.js`, `patrol-styles.css`, `pandectes-rules.js`, `favicon.ico`), and grid rule `.tk-tenby-six { font-family: "tenby-six",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<section.nav-dropdown> — `Selkirk Boomstik® ST with Sharktoo`)**:
   - Landmark `<section class="nav-dropdown">` framing `Selkirk Boomstik® ST with Sharktooth™ Groove Tech...` and `Selkirk OMNI Pickleball Paddle` (*"Spend $150: Get $50 in Bonus Bucks"*) with `#f1f1f1` surface cards, `#333333` accents, and `.tk-kallisto { font-family: "kallisto",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.selkirk.com/pages/omni-pickleball-paddle`)**:
   - Landmark `<footer class="site-footer footer-default">` anchoring `Selkirk OMNI™ Pickleball Paddle ` footer links (`Customer Support · Shop Boomstik ST · Shop the deals · Wholesale Login · Paddles`), copy *"Spend $200: Get $75 in Bonus Bucks"*, and `#030712` structural dividers.
