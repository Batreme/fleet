---
title: "UI & UX Architecture: www-undplus-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-undplus-com

## Overview & Design Identity
- **Target**: `www-undplus-com` (**UNDPLUS — Brand Architecture & Spatial Design Studio**)
- **Production URL**: [https://www.undplus.com](https://www.undplus.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ca9df1` accent)
- **Summary**: Studio for brand architecture, spatial design and live experiences. We build trade fair booths, brand spaces and installations from Berli...
- **Total Clean CSS Variables Extracted**: `29` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins Bold`
- **Body Font Stack**: `Magiel Black`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 52px`, `line-height: 62.4px`, `font-weight: 700`); rule `h1` (`font-size: 108px`, `line-height: 1.1em`, `letter-spacing: 0em`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 205px`, `line-height: 184.5px`, `font-weight: 900`, `letter-spacing: 14.35px`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 1.6em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 52px`, `line-height: 62.4px`, `font-weight: 500`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffd650` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ca9df1` | `r-styles-preset-5qir1a.rich-tex... { color: #ca9df1 }` |
| **Secondary / Muted Copy** | `#0099ff` | `.framer-AYmJg .framer-1dooqsd { color: #0099ff }` |
| **Structural Hairline Border** | `#0099ff` | hairline divider derived from `.framer-AYmJg .framer-1dooqsd { color: #0099ff }` |
| **Variable Token (`--token-fb37ef9f-b04f-4314-9731-cff242a9823b`)** | `#93d4f2` | `var(--token-fb37ef9f-b04f-4314-9731-cff242a9823b)` in `:root` |
| **Variable Token (`--token-86e11354-2bd9-45a6-a3ed-8f01f856a058`)** | `#0daa75` | `var(--token-86e11354-2bd9-45a6-a3ed-8f01f856a058)` in `:root` |
| **Variable Token (`--token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a`)** | `#f3c6b1` | `var(--token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a)` in `:root` |
| **Variable Token (`--token-54b8b414-a4ad-4bad-a655-869fc0cbd561`)** | `#f08fc7` | `var(--token-54b8b414-a4ad-4bad-a655-869fc0cbd561)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-832a9c22-d657-4637-89aa-cbcc712eb257` | `#ca9df1` | Color / Atmospheric Token |
| `--token-d9ed1eb8-0c54-4136-bf85-5e5373c04bfa` | `#ffd650` | Color / Atmospheric Token |
| `--token-fb37ef9f-b04f-4314-9731-cff242a9823b` | `#93d4f2` | Color / Atmospheric Token |
| `--token-86e11354-2bd9-45a6-a3ed-8f01f856a058` | `#0daa75` | Color / Atmospheric Token |
| `--token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a` | `#f3c6b1` | Color / Atmospheric Token |
| `--token-54b8b414-a4ad-4bad-a655-869fc0cbd561` | `#f08fc7` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |
| `--line-height` | `var(--framer-line-height)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.framer-dYpKI> — `www-undplus-com`)**:
   - Landmark `<header class="framer-dYpKI">` (`1440px`) hosting `UNDPLUS — Brand Architecture & Spati` navigation (`Brand Architecture · Retail & Hospitality · Workplace & New Work · More projects`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-ap504g> — `UNDPLUS Studio for brand experienc`)**:
   - Landmark `<section class="framer-ap504g">` presenting display lead `UNDPLUS Studio for brand experiences in real life` and copy excerpt *"or just the degree you need."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.framer-AYmJg> — `or just the degree you need.`)**:
   - Landmark `<section class="framer-AYmJg">` rendering section `or just the degree you need.` with copy *"brand experiences in real life b r a n d e x p e r i e n c e s i "*, asset references (`cXo2Pf7EWgS5at03i8N3qhgZg.svg`, `S6PCFl3VKfoljDTPsWBO3MD8eps.svg`, `script`, `U2mu30OyPRwHZ1Hq7pp8ryGs.mp4`), and grid rule `.hidden-pfdayg { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-3gfgd> — `brand experiences in real life b r`)**:
   - Landmark `<section class="framer-3gfgd">` framing `brand experiences in real life b r a n d e x p e` and `brand experiences in real life` (*"brand experiences in real life"*) with `#ffd650` surface cards, `#ca9df1` accents, and `.hidden-9alzb1 { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-LFW7G> — `https://www.undplus.com`)**:
   - Landmark `<footer class="framer-LFW7G">` anchoring `UNDPLUS — Brand Architecture & S` footer links (`Brand Architecture · Retail & Hospitality · Workplace & New Work · More projects`), copy *"b r a n d e x p e r i e n c e s i n r e a l l i f e"*, and `#0099ff` structural dividers.
