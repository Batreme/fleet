# UI & UX Architecture: articles-gamcare-org-uk

## Overview & Design Identity
- **Target**: `articles-gamcare-org-uk` (**The Gamification of Everything · GamCare**)
- **Production URL**: [https://articles.gamcare.org.uk/](https://articles.gamcare.org.uk/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#3a04a8` canvas, `#fff8ef` ink, `#eee` accent)
- **Summary**: Gambling-like mechanics are becoming part of everyday digital life. Explore how gamification can shape behaviour and why prevention needs...
- **Total Clean CSS Variables Extracted**: `140` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Outfit`
- **Body Font Stack**: `.75rem`
- **Monospace / Technical Font Stack**: `monospace!important`
- **Hero Display (`H1`)**: CSS variables `--_typography---h1--h1-font-size: 5rem`, `--_typography---h1--h1-line-height: var(--font-height--small)`, `--_typography---h1--h1-font-weight: var(--font-weight--bold)`
- **Section Heading (`H2`)**: CSS variables `--_typography---h2--h2-font-size: 3.75rem`, `--_typography---h2--h2-line-height: var(--font-height--medium)`, `--_typography---h2--h2-font-weight: var(--font-weight--bold)`
- **Body Copy**: CSS variables `--font-family--body: Outfit,Arial,sans-serif`, `--_typography---body--body-font-size: 1rem`, `--_typography---body--body-line-height: var(--font-height--xlarge)`
- **Metadata & Labels**: CSS variables `--_typography---body--body-letter-spacing: var(--letter-spacing--default)`, `--_typography---h1--h1-letter-spacing: -.1rem`, `--_typography---h2--h2-letter-spacing: -.1125rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3a04a8` | `var(--brand--indigo)` in `:root` |
| **Primary Typography Ink** | `#ff9c00` | `var(--brand--orange)` in `:root` |
| **Elevated Surface / Card Substrate** | `#291a5c` | `var(--brand--tolopea)` in `:root` |
| **Interactive Accent / Highlight** | `#eee` | `var(--neutral--neutral-light)` in `:root` |
| **Secondary / Muted Copy** | `#fff8ef` | `var(--neutral--cream)` in `:root` |
| **Structural Hairline Border** | `#ffc000` | `var(--brand--light-orange)` in `:root` |

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
   - Landmark `<nav class="nav_link-wrap w-nav-menu">` hosting `The Gamification of Everything · Gam` navigation (`0808 8020 133`), DOM attributes (`data-wf-domain="articles.gamcare.org.uk"`, `data-wf-page="6a9541bcb6d4e8d3269865d8"`, `data-wf-site="6a9541b9b6d4e8d32698651c"`, `data-animation="default"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `The gamification of everything`)**:
   - Landmark `<section class="section is-home-hero">` presenting display lead `The gamification of everything` and copy excerpt *"Gambling-like mechanics are becoming part of everyday digital lif"* over `#3a04a8` canvas and `#fff8ef` ink.
3. **Primary Showcase & Content Grid (<section.section> — `The signal`)**:
   - Landmark `<section class="section">` rendering section `The signal` with copy *"People contacting GamCare’s National Gambling Helpline are increa"*, asset references (`cdn.prod.website-files.com`, `gamcare.webflow.shared.3ff275b4f....`, `clarity.js`, `yqtqehex3o`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `What do we mean by gamification?`)**:
   - Landmark `<section class="section">` framing `What do we mean by gamification?` and `The concern is not The concern is not gamificatio...` (*"We’re talking about design features like variable rewards, near m"*) with `#291a5c` surface cards, `#eee` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://articles.gamcare.org.uk/`)**:
   - Landmark `<footer class="footer">` anchoring `The Gamification of Everything ·` footer links (`0808 8020 133`), copy *"Drawing on nearly three decades’ experience, GamCare treats "*, and `#ffc000` structural dividers.
