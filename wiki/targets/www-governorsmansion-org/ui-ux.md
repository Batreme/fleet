# UI & UX Architecture: www-governorsmansion-org

## Overview & Design Identity
- **Target**: `www-governorsmansion-org` (**Louisiana's House · Louisiana Governor's Mansion**)
- **Production URL**: [https://www.governorsmansion.org/](https://www.governorsmansion.org/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#002b59` canvas, `#f3efe9` ink, `#f2e7d4` accent)
- **Summary**: Step inside the Louisiana Governor’s Mansion and discover a rich blend of history, culture, and civic pride. Take a virtual tour, explore...
- **Total Clean CSS Variables Extracted**: `171` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Luxurious Script`
- **Body Font Stack**: `stevie-sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Metadata & Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--normal)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#002b59` | `var(--swatch--brand-500)` in `:root` |
| **Primary Typography Ink** | `#c3cfd8` | `var(--swatch--brand-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2b2b2b` | `var(--swatch--dark-800)` in `:root` |
| **Interactive Accent / Highlight** | `#f2e7d4` | `var(--swatch--brand-5-200)` in `:root` |
| **Secondary / Muted Copy** | `#f3efe9` | `var(--swatch--light-200)` in `:root` |
| **Structural Hairline Border** | `#c6cfb9` | `var(--swatch--brand-2-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--swatch--light-100)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--secondary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--dark-900)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--huge)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--secondary-book)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--normal)` | Typography Ink Token |
| `--radius--main` | `1rem` | Elevation / Border Token |
| `--_theme---background-2` | `var(--_brand---color-200)` | Canvas / Surface Token |
| `--site--column-count` | `12` | Layout / Spatial Grid Token |
| `--_responsive---large` | `1` | Design System Custom Token |
| `--_responsive---medium` | `0` | Design System Custom Token |
| `--_responsive---small` | `0` | Design System Custom Token |
| `--_responsive---xsmall` | `0` | Design System Custom Token |
| `--max-width--small` | `50rem` | Layout / Spatial Grid Token |
| `--_gap---size` | `var(--site--gutter)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav_desktop_wrap> — `www-governorsmansion-org`)**:
   - Landmark `<header class="nav_desktop_wrap">` hosting `Louisiana's House · Louisiana Govern` navigation (`Tour · History · Activities · Preserve · Contact`), DOM attributes (`data-wf-domain="www.governorsmansion.org"`, `data-wf-page="68f8ead2dc9339599a128c26"`, `data-wf-site="68f8ead1dc9339599a128b88"`, `data-number="10"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.u-section> — `Louisiana Governor's Mansion`)**:
   - Landmark `<section class="u-section u-background-3">` presenting display lead `Louisiana Governor's Mansion` and copy excerpt *"Skip to main content"* over `#002b59` canvas and `#f3efe9` ink.
3. **Primary Showcase & Content Grid (<section.u-section> — `The Legacy of the Governor's Mansi`)**:
   - Landmark `<section class="u-section u-width-full">` rendering section `The Legacy of the Governor's Mansion` with copy *"Button Text Button Text Button Text"*, asset references (`cdn.prod.website-files.com`, `governors-mansion.webflow.shared....`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.footer_group_wrap> — `Meet Our Governor`)**:
   - Landmark `<section class="footer_group_wrap">` framing `Meet Our Governor` and `Meet Our First Family` (*"Mansion.Tours@la.gov"*) with `#2b2b2b` surface cards, `#f2e7d4` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.governorsmansion.org/`)**:
   - Landmark `<footer class="footer_wrap u-theme-dark">` anchoring `Louisiana's House · Louisiana Go` footer links (`Tour · History · Activities · Preserve · Contact`), copy *"1001 Capitol Access Rd. Baton Rouge, LA 70802"*, and `#c6cfb9` structural dividers.
