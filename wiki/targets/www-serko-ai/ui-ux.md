---
title: "UI & UX Architecture: www-serko-ai"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-serko-ai

## Overview & Design Identity
- **Target**: `www-serko-ai` (**Serko.ai · AI Travel Agent for Business Trips**)
- **Production URL**: [https://www.serko.ai](https://www.serko.ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e8f3fe` / `#0082f3`)
- **Summary**: Serko.ai is an AI travel agent for work. Book personalized flights and hotels, follow company policy, manage disruptions and cancel with...
- **Total Clean CSS Variables Extracted**: `591` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jokker`
- **Body Font Stack**: `Jokker`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 70.1985px`, `line-height: 70.1985px`, `font-weight: 500`, `letter-spacing: -2.10595px`); CSS variables `--osano-display-position: "bottom-left"`, `--library_typography---font-size--h1: 5.25rem`, `--library_typography---font-size--display: 6rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 62.3271px`, `line-height: 62.3271px`, `font-weight: 500`, `letter-spacing: -1.86981px`); CSS variables `--library_typography---font-size--h2: 4rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--library_heading-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_text-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_spacing---section-space--small: 5rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e8f3fe` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ebebeb` | `var(--osano-info-dialog-selected-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#058a5e` | `var(--osano-gpc-foreground-color)` in `:root` |
| **Structural Hairline Border** | `#d8d8d8` | `var(--osano-info-dialog-border-color)` in `:root` |
| **Variable Token (`--osano-info-dialog-border-subtle-color`)** | `#e9e9e9` | `var(--osano-info-dialog-border-subtle-color)` in `:root` |
| **Variable Token (`--osano-info-dialog-inset-color`)** | `#f4f4f4` | `var(--osano-info-dialog-inset-color)` in `:root` |
| **Variable Token (`--osano-info-dialog-gpc-tint-color`)** | `#e7f9f0` | `var(--osano-info-dialog-gpc-tint-color)` in `:root` |
| **Variable Token (`--osano-button-foreground-color`)** | `#ffffff` | `var(--osano-button-foreground-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--osano-clear-dialog-background` | `rgba(0,0,0,0)` | Canvas / Surface Token |
| `--osano-info-dialog-border-color` | `#d8d8d8` | Brand / Palette Token |
| `--osano-info-dialog-border-subtle-color` | `#e9e9e9` | Brand / Palette Token |
| `--osano-info-dialog-inset-color` | `#f4f4f4` | Brand / Palette Token |
| `--osano-info-dialog-selected-background-color` | `#ebebeb` | Canvas / Surface Token |
| `--osano-info-dialog-gpc-tint-color` | `#e7f9f0` | Canvas / Surface Token |
| `--osano-theme` | `modern` | Brand / Palette Token |
| `--osano-button-border-color` | `var(--osano-button-foreground-color)` | Brand / Palette Token |
| `--osano-dialog-type` | `box` | Typography / Scale Token |
| `--osano-display-position` | `"bottom-left"` | Design System Custom Token |
| `--osano-info-dialog-position` | `right` | Design System Custom Token |
| `--osano-widget-position` | `right` | Design System Custom Token |
| `--osano-opt-out-widget-position` | `right` | Design System Custom Token |
| `--osano-button-background-color` | `#000000` | Canvas / Surface Token |
| `--osano-button-foreground-color` | `#FFFFFF` | Typography Ink Token |
| `--osano-dialog-background-color` | `#ffffff` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav1_header> — `www-serko-ai`)**:
   - Landmark `<header class="nav1_header">` (`1440x75px`) hosting `Serko.ai · AI Travel Agent for Busin` navigation (`Home · Platform · For companies · About · Sign up free`), DOM attributes (`data-wf-domain="www.serko.ai"`, `data-wf-page="6aa12b65e6dd0b96a2a83430"`, `data-wf-site="6aa12b65e6dd0b96a2a8345b"`, `data-wf-intellimize-customer-id="117114932"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero1_wrap> — `The last travel agent you’ll ever `)**:
   - Landmark `<section class="hero1_wrap u-gradient-bg-1">` presenting display lead `The last travel agent you’ll ever need.` and copy excerpt *"Serko learns how you like to travel, finds the best flights and h"* over `#e8f3fe` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.col3_wrap> — `AI travel agent for business`)**:
   - Landmark `<section class="col3_wrap">` rendering section `AI travel agent for business` with copy *"Venue, location, address..."*, asset references (`cdn.prod.website-files.com`, `serko-ai.webflow.shared.96cab25cb...`, `serko-ai.webflow.6aa12b65e6dd0b96...`, `clientParamBuilder.bundle.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.feature1_wrap> — `How Serko.ai works`)**:
   - Landmark `<section class="feature1_wrap u-background-3">` framing `How Serko.ai works` and `Business travel, booked in one chat.` (*"Trip details and preferences"*) with `#ebebeb` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.osano-cm-window> — `https://www.serko.ai`)**:
   - Landmark `<footer class="osano-cm-window">` anchoring `Serko.ai · AI Travel Agent for B` footer links (`Home · Platform · For companies · About · Sign up free`), copy *"Whether you’ve got a big client meeting in New York this Fri"*, and `#d8d8d8` structural dividers.
