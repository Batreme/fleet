---
title: "UI & UX Architecture: f-list-cleancreatives-org"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: f-list-cleancreatives-org

## Overview & Design Identity
- **Target**: `f-list-cleancreatives-org` (**F-List 2026**)
- **Production URL**: [https://f-list.cleancreatives.org/](https://f-list.cleancreatives.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1d1d1d` ink, `#ffff00` accent)
- **Summary**: Search the F-List 2026 to uncover the 802 advertising and PR agencies behind 1,321 documented fossil fuel contracts worldwide.
- **Total Clean CSS Variables Extracted**: `56` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `roc-grotesk-compressed`
- **Body Font Stack**: `roc-grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 132.951px`, `line-height: 99.7133px`, `font-weight: 700`); rule `,.h1` (`font-size: 4.5rem`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 86.1638px`, `line-height: 73.2393px`, `font-weight: 600`); rule `h2` (`font-size: 17px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-longform-paragraph-margin: 2.125rem 0 0 0`, `--cmplz_category_body_font_size: 12px`; rule `p` (`font-size: 16px`, `line-height: 24px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `small` (`line-height: 100%`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1d1d1d` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#edcc4b` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `header nav a:hover { color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#edcc4b` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f2f2f2` | `var(--cmplz_banner_border_color)` in `:root` |
| **Variable Token (`--fl-grey-1`)** | `#cacaca` | `var(--fl-grey-1)` in `:root` |
| **Variable Token (`--fl-grey-2`)** | `#7d7d7d` | `var(--fl-grey-2)` in `:root` |
| **Variable Token (`--fl-cream`)** | `#eceae3` | `var(--fl-cream)` in `:root` |
| **Variable Token (`--fl-green`)** | `#5da279` | `var(--fl-green)` in `:root` |
| **Variable Token (`--fl-red`)** | `#ff5037` | `var(--fl-red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fl-black-pure` | `#1D1D1D` | Canvas / Surface Token |
| `--fl-black-text` | `#1D1D1D` | Canvas / Surface Token |
| `--fl-white` | `#FFF` | Canvas / Surface Token |
| `--fl-grey-1` | `#CACACA` | Color / Atmospheric Token |
| `--fl-grey-2` | `#7D7D7D` | Color / Atmospheric Token |
| `--fl-cream` | `#ECEAE3` | Color / Atmospheric Token |
| `--fl-yellow` | `#EDCC4B` | Color / Atmospheric Token |
| `--fl-green` | `#5DA279` | Color / Atmospheric Token |
| `--fl-red` | `#FF5037` | Color / Atmospheric Token |
| `--font-longform-family` | `"roc-grotesk", sans-serif` | Typography / Scale Token |
| `--font-longform-line-height` | `165%` | Typography / Scale Token |
| `--font-longform-size` | `1.25rem` | Typography / Scale Token |
| `--font-longform-style` | `normal` | Typography / Scale Token |
| `--font-longform-weight` | `400` | Typography / Scale Token |
| `--font-longform-weight-bold` | `600` | Typography / Scale Token |
| `--font-longform-paragraph-margin` | `2.125rem 0 0 0` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.browser-chrome> — `f-list-cleancreatives-org`)**:
   - Landmark `<header class="browser-chrome">` (`1440x95px`) hosting `F-List 2026` navigation (`The report · The F-List · Dirty work · Take Action`), DOM attributes (`data-cmplz="1"`, `data-nosnippet="true"`, `data-prefix="fas"`, `data-icon="times"`), and stylesheet rule `opular_post_widget .icon-comment:... { content: "\e900"; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `THE CREATIVE COVER-UP`)**:
   - Landmark `<section class="hero home">` presenting display lead `THE CREATIVE COVER-UP` and copy excerpt *"The agencies providing cover for the fossil fuel industry."* over `#ffffff` canvas and `#1d1d1d` ink.
3. **Primary Showcase & Content Grid (<section.call-intro> — `The Creative Cover-up`)**:
   - Landmark `<section class="call-intro flex">` rendering section `The Creative Cover-up` with copy *"Functional Always active"*, asset references (`xmlrpc.php`, `www.googletagmanager.com`, `flist2026.b-cdn.net`, `embed`), and grid rule `s_popular_post_widget .icon-chat:... { content: "\e900"; }`.
4. **Interactive Detail & Feature Matrix (<section.redacted> — `Functional Always active`)**:
   - Landmark `<section class="redacted bg-cream">` framing `Functional Always active` and `The technical storage or access is strictly nece` (*"The technical storage or access is strictly necessary for the leg"*) with `#edcc4b` surface cards, `#ffff00` accents, and `s_popular_post_widget .icon-talk:... { content: "\e900"; }`.
5. **Colophon & Global Directory Footer (<footer.page-template> — `https://f-list.cleancreatives.org/`)**:
   - Landmark `<footer class="page-template">` anchoring `F-List 2026` footer links (`The report · The F-List · Dirty work · Take Action`), copy *"The technical storage or access is necessary for the legitim"*, and `#f2f2f2` structural dividers.
