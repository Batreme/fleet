---
title: "UI & UX Architecture: performeurope-eu"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: performeurope-eu

## Overview & Design Identity
- **Target**: `performeurope-eu` (**Perform Europe - Reimagine International Touring**)
- **Production URL**: [https://performeurope.eu/](https://performeurope.eu/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#0000ff` accent)
- **Summary**: Discover Perform Europe: a funding scheme for the European performing arts. Supporting inclusive, diverse and green touring projects via...
- **Total Clean CSS Variables Extracted**: `228` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Favorit`
- **Body Font Stack**: `Favorit`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 400`, `letter-spacing: -2.4px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 19px`, `line-height: 22.8px`, `font-weight: 400`); rule `p` (`font-size: 1.25rem`, `line-height: 130%`, `letter-spacing: -.05rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 19px`, `line-height: 22.8px`, `font-weight: 400`); CSS variables `--wp--custom--spacing--small: max(1.5rem, 2vw)`, `--wp--custom--typography--line-height--small: 1.2`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0000ff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#111111` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#5897fb` | `--classic .select2-selection--s... { border: #5897fb }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

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
| `--wp--custom--spacing--small` | `max(1.5rem, 2vw)` | Layout / Spatial Grid Token |
| `--wp--custom--spacing--medium` | `clamp(2rem, 8vw, calc(4 * 1.5rem))` | Layout / Spatial Grid Token |
| `--wp--custom--spacing--large` | `clamp(4rem, 10vw, 8rem)` | Layout / Spatial Grid Token |
| `--wp--custom--spacing--outer` | `var(--wp--custom--spacing--small, 1.5rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav__cont> — `performeurope-eu`)**:
   - Landmark `<nav class="nav__cont">` (`1440x0px`) hosting `Perform Europe - Reimagine Internati` navigation (`L o g i n · Home · About Us · who we are · Timeline`), DOM attributes (`data-speed="1.09"`, `data-lag="0"`, `data-speed="0.95"`, `data-lag="0"`), and stylesheet rule `.select2-container { box-sizing:border-box;display:inline-block;margin:0;position:relative;ve... }`.
2. **Hero Stage & Focal Lead (<section.section-wrp> — `Dear performing arts communities a`)**:
   - Landmark `<section class="section-wrp s-landing-animation">` presenting display lead `Dear performing arts communities across Europe… hi!` and copy excerpt *"Perform Europe is a forward-looking funding scheme for the Europe"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.s-card> — `Collaborative`)**:
   - Landmark `<section class="section-wrp s-card">` rendering section `Collaborative` with copy *"Submissions for the Perform Europe Open Call are now closed. A to"*, asset references (`perform-europe-fav.png`, `cdnjs.cloudflare.com`, `embed`, `password-lost.css`), and grid rule `t2-container .select2-selection--... { box-sizing:border-box;cursor:pointer;display:block;height:28px;user-sele... }`.
4. **Interactive Detail & Feature Matrix (<section.s-latest> — `Perform Europe’s Open Call is clos`)**:
   - Landmark `<section class="section-wrp s-latest">` framing `Perform Europe’s Open Call is closed. What Happen...` and `Latest news and events` (*"While we await the public announcement of the selected projects f"*) with `#0000ff` surface cards, `#0000ff` accents, and `on--single .select2-selection__re... { display:block;padding-left:8px;padding-right:20px;overflow:hidden;text-o... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://performeurope.eu/`)**:
   - Landmark `<footer class="footer">` anchoring `Perform Europe - Reimagine Inter` footer links (`L o g i n · Home · About Us · who we are · Timeline`), copy *"Perform Europe is co-funded by the European Union and implem"*, and `#5897fb` structural dividers.
