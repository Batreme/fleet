---
title: "UI & UX Architecture: articles-gamcare-org-uk"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: articles-gamcare-org-uk

## Overview & Design Identity
- **Target**: `articles-gamcare-org-uk` (**The Gamification of Everything · GamCare**)
- **Production URL**: [https://articles.gamcare.org.uk/](https://articles.gamcare.org.uk/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff8ef` canvas, `#000000` ink, `#ff9c00` accent)
- **Summary**: Gambling-like mechanics are becoming part of everyday digital life. Explore how gamification can shape behaviour and why prevention needs...
- **Total Clean CSS Variables Extracted**: `140` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Outfit`
- **Body Font Stack**: `Outfit`
- **Monospace / Technical Font Stack**: `Inconsolata`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 88px`, `font-weight: 700`, `letter-spacing: -1.6px`); CSS variables `--_typography---h1--h1-font-size: 5rem`, `--_typography---h1--h1-line-height: var(--font-height--small)`, `--_typography---h1--h1-font-weight: var(--font-weight--bold)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 88px`, `font-weight: 700`, `letter-spacing: -1.6px`); CSS variables `--_typography---h2--h2-font-size: 3.75rem`, `--_typography---h2--h2-line-height: var(--font-height--medium)`, `--_typography---h2--h2-font-weight: var(--font-weight--bold)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-family--body: Outfit,Arial,sans-serif`, `--_typography---body--body-font-size: 1rem`, `--_typography---body--body-line-height: var(--font-height--xlarge)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---body--body-letter-spacing: var(--letter-spacing--default)`, `--_typography---h1--h1-letter-spacing: -.1rem`, `--_typography---h2--h2-letter-spacing: -.1125rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fff8ef` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#ff9c00` | `var(--brand--orange)` in `:root` |
| **Secondary / Muted Copy** | `#333333` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-family--body` | `Outfit,Arial,sans-serif` | Typography / Scale Token |
| `--_theme---text--primary` | `var(--neutral--black)` | Typography Ink Token |
| `--_typography---body--body-font-size` | `1rem` | Typography / Scale Token |
| `--_typography---body--body-line-height` | `var(--font-height--xlarge)` | Typography / Scale Token |
| `--_typography---body--body-font-weight` | `var(--font-weight--normal)` | Typography / Scale Token |
| `--_typography---body--body-letter-spacing` | `var(--letter-spacing--default)` | Typography / Scale Token |
| `--_layout---spacing--none` | `0rem` | Layout / Spatial Grid Token |
| `--font-family--heading` | `Outfit,Arial,sans-serif` | Typography Ink Token |
| `--_typography---h1--h1-font-size` | `5rem` | Typography / Scale Token |
| `--_typography---h1--h1-line-height` | `var(--font-height--small)` | Typography / Scale Token |
| `--_typography---h1--h1-font-weight` | `var(--font-weight--bold)` | Typography / Scale Token |
| `--_typography---h1--h1-letter-spacing` | `-.1rem` | Typography / Scale Token |
| `--_typography---h2--h2-font-size` | `3.75rem` | Typography / Scale Token |
| `--_typography---h2--h2-line-height` | `var(--font-height--medium)` | Typography / Scale Token |
| `--_typography---h2--h2-font-weight` | `var(--font-weight--bold)` | Typography / Scale Token |
| `--_typography---h2--h2-letter-spacing` | `-.1125rem` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav_link-wrap> — `articles-gamcare-org-uk`)**:
   - Landmark `<nav class="nav_link-wrap w-nav-menu">` (`137x26px`) hosting `The Gamification of Everything · Gam` navigation (`0808 8020 133`), DOM attributes (`data-wf-domain="articles.gamcare.org.uk"`, `data-wf-page="6a9541bcb6d4e8d3269865d8"`, `data-wf-site="6a9541b9b6d4e8d32698651c"`, `data-animation="default"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.section> — `The gamification of everything`)**:
   - Landmark `<section class="section is-home-hero">` presenting display lead `The gamification of everything` and copy excerpt *"Gambling-like mechanics are becoming part of everyday digital lif"* over `#fff8ef` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section:nth(2)> — `What do we mean by gamification?`)**:
   - Landmark `<section class="section">` rendering section `What do we mean by gamification?` with copy *"People contacting GamCare’s National Gambling Helpline are increa"*, asset references (`cdn.prod.website-files.com`, `gamcare.webflow.shared.3ff275b4f....`, `clarity.js`, `yqtqehex3o`), and grid rule `host { position:relative;display:block;margin-left:auto;margin-right:auto;z-ind... }`.
4. **Interactive Detail & Feature Matrix (<section.section:nth(3)> — `The concern is not The concern is `)**:
   - Landmark `<section class="section">` framing `The concern is not The concern is not gamificatio...` and `Gambling harm is changing shape.` (*"We’re talking about design features like variable rewards, near m"*) with `#ffff00` surface cards, `#ff9c00` accents, and `.swiper { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://articles.gamcare.org.uk/`)**:
   - Landmark `<footer class="footer">` anchoring `The Gamification of Everything ·` footer links (`0808 8020 133`), copy *"Drawing on nearly three decades’ experience, GamCare treats "*, and `#e2e2e2` structural dividers.
