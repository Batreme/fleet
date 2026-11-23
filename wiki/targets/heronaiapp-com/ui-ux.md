---
title: "UI & UX Architecture: heronaiapp-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: heronaiapp-com

## Overview & Design Identity
- **Target**: `heronaiapp-com` (**Heron AI · Works inside your design tools**)
- **Production URL**: [https://heronaiapp.com/](https://heronaiapp.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#fa3600`)
- **Summary**: Heron sees your model, spots problems, and suggests fixes as you design. When you approve, it makes the edit itself, all without leaving...
- **Total Clean CSS Variables Extracted**: `43` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `BT Grotesk`
- **Body Font Stack**: `BT Grotesk`
- **Monospace / Technical Font Stack**: `Geistmono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 46.6667px`, `line-height: 46.6667px`, `font-weight: 700`, `letter-spacing: -0.933333px`); rule `h1` (`font-size: 7.2rem`, `line-height: 1em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 33.3333px`, `line-height: 33.3333px`, `font-weight: 600`, `letter-spacing: -0.666667px`); rule `h2` (`font-size: 2.4rem`, `line-height: 1.1em`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 13.3333px`, `line-height: 17.3333px`, `font-weight: 500`, `letter-spacing: -0.266667px`); rule `p` (`font-size: 1rem`, `line-height: 1.1em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11.6667px`, `line-height: 15.1667px`, `font-weight: 500`, `letter-spacing: -0.266667px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#282828` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#efefef` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#fa3600` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b4b4b0` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#b3b3af` | `var(--content--border)` in `:root` |
| **Variable Token (`--content--surface`)** | `#72726f` | `var(--content--surface)` in `:root` |
| **Variable Token (`--content--granite-gray`)** | `#626260` | `var(--content--granite-gray)` in `:root` |
| **Variable Token (`--content--secondary`)** | `#414140` | `var(--content--secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--content--terriary` | `#282828b8` | Color / Atmospheric Token |
| `--size--padding-hero` | `calc(4.4rem + 1rem*2)` | Layout / Spatial Grid Token |
| `--size--max-screen-height` | `calc(100dvh - 1.6rem)` | Layout / Spatial Grid Token |
| `--content--border` | `#b3b3af` | Elevation / Border Token |
| `--size--border` | `max(1px,.1rem)` | Layout / Spatial Grid Token |
| `--content--brand` | `#fa3600` | Brand / Palette Token |
| `--content--primary` | `#282828` | Brand / Palette Token |
| `--content--white` | `white` | Canvas / Surface Token |
| `--content--disable` | `#b4b4b0` | Color / Atmospheric Token |
| `--content--surface` | `#72726f` | Canvas / Surface Token |
| `--content--granite-gray` | `#626260` | Color / Atmospheric Token |
| `--content--transparent` | `transparent` | Design System Custom Token |
| `--content--secondary` | `#414140` | Brand / Palette Token |
| `--size--line` | `0px` | Layout / Spatial Grid Token |
| `--trans-percent` | `0%` | Dimension / Scale Token |
| `--mask-percent` | `0%` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `heronaiapp-com`)**:
   - Landmark `<header class="header">` (`1427x56px`) hosting `Heron AI · Works inside your design ` navigation (`Menu · Pricing Pricing · Insights Insights · About About`), DOM attributes (`data-wf-domain="heronai.webflow.io"`, `data-wf-page="6a4b5161f0d11f1602cc3ba1"`, `data-wf-site="6a4b5161f0d11f1602cc3bbf"`, `data-resources-saver-cleanup="branding"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `AN AI AGENT THAT WORKS INSIDE YOUR`)**:
   - Landmark `<section class="home-hero">` presenting display lead `AN AI AGENT THAT WORKS INSIDE YOUR DESIGN TOOLS` and copy excerpt *"This website uses cookies. LEARN MORE"* over `#ffffff` canvas and `#282828` ink.
3. **Primary Showcase & Content Grid (<section.home-intro> — `An AI agent that works inside your`)**:
   - Landmark `<section class="home-intro">` rendering section `An AI agent that works inside your design tools` with copy *"©2026 HERON AI. All rights reserved. Concept Crafted by Bearplus"*, asset references (`cdn.prod.website-files.com`, `heronai.webflow.shared.9f21166e0....`, `clarity.js`, `xxzxds4q6a`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.home-problem> — `T H E R E P E T I T I V E P A R T `)**:
   - Landmark `<section class="home-problem">` framing `T H E R E P E T I T I V E P A R T S O F M O D E L...` and `Your design tools do what you tell them, nothing...` (*"An AI agent that works inside your design tools"*) with `#efefef` surface cards, `#fa3600` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://heronaiapp.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Heron AI · Works inside your des` footer links (`Menu · Pricing Pricing · Insights Insights · About About`), copy *"T H E R E P E T I T I V E P A R T S O F M O D E L..."*, and `#b3b3af` structural dividers.
