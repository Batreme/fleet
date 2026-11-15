# UI & UX Architecture: ruthgriffioen-art

## Overview & Design Identity
- **Target**: `ruthgriffioen-art` (**Ruth Griffioen – Colourful paintings & art prints**)
- **Production URL**: [https://ruthgriffioen.art/](https://ruthgriffioen.art/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111111` canvas, `#ffffff` ink, `#f8f1eb` accent)
- **Summary**: Discover colourful paintings by Dutch artist Ruth Griffioen, from portraits of women to still lifes and landscapes. Art prints coming Jan...
- **Total Clean CSS Variables Extracted**: `58` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Playfair Display`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Playfair Display", Georgia, "Times New Roman", serif`; rule `h1` (`font-size: var(--step-7)`, `line-height: .95`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--step-2)`, `font-weight: 400`)
- **Body Copy**: CSS variables `--font-body: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif`; rule `p` (`font-size: var(--step--1)`, `letter-spacing: .3em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--step-0)`, `var(--step--2)`, `var(--step--1)`, `.8em`, `var(--step-4)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6f6f6f` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#f8f1eb` | `var(--soft)` in `:root` |
| **Secondary / Muted Copy** | `#4d1224` | `var(--accent)` in `:root` |
| **Structural Hairline Border** | `#c77b8c` | `var(--accent-light)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#111111` | Typography Ink Token |
| `--paper` | `#ffffff` | Canvas / Surface Token |
| `--muted` | `#6f6f6f` | Color / Atmospheric Token |
| `--line` | `rgba(17, 17, 17, .12)` | Color / Atmospheric Token |
| `--soft` | `#f8f1eb` | Color / Atmospheric Token |
| `--accent` | `#4d1224` | Brand / Palette Token |
| `--accent-ink` | `#ffffff` | Typography Ink Token |
| `--accent-light` | `#c77b8c` | Canvas / Surface Token |
| `--font-display` | `"Playfair Display", Georgia, "Times New Roman", serif` | Typography / Scale Token |
| `--font-body` | `"Inter", system-ui, -apple-system, "Segoe UI", sans-serif` | Typography / Scale Token |
| `--step--2` | `.6875rem` | Dimension / Scale Token |
| `--step--1` | `.8125rem` | Dimension / Scale Token |
| `--step-0` | `1rem` | Dimension / Scale Token |
| `--step-1` | `clamp(1.125rem, 1.042rem + .3704vw, 1.375rem)` | Dimension / Scale Token |
| `--step-2` | `clamp(1.312rem, 1.125rem + .8333vw, 1.875rem)` | Dimension / Scale Token |
| `--step-3` | `clamp(1.75rem, 1.417rem + 1.481vw, 2.75rem)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `ruthgriffioen-art`)**:
   - Landmark `<header class="site-header">` hosting `Ruth Griffioen – Colourful paintings` navigation (`Home H o m e · Work W o r k · About A b o u t`), DOM attributes (`data-cookie-preferences-ready="true"`, `data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="109163413834"`, `data-venmo-supported="false"`), and stylesheet rule `font-face { font-family:Inter;font-style:normal;font-weight:400 500;font-display:swa... }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"We and our partners, including Shopify, use cookies and other tec"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.artwall> — `Ruth Griffioen`)**:
   - Landmark `<section class="artwall is-ready">` rendering section `Ruth Griffioen` with copy *"Manage preferences"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `playfair-display.woff2`), and grid rule `root { --header-h: 4.5rem }`.
4. **Interactive Detail & Feature Matrix (<section.artwall> — `Cart 0`)**:
   - Landmark `<section class="artwall is-ready">` framing `Cart 0` and `Account A c c o u n t` (*"Account A c c o u n t"*) with `#6f6f6f` surface cards, `#f8f1eb` accents, and `after { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://ruthgriffioen.art/`)**:
   - Landmark `<footer class="site-footer site-footer--overlay">` anchoring `Ruth Griffioen – Colourful paint` footer links (`Home H o m e · Work W o r k · About A b o u t`), copy *"Contact me C o n t a c t m e"*, and `#c77b8c` structural dividers.
