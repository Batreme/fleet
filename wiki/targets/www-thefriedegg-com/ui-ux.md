---
title: "UI & UX Architecture: www-thefriedegg-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-thefriedegg-com

## Overview & Design Identity
- **Target**: `www-thefriedegg-com` (**Fried Egg Golf**)
- **Production URL**: [https://www.thefriedegg.com/](https://www.thefriedegg.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1b1a1a` ink, `#ffa500` accent)
- **Summary**: Visit Fried Egg Golf for in-depth golf course profiles, entertaining podcasts, premium event access, and all of the merch you never knew...
- **Total Clean CSS Variables Extracted**: `236` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Grey`
- **Body Font Stack**: `Grey`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 59.9984px`, `line-height: 71.9981px`, `font-weight: 500`, `letter-spacing: -1.19997px`); CSS variables `--_typography---font-size--h1: 5rem`, `--_typography---font-size--display: 6rem`; rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50px`, `line-height: 60px`, `font-weight: 500`, `letter-spacing: -1px`); CSS variables `--_typography---font-size--h2: 4rem`; rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: live computed `body` (`font-size: 15.9888px`, `line-height: 22.3843px`, `font-weight: 400`); rule `p` (`font-size: var(--_typography---font-size...`, `line-height: var(--_typography---l...`, `letter-spacing: var(--_typography---l...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15.9888px`, `line-height: 22.3843px`, `font-weight: 400`); CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--_typography---letter-spacing--0-03em: -.03em`, `--radius--small: .5rem`; rule `small` (`font-size: 0.75rem`, `letter-spacing: 0.06em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1b1a1a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f1e7` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffa500` | `.upvote-btn-icon.is-upvoted { background-color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#ffee54` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--_typography---line-height--1-6` | `1.6` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header_main_wrap> — `www-thefriedegg-com`)**:
   - Landmark `<header class="header_main_wrap">` (`1440x900px`) hosting `Fried Egg Golf` navigation (`Newsletter · Pro Shop · Architecture · Course Profiles · Architect Profiles`), DOM attributes (`data-wf-domain="www.thefriedegg.com"`, `data-wf-page="67ab6ef769ff843db623d6fa"`, `data-wf-site="67ab6ef769ff843db623d6f5"`, `data-hubspot-styled-components`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.explore_content_wrap> — `A deeper level of golf`)**:
   - Landmark `<section class="explore_content_wrap">` presenting display lead `A deeper level of golf` and copy excerpt *"List of former LIV players to take up membership in 2027"* over `#ffffff` canvas and `#1b1a1a` ink.
3. **Primary Showcase & Content Grid (<section.latest_wrap> — `2026 U.S. Mid-Amateur Champion And`)**:
   - Landmark `<section class="latest_wrap">` rendering section `2026 U.S. Mid-Amateur Champion Andrew Bailey` with copy *"Q&A with Aaron Wise"*, asset references (`cdn.prod.website-files.com`, `friedegg-staging.shared.feb62e49d...`, `iframe_api.bc7198a0fbd8d2409df5.js`, `www-widgetapi.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.major_cta_wrap> — `Davenport Country Club`)**:
   - Landmark `<section class="major_cta_wrap">` framing `Davenport Country Club` and `Aaron Wise Q&A: On His PGA Tour Return, Mental He...` (*"On his PGA Tour return, mental health, and more"*) with `#f3f1e7` surface cards, `#ffa500` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.thefriedegg.com/`)**:
   - Landmark `<footer class="footer_wrap">` anchoring `Fried Egg Golf` footer links (`Newsletter · Pro Shop · Architecture · Course Profiles · Architect Profiles`), copy *"Liking and Subscribing to the DP World Tour"*, and `#e2e2e2` structural dividers.
