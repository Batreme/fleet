---
title: "UI & UX Architecture: southandstonestudio-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: southandstonestudio-com

## Overview & Design Identity
- **Target**: `southandstonestudio-com` (**South & Stone Studio · Web Design & Brand Identity**)
- **Production URL**: [http://southandstonestudio.com](http://southandstonestudio.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff9900`)
- **Summary**: Websites written and built by Kelli Covey, a novelist and designer. Custom sites and brand identities for small businesses, with prices p...
- **Total Clean CSS Variables Extracted**: `140` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80.64px`, `line-height: 72.576px`, `font-weight: 780`, `letter-spacing: -2.8224px`); CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: clamp(2.7rem,7.6vw,8.2rem)`, `line-height: .92`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 106.56px`, `line-height: 101.232px`, `font-weight: 780`, `letter-spacing: -3.7296px`); rule `h2` (`font-size: clamp(1.5rem,2.4vw,2rem)`, `line-height: 1.1`, `letter-spacing: -.02em`, `font-weight: 760`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 1em`, `line-height: 1.8`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: .85rem`, `font-weight: 650`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#673de6` | `.hostinger-reach-block-dialog__... { background: #673de6 }` |
| **Interactive Accent / Highlight** | `#ff9900` | `.wp-social-link-amazon { color: #ff9900 }` |
| **Secondary / Muted Copy** | `#7a7a7a` | `var(--e-global-color-text)` in `:root` |
| **Structural Hairline Border** | `#252422` | `var(--sx-line-d)` in `:root` (`rgba(232,225,211,.16)`) |
| **Variable Token (`--edd-blocks-light-grey`)** | `#eeeeee` | `var(--edd-blocks-light-grey)` in `:root` |
| **Variable Token (`--sx-raise`)** | `#121212` | `var(--sx-raise)` in `:root` |
| **Variable Token (`--sx-bone`)** | `#e8e1d3` | `var(--sx-bone)` in `:root` |
| **Variable Token (`--sx-bone-2`)** | `#dcd3c1` | `var(--sx-bone-2)` in `:root` |
| **Variable Token (`--sx-red`)** | `#e1251b` | `var(--sx-red)` in `:root` |
| **Variable Token (`--sx-red-ink`)** | `#b3170f` | `var(--sx-red-ink)` in `:root` |
| **Variable Token (`--sx-red-lit`)** | `#ff5146` | `var(--sx-red-lit)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--edd-blocks-light-grey` | `#eee` | Canvas / Surface Token |
| `--wp--style--global--content-size` | `800px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1200px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--sx-serif` | `"Instrument Serif",Georgia,"Times New Roman",serif` | Typography / Scale Token |
| `--sx-hand` | `"Caveat","Segoe Print","Bradley Hand",cursive` | Design System Custom Token |
| `--sx-black` | `#000` | Canvas / Surface Token |
| `--sx-raise` | `#121212` | Color / Atmospheric Token |
| `--sx-bone` | `#E8E1D3` | Color / Atmospheric Token |
| `--sx-bone-2` | `#DCD3C1` | Color / Atmospheric Token |
| `--sx-white` | `#fff` | Canvas / Surface Token |
| `--sx-red` | `#E1251B` | Color / Atmospheric Token |
| `--sx-red-ink` | `#B3170F` | Typography Ink Token |
| `--sx-red-lit` | `#FF5146` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sx-head> — `southandstonestudio-com`)**:
   - Landmark `<header class="sx-head">` (`1440x76px`) hosting `South & Stone Studio · Web Design & ` navigation (`Services · Portfolio · Industries · Estimate Desk · Shop`), DOM attributes (`data-domain="southandstonestudio.com"`, `data-elementor-device-mode="desktop"`, `data-sx-industry`, `data-trade="contractors"`), and stylesheet rule `.hostinger-reach-block-connect__t... { color:1d1e20;font-weight:700;margin-bottom:4px }`.
2. **Hero Stage & Focal Lead (<section.sx-hero> — `Every website has a better version`)**:
   - Landmark `<section class="sx-hero">` presenting display lead `Every website has a better version.` and copy excerpt *"Booking projects now Written & built by Kelli Covey Fort Myers, F"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.sx-sec> — `Booking projects now Written & bui`)**:
   - Landmark `<section class="sx-sec sx-t-bone">` rendering section `Booking projects now Written & built by Kelli Co` with copy *"Try the live demo Holloway Home Repair"*, asset references (`cdn-reach.hostinger.com`, `js.stripe.com`, `embed`, `south-stone-favicon.png`), and grid rule `hostinger-reach-block-connect__su... { color:727586;margin-bottom:4px }`.
4. **Interactive Detail & Feature Matrix (<section.sx-fst-band> — `Try the live demo Holloway Home Re`)**:
   - Landmark `<section class="sx-fst-band">` framing `Try the live demo Holloway Home Repair` and `Websites for contractors from $1,250` (*"Websites for contractors from $1,250"*) with `#673de6` surface cards, `#ff9900` accents, and `.hostinger-reach-block-connect a { color:rgba(var(--bs-link-color-rgb), var(--bs-link-opacity, 1));text-dec... }`.
5. **Colophon & Global Directory Footer (<footer.sx-foot> — `http://southandstonestudio.com`)**:
   - Landmark `<footer class="sx-foot">` anchoring `South & Stone Studio · Web Desig` footer links (`Services · Portfolio · Industries · Estimate Desk · Shop`), copy *"Eight concept sites see Meridian Contracting"*, and `#252422` structural dividers.
