---
title: "UI & UX Architecture: armor-bd-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: armor-bd-com

## Overview & Design Identity
- **Target**: `armor-bd-com` (**Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions**)
- **Production URL**: [https://armor-bd.com](https://armor-bd.com)
- **Final Redirected URL**: [https://www.armor-bd.com/](https://www.armor-bd.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#2d1f1a` / `#ea580c`)
- **Summary**: Armor Bangladesh Limited provides banking hardware and software — cash recyclers, ATMs, kiosks, UPS, payment switching and card managemen...
- **Total Clean CSS Variables Extracted**: `43` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Work Sans`
- **Body Font Stack**: `Unbounded`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 72px`, `font-weight: 700`, `letter-spacing: -1.8px`); rule `h1` (`font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 72px`, `font-weight: 700`); rule `h2` (`font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#2d1f1a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ea580c` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ea580c` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#faebe3` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2d201c` | `10 { border-color: #2d201c }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--toast-icon-margin-start` | `-3px` | Layout / Spatial Grid Token |
| `--toast-icon-margin-end` | `4px` | Layout / Spatial Grid Token |
| `--toast-svg-margin-start` | `-1px` | Layout / Spatial Grid Token |
| `--toast-svg-margin-end` | `0px` | Layout / Spatial Grid Token |
| `--toast-button-margin-start` | `auto` | Layout / Spatial Grid Token |
| `--toast-button-margin-end` | `0` | Layout / Spatial Grid Token |
| `--toast-close-button-start` | `0` | Design System Custom Token |
| `--toast-close-button-end` | `unset` | Design System Custom Token |
| `--toast-close-button-transform` | `translate(-35%, -35%)` | Dimension / Scale Token |
| `--gray1` | `hsl(0, 0%, 99%)` | Color / Atmospheric Token |
| `--gray2` | `hsl(0, 0%, 97.3%)` | Color / Atmospheric Token |
| `--gray3` | `hsl(0, 0%, 95.1%)` | Color / Atmospheric Token |
| `--gray4` | `hsl(0, 0%, 93%)` | Color / Atmospheric Token |
| `--gray5` | `hsl(0, 0%, 90.9%)` | Color / Atmospheric Token |
| `--gray6` | `hsl(0, 0%, 88.7%)` | Color / Atmospheric Token |
| `--gray7` | `hsl(0, 0%, 85.8%)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.rounded-full> — `armor-bd-com`)**:
   - Landmark `<nav class="rounded-full shadow-lg">` (`1280x56px`) hosting `Armor Bangladesh Limited — ATM, CRM ` navigation (`Products · Why us · About · Career · Contact`), DOM attributes (`data-discover="true"`, `data-discover="true"`, `data-discover="true"`, `data-discover="true"`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.lenis-smooth> — `Pioneering Banking Technology Solu`)**:
   - Landmark `<section class="lenis-smooth">` presenting display lead `Pioneering Banking Technology Solutions` and copy excerpt *"Trusted nationwide"* over `#2d1f1a` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Trusted nationwide`)**:
   - Landmark `<section class="relative overflow-hidden">` rendering section `Trusted nationwide` with copy *"Technology Solutions"*, asset references (`favicon.ico`, `index-CjIBsQtn.js`, `index-BvNfHRqr.css`, `HomeV2-CKyWaDQ7.js`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-6> — `Technology Solutions`)**:
   - Landmark `<section class="py-6 bg-primary">` framing `Technology Solutions` and `At Armor, we empower financial institutions to r` (*"At Armor, we empower financial institutions to reach new heights "*) with `#ea580c` surface cards, `#ea580c` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-primary> — `https://armor-bd.com`)**:
   - Landmark `<footer class="bg-primary text-secondary">` anchoring `Armor Bangladesh Limited — ATM, ` footer links (`Products · Why us · About · Career · Contact`), copy *"Specialized Technical Experts"*, and `#2d201c` structural dividers.
