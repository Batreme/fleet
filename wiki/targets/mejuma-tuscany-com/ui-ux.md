# UI & UX Architecture: mejuma-tuscany-com

## Overview & Design Identity
- **Target**: `mejuma-tuscany-com` (**Mejuma Tuscany**)
- **Production URL**: [https://mejuma-tuscany.com/](https://mejuma-tuscany.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f1f1f1` canvas, `#38352c` ink, `#c5beb4` accent)
- **Summary**: Find your dream home in Tuscany with expert guidance. We handle property search, purchase, renovation & local coordination. Trusted turnk...
- **Total Clean CSS Variables Extracted**: `99` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Made Mirage`
- **Body Font Stack**: `Roxale Story 400`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: CSS variables `--cs-font-size-body: calc(var(--cs-base) * .875)`, `--cs-font-size-body-min: 0px`, `--cs-font-weight-body: 400`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--cs-font-weight-toggle-label: var(--cs-font-weight-medium)`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1f1f1` | `var(--sand--50)` in `:root` |
| **Primary Typography Ink** | `#38352c` | `var(--green--950)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffca4f` | `var(--yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#c5beb4` | `var(--sand--300)` in `:root` |
| **Secondary / Muted Copy** | `#e8e4e1` | `var(--sand--100)` in `:root` |
| **Structural Hairline Border** | `#82886e` | `var(--green--600)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--sand--50` | `#f1f1f1` | Color / Atmospheric Token |
| `--green--950` | `#38352c` | Color / Atmospheric Token |
| `--yellow` | `#ffca4f` | Color / Atmospheric Token |
| `--sand--300` | `#c5beb4` | Color / Atmospheric Token |
| `--sand--100` | `#e8e4e1` | Color / Atmospheric Token |
| `--green--600` | `#82886e` | Color / Atmospheric Token |
| `--cs-color-header-action-text` | `var(--cs-color-header-action-text-hover)` | Typography Ink Token |
| `--cs-base` | `max(1rem,15px)` | Dimension / Scale Token |
| `--cs-space-1` | `calc(var(--cs-base) * .25)` | Layout / Spatial Grid Token |
| `--cs-space-2` | `calc(var(--cs-base) * .5)` | Layout / Spatial Grid Token |
| `--cs-space-3` | `calc(var(--cs-base) * .75)` | Layout / Spatial Grid Token |
| `--cs-space-4` | `calc(var(--cs-base) * 1)` | Layout / Spatial Grid Token |
| `--cs-space-5` | `calc(var(--cs-base) * 1.25)` | Layout / Spatial Grid Token |
| `--cs-space-6` | `calc(var(--cs-base) * 1.5)` | Layout / Spatial Grid Token |
| `--cs-space-7` | `calc(var(--cs-base) * 1.75)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cs-banner__header> — `mejuma-tuscany-com`)**:
   - Landmark `<header class="cs-banner__header">` hosting `Mejuma Tuscany` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wf-domain="www.mejuma-tuscany.com"`, `data-wf-page="6a71d6d6aa3293dbfd19a3b3"`, `data-wf-site="6a71d6d6aa3293dbfd19a3b7"`, `data-scroll-orientation="vertical"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.js> — `m e j u m a`)**:
   - Landmark `<section class="js">` presenting display lead `m e j u m a` and copy excerpt *"info@mejuma-tuscany.com"* over `#f1f1f1` canvas and `#38352c` ink.
3. **Primary Showcase & Content Grid (<section.wf-golostext-n4-active> — `We guide the search, purchase, ren`)**:
   - Landmark `<section class="wf-golostext-n4-active">` rendering section `We guide the search, purchase, renovation and loc...` with copy *"Discover a carefully curated selection of Tuscan homes, with pers"*, asset references (`cdn.prod.website-files.com`, `mejuma-staging.webflow.shared.777...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.wf-golostext-n7-active> — `La Valle di Semifonte`)**:
   - Landmark `<section class="wf-golostext-n7-active">` framing `La Valle di Semifonte` and `Dimora Montecchio` (*"Explore our properties"*) with `#ffca4f` surface cards, `#c5beb4` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://mejuma-tuscany.com/`)**:
   - Landmark `<footer class="wf-active">` anchoring `Mejuma Tuscany` footer links (`Overview · Index · Archive · About · Contact`), copy *"Our mission is simple: to make buying and owning a home in T"*, and `#82886e` structural dividers.
