# UI & UX Architecture: theobromachocolat-com

## Overview & Design Identity
- **Target**: `theobromachocolat-com` (**Cure Your Chocolate Craving · Theobroma Chocolate**)
- **Production URL**: [https://theobromachocolat.com/](https://theobromachocolat.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#d7f087` / `#fff4e3`)
- **Summary**: Shop handcrafted fine chocolate online at Theobroma Chocolate. Premium ingredients, small batch quality, and fast shipping. Order yours t...
- **Total Clean CSS Variables Extracted**: `52` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bowlby One SC`
- **Body Font Stack**: `Figtree`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--h1: 6vw`; rule `h1` (`font-size: var(--h1)`)
- **Section Heading (`H2`)**: CSS variables `--h2: 52px`; rule `h2` (`font-size: 1rem`)
- **Body Copy**: rule `p` (`font-size: var(--h4)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--h1)`, `var(--h2)`, `var(--h3)`, `var(--h4)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d7f087` | `var(--tint-green)` in `:root` |
| **Primary Typography Ink** | `#c2db6f` | `var(--green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b1cf4e` | `var(--link-green)` in `:root` |
| **Interactive Accent / Highlight** | `#fff4e3` | `var(--eggshell)` in `:root` |
| **Secondary / Muted Copy** | `#2f1b12` | `var(--brown)` in `:root` |
| **Structural Hairline Border** | `#91624d` | `var(--lbrown)` in `:root` |
| **Variable Token (`--tint-eggshell`)** | `#fdf7ee27` | `var(--tint-eggshell)` in `:root` |
| **Variable Token (`--ting-white`)** | `#fdf7eea1` | `var(--ting-white)` in `:root` |
| **Variable Token (`--tint-brown`)** | `#45261876` | `var(--tint-brown)` in `:root` |
| **Variable Token (`--tint`)** | `#2f1b1217` | `var(--tint)` in `:root` |
| **Variable Token (`--blue`)** | `#1147a2` | `var(--blue)` in `:root` |
| **Variable Token (`--lblue`)** | `#3368c2` | `var(--lblue)` in `:root` |
| **Variable Token (`--orange`)** | `#ff9800` | `var(--orange)` in `:root` |
| **Variable Token (`--pink`)** | `#d83594` | `var(--pink)` in `:root` |
| **Variable Token (`--red`)** | `#d31127` | `var(--red)` in `:root` |
| **Variable Token (`--yellow`)** | `#ffc800` | `var(--yellow)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--blue` | `#1147a2` | Color / Atmospheric Token |
| `--lblue` | `#3368c2` | Color / Atmospheric Token |
| `--orange` | `#ff9800` | Color / Atmospheric Token |
| `--pink` | `#d83594` | Typography Ink Token |
| `--red` | `#d31127` | Color / Atmospheric Token |
| `--yellow` | `#ffc800` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `theobromachocolat-com`)**:
   - Landmark `<header class="site-header">` hosting `Cure Your Chocolate Craving · Theobr` navigation (`Sticks ▸ · Chunkies ▸ · Minis ▸ · View all · Shop▾`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<div.mouse-follow> — `Cart`)**:
   - Landmark `<div class="mouse-follow">` presenting display lead `Cart` and copy excerpt *"Your cart is currently empty."* over `#d7f087` canvas and `#2f1b12` ink.
3. **Primary Showcase & Content Grid (<div.mouse-follow> — `Pause mode: on Flavour: loud`)**:
   - Landmark `<div class="mouse-follow">` rendering section `Pause mode: on Flavour: loud` with copy *"FOR CRAVINGS. FOR SHARING. FOR DAYS THAT END IN “Y.” BETTER-FOR-Y"*, asset references (`fonts.shopifycdn.com`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<div.mouse-follow> — `Mini Sugar Free Dark Chocolate wit`)**:
   - Landmark `<div class="mouse-follow">` framing `Mini Sugar Free Dark Chocolate with Raspberry 90g` and `OUR PRODUCTS` (*"Creamy chocolate bars. Mouthwatering flavours. Just enough for ev"*) with `#b1cf4e` surface cards, `#fff4e3` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.full-width> — `https://theobromachocolat.com/`)**:
   - Landmark `<footer class="full-width full-width-padded">` anchoring `Cure Your Chocolate Craving · Th` footer links (`Sticks ▸ · Chunkies ▸ · Minis ▸ · View all · Shop▾`), copy *"Clusters with crunch. Chocolate with protein. Built for the "*, and `#91624d` structural dividers.
