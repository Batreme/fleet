---
title: "UI & UX Architecture: www-flatlineagency-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-flatlineagency-com

## Overview & Design Identity
- **Target**: `www-flatlineagency-com` (**Shopify, Marketing & AI Agency Amsterdam · Flatline**)
- **Production URL**: [https://www.flatlineagency.com/](https://www.flatlineagency.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3f0e9` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: Flatline is a Shopify Platinum Partner in Amsterdam. We build, migrate and grow Shopify Plus stores and run marketing and AI for premium...
- **Total Clean CSS Variables Extracted**: `48` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Canela Web Thin`
- **Body Font Stack**: `Canela Web Thin Placeholder`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 72px`, `font-weight: 100`); CSS variables `--text-truncation-display-inline-for-safari-16: inline`, `--text-truncation-display-none-for-safari-16: none`; rule `h1` (`font-size: 80px`, `line-height: 90%`, `letter-spacing: 0em`, `font-weight: 100`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 72px`, `font-weight: 100`); rule `h2` (`font-size: 40px`, `line-height: 1em`, `letter-spacing: 0px`, `font-weight: 100`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f0e9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#050505` | `var(--selection-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dedbd6` | `var(--border-color)` in `:root` (`8883`) |
| **Variable Token (`--token-715d5f28-67a4-4211-a580-93fd5f080aaa`)** | `#fdfaf5` | `var(--token-715d5f28-67a4-4211-a580-93fd5f080aaa)` in `:root` |
| **Variable Token (`--token-a1931803-7cdb-4638-b54d-105fe7944f17`)** | `#ece9e0` | `var(--token-a1931803-7cdb-4638-b54d-105fe7944f17)` in `:root` |
| **Variable Token (`--token-9218c30c-f55e-4ab0-8878-b6991b7cf484`)** | `#0a2315` | `var(--token-9218c30c-f55e-4ab0-8878-b6991b7cf484)` in `:root` |
| **Variable Token (`--token-054adc8c-fb63-490f-a5ca-c48666fdfb8c`)** | `#060f23` | `var(--token-054adc8c-fb63-490f-a5ca-c48666fdfb8c)` in `:root` |
| **Variable Token (`--token-758cee22-2452-4bed-9dbf-0b445d8c6457`)** | `#afdbf6` | `var(--token-758cee22-2452-4bed-9dbf-0b445d8c6457)` in `:root` |
| **Variable Token (`--token-84e9d4de-a1f9-41a3-90c4-b17803185d3f`)** | `#4cc352` | `var(--token-84e9d4de-a1f9-41a3-90c4-b17803185d3f)` in `:root` |
| **Variable Token (`--token-523425b1-9af9-406c-86b2-b80d42d167c2`)** | `#ff2142` | `var(--token-523425b1-9af9-406c-86b2-b80d42d167c2)` in `:root` |
| **Variable Token (`--token-3f6d4d2a-4271-4963-bcc0-922062838b2e`)** | `#0003` | `var(--token-3f6d4d2a-4271-4963-bcc0-922062838b2e)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-ee10f296-15d9-41da-871d-89b364a646e0` | `#f3f0e9` | Color / Atmospheric Token |
| `--token-715d5f28-67a4-4211-a580-93fd5f080aaa` | `#fdfaf5` | Color / Atmospheric Token |
| `--token-a1931803-7cdb-4638-b54d-105fe7944f17` | `#ece9e0` | Color / Atmospheric Token |
| `--token-1efbab02-5753-4dc6-9b5a-17f4306b9402` | `#000` | Color / Atmospheric Token |
| `--token-417808d0-1dfe-483f-9164-e0725b1b82a7` | `#050505` | Color / Atmospheric Token |
| `--token-9218c30c-f55e-4ab0-8878-b6991b7cf484` | `#0a2315` | Color / Atmospheric Token |
| `--token-054adc8c-fb63-490f-a5ca-c48666fdfb8c` | `#060f23` | Color / Atmospheric Token |
| `--token-758cee22-2452-4bed-9dbf-0b445d8c6457` | `#afdbf6` | Color / Atmospheric Token |
| `--token-84e9d4de-a1f9-41a3-90c4-b17803185d3f` | `#4cc352` | Color / Atmospheric Token |
| `--token-523425b1-9af9-406c-86b2-b80d42d167c2` | `#ff2142` | Color / Atmospheric Token |
| `--token-3f6d4d2a-4271-4963-bcc0-922062838b2e` | `#0003` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.framer-ha9xM> — `www-flatlineagency-com`)**:
   - Landmark `<header class="framer-ha9xM framer-1sgxrsx">` (`1440x100px`) hosting `Shopify, Marketing & AI Agency Amste` navigation (`What we do · Work · About · Insights · Events`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-generated-hreflang`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-yjze81> — `THE LUXURY STANDARD IN DIGITAL`)**:
   - Landmark `<section class="framer-yjze81">` presenting display lead `THE LUXURY STANDARD IN DIGITAL` and copy excerpt *"We build and run the digital side of premium consumer brands."* over `#f3f0e9` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.framer-yjze81:nth(2)> — `Elevating modern menswear through `)**:
   - Landmark `<section class="framer-yjze81">` rendering section `Elevating modern menswear through a refined digit...` with copy *"350+ Shopify Plus migrations"*, asset references (`goPYDmczsQmWoGJRaZvSdomTZc.png`, `fonts.gstatic.com`, `script`, `gv5TmFnYtTK9GLZ9FjU09gs1guk.mp4`), and grid rule `.hidden-19c8o6d { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-yjze81:nth(3)> — `Powering a smoother digital journe`)**:
   - Landmark `<section class="framer-yjze81">` framing `Powering a smoother digital journey for cycling e...` and `Crafting a premium digital home for contemporary...` (*"2x Agency of the Year"*) with `#050505` surface cards, `#0000ee` accents, and `.hidden-1us1r0u { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-uH155> — `https://www.flatlineagency.com/`)**:
   - Landmark `<footer class="framer-uH155 framer-gkoC1">` anchoring `Shopify, Marketing & AI Agency A` footer links (`What we do · Work · About · Insights · Events`), copy *"Omnichannel eCommerce, where every touchpoint is united"*, and `#dedbd6` structural dividers.
