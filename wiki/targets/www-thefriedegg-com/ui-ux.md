# UI & UX Architecture: www-thefriedegg-com

## Overview & Design Identity
- **Target**: `www-thefriedegg-com` (**Fried Egg Golf**)
- **Production URL**: [https://www.thefriedegg.com/](https://www.thefriedegg.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#666` canvas, `#f3f1e7` ink, `#fff0` accent)
- **Summary**: Visit Fried Egg Golf for in-depth golf course profiles, entertaining podcasts, premium event access, and all of the merch you never knew...
- **Total Clean CSS Variables Extracted**: `233` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Stanley`
- **Body Font Stack**: `Grey`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_typography---font-size--h1: 5rem`, `--_typography---font-size--display: 6rem`; rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: CSS variables `--_typography---font-size--h2: 4rem`; rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: rule `p` (`font-size: var(--_typography---font-size...`, `line-height: var(--_typography---l...`, `letter-spacing: var(--_typography---l...`)
- **Metadata & Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--_typography---letter-spacing--0-03em: -.03em`, `--radius--small: .5rem`; rule `small` (`font-size: 0.75rem`, `letter-spacing: 0.06em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#666` | `var(--_colours---base--grey-100)` in `:root` |
| **Primary Typography Ink** | `#f3f1e7` | `var(--_colours---base--cream)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1b1a1a` | `var(--_colours---base--black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff0` | `var(--_colours---base--transparent)` in `:root` |
| **Secondary / Muted Copy** | `#ffee54` | `var(--_colours---base--brand)` in `:root` |
| **Structural Hairline Border** | `#fe4d12` | `var(--_colours---base--orange)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_theme---background` | `var(--_colours---base--white)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--_colours---base--black)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--1-4)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-regular)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--0em)` | Typography Ink Token |
| `--_spacing---space--5` | `1.25rem` | Layout / Spatial Grid Token |
| `--_typography---font--primary-medium` | `500` | Brand / Palette Token |
| `--size--0-5rem` | `.5rem` | Layout / Spatial Grid Token |
| `--size--2rem` | `2rem` | Layout / Spatial Grid Token |
| `--size--1-5rem` | `1.5rem` | Layout / Spatial Grid Token |
| `--size--1rem` | `1rem` | Layout / Spatial Grid Token |
| `--_typography---font--secondary-family` | `Stanley,Arial,sans-serif` | Brand / Palette Token |
| `--_typography---font-size--text-medium` | `1.125rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header_main_wrap> — `www-thefriedegg-com`)**:
   - Landmark `<header class="header_main_wrap">` hosting `Fried Egg Golf` navigation (`Log in · Newsletter · Pro Shop · Architecture · Course Profiles`), DOM attributes (`data-wf-domain="www.thefriedegg.com"`, `data-wf-page="67ab6ef769ff843db623d6fa"`, `data-wf-site="67ab6ef769ff843db623d6f5"`, `data-hubspot-styled-components`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.cms_filters_wrap> — `A deeper level of golf`)**:
   - Landmark `<section class="cms_filters_wrap cms_home_filters">` presenting display lead `A deeper level of golf` and copy excerpt *"Skip to main content"* over `#666` canvas and `#f3f1e7` ink.
3. **Primary Showcase & Content Grid (<section.explore_content_wrap> — `2026 U.S. Mid-Amateur Champion And`)**:
   - Landmark `<section class="explore_content_wrap">` rendering section `2026 U.S. Mid-Amateur Champion Andrew Bailey` with copy *"Architect Profiles"*, asset references (`cdn.prod.website-files.com`, `friedegg-staging.shared.1a7f178f4...`, `iframe_api.b14cb21cf7e4cfe54860.js`, `www-widgetapi.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.latest_wrap> — `The Commons`)**:
   - Landmark `<section class="latest_wrap">` framing `The Commons` and `Paulie's Picks: 2026 Austin Championship presente...` (*"Eggstracurriculars"*) with `#1b1a1a` surface cards, `#fff0` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.thefriedegg.com/`)**:
   - Landmark `<footer class="footer_wrap">` anchoring `Fried Egg Golf` footer links (`Log in · Newsletter · Pro Shop · Architecture · Course Profiles`), copy *"Fried Egg Golf Guides"*, and `#fe4d12` structural dividers.
