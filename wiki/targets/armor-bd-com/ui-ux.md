# UI & UX Architecture: armor-bd-com

## Overview & Design Identity
- **Target**: `armor-bd-com` (**Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions**)
- **Production URL**: [https://armor-bd.com](https://armor-bd.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#faebe3`)
- **Summary**: Armor Bangladesh Limited provides banking hardware and software — cash recyclers, ATMs, kiosks, UPS, payment switching and card managemen...
- **Total Clean CSS Variables Extracted**: `43` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Unbounded`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-weight: 700`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.25em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.25em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--normal-bg)` in `:root` |
| **Primary Typography Ink** | `#e5e7eb` | `:after { border-color: #e5e7eb }` |
| **Elevated Surface / Card Substrate** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Interactive Accent / Highlight** | `#faebe3` | `.prose-primary { color: #faebe3 }` |
| **Secondary / Muted Copy** | `#fff3` | `20 { border-color: #fff3 }` |
| **Structural Hairline Border** | `#fffc` | `80 { color: #fffc }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--toast-icon-margin-start` | `-3px` | Layout / Spatial Grid Token |
| `--toast-icon-margin-end` | `4px` | Layout / Spatial Grid Token |
| `--toast-svg-margin-start` | `-1px` | Layout / Spatial Grid Token |
| `--toast-svg-margin-end` | `0px` | Layout / Spatial Grid Token |
| `--toast-button-margin-start` | `auto` | Layout / Spatial Grid Token |
| `--toast-button-margin-end` | `0` | Layout / Spatial Grid Token |
| `--toast-close-button-start` | `0` | Design System Custom Token |
| `--toast-close-button-end` | `unset` | Design System Custom Token |
| `--toast-close-button-transform` | `translate(-35%, -35%)` | Dimension / Scale Token |
| `--gray1` | `hsl(0, 0%, 99%)` | Color / Atmospheric Token |
| `--gray2` | `hsl(0, 0%, 97.3%)` | Color / Atmospheric Token |
| `--gray3` | `hsl(0, 0%, 95.1%)` | Color / Atmospheric Token |
| `--gray4` | `hsl(0, 0%, 93%)` | Color / Atmospheric Token |
| `--gray5` | `hsl(0, 0%, 90.9%)` | Color / Atmospheric Token |
| `--gray6` | `hsl(0, 0%, 88.7%)` | Color / Atmospheric Token |
| `--gray7` | `hsl(0, 0%, 85.8%)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.relative> — `armor-bd-com`)**:
   - Landmark `<nav class="relative mx-auto">` hosting `Armor Bangladesh Limited — ATM, CRM ` navigation (`Products · Why us · About · Career · Contact`), DOM attributes (`data-discover="true"`, `data-discover="true"`, `data-discover="true"`, `data-discover="true"`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.lenis-smooth> — `Pioneering Banking Technology Solu`)**:
   - Landmark `<section class="lenis-smooth">` presenting display lead `Pioneering Banking Technology Solutions` and copy excerpt *"Loading Armor experience"* over `#fff` canvas and `#fff3` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `We are constantly introducing new `)**:
   - Landmark `<section class="relative overflow-hidden">` rendering section `We are constantly introducing new products & solu...` with copy *"Technology Solutions"*, asset references (`favicon.ico`, `index-CjIBsQtn.js`, `index-BvNfHRqr.css`, `HomeV2-CKyWaDQ7.js`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-6> — `150+`)**:
   - Landmark `<section class="py-6 overflow-hidden">` framing `150+` and `Everything you need to run modern banking` (*"Trusted nationwide"*) with `#9ca3af` surface cards, `#faebe3` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.w-full> — `https://armor-bd.com`)**:
   - Landmark `<footer class="w-full bg-primary">` anchoring `Armor Bangladesh Limited — ATM, ` footer links (`Products · Why us · About · Career · Contact`), copy *"At Armor, we empower financial institutions to reach new hei"*, and `#fffc` structural dividers.
