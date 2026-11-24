---
title: "UI & UX Architecture: jozue-fr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: jozue-fr

## Overview & Design Identity
- **Target**: `jozue-fr` (**Josué Pichot, freelance art director and photographer in Paris**)
- **Production URL**: [https://jozue.fr](https://jozue.fr)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#111319` ink, `#f73326` accent)
- **Summary**: Paris-based freelance art director, photographer, director and product designer. 15+ years in advertising and digital. Available in-house...
- **Total Clean CSS Variables Extracted**: `104` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Grotesk Display`
- **Body Font Stack**: `Neue Haas Grotesk Display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 170px`, `line-height: 125.8px`, `font-weight: 700`, `letter-spacing: -5.1px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 170px`, `line-height: 125.8px`, `font-weight: 700`, `letter-spacing: -5.1px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `p` (`font-size: 2.3rem`, `line-height: 1.22`, `letter-spacing: .03em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111319` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f2f0` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f73326` | `.button-selected:hover { color: #f73326 }` |
| **Secondary / Muted Copy** | `#999999` | `.lightbox { color: #999999 }` |
| **Structural Hairline Border** | `#8c8c8c` | `.button-slide:hover path { stroke: #8c8c8c }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--motion-fast` | `200ms` | Motion / Easing Token |
| `--motion-base` | `300ms` | Motion / Easing Token |
| `--motion-slow` | `1000ms` | Motion / Easing Token |
| `--ease-default` | `ease` | Motion / Easing Token |
| `--ease-in` | `ease-in` | Motion / Easing Token |
| `--ease-in-out` | `ease-in-out` | Motion / Easing Token |
| `--transition-fade-in` | `300ms` | Motion / Easing Token |
| `--transition-hold` | `1000ms` | Motion / Easing Token |
| `--transition-fade-out` | `300ms` | Motion / Easing Token |
| `--dur-micro` | `160ms` | Motion / Timing Token |
| `--dur-base` | `380ms` | Motion / Timing Token |
| `--dur-move` | `720ms` | Motion / Timing Token |
| `--dur-cine` | `1400ms` | Motion / Timing Token |
| `--ease-enter` | `cubic-bezier(0.22,0.61,0.36,1)` | Motion / Easing Token |
| `--ease-exit` | `cubic-bezier(0.4,0,1,1)` | Motion / Easing Token |
| `--ease-move` | `cubic-bezier(0.4,0,0.2,1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.menu> — `jozue-fr`)**:
   - Landmark `<nav class="menu menu--site">` (`1440x900px`) hosting `Josué Pichot, freelance art director` navigation (`About. · Works. · Contact. · Français.`), DOM attributes (`data-intro="done"`, `data-color="111319"`, `data-color="F73326"`, `data-title="About"`), and stylesheet rule `.lazyframe__title { z-index:3;padding:15px 17px;position:absolute;top:0;left:0;right:0 }`.
2. **Hero Stage & Focal Lead (<article.homepage> — `art director + photo grapher`)**:
   - Landmark `<article class="homepage">` presenting display lead `art director + photo grapher` and copy excerpt *"93310 Le Pré-Saint-Gervais"* over `#ffffff` canvas and `#111319` ink.
3. **Primary Showcase & Content Grid (<section.js-infos> — `a r t d i r e c t o r + p h o t o `)**:
   - Landmark `<section class="js-infos homepage__infos">` rendering section `a r t d i r e c t o r + p h o t o g r a p h e r c...` with copy *"English. Français."*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `jozue-logo-full.DpMZCk-F.svg`), and grid rule `.lazyframe__title:after { z-index:-1 }`.
4. **Interactive Detail & Feature Matrix (<section.wrapper> — `selected works 18`)**:
   - Landmark `<section class="wrapper wrapper--infos">` framing `selected works 18` and `Awards & Archives` (*"a r t d i r e c t o r + p h o t o g r a p h e r"*) with `#f3f2f0` surface cards, `#f73326` accents, and `.lazyframe:hover { cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.transi> — `https://jozue.fr`)**:
   - Landmark `<footer class="transi">` anchoring `Josué Pichot, freelance art dire` footer links (`About. · Works. · Contact. · Français.`), copy *"a r t d i r e c t o r"*, and `#8c8c8c` structural dividers.
