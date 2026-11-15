# UI & UX Architecture: lofliballs-com

## Overview & Design Identity
- **Target**: `lofliballs-com` (**LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli**)
- **Production URL**: [http://lofliballs.com](http://lofliballs.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#FDFBEE` / `#F5E9A9`)
- **Summary**: LoFli Balls are weighted training tools with emulated stitching to mimic the feel of a real ball. Flying about half the distance of a sta...
- **Total Clean CSS Variables Extracted**: `195` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Alumni Sans`
- **Body Font Stack**: `Albert Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `clamp(var(--font-size-96)`, `clamp(var(--font-size-40)`, `clamp(var(--font-size-32)`, `var(--font-size-32)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: calc(var(--kl-reviews-reviews...`, `line-height: 122%`, `font-weight: calc(var(--kl...`)
- **Body Copy**: CSS variables `--gw-ball-body: var(--bg-brand)`, `--font-body: Assistant, sans-serif`; rule `p` (`font-size: medium`, `line-height: normal`, `letter-spacing: normal`, `font-weight: normal`)
- **Metadata & Labels**: rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#FDFBEE` | `var(--color-yellow-5)` in `:root` |
| **Primary Typography Ink** | `#F8F4D9` | `var(--color-yellow-50)` in `:root` |
| **Elevated Surface / Card Substrate** | `#F6EEC2` | `var(--color-yellow-100)` in `:root` |
| **Interactive Accent / Highlight** | `#F5E9A9` | `var(--color-yellow-200)` in `:root` |
| **Secondary / Muted Copy** | `#F4E48D` | `var(--color-yellow-300)` in `:root` |
| **Structural Hairline Border** | `#F4DF6C` | `var(--color-yellow-400)` in `:root` |
| **Variable Token (`--color-yellow-500`)** | `#F4DA40` | `var(--color-yellow-500)` in `:root` |
| **Variable Token (`--color-yellow-600`)** | `#C9940D` | `var(--color-yellow-600)` in `:root` |
| **Variable Token (`--color-yellow-700`)** | `#8E5A0B` | `var(--color-yellow-700)` in `:root` |
| **Variable Token (`--color-yellow-800`)** | `#5D3309` | `var(--color-yellow-800)` in `:root` |
| **Variable Token (`--color-yellow-900`)** | `#361C08` | `var(--color-yellow-900)` in `:root` |
| **Variable Token (`--color-cyan-5`)** | `#F1FDFF` | `var(--color-cyan-5)` in `:root` |
| **Variable Token (`--color-cyan-50`)** | `#D4EDF5` | `var(--color-cyan-50)` in `:root` |
| **Variable Token (`--color-cyan-100`)** | `#B8E2EF` | `var(--color-cyan-100)` in `:root` |
| **Variable Token (`--color-cyan-200`)** | `#9BD8EA` | `var(--color-cyan-200)` in `:root` |
| **Variable Token (`--color-cyan-300`)** | `#7BCEE7` | `var(--color-cyan-300)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-yellow-5` | `#FDFBEE` | Brand / Palette Token |
| `--color-yellow-50` | `#F8F4D9` | Brand / Palette Token |
| `--color-yellow-100` | `#F6EEC2` | Brand / Palette Token |
| `--color-yellow-200` | `#F5E9A9` | Brand / Palette Token |
| `--color-yellow-300` | `#F4E48D` | Brand / Palette Token |
| `--color-yellow-400` | `#F4DF6C` | Brand / Palette Token |
| `--color-yellow-500` | `#F4DA40` | Brand / Palette Token |
| `--color-yellow-600` | `#C9940D` | Brand / Palette Token |
| `--color-yellow-700` | `#8E5A0B` | Brand / Palette Token |
| `--color-yellow-800` | `#5D3309` | Brand / Palette Token |
| `--color-yellow-900` | `#361C08` | Brand / Palette Token |
| `--color-cyan-5` | `#F1FDFF` | Brand / Palette Token |
| `--color-cyan-50` | `#D4EDF5` | Brand / Palette Token |
| `--color-cyan-100` | `#B8E2EF` | Brand / Palette Token |
| `--color-cyan-200` | `#9BD8EA` | Brand / Palette Token |
| `--color-cyan-300` | `#7BCEE7` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.gw-header> — `lofliballs-com`)**:
   - Landmark `<header class="gw-header gw-header--dark">` hosting `LoFli Balls—Innovative Training Tool` navigation (`Shop · Shop All · LoFli Baseball · LoFli Softball · About`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="77292208214"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Shop All`)**:
   - Landmark `<section class="shopify-section">` presenting display lead `Shop All` and copy excerpt *"Shop Shop Shop All LoFli Baseball LoFli Baseball LoFli Softball L"* over `#FDFBEE` canvas and `#F4DF6C` ink.
3. **Primary Showcase & Content Grid (<section.gw-hero> — `LoFli Baseball`)**:
   - Landmark `<section class="gw-hero color-scheme-1">` rendering section `LoFli Baseball` with copy *"Shop LoFli Baseball LoFli Baseball LoFli Softball LoFli Softball "*, asset references (`destination`, `1129077949490951`, `fbevents.js`, `lofli-favicon.png`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `LoFli Softball`)**:
   - Landmark `<section class="shopify-section">` framing `LoFli Softball` and `Swing hard Fly low` (*"Hits like a real ball, but travels about half as far."*) with `#F6EEC2` surface cards, `#F5E9A9` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.gw-footer> — `http://lofliballs.com`)**:
   - Landmark `<footer class="gw-footer gw-footer--black">` anchoring `LoFli Balls—Innovative Training ` footer links (`Shop · Shop All · LoFli Baseball · LoFli Softball · About`), copy *"We built the LoFli ball to fly like a real baseball when thr"*, and `#F4DF6C` structural dividers.
