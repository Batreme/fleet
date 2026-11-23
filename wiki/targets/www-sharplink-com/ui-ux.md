---
title: "UI & UX Architecture: www-sharplink-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-sharplink-com

## Overview & Design Identity
- **Target**: `www-sharplink-com` (**Sharplink : Home**)
- **Production URL**: [https://www.sharplink.com/](https://www.sharplink.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f7f5` / `#0e76ff`)
- **Summary**: Sharplink is the institutional-grade Ethereum treasury platform giving investors a smarter, more productive access vehicle to ETH
- **Total Clean CSS Variables Extracted**: `590` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 88px`, `line-height: 84.48px`, `font-weight: 400`, `letter-spacing: -2.64px`); rule `,h1` (`font-size: 88px`, `line-height: .96`, `letter-spacing: -2.64px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 68px`, `line-height: 72.08px`, `font-weight: 400`, `letter-spacing: -1.36px`); rule `,h2` (`font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.35`, `letter-spacing: 0`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f7f5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `:after { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#0e76ff` | `var(--brand-blue-primary)` in `:root` |
| **Secondary / Muted Copy** | `#a9a9a9` | `var(--grey-secondary)` in `:root` |
| **Structural Hairline Border** | `#dededc` | `var(--stroke-black-10)` in `:root` (`rgba(0,0,0,.1)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--layout-columns-count` | `4` | Layout / Spatial Grid Token |
| `--layout-columns-gap` | `16px` | Layout / Spatial Grid Token |
| `--layout-rows-gap` | `8px` | Layout / Spatial Grid Token |
| `--layout-margin` | `16px` | Layout / Spatial Grid Token |
| `--layout-width` | `calc(100vw - var(--layout-margin)*2)` | Layout / Spatial Grid Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--black-0` | `transparent` | Canvas / Surface Token |
| `--black-5` | `rgb(0 0 0/5%)` | Canvas / Surface Token |
| `--black-10` | `rgba(0,0,0,.1)` | Canvas / Surface Token |
| `--black-15` | `rgba(0,0,0,.15)` | Canvas / Surface Token |
| `--black-20` | `rgba(0,0,0,.2)` | Canvas / Surface Token |
| `--black-25` | `rgba(0,0,0,.25)` | Canvas / Surface Token |
| `--black-30` | `rgba(0,0,0,.3)` | Canvas / Surface Token |
| `--black-35` | `rgba(0,0,0,.35)` | Canvas / Surface Token |
| `--black-40` | `rgba(0,0,0,.4)` | Canvas / Surface Token |
| `--black-45` | `rgba(0,0,0,.45)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-sharplink-com`)**:
   - Landmark `<header class="site-header theme-dark">` (`1440x98px`) hosting `Sharplink : Home` navigation (`Home · About · Investors · Opportunity · News`), DOM attributes (`data-v-00374420`, `data-v-e2147945`, `data-v-9d8fa70e`, `data-v-15fa0cd1`), and stylesheet rule `.body-large { font-size:19px;font-style:normal;line-height:1.35 }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Ethereum with an Edge`)**:
   - Landmark `<section class="home-hero mobile-only">` presenting display lead `Ethereum with an Edge` and copy excerpt *"Ethereum for Everyone,Engineered to Compound."* over `#f7f7f5` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.home-productivity> — `Please enable JavaScript`)**:
   - Landmark `<section class="home-productivity">` rendering section `Please enable JavaScript` with copy *"SharpLink is proudly listed on NASDAQ under the trading symbol SB"*, asset references (`entry.097ojG-J.css`, `Content.DYtseY0i.css`, `colors.DCDPWAmH.css`, `Wrapper.CA5eSekD.css`), and grid rule `.body-blog { font-size:16px;font-style:medium;line-height:1.56 }`.
4. **Interactive Detail & Feature Matrix (<section.wrapped-hero> — `This website requires JavaScript i`)**:
   - Landmark `<section class="home-hero wrapped-hero">` framing `This website requires JavaScript in order to work...` and `Investors Investors` (*"Investors Investors"*) with `#ffffff` surface cards, `#0e76ff` accents, and `.mono { font-size:13px;font-weight:500 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.sharplink.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Sharplink : Home` footer links (`Home · About · Investors · Opportunity · News`), copy *"Opportunity Opportunity"*, and `#dededc` structural dividers.
