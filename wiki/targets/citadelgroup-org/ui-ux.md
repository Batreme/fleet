---
title: "UI & UX Architecture: citadelgroup-org"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: citadelgroup-org

## Overview & Design Identity
- **Target**: `citadelgroup-org` (**Citadel National Construction Group · Nationwide Construction**)
- **Production URL**: [https://citadelgroup.org/](https://citadelgroup.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ffa500`)
- **Summary**: Citadel connects leading regional construction firms into one nationwide network, combining local expertise with national resources to de...
- **Total Clean CSS Variables Extracted**: `79` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Montserrat`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`, `letter-spacing: 3.84px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 30px`, `line-height: 36px`, `font-weight: 600`, `letter-spacing: 4.5px`); rule `h2` (`font-size: clamp(2.9rem,2.9vw,3.9rem)`, `line-height: 1.02`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-citadel-body: "Montserrat", system-ui, sans-serif`; rule `p` (`font-size: .88rem`, `line-height: 1.35`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7953e` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffa500` | `.citadel-footer-brand-grid a:hover { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#555555` | `var(--resource-hub-text-muted)` in `:root` |
| **Structural Hairline Border** | `#aaa69e` | `var(--resource-hub-border)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--citadel-dark-orange`)** | `#f87000` | `var(--citadel-dark-orange)` in `:root` |
| **Variable Token (`--citadel-medium-grey`)** | `#818486` | `var(--citadel-medium-grey)` in `:root` |
| **Variable Token (`--citadel-light-grey`)** | `#e3e3e4` | `var(--citadel-light-grey)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--citadel-orange` | `#f7953e` | Color / Atmospheric Token |
| `--citadel-dark-orange` | `#f87000` | Canvas / Surface Token |
| `--citadel-medium-grey` | `#818486` | Color / Atmospheric Token |
| `--citadel-light-grey` | `#e3e3e4` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.citadel-site-header> — `citadelgroup-org`)**:
   - Landmark `<header class="citadel-site-header is-over-hero">` (`1440x91px`) hosting `Citadel National Construction Group ` navigation (`About · Case Studies · Map · Principals`), DOM attributes (`data-wp-strategy="async"`, `data-loaded="true"`, `data-module="scrollspy-nav"`, `data-logo-cover-surface="hidden"`), and stylesheet rule `html { scroll-behavior:smooth;overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<section.citadel-hero> — `NATIONAL REACH. LOCAL EXPERTISE.`)**:
   - Landmark `<section class="citadel-hero">` presenting display lead `NATIONAL REACH. LOCAL EXPERTISE.` and copy excerpt *"Citadel National Construction Group leverages seven best-in-class"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.citadel-about> — `National Reach. Local Expertise.`)**:
   - Landmark `<section class="citadel-about">` rendering section `National Reach. Local Expertise.` with copy *"L o c a l s t r e n g t h . N a t i o n a l s c a l e ."*, asset references (`www.googletagmanager.com`, `embed`, `theme-core.min.css`, `framework-md.min.css`), and grid rule `body { margin:0;font-family:var(--font-citadel-body);color:var(--color-text-pri... }`.
4. **Interactive Detail & Feature Matrix (<section.citadel-partners> — `Serving Clients With National Need`)**:
   - Landmark `<section class="citadel-partners py-10">` framing `Serving Clients With National Needs` and `Seven firms. One connected construction network.` (*"L o c a l s t r e n g t h ."*) with `#f7953e` surface cards, `#ffa500` accents, and `.screen-reader-text { position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hi... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer-meta> — `https://citadelgroup.org/`)**:
   - Landmark `<footer class="site-footer-meta">` anchoring `Citadel National Construction Gr` footer links (`About · Case Studies · Map · Principals`), copy *"N a t i o n a l s c a l e ."*, and `#aaa69e` structural dividers.
