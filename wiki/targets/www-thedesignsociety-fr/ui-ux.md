---
title: "UI & UX Architecture: www-thedesignsociety-fr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-thedesignsociety-fr

## Overview & Design Identity
- **Target**: `www-thedesignsociety-fr` (**The Design Society Lyon — la communauté des designers**)
- **Production URL**: [https://www.thedesignsociety.fr/](https://www.thedesignsociety.fr/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#350aff` canvas, `#ffffff` ink, `#0082f3` accent)
- **Summary**: L'association qui réunit les designers de Lyon autour de talks et d'apéros. Une société secrète si mal gardée qu'on a fait un site. Proch...
- **Total Clean CSS Variables Extracted**: `60` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica Neue`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 38px`, `line-height: 44px`, `font-weight: 700`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#350aff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0b0e01` | `var(--green--background)` in `:root` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#999999` | `var(--green--content-subtle)` in `:root` |
| **Structural Hairline Border** | `#310ddd` | `var(--border)` in `:root` (`1d1d1d26`) |
| **Variable Token (`--background`)** | `#ebedf5` | `var(--background)` in `:root` |
| **Variable Token (`--border`)** | `#1d1d1d` | `var(--border)` in `:root` |
| **Variable Token (`--blue--content`)** | `#f0f0f0` | `var(--blue--content)` in `:root` |
| **Variable Token (`--brand-color-1`)** | `#bcf015` | `var(--brand-color-1)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#ebedf5` | Canvas / Surface Token |
| `--_theme---content` | `var(--content)` | Brand / Palette Token |
| `--radius--radius-s` | `4px` | Elevation / Border Token |
| `--border` | `#1d1d1d26` | Elevation / Border Token |
| `--radius--radius-m` | `6px` | Elevation / Border Token |
| `--_theme---background-accent` | `var(--background-accent)` | Canvas / Surface Token |
| `--_theme---brand-color-2` | `var(--brand-color-2)` | Brand / Palette Token |
| `--_responsive---hero--padding-top` | `10em` | Layout / Spatial Grid Token |
| `--blue--content` | `#f0f0f0` | Color / Atmospheric Token |
| `--_responsive---hero--title-marquee` | `10em` | Dimension / Scale Token |
| `--brand-color-2` | `#350aff` | Brand / Palette Token |
| `--brand-color-1` | `#bcf015` | Brand / Palette Token |
| `--_responsive---hero--eye` | `150px` | Dimension / Scale Token |
| `--_responsive---hero--margin` | `var(--size--m)` | Layout / Spatial Grid Token |
| `--_theme---border` | `var(--border)` | Brand / Palette Token |
| `--_theme---content-subtle` | `var(--content-subtle)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.twostep-nav> — `www-thedesignsociety-fr`)**:
   - Landmark `<nav class="twostep-nav">` (`1440x900px`) hosting `The Design Society Lyon — la communa` navigation (`A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`), DOM attributes (`data-wf-domain="www.thedesignsociety.fr"`, `data-wf-page="698de82380130d2fe9cadaf6"`, `data-wf-site="698de82080130d2fe9cada54"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.mwg020> — `The Design Society — La société se`)**:
   - Landmark `<section class="mwg020">` presenting display lead `The Design Society — La société secrète la moins...` and copy excerpt *"Née de l'envie de 5 designers, The Design Society organise des év"* over `#350aff` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.mwg005> — `Née de l'envie de 5 designers, The`)**:
   - Landmark `<section class="mwg005">` rendering section `Née de l'envie de 5 designers, The Design Societ` with copy *"THE DESIGN SOCIETY EST UNE SOCIÉTÉ SECRÈTE QUI COMMUNIQUE SUR LIN"*, asset references (`cdn.prod.website-files.com`, `the-design-society-22535e.webflow...`, `6a96a56caf2dbc50ad13753b_webclip.png`, `6a96a56c5cc7207fcb2e955c_webclip.png`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-6> — `THE DESIGN SOCIETY EST UNE SOCIÉTÉ`)**:
   - Landmark `<section class="section-6">` framing `THE DESIGN SOCIETY EST UNE SOCIÉTÉ SECRÈTE QUI C` and `É v è n e m e n t s` (*"É v è n e m e n t s"*) with `#0b0e01` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.thedesignsociety.fr/`)**:
   - Landmark `<footer class="footer">` anchoring `The Design Society Lyon — la com` footer links (`A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`), copy *"E v e n t b r i t e"*, and `#310ddd` structural dividers.
