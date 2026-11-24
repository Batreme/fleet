---
title: "UI & UX Architecture: mejuma-tuscany-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: mejuma-tuscany-com

## Overview & Design Identity
- **Target**: `mejuma-tuscany-com` (**Mejuma Tuscany**)
- **Production URL**: [https://mejuma-tuscany.com/](https://mejuma-tuscany.com/)
- **Final Redirected URL**: [https://www.mejuma-tuscany.com/](https://www.mejuma-tuscany.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f1f1f1` canvas, `#0000ee` ink, `#ffff00` accent)
- **Summary**: Find your dream home in Tuscany with expert guidance. We handle property search, purchase, renovation & local coordination. Trusted turnk...
- **Total Clean CSS Variables Extracted**: `99` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roxale Story 400`
- **Body Font Stack**: `Golos Text`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 411.231px`, `line-height: 452.355px`, `font-weight: 400`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 120px`, `line-height: 120px`, `font-weight: 400`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--cs-font-size-body: calc(var(--cs-base) * .875)`, `--cs-font-size-body-min: 0px`, `--cs-font-weight-body: 400`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--cs-font-weight-toggle-label: var(--cs-font-weight-medium)`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f1f1f1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e8e4e1` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `.small-cta-base { background-color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#38352c` | live computed `body` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e0e0e0` | `var(--cs-color-secondary-border)` in `:root` |
| **Variable Token (`--yellow`)** | `#ffca4f` | `var(--yellow)` in `:root` |
| **Variable Token (`--sand--300`)** | `#c5beb4` | `var(--sand--300)` in `:root` |
| **Variable Token (`--green--600`)** | `#82886e` | `var(--green--600)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sand--50` | `#f1f1f1` | Color / Atmospheric Token |
| `--green--950` | `#38352c` | Color / Atmospheric Token |
| `--yellow` | `#ffca4f` | Color / Atmospheric Token |
| `--sand--300` | `#c5beb4` | Color / Atmospheric Token |
| `--sand--100` | `#e8e4e1` | Color / Atmospheric Token |
| `--green--600` | `#82886e` | Color / Atmospheric Token |
| `--cs-base` | `max(1rem,15px)` | Dimension / Scale Token |
| `--cs-space-1` | `calc(var(--cs-base) * .25)` | Layout / Spatial Grid Token |
| `--cs-space-2` | `calc(var(--cs-base) * .5)` | Layout / Spatial Grid Token |
| `--cs-space-3` | `calc(var(--cs-base) * .75)` | Layout / Spatial Grid Token |
| `--cs-space-4` | `calc(var(--cs-base) * 1)` | Layout / Spatial Grid Token |
| `--cs-space-5` | `calc(var(--cs-base) * 1.25)` | Layout / Spatial Grid Token |
| `--cs-space-6` | `calc(var(--cs-base) * 1.5)` | Layout / Spatial Grid Token |
| `--cs-space-7` | `calc(var(--cs-base) * 1.75)` | Layout / Spatial Grid Token |
| `--cs-space-8` | `calc(var(--cs-base) * 2)` | Layout / Spatial Grid Token |
| `--cs-radius-sm` | `calc(var(--cs-base) * .25)` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cs-banner__header> — `mejuma-tuscany-com`)**:
   - Landmark `<header class="cs-banner__header">` (`1440px`) hosting `Mejuma Tuscany` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wf-domain="www.mejuma-tuscany.com"`, `data-wf-page="6a71d6d6aa3293dbfd19a3b3"`, `data-wf-site="6a71d6d6aa3293dbfd19a3b7"`, `data-scroll-orientation="vertical"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.js> — `mejuma`)**:
   - Landmark `<section class="js">` presenting display lead `mejuma` and copy excerpt *"Discover a carefully curated selection of Tuscan homes, with pers"* over `#f1f1f1` canvas and `#0000ee` ink.
3. **Primary Showcase & Content Grid (<section.wf-golostext-n4-active> — `m e j u m a`)**:
   - Landmark `<section class="wf-golostext-n4-active">` rendering section `m e j u m a` with copy *"Explore our properties"*, asset references (`cdn.prod.website-files.com`, `mejuma-staging.webflow.shared.777...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.wf-golostext-n7-active> — `Explore our properties`)**:
   - Landmark `<section class="wf-golostext-n7-active">` framing `Explore our properties` and `Our mission is simple: to make buying and owning` (*"Our mission is simple: to make buying and owning a home in Tuscan"*) with `#e8e4e1` surface cards, `#ffff00` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://mejuma-tuscany.com/`)**:
   - Landmark `<footer class="wf-active">` anchoring `Mejuma Tuscany` footer links (`Overview · Index · Archive · About · Contact`), copy *"Selected properties"*, and `#e0e0e0` structural dividers.
