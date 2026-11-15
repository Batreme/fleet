# UI & UX Architecture: edisonfangworkshop-com

## Overview & Design Identity
- **Target**: `edisonfangworkshop-com` (**Edison Fang Workshop**)
- **Production URL**: [https://edisonfangworkshop.com](https://edisonfangworkshop.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#dededc`)
- **Summary**: Edison Fang Workshop is a spatial design practice in Taichung, Taiwan, working across interiors, exhibitions, visual identity and spatial...
- **Total Clean CSS Variables Extracted**: `125` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EFW`
- **Body Font Stack**: `Source Code Variable`
- **Monospace / Technical Font Stack**: `Source Code Variable`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(4.5rem,8.3vw,9rem)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2.65rem,4.5vw,5.1rem)`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-body: Arial, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: clamp(.42rem,.54vw,.58rem)`, `letter-spacing: .12em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0b0b0b` | `var(--quiet-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#dededc` | `var(--quiet-paper)` in `:root` |
| **Secondary / Muted Copy** | `#efdda9` | `var(--quiet-warm)` in `:root` |
| **Structural Hairline Border** | `#c9e5e5` | `var(--quiet-soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mood-line` | `color-mix(in srgb,var(--mood-fg) 30%,transparent)` | Dimension / Scale Token |
| `--project-bg` | `var(--mood-bg)` | Canvas / Surface Token |
| `--project-text` | `var(--mood-fg)` | Typography Ink Token |
| `--project-muted` | `var(--mood-fg)` | Design System Custom Token |
| `--echo-paper` | `var(--mood-bg)` | Canvas / Surface Token |
| `--echo-ink` | `var(--mood-fg)` | Typography Ink Token |
| `--echo-muted` | `var(--project-muted)` | Design System Custom Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xs` | `20rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.portfolio-header> — `edisonfangworkshop-com`)**:
   - Landmark `<header class="portfolio-header smart-header">` hosting `Edison Fang Workshop` navigation (`H O M E Introduction`), DOM attributes (`data-mood="true"`, `data-precedence="vite-rsc/client-refer..."`, `data-precedence="vite-rsc/client-refer..."`, `data-rsc-css-href="/assets/index-CHG0PVT..."`), and stylesheet rule `main { margin:0;width:100%;height:100%;overflow:hidden;background:var(--paper,e... }`.
2. **Hero Stage & Focal Lead (<section.unreleased-home-intro> — `Let’s give it form.`)**:
   - Landmark `<section class="unreleased-home-intro home-formation">` presenting display lead `Let’s give it form.` and copy excerpt *"EDISON FANG WORKSHOP"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.home-form-poster> — `Spatial & graphic design`)**:
   - Landmark `<section class="home-form-poster home-train-poster">` rendering section `Spatial & graphic design` with copy *"MENU CLOSE MENU CLOSE"*, asset references (`source-code-pro-variable-latin.woff2`, `workshop-shell-qHtOR3l2.css`, `page-Cg2bIiDZ.css`, `index-CHG0PVT-.css`), and grid rule `svg { display:block;width:100%;height:100%;font-family:EFW,monospace }`.
4. **Interactive Detail & Feature Matrix (<section.portfolio-contact> — `MENU CLOSE MENU CLOSE`)**:
   - Landmark `<section class="portfolio-contact home-contact-invitation">` framing `MENU CLOSE MENU CLOSE` and `COLLECTION INDEX SPATIAL / GRAPHIC` (*"COLLECTION INDEX SPATIAL / GRAPHIC"*) with `#0b0b0b` surface cards, `#dededc` accents, and `number { font-weight:300;letter-spacing:.03em;font-variant-numeric:tabular-nums }`.
5. **Colophon & Global Directory Footer (<footer.collection-menu-footer> — `https://edisonfangworkshop.com`)**:
   - Landmark `<footer class="collection-menu-footer">` anchoring `Edison Fang Workshop` footer links (`H O M E Introduction`), copy *"H O M E Introduction"*, and `#c9e5e5` structural dividers.
