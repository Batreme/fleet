---
title: "UI & UX Architecture: opportunity-waltonfamilyfoundation-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: opportunity-waltonfamilyfoundation-org

## Overview & Design Identity
- **Target**: `opportunity-waltonfamilyfoundation-org` (**Access to Opportunity: Gallup Research · Walton Family Foundation**)
- **Production URL**: [https://opportunity.waltonfamilyfoundation.org/](https://opportunity.waltonfamilyfoundation.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#e7e72b`)
- **Summary**: Explore Walton Family Foundation and Gallup research on opportunity. See how investments in education, nature, and communities help oppor...
- **Total Clean CSS Variables Extracted**: `74` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SerrifCompressed`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 212.543px`, `line-height: 191.289px`, `font-weight: 400`, `letter-spacing: -3.825px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50.5422px`, `line-height: 50.5422px`, `font-weight: 400`, `letter-spacing: -0.96px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#12110e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `.bg-yellow { background-color: yellow }` (`#ffff00`) |
| **Interactive Accent / Highlight** | `#e7e72b` | `var(--highlight)` in `:root` |
| **Secondary / Muted Copy** | `#e7e72b` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ff7f7f` | `50 { border-color: #ff7f7f }` |
| **Variable Token (`--green`)** | `#5f8763` | `var(--green)` in `:root` |
| **Variable Token (`--teal`)** | `#337c83` | `var(--teal)` in `:root` |
| **Variable Token (`--blue`)** | `#5a7580` | `var(--blue)` in `:root` |
| **Variable Token (`--yellow`)** | `#cb9a56` | `var(--yellow)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--z-footer` | `10` | Elevation / Border Token |
| `--z-main` | `20` | Elevation / Border Token |
| `--z-header` | `30` | Layout / Spatial Grid Token |
| `--z-context-cta` | `300` | Typography Ink Token |
| `--z-progress-bar` | `400` | Elevation / Border Token |
| `--z-menu-mask` | `500` | Elevation / Border Token |
| `--z-menu` | `600` | Elevation / Border Token |
| `--z-menu-button` | `700` | Elevation / Border Token |
| `--z-image-scatter` | `200` | Elevation / Border Token |
| `--z-cinematic-scroll` | `100` | Elevation / Border Token |
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#12110e` | Typography Ink Token |
| `--green` | `#5f8763` | Color / Atmospheric Token |
| `--teal` | `#337c83` | Color / Atmospheric Token |
| `--blue` | `#5a7580` | Color / Atmospheric Token |
| `--yellow` | `#cb9a56` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.antialiased> — `opportunity-waltonfamilyfoundation-org`)**:
   - Landmark `<header class="antialiased">` (`1440x0px`) hosting `Access to Opportunity: Gallup Resear` navigation (`Privacy Policy · Terms of Use`), DOM attributes (`data-precedence="next"`, `data-lenis-prevent="true"`, `data-gtm-vis-polling-id252455071_20="69"`, `data-menu-background="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.lenis> — `WHERE OPPORTUNITY TAKES ROOT`)**:
   - Landmark `<section class="lenis">` presenting display lead `WHERE OPPORTUNITY TAKES ROOT` and copy excerpt *"To build choice-filled lives. Our work helps create access to opp"* over `#ffffff` canvas and `#12110e` ink.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Where opportunity takes root`)**:
   - Landmark `<section class="bg-background">` rendering section `Where opportunity takes root` with copy *"The conditions that shape opportunity change over time. So we ask"*, asset references (`03_wvljxzi0as.css`, `0ji28_e_~fdtg.js`, `0nz2u-qe8z68i.js`, `0yjw-7sa79pfd.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.text-foreground> — `Opportunity enables people to fulf`)**:
   - Landmark `<section class="text-foreground">` framing `Opportunity enables people to fulfill their highe...` and `What does opportunity mean today? What does oppor...` (*"Our partners at Gallup asked the American people to share their i"*) with `#ffff00` surface cards, `#e7e72b` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.inset-x-0> — `https://opportunity.waltonfamilyfoundation.org/`)**:
   - Landmark `<footer class="inset-x-0 bottom-0">` anchoring `Access to Opportunity: Gallup Re` footer links (`Privacy Policy · Terms of Use`), copy *"This is what they had to say."*, and `#ff7f7f` structural dividers.
