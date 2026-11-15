# UI & UX Architecture: zeyraglow-com

## Overview & Design Identity
- **Target**: `zeyraglow-com` (**Zeyra Glow · Natural Body Care Products in the UAE**)
- **Production URL**: [https://zeyraglow.com/](https://zeyraglow.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)
- **Summary**: Discover natural body care products by Zeyra Glow, made with comfortable, skin-friendly ingredients for simple everyday care. Shop online...
- **Total Clean CSS Variables Extracted**: `146` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `WooCommerce`
- **Body Font Stack**: `TikTok Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: 28px`, `line-height: 1.1`, `letter-spacing: 0.01em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 28px`, `line-height: .96`, `letter-spacing: 0.001em`, `font-weight: 500`)
- **Body Copy**: CSS variables `--e-global-typography-v4-zg-body-font-family: var(--za-font-fam)`, `--e-global-typography-v4-zg-body-font-size: var(--zg-b-desk-to-tab)`, `--e-global-typography-v4-zg-body-font-weight: 400`; rule `p` (`font-size: 15px`, `line-height: 1.6`, `font-weight: 300`)
- **Metadata & Labels**: rule `small` (`font-size: 15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Primary Typography Ink** | `#007518` | `var(--wc-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a00` | `var(--wc-red)` in `:root` |
| **Interactive Accent / Highlight** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Secondary / Muted Copy** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Structural Hairline Border** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |
| **Variable Token (`--wc-content-bg`)** | `#fff` | `var(--wc-content-bg)` in `:root` |
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
   - Landmark `<header class="elementor elementor-1083">` hosting `Zeyra Glow · Natural Body Care Produ` navigation (`Our story · Shop`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `merce-page .woocommerce-message .... { float:right }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Body care you'll actually keep usi`)**:
   - Landmark `<section class="hero">` presenting display lead `Body care you'll actually keep using` and copy excerpt *"Taxes, shipping and promos are calculated at checkout."* over `#720eec` canvas and `#fcfbfe` ink.
3. **Primary Showcase & Content Grid (<section.products> — `Glow Nila Body Cream`)**:
   - Landmark `<section class="products">` rendering section `Glow Nila Body Cream` with copy *"Taxes, shipping and promos are"*, asset references (`fonts.googleapis.com`, `embed`, `woocommerce-layout.css`, `woocommerce-smallscreen.css`), and grid rule `.woocommerce-page .col2-set { width:100% }`.
4. **Interactive Detail & Feature Matrix (<article.p-card> — `Glow Nila Body Scrub`)**:
   - Landmark `<article class="p-card">` framing `Glow Nila Body Scrub` and `Glow Nila Powder` (*"calculated at checkout."*) with `#a00` surface cards, `#ffba00` accents, and `.woocommerce-page .col2-set::before { content:" ";display:table }`.
5. **Colophon & Global Directory Footer (<footer.cart-footer> — `https://zeyraglow.com/`)**:
   - Landmark `<footer class="cart-footer cart-footer--empty">` anchoring `Zeyra Glow · Natural Body Care P` footer links (`Our story · Shop`), copy *"Inspired by Moroccan beauty rituals and crafted with natural"*, and `#fcfbfe` structural dividers.
