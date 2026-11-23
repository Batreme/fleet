---
title: "UI & UX Architecture: www-banham-co-uk"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-banham-co-uk

## Overview & Design Identity
- **Target**: `www-banham-co-uk` (**Banham · Experts in Security Services Since 1926**)
- **Production URL**: [https://www.banham.co.uk/](https://www.banham.co.uk/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ff0000` accent)
- **Summary**: Welcome to Banham, market-leaders in the security industry since 1926, and the perfect people to help secure your property
- **Total Clean CSS Variables Extracted**: `138` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IvarHeadline`
- **Body Font Stack**: `IvarText`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`, `letter-spacing: 1.2px`); CSS variables `--dfd-btn-display: inline-flex`, `--dfd-btn-group-display: flex`; rule `,h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `letter-spacing: .36px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 30px`, `font-weight: 400`, `letter-spacing: 0.24px`); rule `,h2` (`font-size: 28px`, `line-height: 1.25`, `letter-spacing: .28px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: .875rem`, `line-height: 1.25rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `.label` (`font-size: 1rem`, `line-height: 1.5rem`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eeeeee` | live computed `p` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.dfd-btn-error { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#737678` | `var(--df-accent-secondary)` in `:root` |
| **Structural Hairline Border** | `#cbcccd` | `var(--df-neutral-outline)` in `:root` |
| **Variable Token (`--btn-stroke`)** | `#0000` | `var(--btn-stroke)` in `:root` |
| **Variable Token (`--btn-bg`)** | `#333e48` | `var(--btn-bg)` in `:root` |
| **Variable Token (`--btn-hover-bg`)** | `#2b3239` | `var(--btn-hover-bg)` in `:root` |
| **Variable Token (`--color-cornflower-100`)** | `#8392a7` | `var(--color-cornflower-100)` in `:root` |
| **Variable Token (`--color-amsb_graystarts`)** | `#cbd5e0` | `var(--color-amsb_graystarts)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--btn-stroke` | `#0000` | Elevation / Border Token |
| `--btn-bg` | `#333e48` | Canvas / Surface Token |
| `--btn-color` | `#fff` | Brand / Palette Token |
| `--btn-hover-bg` | `#2b3239` | Canvas / Surface Token |
| `--btn-active-bg` | `#2b3239` | Canvas / Surface Token |
| `--line-after` | `#000` | Color / Atmospheric Token |
| `--line-before` | `#0000` | Color / Atmospheric Token |
| `--width-am-latter` | `32px` | Layout / Spatial Grid Token |
| `--width-am-brand` | `120px` | Brand / Palette Token |
| `--width-am-popup-content` | `600px` | Layout / Spatial Grid Token |
| `--height-am-latter` | `32px` | Layout / Spatial Grid Token |
| `--height-am-popup-content` | `415px` | Layout / Spatial Grid Token |
| `--background-size-size20` | `20px` | Canvas / Surface Token |
| `--color-cornflower-100` | `#8392a7` | Brand / Palette Token |
| `--padding-full` | `100%` | Layout / Spatial Grid Token |
| `--color-amsb_graystarts` | `#cbd5e0` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.page-header> — `www-banham-co-uk`)**:
   - Landmark `<header class="page-header">` (`1425x0px`) hosting `Banham · Experts in Security Service` navigation (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), DOM attributes (`data-mm-order="40"`, `data-mm-order="50"`, `data-ueto="ueto_12e8e1f459"`, `data-hj-csq-tag`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.message> — `Protect What You Cherish`)**:
   - Landmark `<section class="message global">` presenting display lead `Protect What You Cherish` and copy excerpt *"Prefer to call? Reach us on 020 7819 3730"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.storyblok-home> — `Handcrafted in Britain Since 1926`)**:
   - Landmark `<section class="storyblok-home">` rendering section `Handcrafted in Britain Since 1926` with copy *"To celebrate 100 years of Banham, we went behind closed doors to "*, asset references (`styles.min.css`, `chosen.min.css`, `trustpilot.min.css`, `Banham_Logo_FA-04.png`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `Bespoke Doors`)**:
   - Landmark `<section class="fixed w-full">` framing `Bespoke Doors` and `Explore Banham` (*"Marrying innovation with time honoured techniques, every detail o"*) with `#eeeeee` surface cards, `#ff0000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.footer-container> — `https://www.banham.co.uk/`)**:
   - Landmark `<footer class="footer-container">` anchoring `Banham · Experts in Security Ser` footer links (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), copy *"Innovative, award-winning and precision engineered in Britai"*, and `#cbcccd` structural dividers.
