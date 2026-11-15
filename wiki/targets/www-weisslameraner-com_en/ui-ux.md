# UI & UX Architecture: www-weisslameraner-com_en

## Overview & Design Identity
- **Target**: `www-weisslameraner-com_en` (**Weiss & Lameraner Media Group – Lifestyle Media House Vienna**)
- **Production URL**: [https://www.weisslameraner.com/en](https://www.weisslameraner.com/en)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fef2f2` canvas, `#bf000f` ink, `#fb2c36` accent)
- **Summary**: Vienna media house: STYLE UP YOUR LIFE!, Y, OBEGG and ADIWEISS.TV. Advertising in print, online, social and TV, plus content and events f...
- **Total Clean CSS Variables Extracted**: `152` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `figtreeUpright`
- **Body Font Stack**: `figtreeUpright Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: inherit!important`, `line-height: normal`, `letter-spacing: normal`, `font-weight: inherit`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .36em`, `letter-spacing: .02em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fef2f2` | `var(--color-red-50)` in `:root` |
| **Primary Typography Ink** | `#ffcaca` | `var(--color-red-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Interactive Accent / Highlight** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Secondary / Muted Copy** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Structural Hairline Border** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--color-amber-400`)** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Variable Token (`--color-amber-500`)** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Variable Token (`--color-amber-600`)** | `#dd7400` | `var(--color-amber-600)` in `:root` |
| **Variable Token (`--color-amber-700`)** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Variable Token (`--color-green-50`)** | `#f0fdf4` | `var(--color-green-50)` in `:root` |
| **Variable Token (`--color-green-200`)** | `#b9f8cf` | `var(--color-green-200)` in `:root` |
| **Variable Token (`--color-green-400`)** | `#05df72` | `var(--color-green-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--trigger-left` | `0` | Design System Custom Token |
| `--font-sans` | `var(--font-figtree)` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-red-50` | `#fef2f2` | Brand / Palette Token |
| `--color-red-200` | `#ffcaca` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-amber-600` | `#dd7400` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-green-50` | `#f0fdf4` | Brand / Palette Token |
| `--color-green-200` | `#b9f8cf` | Brand / Palette Token |
| `--color-green-400` | `#05df72` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `www-weisslameraner-com_en`)**:
   - Landmark `<header class="fixed top-0">` hosting `Weiss & Lameraner Media Group – Life` navigation (`About · Services · Media · Brand Events · WLX`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="cms-o9gdh8"`, `data-href="cms-o9gdh8"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Lifestyle media for your brand.`)**:
   - Landmark `<section class="relative bg-white">` presenting display lead `Lifestyle media for your brand.` and copy excerpt *"Media Data 2027 Media Data 2027"* over `#fef2f2` canvas and `#bf000f` ink.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Brands that work with us.`)**:
   - Landmark `<section class="bg-white py-16">` rendering section `Brands that work with us.` with copy *"(opens in a new window)"*, asset references (`Figtree_VariableFont_wght-s.p.0r5...`, `3emm7imx_eab9.css`, `1lfjsiuslldzn.css`, `37mpl03i35te0.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Austria's media house for lifestyl`)**:
   - Landmark `<section class="relative overflow-hidden">` framing `Austria's media house for lifestyle.` and `Guide for brands What do you want to achieve? Dis...` (*"Austria's media house"*) with `#ffa3a3` surface cards, `#fb2c36` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://www.weisslameraner.com/en`)**:
   - Landmark `<footer class="border-t bg-stone-950">` anchoring `Weiss & Lameraner Media Group – ` footer links (`About · Services · Media · Brand Events · WLX`), copy *"Since 2009 we have been taking brands to where their audienc"*, and `#bf000f` structural dividers.
