---
title: "UI & UX Architecture: mrcresidencesbocaraton-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: mrcresidencesbocaraton-com

## Overview & Design Identity
- **Target**: `mrcresidencesbocaraton-com` (**Mr. C Residences Boca Raton · New Luxury Residences for Sale**)
- **Production URL**: [https://mrcresidencesbocaraton.com](https://mrcresidencesbocaraton.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#a73c38` canvas, `#ffffff` ink, `#000000` accent)
- **Summary**: 133 impeccably designed two- and three-bedroom residences in Downtown Boca Raton, featuring elevated design and a lifestyle defined by Mr...
- **Total Clean CSS Variables Extracted**: `14` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat-Regular`
- **Body Font Stack**: `Montserrat-SemiBold`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 42px`, `line-height: 48.3px`, `font-weight: 400`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 14px`, `line-height: 1.6em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `p` (`font-size: 11px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#a73c38` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.hero_wrap .parallax_wrap .tint... { background: #000000 }` |
| **Interactive Accent / Highlight** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#000000` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dddddd` | `var(--border-color)` in `:root` |
| **Variable Token (`--text-color`)** | `#111111` | `var(--text-color)` in `:root` |
| **Variable Token (`--head-bg-color`)** | `#d9edf7` | `var(--head-bg-color)` in `:root` |
| **Variable Token (`--even-bg-color`)** | `#f9f9f9` | `var(--even-bg-color)` in `:root` |
| **Variable Token (`--hover-bg-color`)** | `#f3f3f3` | `var(--hover-bg-color)` in `:root` |
| **Variable Token (`--head-active-bg-color`)** | `#049cdb` | `var(--head-active-bg-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-color` | `#111` | Typography Ink Token |
| `--head-text-color` | `var(--text-color)` | Typography Ink Token |
| `--head-bg-color` | `#d9edf7` | Canvas / Surface Token |
| `--odd-text-color` | `var(--text-color)` | Typography Ink Token |
| `--odd-bg-color` | `#fff` | Canvas / Surface Token |
| `--even-text-color` | `var(--text-color)` | Typography Ink Token |
| `--even-bg-color` | `#f9f9f9` | Canvas / Surface Token |
| `--hover-text-color` | `var(--text-color)` | Typography Ink Token |
| `--hover-bg-color` | `#f3f3f3` | Canvas / Surface Token |
| `--border-color` | `#ddd` | Brand / Palette Token |
| `--padding` | `0.5rem` | Layout / Spatial Grid Token |
| `--head-active-bg-color` | `#049cdb` | Canvas / Surface Token |
| `--head-active-text-color` | `var(--head-text-color)` | Typography Ink Token |
| `--head-sort-arrow-color` | `var(--head-active-text-color)` | Brand / Palette Token |
| `--mrcresidencesboc-bg` | `#a73c38` | Canvas Substrate (from live computed `section` `background-color` (`computed_styles.json`)) |
| `--mrcresidencesboc-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.large> — `mrcresidencesbocaraton-com`)**:
   - Landmark `<header class="large">` (`1440x284px`) hosting `Mr. C Residences Boca Raton · New Lu` navigation (`Home · THE MR. C STORY · Residences · Services & Amenities · Neighborhood`), DOM attributes (`data-key="dss5024"`, `data-domain="stats-dss5024-serving..."`, `data-src="https://mrcresidences..."`, `data-src="https://mrcresidences..."`), and stylesheet rule `body { overscroll-behavior: none; }`.
2. **Hero Stage & Focal Lead (<section.patern_text> — `COME HOME TO MR. C`)**:
   - Landmark `<section class="patern_text dark">` presenting display lead `COME HOME TO MR. C` and copy excerpt *"Services & Amenities"* over `#a73c38` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.full-width-image> — `Services & Amenities`)**:
   - Landmark `<section class="full-width-image">` rendering section `Services & Amenities` with copy *"2 Bedroom 2 Bedroom Plus Den 3 Bedroom 3 Bedroom Plus Den"*, asset references (`xmlrpc.php`, `oaiq.min.js`, `1839718990069567`, `fbevents.js`), and grid rule `strong { font-weight: bold; }`.
4. **Interactive Detail & Feature Matrix (<section.light> — `2 Bedroom 2 Bedroom Plus Den 3 Bed`)**:
   - Landmark `<section class="patern_text light">` framing `2 Bedroom 2 Bedroom Plus Den 3 Bedroom 3 Bedroom` and `2 Bedroom Plus Den` (*"2 Bedroom Plus Den"*) with `#000000` surface cards, `#000000` accents, and `.has-bgr { background-size: cover; background-position: center center; background-r... }`.
5. **Colophon & Global Directory Footer (<footer.page> — `https://mrcresidencesbocaraton.com`)**:
   - Landmark `<footer class="page">` anchoring `Mr. C Residences Boca Raton · Ne` footer links (`Home · THE MR. C STORY · Residences · Services & Amenities · Neighborhood`), copy *"3 Bedroom Plus Den"*, and `#dddddd` structural dividers.
