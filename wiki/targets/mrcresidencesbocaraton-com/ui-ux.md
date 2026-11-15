# UI & UX Architecture: mrcresidencesbocaraton-com

## Overview & Design Identity
- **Target**: `mrcresidencesbocaraton-com` (**Mr. C Residences Boca Raton · New Luxury Residences for Sale**)
- **Production URL**: [https://mrcresidencesbocaraton.com](https://mrcresidencesbocaraton.com)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111` canvas, `#fff` ink, `#f9f9f9` accent)
- **Summary**: 133 impeccably designed two- and three-bedroom residences in Downtown Boca Raton, featuring elevated design and a lifestyle defined by Mr...
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat-Bold`
- **Body Font Stack**: `Montserrat-Medium`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 14px`, `line-height: 1.6em`)
- **Body Copy**: rule `p` (`font-size: 11px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111` | `var(--text-color)` in `:root` |
| **Primary Typography Ink** | `#d9edf7` | `var(--head-bg-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--odd-bg-color)` in `:root` |
| **Interactive Accent / Highlight** | `#f9f9f9` | `var(--even-bg-color)` in `:root` |
| **Secondary / Muted Copy** | `#f3f3f3` | `var(--hover-bg-color)` in `:root` |
| **Structural Hairline Border** | `#ddd` | `var(--border-color)` in `:root` |
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
| `--mrcresidencesboc-bg` | `#111` | Canvas Substrate (from `var(--text-color)` in `:root`) |
| `--mrcresidencesboc-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.large> — `mrcresidencesbocaraton-com`)**:
   - Landmark `<header class="large">` hosting `Mr. C Residences Boca Raton · New Lu` navigation (`Home · THE MR. C STORY · Residences · Services & Amenities · Neighborhood`), DOM attributes (`data-key="dss5024"`, `data-domain="stats-dss5024-serving..."`, `data-src="https://mrcresidences..."`, `data-src="https://mrcresidences..."`), and stylesheet rule `.tablepress>.row-hover>tr { content-visibility:auto }`.
2. **Hero Stage & Focal Lead (<section.patern_text> — `COME HOME TO MR. C`)**:
   - Landmark `<section class="patern_text dark">` presenting display lead `COME HOME TO MR. C` and copy excerpt *"Services & Amenities"* over `#111` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.full-width-image> — `Services & Amenities`)**:
   - Landmark `<section class="full-width-image">` rendering section `Services & Amenities` with copy *"EXPLORE RESIDENCES"*, asset references (`xmlrpc.php`, `oaiq.min.js`, `1839718990069567`, `fbevents.js`), and grid rule `.tablepress img { border:none;margin:0;max-width:none;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.patern_text> — `EXPLORE RESIDENCES`)**:
   - Landmark `<section class="patern_text light">` framing `EXPLORE RESIDENCES` and `EXPLORE BOCA RATON` (*"EXPLORE BOCA RATON"*) with `#fff` surface cards, `#f9f9f9` accents, and `.tablepress-table-description { clear:both;display:block }`.
5. **Colophon & Global Directory Footer (<footer.page> — `https://mrcresidencesbocaraton.com`)**:
   - Landmark `<footer class="page">` anchoring `Mr. C Residences Boca Raton · Ne` footer links (`Home · THE MR. C STORY · Residences · Services & Amenities · Neighborhood`), copy *"Antigua and Barbuda"*, and `#ddd` structural dividers.
