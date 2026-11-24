---
title: "UI & UX Architecture: theobromachocolat-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: theobromachocolat-com

## Overview & Design Identity
- **Target**: `theobromachocolat-com` (**Cure Your Chocolate Craving · Theobroma Chocolate**)
- **Production URL**: [https://theobromachocolat.com/](https://theobromachocolat.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff4e3` / `#ff0000`)
- **Summary**: Shop handcrafted fine chocolate online at Theobroma Chocolate. Premium ingredients, small batch quality, and fast shipping. Order yours t...
- **Total Clean CSS Variables Extracted**: `58` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bowlby One SC`
- **Body Font Stack**: `Figtree`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 86.4px`, `line-height: 86.4px`, `font-weight: 400`); CSS variables `--h1: 6vw`; rule `h1` (`font-size: var(--h1)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 86.4px`, `line-height: 86.4px`, `font-weight: 400`); CSS variables `--h2: 52px`; rule `h2` (`font-size: 1rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: var(--h4)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fff4e3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f6f7` | `.welcome { background-color: #f6f6f7 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `ion .hero--product-cta .product... { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#d83594` | `var(--pink)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `on.loading>.loading-overlay__sp... { stroke: #ffffff }` |
| **Variable Token (`--color-foreground`)** | `#2f1b12` | `var(--color-foreground)` in `:root` |
| **Variable Token (`--tint-green`)** | `#d7f087` | `var(--tint-green)` in `:root` |
| **Variable Token (`--tint-eggshell`)** | `#fdf7ee` | `var(--tint-eggshell)` in `:root` |
| **Variable Token (`--tint-brown`)** | `#452618` | `var(--tint-brown)` in `:root` |
| **Variable Token (`--green`)** | `#c2db6f` | `var(--green)` in `:root` |
| **Variable Token (`--link-green`)** | `#b1cf4e` | `var(--link-green)` in `:root` |
| **Variable Token (`--lbrown`)** | `#91624d` | `var(--lbrown)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-primary--family` | `"Work Sans", sans-serif` | Brand / Palette Token |
| `--font-primary--style` | `normal` | Brand / Palette Token |
| `--font-primary--weight` | `400` | Brand / Palette Token |
| `--color-background` | `#fff4e3` | Canvas / Surface Token |
| `--color-foreground` | `#2F1B12` | Typography Ink Token |
| `--style-border-radius-inputs` | `4px` | Elevation / Border Token |
| `--tint-green` | `#d7f087` | Canvas / Surface Token |
| `--tint-eggshell` | `#fdf7ee27` | Canvas / Surface Token |
| `--ting-white` | `#fdf7eea1` | Canvas / Surface Token |
| `--tint-brown` | `#45261876` | Canvas / Surface Token |
| `--tint` | `#2f1b1217` | Canvas / Surface Token |
| `--green` | `#c2db6f` | Color / Atmospheric Token |
| `--link-green` | `#b1cf4e` | Typography Ink Token |
| `--eggshell` | `#fff4e3` | Color / Atmospheric Token |
| `--brown` | `#2f1b12` | Color / Atmospheric Token |
| `--lbrown` | `#91624d` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `theobromachocolat-com`)**:
   - Landmark `<header class="site-header">` (`1440x80px`) hosting `Cure Your Chocolate Craving · Theobr` navigation (`Sticks ▸ · Chunkies ▸ · Minis ▸ · View all · Shop▾`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `button { background-color:transparent;border:none }`.
2. **Hero Stage & Focal Lead (<div.mouse-follow> — `Pause mode: on Flavour: loud`)**:
   - Landmark `<div class="mouse-follow">` presenting display lead `Pause mode: on Flavour: loud` and copy excerpt *"YOUR CART IS CURRENTLY EMPTY."* over `#fff4e3` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.mouse-follow:nth(2)> — `YOUR CART IS CURRENTLY EMPTY.`)**:
   - Landmark `<div class="mouse-follow">` rendering section `YOUR CART IS CURRENTLY EMPTY.` with copy *"Your cart is currently empty."*, asset references (`fonts.shopifycdn.com`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `.button:hover:after { scale:1.05 }`.
4. **Interactive Detail & Feature Matrix (<div.mouse-follow:nth(3)> — `Your cart is currently empty.`)**:
   - Landmark `<div class="mouse-follow">` framing `Your cart is currently empty.` and `FOR CRAVINGS. FOR SHARING. FOR DAYS THAT END IN ` (*"FOR CRAVINGS. FOR SHARING. FOR DAYS THAT END IN “Y.” BETTER-FOR-Y"*) with `#f6f6f7` surface cards, `#ff0000` accents, and `.Accordion .Accordion--tab-trigger { overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.full-width> — `https://theobromachocolat.com/`)**:
   - Landmark `<footer class="full-width full-width-padded">` anchoring `Cure Your Chocolate Craving · Th` footer links (`Sticks ▸ · Chunkies ▸ · Minis ▸ · View all · Shop▾`), copy *"Creamy chocolate bars. Mouthwatering flavours. Just enough f"*, and `#ffffff` structural dividers.
