# UI & UX Architecture: seedance3-si

## Overview & Design Identity
- **Target**: `seedance3-si` (**Seedance 3.0 AI Video Generator: Make Videos from References**)
- **Production URL**: [https://seedance3.si/](https://seedance3.si/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#242520` canvas, `#e4e4e7` ink, `#111113` accent)
- **Summary**: Try Seedance 3.0 free online. Turn text, images, video clips, and audio into videos with sound. Keep faces the same and edit any part wit...
- **Total Clean CSS Variables Extracted**: `431` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Montserrat Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-home-heading)`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`; rule `h1` (`font-weight: 800`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--font-body: "Geist","Geist Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: clamp(16px,1.4vw,18px)`, `letter-spacing: .01em`, `font-weight: 500`)
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#242520` | `var(--menu-ink)` in `:root` |
| **Primary Typography Ink** | `#777970` | `var(--menu-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d3ff02` | `var(--theme-promotion)` in `:root` |
| **Interactive Accent / Highlight** | `#111113` | `var(--theme-promo-background)` in `:root` |
| **Secondary / Muted Copy** | `#e4e4e7` | `var(--theme-promo-foreground)` in `:root` |
| **Structural Hairline Border** | `#b5df00` | `var(--theme-primary-strong)` in `:root` |
| **Variable Token (`--menu-line`)** | `#1c1e181a` | `var(--menu-line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--menu-ink` | `#242520` | Typography Ink Token |
| `--menu-muted` | `#777970` | Color / Atmospheric Token |
| `--menu-line` | `#1c1e181a` | Color / Atmospheric Token |
| `--theme-promotion` | `#d3ff02` | Brand / Palette Token |
| `--theme-promotion-text` | `#d3ff02` | Typography Ink Token |
| `--theme-discount` | `var(--theme-promotion-text)` | Brand / Palette Token |
| `--theme-primary` | `#d3ff02` | Brand / Palette Token |
| `--theme-primary-text` | `var(--theme-promotion-text)` | Typography Ink Token |
| `--theme-logo-gradient` | `linear-gradient(var(--theme-promotion-text),var(--theme-promotion-text))` | Brand / Palette Token |
| `--theme-highlight` | `var(--theme-primary)` | Canvas / Surface Token |
| `--theme-promo-background` | `#111113` | Canvas / Surface Token |
| `--theme-promo-foreground` | `#e4e4e7` | Typography Ink Token |
| `--brand-from` | `var(--theme-highlight)` | Brand / Palette Token |
| `--brand-via` | `var(--theme-highlight)` | Brand / Palette Token |
| `--brand-to` | `var(--theme-secondary)` | Brand / Palette Token |
| `--brand-accent` | `var(--theme-primary)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.tool-header> — `seedance3-si`)**:
   - Landmark `<header class="tool-header fixed">` hosting `Seedance 3.0 AI Video Generator: Mak` navigation (`Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.navigation-module__C5Mk9a__image... { width:min(380px,100vw - 32px) }`.
2. **Hero Stage & Focal Lead (<section.theme-gold> — `Seedance 3.0 AI Video Generator`)**:
   - Landmark `<section class="theme-gold">` presenting display lead `Seedance 3.0 AI Video Generator` and copy excerpt *"Seedance 3.0 Launch Sale: Get 50% off all yearly plans"* over `#242520` canvas and `#e4e4e7` ink.
3. **Primary Showcase & Content Grid (<section.py-14> — `Seedance 3.0 Features`)**:
   - Landmark `<section class="py-14 text-white">` rendering section `Seedance 3.0 Features` with copy *"Seedance 3.0 Launch Sale:"*, asset references (`logo.png`, `799ac774ede1e27a.css`, `49ebc7f384a00a1c.css`, `41592914de078ed4.css`), and grid rule `.navigation-module__C5Mk9a__eyebrow { align-items:center;gap:10px;margin:2px 2px 14px;display:flex }`.
4. **Interactive Detail & Feature Matrix (<article.cursor-pointer> — `Multi-Material Input`)**:
   - Landmark `<article class="cursor-pointer rounded-2xl">` framing `Multi-Material Input` and `Precise Editing` (*"Seedance 3.0 Seedance 3.0"*) with `#d3ff02` surface cards, `#111113` accents, and `vigation-module__C5Mk9a__eyebrow:... { content:"";background:var(--primary);border-radius:50%;width:5px;height:5px }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://seedance3.si/`)**:
   - Landmark `<footer class="flex">` anchoring `Seedance 3.0 AI Video Generator:` footer links (`Pricing`), copy *"Models Seedance 2.5 Seedance 2.0"*, and `#b5df00` structural dividers.
