---
title: "UI & UX Architecture: www-barebonescollective-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-barebonescollective-com

## Overview & Design Identity
- **Target**: `www-barebonescollective-com` (**Bare Bones Collective**)
- **Production URL**: [https://www.barebonescollective.com/](https://www.barebonescollective.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#333333` ink, `#ffcc00` accent)
- **Summary**: We are a creative agency that believes great brands are built through audacious work
- **Total Clean CSS Variables Extracted**: `184` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Oswald`
- **Body Font Stack**: `PT Serif`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 100px`, `line-height: 105px`, `font-weight: 700`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 75.6px`, `font-weight: 600`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#333333` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#ffcc00` | `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }` |
| **Secondary / Muted Copy** | `#ffd527` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--td176b92ada598f8f` | `initial` | Design System Custom Token |
| `--td851cd75a8793667` | `initial` | Design System Custom Token |
| `--tc58f4bf5a9869b3e` | `initial` | Design System Custom Token |
| `--t3a480c2f814ef19c` | `initial` | Design System Custom Token |
| `--t77e217518bcd986b` | `initial` | Design System Custom Token |
| `--tc5e0863356bf5767` | `initial` | Design System Custom Token |
| `--t7a2234c5eadde886` | `initial` | Design System Custom Token |
| `--td340014d093b0821` | `initial` | Design System Custom Token |
| `--tf8c80baf678711b8` | `initial` | Design System Custom Token |
| `--t2986df03ecf88759` | `initial` | Design System Custom Token |
| `--te0c856964146535b` | `initial` | Design System Custom Token |
| `--tf630d2cff7da8057` | `initial` | Design System Custom Token |
| `--tf69032263d26c015` | `initial` | Design System Custom Token |
| `--ta5930fb3c4c7209c` | `initial` | Design System Custom Token |
| `--t1f1729a8e756e8bf` | `initial` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-barebonescollective-com`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `Bare Bones Collective` navigation (`Menu · Work · Services · 360° Campaigns · films`), DOM attributes (`data-wf-domain="www.barebonescollecti..."`, `data-wf-page="68358a988d15891f5e5e5ab6"`, `data-wf-site="68358a988d15891f5e5e5aad"`, `data-w-id="21dd915e-a730-31e5-d8..."`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.menu_element> — `BARE`)**:
   - Landmark `<section class="menu_element">` presenting display lead `BARE` and copy excerpt *"We are a creative agency that believes great brands are built thr"* over `#ffffff` canvas and `#333333` ink.
3. **Primary Showcase & Content Grid (<section.logo_element> — `Bare Bones Collective Primary Show`)**:
   - Landmark `<section class="logo_element">` rendering section `Bare Bones Collective Primary Showcase` with copy *"BARE"*, asset references (`cdn.prod.website-files.com`, `bare-bones-collective.webflow.sha...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-hero> — `www-barebonescollective-com Intera`)**:
   - Landmark `<section class="section-hero">` framing `www-barebonescollective-com Interactive Matrix` and `www-barebonescollective-com Archive & Directory` (*"Bare Bones Collective Primary Showcase"*) with `#ffff00` surface cards, `#ffcc00` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-oswald-n2-active> — `https://www.barebonescollective.com/`)**:
   - Landmark `<footer class="wf-oswald-n2-active">` anchoring `Bare Bones Collective` footer links (`Menu · Work · Services · 360° Campaigns · films`), copy *"www-barebonescollective-com Interactive Matrix"*, and `#e2e2e2` structural dividers.
