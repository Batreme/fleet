# UI & UX Architecture: realevate-agency

## Overview & Design Identity
- **Target**: `realevate-agency` (**Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...**)
- **Production URL**: [https://realevate.agency/](https://realevate.agency/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#1F2B5E` canvas, `#FFFFFF` ink, `#222A4C` accent)
- **Summary**: Realevate is a global real estate agency specializing in unique properties and exceptional developments in high-demand markets, offering...
- **Total Clean CSS Variables Extracted**: `305` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Google Sans`
- **Body Font Stack**: `Roslindale Display`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--display-font: "Roslindale Display", Georgia, "Times New Roman", serif`, `--desktop-h1-size: 16vw`, `--desktop-h1-line-height: 1`; rule `h1` (`font-size: 5.5vw`)
- **Section Heading (`H2`)**: CSS variables `--desktop-h2-size: 5.2vw`, `--desktop-h2-line-height: .94`, `--desktop-h2-letter-spacing: -.03em`; rule `h2` (`font-weight: 200`)
- **Body Copy**: CSS variables `--body-leading: 1.35`; rule `,body` (`font-size: var(--text-size)`, `letter-spacing: -.01em`, `font-weight: 500`)
- **Metadata & Labels**: CSS variables `--desktop-h1-letter-spacing: -.02em`, `--desktop-h2-letter-spacing: -.03em`, `--desktop-h3-letter-spacing: -.05em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1F2B5E` | `var(--brand-navy)` in `:root` |
| **Primary Typography Ink** | `#626C95` | `var(--muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#FFFFFF` | `var(--white)` in `:root` |
| **Interactive Accent / Highlight** | `#222A4C` | `var(--category-by-the-sea-color)` in `:root` |
| **Secondary / Muted Copy** | `#5D668D` | `var(--category-by-the-sea-muted)` in `:root` |
| **Structural Hairline Border** | `#36614D` | `var(--category-evergreen-color)` in `:root` |
| **Variable Token (`--category-evergreen-muted`)** | `#80988E` | `var(--category-evergreen-muted)` in `:root` |
| **Variable Token (`--category-urban-living-color`)** | `#2D1C2D` | `var(--category-urban-living-color)` in `:root` |
| **Variable Token (`--category-urban-living-muted`)** | `#6B5A6B` | `var(--category-urban-living-muted)` in `:root` |
| **Variable Token (`--category-rare-gems-color`)** | `#1C181D` | `var(--category-rare-gems-color)` in `:root` |
| **Variable Token (`--category-rare-gems-muted`)** | `#5C585D` | `var(--category-rare-gems-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand-navy` | `#1F2B5E` | Brand / Palette Token |
| `--navy` | `var(--brand-navy)` | Layout / Spatial Grid Token |
| `--muted` | `#626C95` | Color / Atmospheric Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--category-color-light` | `var(--white)` | Canvas / Surface Token |
| `--category-by-the-sea-color` | `#222A4C` | Brand / Palette Token |
| `--category-by-the-sea-muted` | `#5D668D` | Color / Atmospheric Token |
| `--category-evergreen-color` | `#36614D` | Brand / Palette Token |
| `--category-evergreen-muted` | `#80988E` | Color / Atmospheric Token |
| `--category-urban-living-color` | `#2D1C2D` | Brand / Palette Token |
| `--category-urban-living-muted` | `#6B5A6B` | Color / Atmospheric Token |
| `--category-rare-gems-color` | `#1C181D` | Brand / Palette Token |
| `--category-rare-gems-muted` | `#5C585D` | Color / Atmospheric Token |
| `--custom-scrollbar-thumb-color` | `var(--muted)` | Brand / Palette Token |
| `--sans-font` | `"Google Sans", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--display-font` | `"Roslindale Display", Georgia, "Times New Roman", serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.logo> — `realevate-agency`)**:
   - Landmark `<header class="logo">` hosting `Realevate · Exceptional Real Estate ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-index="0"`, `data-index="1"`, `data-index="2"`, `data-index="3"`), and stylesheet rule `after { box-sizing:border-box;-webkit-user-select:none;-moz-user-select:none;-ms... }`.
2. **Hero Stage & Focal Lead (<main.site-preloader-counter-init> — `Invest in Exceptional Real Estate `)**:
   - Landmark `<main class="site-preloader-counter-init">` presenting display lead `Invest in Exceptional Real Estate Properties in C...` and copy excerpt *"Please rotate your device"* over `#1F2B5E` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<main.spa-transition-scroll-locked> — `Please rotate your device`)**:
   - Landmark `<main class="spa-transition-scroll-locked">` rendering section `Please rotate your device` with copy *"Homepage Invest in Cyprus, Montenegro and Georgia"*, asset references (`fbevents.js`, `favicon.png`, `site.webmanifest`, `www.googletagmanager.com`), and grid rule `html { scrollbar-width:none;width:100%;height:100svh }`.
4. **Interactive Detail & Feature Matrix (<main.site-preloader-exit> — `Homepage Invest in Cyprus, Montene`)**:
   - Landmark `<main class="site-preloader-exit">` framing `Homepage Invest in Cyprus, Montenegro and Georgi` and `Invest in Cyprus, Montenegro and Georgia` (*"Invest in Cyprus, Montenegro and Georgia"*) with `#FFFFFF` surface cards, `#222A4C` accents, and `body::-webkit-scrollbar { display:none }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://realevate.agency/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Realevate · Exceptional Real Est` footer links (`Overview · Index · Archive · About · Contact`), copy *"By The Sea Coastal, Marina & Seafront properties"*, and `#36614D` structural dividers.
