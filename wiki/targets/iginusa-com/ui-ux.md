---
title: "UI & UX Architecture: iginusa-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: iginusa-com

## Overview & Design Identity
- **Target**: `iginusa-com` (**IGIN USA · Official Home of IGIN in the United States**)
- **Production URL**: [https://iginusa.com](https://iginusa.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)
- **Summary**: IGIN in the USA. Doodle merch, non-alcoholic Apple Citrus and Apple Peach, and where to find IGIN near you. Official store.
- **Total Clean CSS Variables Extracted**: `204` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 149.76px`, `line-height: 122.803px`, `font-weight: 400`, `letter-spacing: 0.59904px`); rule `,.h1` (`font-size: calc(var(--font-heading-scale...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 86px`, `line-height: 86px`, `font-weight: 400`, `letter-spacing: 0.344px`); rule `,.h2` (`font-size: calc(var(--font-heading-scale...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 400`, `letter-spacing: 0.6px`); CSS variables `--font-body-family: Assistant, sans-serif`, `--font-body-style: normal`, `--font-body-weight: 400`; rule `p` (`font-size: 19px`, `line-height: 1.15`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 300`); CSS variables `--mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace`, `--dp-mono: 'JetBrains Mono',ui-monospace,'SF Mono',Menlo,monospace`; rule `small` (`font-size: 10px`, `letter-spacing: .12em`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `nav` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ececec` | `.igST__bar span { background: #ececec }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.igin-btn-black:hover { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#ff6b8a` | `var(--pink)` in `:root` |
| **Structural Hairline Border** | `#f9b9b7` | `.stage { border: #f9b9b7 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-background` | `255,255,255` | Canvas / Surface Token |
| `--gradient-background` | `#ffffff` | Canvas / Surface Token |
| `--color-foreground` | `18,18,18` | Typography Ink Token |
| `--color-background-contrast` | `191,191,191` | Canvas / Surface Token |
| `--color-shadow` | `18,18,18` | Brand / Palette Token |
| `--color-button` | `18,18,18` | Brand / Palette Token |
| `--color-button-text` | `255,255,255` | Typography Ink Token |
| `--color-secondary-button` | `255,255,255` | Brand / Palette Token |
| `--color-secondary-button-text` | `18,18,18` | Typography Ink Token |
| `--color-link` | `18,18,18` | Typography Ink Token |
| `--color-badge-foreground` | `18,18,18` | Typography Ink Token |
| `--color-badge-background` | `255,255,255` | Canvas / Surface Token |
| `--color-badge-border` | `18,18,18` | Brand / Palette Token |
| `--payment-terms-background-color` | `rgb(255 255 255)` | Canvas / Surface Token |
| `--font-body-family` | `Assistant, sans-serif` | Typography / Scale Token |
| `--font-body-style` | `normal` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.igin-rv> — `iginusa-com`)**:
   - Landmark `<header class="igin-rv hdr">` (`1440x104px`) hosting `IGIN USA · Official Home of IGIN in ` navigation (`SHOP · Drinks · Our Story · Where to Buy · Play Doodle Pop`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="100223058239"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.page-width { max-width:var(--page-width);margin:0 auto;padding:0 1.5rem }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `IGIN USA: WHERE SMILES BEGIN`)**:
   - Landmark `<section class="shopify-section igin-doodle-pop-section">` presenting display lead `IGIN USA: WHERE SMILES BEGIN` and copy excerpt *"KOREAN MODERN GIN AND APPLE TONIC"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.igin-rv-section> — `IGIN USA: Where Smiles Begin`)**:
   - Landmark `<section class="shopify-section igin-rv-section">` rendering section `IGIN USA: Where Smiles Begin` with copy *"Korean modern gin and apple tonic"*, asset references (`2721185198297886`, `fbevents.js`, `LOGO-IGIN_USA_SNS_Profile.png`, `fonts.shopifycdn.com`), and grid rule `.announcement-bar-section .page-w... { max-width:100% }`.
4. **Interactive Detail & Feature Matrix (<section.igin-rv> — `Zero proof, same apples.`)**:
   - Landmark `<section class="igin-rv hero">` framing `Zero proof, same apples.` and `Two fans chatting about the new IGIN non alcoholi...` (*"Such a good-looking gin."*) with `#ececec` surface cards, `#ff0000` accents, and `.page-width.drawer-menu { max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.igin-rv> — `https://iginusa.com`)**:
   - Landmark `<footer class="igin-rv ftr">` anchoring `IGIN USA · Official Home of IGIN` footer links (`SHOP · Drinks · Our Story · Where to Buy · Play Doodle Pop`), copy *"Apple Citrus and Apple Peach. Buy now at BevMo and Gopuff."*, and `#f9b9b7` structural dividers.
