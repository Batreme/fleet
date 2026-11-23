---
title: "UI & UX Architecture: www-agrumeafarm-it_en"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-agrumeafarm-it_en

## Overview & Design Identity
- **Target**: `www-agrumeafarm-it_en` (**Agrumea Farm · Jams, pestos and flavours of Sicily**)
- **Production URL**: [https://www.agrumeafarm.it/en](https://www.agrumeafarm.it/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fdf3eb` / `#e94e1b`)
- **Summary**: Agrumea Farm transforms Sicilian citrus fruits, other fruits and produce into artisanal jams, pestos and preserves with an authentic flavour
- **Total Clean CSS Variables Extracted**: `66` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ivystyle-sans`
- **Body Font Stack**: `ivystyle-sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 41.6px`, `font-weight: 400`); CSS variables `--text-display: clamp(4rem, calc(2.9rem + 11vw) ,999999px)`
- **Section Heading (`H2`)**: observed font-size ladder: `32px`, `16px`, `13px`, `14px`, `var(--text-base)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); CSS variables `--text-base: 1rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); CSS variables `--text-small: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fdf3eb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#762530` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `body { background: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#e94e1b` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ffa500` | `:hover { color: orange }` (`#ffa500`) |
| **Structural Hairline Border** | `#762530` | `var(--color-border)` in `:root` |
| **Variable Token (`--color-yellow`)** | `#f39200` | `var(--color-yellow)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-orange` | `#e94e1b` | Brand / Palette Token |
| `--color-border` | `#762530` | Brand / Palette Token |
| `--color-white` | `#fdf3eb` | Canvas / Surface Token |
| `--color-yellow` | `#f39200` | Brand / Palette Token |
| `--border-round` | `15px` | Elevation / Border Token |
| `--container-padding` | `clamp(30px,2vw,40px)` | Layout / Spatial Grid Token |
| `--grid-columns` | `12` | Layout / Spatial Grid Token |
| `--grid-gap-x` | `clamp(12px,1.45vw,30px)` | Layout / Spatial Grid Token |
| `--grid-gap-y` | `0` | Layout / Spatial Grid Token |
| `--header-offset` | `clamp(20px,2vw,30px)` | Layout / Spatial Grid Token |
| `--header-logo-width` | `clamp(126px,10vw,152px)` | Layout / Spatial Grid Token |
| `--header-pad-y` | `30px` | Layout / Spatial Grid Token |
| `--header-brand-width` | `135px` | Brand / Palette Token |
| `--header-safe-top` | `calc(var(--header-pad-y) + var(--header-brand-width)*130/151)` | Layout / Spatial Grid Token |
| `--font-sans` | `"ivystyle-sans","Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--text-small` | `.875rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-agrumeafarm-it_en`)**:
   - Landmark `<header class="site-header">` (`1440x97px`) hosting `Agrumea Farm · Jams, pestos and flav` navigation (`IT · EN`), DOM attributes (`data-v-aa931410`, `data-v-3a145d88`, `data-header-theme="dark"`, `data-header-logo="full"`), and stylesheet rule `active { cursor:grabbing }`.
2. **Hero Stage & Focal Lead (<section.jar-slider> — `Agrumea Farm: Sicilian artisan mar`)**:
   - Landmark `<section class="jar-slider">` presenting display lead `Agrumea Farm: Sicilian artisan marmalades, spread...` and copy excerpt *"SCROLL TO DISCOVER"* over `#fdf3eb` canvas and `#762530` ink.
3. **Primary Showcase & Content Grid (<section.jar-slider:nth(2)> — `SCROLL TO DISCOVER`)**:
   - Landmark `<section class="jar-slider">` rendering section `SCROLL TO DISCOVER` with copy *"Scroll to discover"*, asset references (`use.typekit.net`, `p.typekit.net`, `yey3ruw.css`, `CmsHomePage.CpbPGEL3.css`), and grid rule `.tk-ivystyle-sans { font-family: "ivystyle-sans",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<section.jar-slider:nth(3)> — `Scroll to discover`)**:
   - Landmark `<section class="jar-slider">` framing `Scroll to discover` and `Agrumea Farm · Jams, pestos and flavours of Sici` (*"Agrumea Farm · Jams, pestos and flavours of Sicily"*) with `#ffffff` surface cards, `#e94e1b` accents, and `.tk-ivymode { font-family: "ivymode",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.site-shell__legal> — `https://www.agrumeafarm.it/en`)**:
   - Landmark `<footer class="site-shell__legal">` anchoring `Agrumea Farm · Jams, pestos and ` footer links (`IT · EN`), copy *"m m e e n n u u c c l l o o s s e e"*, and `#762530` structural dividers.
