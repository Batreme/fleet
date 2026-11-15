# UI & UX Architecture: lajoya-foods-com_en

## Overview & Design Identity
- **Target**: `lajoya-foods-com_en` (**LAJOYA GOURMET**)
- **Production URL**: [https://lajoya-foods.com/en](https://lajoya-foods.com/en)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#00EF84` / `#000000`)
- **Summary**: Optimal preservation of porcelain interior
- **Total Clean CSS Variables Extracted**: `13` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `JoyaMaison`
- **Body Font Stack**: `JoyaAmbiant`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: -2px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 28px`)
- **Body Copy**: rule `p` (`font-size: 12px`, `letter-spacing: 2px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `12px`, `19px`, `14px`, `13px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#00EF84` | `var(--color-primary)` in `:root` |
| **Primary Typography Ink** | `#EA3323` | `var(--color-secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#FFFF54` | `var(--color-tertiary)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--text-color)` in `:root` |
| **Secondary / Muted Copy** | `#ffffff` | `var(--background-color)` in `:root` |
| **Structural Hairline Border** | `#1990c6` | `.shopify-payment-button__button... { background-color: #1990c6 }` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-primary` | `#00EF84` | Brand / Palette Token |
| `--color-secondary` | `#EA3323` | Brand / Palette Token |
| `--color-tertiary` | `#FFFF54` | Brand / Palette Token |
| `--font-primary` | `"Maison Neue"` | Brand / Palette Token |
| `--font-support` | `"Ambiant Light Spiky"` | Typography / Scale Token |
| `--font-support-s` | `"Ambiant Light Sans"` | Typography / Scale Token |
| `--text-reveal-bleed` | `.2em` | Typography Ink Token |
| `--space` | `4vw` | Layout / Spatial Grid Token |
| `--star-direction` | `reverse` | Design System Custom Token |
| `--height` | `790` | Layout / Spatial Grid Token |
| `--background` | `#ea3323` | Canvas / Surface Token |
| `--text-color` | `#000000` | Typography Ink Token |
| `--background-color` | `#ffffff` | Canvas / Surface Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--lajoya-foods-com-bg` | `#00EF84` | Canvas Substrate (from `var(--color-primary)` in `:root`) |
| `--lajoya-foods-com-ink` | `#000000` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `lajoya-foods-com_en`)**:
   - Landmark `<header class="header">` hosting `LAJOYA GOURMET` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="57685803183"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Lajoya Gourmet`)**:
   - Landmark `<section class="hero">` presenting display lead `Lajoya Gourmet` and copy excerpt *"Privacy policy Privacy policy"* over `#00EF84` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.tiles> — `Shopping Cart`)**:
   - Landmark `<section class="tiles">` rendering section `Shopping Cart` with copy *"Terms of service Terms of service"*, asset references (`171ed732002c6631efbca8f91.js`, `klaviyo.js`, `1349771745561073`, `fbevents.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.tiles> — `Chopped Peeled Tomato Chopped Peel`)**:
   - Landmark `<section class="tiles">` framing `Chopped Peeled Tomato Chopped Peeled Tomato Chopp...` and `Whole Peeled Tomato Whole Peeled Tomato Whole Pee...` (*"Legal notice Legal notice"*) with `#FFFF54` surface cards, `#000000` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.header--mobile> — `https://lajoya-foods.com/en`)**:
   - Landmark `<footer class="header--mobile">` anchoring `LAJOYA GOURMET` footer links (`Overview · Index · Archive · About · Contact`), copy *"© LaJoya 2026 © LaJoya 2026"*, and `#1990c6` structural dividers.
