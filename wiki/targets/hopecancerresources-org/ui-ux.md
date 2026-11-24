---
title: "UI & UX Architecture: hopecancerresources-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: hopecancerresources-org

## Overview & Design Identity
- **Target**: `hopecancerresources-org` (**Hope Cancer Resources - Support. Educate. Prevent.**)
- **Production URL**: [https://hopecancerresources.org/](https://hopecancerresources.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×5796px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ff` accent)
- **Summary**: Providing free cancer support services through counseling, transportation, financial assistance, personal training, tobacco treatment, &...
- **Total Clean CSS Variables Extracted**: `32` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `BrandonText`
- **Body Font Stack**: `BrandonText`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 100px`, `line-height: 100px`, `font-weight: 800`); rule `h1` (`font-size: 2rem`, `line-height: 1`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50px`, `line-height: 57.5px`, `font-weight: 800`); rule `h2` (`font-size: clamp(1.6rem,5vw,3rem)`, `font-weight: 900`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: 11.5px`, `font-weight: 400`); rule `p` (`font-size: 2rem`, `line-height: 1.5`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: 11.5px`, `font-weight: 400`); CSS variables `--dbcqt-small-desktop-columns: minmax(clamp(208px, 22vw, 248px), 1.05fr) minmax(0, 1.1fr) 135px 40px`; rule `.label` (`font-size: 1rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `main` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#edf1f4` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.link { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#476577` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#b0c5dc` | `hr { border-top: #b0c5dc }` |
| **Variable Token (`--color-brand-black`)** | `#0e1829` | `var(--color-brand-black)` in `:root` |
| **Variable Token (`--color-brand-blue`)** | `#1b7aaf` | `var(--color-brand-blue)` in `:root` |
| **Variable Token (`--color-brand-lightblue`)** | `#1fa0e5` | `var(--color-brand-lightblue)` in `:root` |
| **Variable Token (`--color-brand-gray-500`)** | `#90a3bf` | `var(--color-brand-gray-500)` in `:root` |
| **Variable Token (`--color-notice-warning`)** | `#dc4b4b` | `var(--color-notice-warning)` in `:root` |
| **Variable Token (`--color-notice-success`)** | `#2db292` | `var(--color-notice-success)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-primary` | `"BrandonText", Arial, Helvetica, sans-serif` | Brand / Palette Token |
| `--font-heading` | `"BrandonText", Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--font-base` | `"SourceSans", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-serif` | `"EightiesComebackIt", "Times New Roman", "Garamond", serif` | Typography / Scale Token |
| `--color-brand-black` | `#0e1829` | Canvas / Surface Token |
| `--color-brand-blue` | `#1b7aaf` | Brand / Palette Token |
| `--color-brand-lightblue` | `#1fa0e5` | Canvas / Surface Token |
| `--color-brand-darkblue` | `#476577` | Canvas / Surface Token |
| `--color-brand-gray-500` | `#90a3bf` | Brand / Palette Token |
| `--color-light-gray` | `#476577` | Canvas / Surface Token |
| `--color-lightest-gray` | `#edf1f4` | Canvas / Surface Token |
| `--color-notice-warning` | `#dc4b4b` | Brand / Palette Token |
| `--color-notice-success` | `#2DB292` | Brand / Palette Token |
| `--color-primary` | `var(--color-brand-black)` | Brand / Palette Token |
| `--color-secondary` | `var(--color-brand-black)` | Brand / Palette Token |
| `--color-brand-text-base` | `var(--color-brand-black)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `hopecancerresources-org`)**:
   - Landmark `<header class="site-header template-home">` (`1440x60px`) hosting `Hope Cancer Resources - Support. Edu` navigation (`Shop for Hope · About Hope · Our Story · Our Foundation · Staff`), DOM attributes (`data-template="base.twig"`, `data-date-iso="2026-11-27CST05:43:16..."`, `data-types="Yoga"`, `data-date-iso="2026-11-30CST05:43:17..."`), and stylesheet rule `content { background:fff;background-size:100% }`.
2. **Hero Stage & Focal Lead (<article.post-type-page> — `Support. Educate. Prevent.`)**:
   - Landmark `<article class="post-type-page">` presenting display lead `Support. Educate. Prevent.` and copy excerpt *"Providing hope and healing through compassionate care, support, c"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.page_heading> — `Driving real Change in Northwest A`)**:
   - Landmark `<section class="page_heading section-block">` rendering section `Driving real Change in Northwest Arkansas (2025 R...` with copy *"Hope Cancer Resources"*, asset references (`gtm.js`, `style.css`, `humans.txt`, `xmlrpc.php`), and grid rule `ge-template-wp-content .default-h... { padding-top:100px }`.
4. **Interactive Detail & Feature Matrix (<section.stats_block_one> — `At Hope Cancer Resources, we walk `)**:
   - Landmark `<section class="stats_block_one section-block">` framing `At Hope Cancer Resources, we walk beside those fa...` and `Ways We Help` (*"We exist to soften the weight of a diagnosis—with every ride give"*) with `#edf1f4` surface cards, `#0000ff` accents, and `projects-template-default .post-h... { padding-top:80px }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://hopecancerresources.org/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Hope Cancer Resources - Support.` footer links (`Shop for Hope · About Hope · Our Story · Our Foundation · Staff`), copy *"We are dedicated to providing support for the journey and ed"*, and `#b0c5dc` structural dividers.
