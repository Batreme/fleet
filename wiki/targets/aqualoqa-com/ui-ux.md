# UI & UX Architecture: aqualoqa-com

## Overview & Design Identity
- **Target**: `aqualoqa-com` (**AQUALOQA**)
- **Production URL**: [https://aqualoqa.com/](https://aqualoqa.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff`)
- **Summary**: Haircare is a ritual
- **Total Clean CSS Variables Extracted**: `0` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Playfair Display`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80px`, `14px`, `20px`, `16px`, `11px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80px`, `14px`, `20px`, `16px`, `11px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80px`, `14px`, `20px`, `16px`, `11px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80px`, `14px`, `20px`, `16px`, `11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `.tvvid { background: #000 }` |
| **Primary Typography Ink** | `#F2643E` | `#loadPct { color: #F2643E }` |
| **Elevated Surface / Card Substrate** | `#fff` | `#loadLabel { color: #fff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--aqualoqa-com-bg` | `#000` | Canvas Substrate (from `.tvvid { background: #000 }`) |
| `--aqualoqa-com-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--aqualoqa-com-surface` | `#fff` | Surface Substrate (stylesheet-derived) |
| `--aqualoqa-com-accent` | `#fff` | Interactive Accent (stylesheet-derived) |
| `--aqualoqa-com-muted` | `#fff` | Secondary Ink (stylesheet-derived) |
| `--aqualoqa-com-border` | `#fff` | Structural Border (stylesheet-derived) |
| `--aqualoqa-com-container` | `640px` | Container Bound (stylesheet-derived) |
| `--aqualoqa-com-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--aqualoqa-com-pad` | `10px` | Lateral Padding (stylesheet-derived) |
| `--aqualoqa-com-ease` | `cubic-bezier(0.22,1,0.36,1)` | Primary Easing Function |
| `--aqualoqa-com-radius` | `50%` | Corner Radius (stylesheet-derived) |
| `--aqualoqa-com-fs-base` | `80px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.analytics> — `aqualoqa-com`)**:
   - Landmark `<header class="analytics">` hosting `AQUALOQA` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.event_observe..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `noise { position: fixed; inset: 0; width: 100vw; height: 100vh; pointer-events:... }`.
2. **Hero Stage & Focal Lead (<div.shopify-section> — `AQUALOQA`)**:
   - Landmark `<div class="shopify-section">` presenting display lead `AQUALOQA` and copy excerpt *"© Aqualoqa 2026, All rights reserved."* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.shopify-section> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="shopify-section">` rendering section `Featured Work & Interactive Showcase` with copy *"AQUALOQA"*, asset references (`favicon.svg`, `preloads.js`, `loader.init-shop-cart-sync.en.esm.js`, `load_feature-ed94c51f.js`), and grid rule `scene { position: fixed; inset: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.shopify-section> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="shopify-section">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#fff` surface cards, `#fff` accents, and `scene.zooming { transition: transform 1.8s cubic-bezier(0.22,1,0.36,1); will-change:... }`.
5. **Colophon & Global Directory Footer (<footer.done> — `https://aqualoqa.com/`)**:
   - Landmark `<footer class="done">` anchoring `AQUALOQA` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#fff` structural dividers.
