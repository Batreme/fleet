# UI & UX Architecture: theinfinitysocks-com

## Overview & Design Identity
- **Target**: `theinfinitysocks-com` (**Infinity Socks — Performance Basketball Socks**)
- **Production URL**: [https://theinfinitysocks.com/](https://theinfinitysocks.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`)
- **Summary**: Infinity performance basketball socks. Court System™ — four technologies engineered for the hardwood. Tested by professional players. Pro...
- **Total Clean CSS Variables Extracted**: `174` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `FK Screamer`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25em`, `--display: var(--font-heading)`, `--h1-top: 18.2%`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5em`, `--text-3xl: 1.875em`
- **Body Copy**: CSS variables `--font-body: "Geist", system-ui, sans-serif`, `--text-base: .875em`, `--body: var(--font-body)`
- **Metadata & Labels**: CSS variables `--cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--cc-small-size: .8125em`, `--font-mono: "Geist Mono", ui-monospace, Menlo, monospace`; rule `small` (`font-size: calc(var(--size-font) * .6875)`, `letter-spacing: .26em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--cc-color-bg)` in `:root` |
| **Primary Typography Ink** | `#171717` | `var(--cc-color-fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6b6b6b` | `var(--cc-color-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--cc-color-accent-hover)` in `:root` |
| **Secondary / Muted Copy** | `#2f6acf` | `var(--cc-color-focus)` in `:root` |
| **Structural Hairline Border** | `#706A5E` | `var(--taupe)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-font-family` | `inherit` | Typography / Scale Token |
| `--cc-font-family-heading` | `var(--cc-font-family)` | Typography Ink Token |
| `--cc-font-family-mono` | `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` | Typography / Scale Token |
| `--cc-font-size` | `1em` | Typography / Scale Token |
| `--cc-line-height` | `1.5` | Typography / Scale Token |
| `--cc-title-size` | `1.125em` | Layout / Spatial Grid Token |
| `--cc-title-weight` | `600` | Design System Custom Token |
| `--cc-title-transform` | `none` | Design System Custom Token |
| `--cc-title-spacing` | `0` | Layout / Spatial Grid Token |
| `--cc-text-size` | `.9375em` | Typography Ink Token |
| `--cc-small-size` | `.8125em` | Layout / Spatial Grid Token |
| `--cc-btn-size` | `.9375em` | Layout / Spatial Grid Token |
| `--cc-btn-weight` | `500` | Design System Custom Token |
| `--cc-btn-spacing` | `0` | Layout / Spatial Grid Token |
| `--cc-btn-transform` | `none` | Design System Custom Token |
| `--cc-color-bg` | `#ffffff` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cc__dialog-head> — `theinfinitysocks-com`)**:
   - Landmark `<header class="cc__dialog-head">` hosting `Infinity Socks — Performance Basketb` navigation (`Cookie Policy`), DOM attributes (`data-skip`, `data-motion-toggle`, `data-motion-label`, `data-cc-host`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.cc__banner> — `Cookies`)**:
   - Landmark `<section class="cc__banner">` presenting display lead `Cookies` and copy excerpt *"Strictly necessary Needed for the site to work and to remember yo"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.cc__dialog> — `Cookie settings`)**:
   - Landmark `<section class="cc__dialog">` rendering section `Cookie settings` with copy *"Analytics Google Analytics and Microsoft Clarity, to see which pa"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `button { font:inherit;color:inherit;background:none;border:0;margin:0;cursor:poin... }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `High-Performance Socks High-Perfor`)**:
   - Landmark `<section class="hero hero--h1a">` framing `High-Performance Socks High-Performance Socks Hig...` and `Trusted every possession.` (*"Marketing Google Ads conversion measurement, to see whether our a"*) with `#6b6b6b` surface cards, `#000000` accents, and `.cc__placeholder :focus-visible { outline:2px solid var(--cc-color-focus);outline-offset:2px }`.
5. **Colophon & Global Directory Footer (<footer.cc__dialog-actions> — `https://theinfinitysocks.com/`)**:
   - Landmark `<footer class="cc__dialog-actions cc__actions">` anchoring `Infinity Socks — Performance Bas` footer links (`Cookie Policy`), copy *"High-Performance Socks High-Performance Socks High-Performan"*, and `#706A5E` structural dividers.
