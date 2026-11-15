# UI & UX Architecture: gallery-play-be

## Overview & Design Identity
- **Target**: `gallery-play-be` (**Home - Gallery Play**)
- **Production URL**: [https://gallery-play.be/](https://gallery-play.be/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ccd6df` / `#1E1E1E`)
- **Summary**: We craft bold campaigns, authentic stories and premium collaborations that move sport and culture forward.
- **Total Clean CSS Variables Extracted**: `182` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Telegraf`
- **Body Font Stack**: `block`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: var( --e-global-typography-pr...`, `line-height: var( --e-global-typog...`, `font-weight: var( --e-glob...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 0.9em`, `font-weight: 400`)
- **Body Copy**: CSS variables `--cmplz_category_body_font_size: 12px`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `1rem`, `2.5rem`, `2rem`, `1.75rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ccd6df` | `var(--e-rating-icon-color)` in `:root` |
| **Primary Typography Ink** | `#f0ad4e` | `var(--e-rating-icon-marked-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#FFFFFF` | `var(--e-global-color-primary)` in `:root` |
| **Interactive Accent / Highlight** | `#1E1E1E` | `var(--e-global-color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#000000` | `var(--e-global-color-0560f42)` in `:root` |
| **Structural Hairline Border** | `#E1E1E1` | `var(--e-global-color-160fc90)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--justify-content` | `initial` | Design System Custom Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |
| `--order` | `initial` | Design System Custom Token |
| `--align-self` | `initial` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--border-radius` | `0` | Elevation / Border Token |
| `--border-top-width` | `0px` | Layout / Spatial Grid Token |
| `--border-right-width` | `0px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `gallery-play-be`)**:
   - Landmark `<header class="elementor elementor-100">` hosting `Home - Gallery Play` navigation (`Projects · Services · Athletes · Team · Contact`), DOM attributes (`data-mp="true"`, `data-cfasync="false"`, `data-mp="true"`, `data-cfasync="false"`), and stylesheet rule `.cmplz-video.cmplz-iframe-styles { background-color:transparent }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `Culture-shifting creativity for th`)**:
   - Landmark `<main class="site-main post-15">` presenting display lead `Culture-shifting creativity for the world of sports` and copy excerpt *"To provide the best experience, we use technologies such as cooki"* over `#ccd6df` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.site-main> — `Rooted in top-level football, flue`)**:
   - Landmark `<main class="site-main post-15">` rendering section `Rooted in top-level football, fluent in branding,...` with copy *"Functional Altijd actief"*, asset references (`player.js`, `recaptcha__en.js`, `embed`, `cookieblocker.min.css`), and grid rule `.cmplz-video.cmplz-hidden { visibility:hidden !important }`.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `Work that speaks louder than words`)**:
   - Landmark `<main class="site-main post-15">` framing `Work that speaks louder than words.` and `125 Years of AFC Ajax` (*"The technical storage or access is strictly necessary for the leg"*) with `#FFFFFF` surface cards, `#1E1E1E` accents, and `.cmplz-blocked-content-notice { display:none }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://gallery-play.be/`)**:
   - Landmark `<footer class="elementor elementor-102">` anchoring `Home - Gallery Play` footer links (`Projects · Services · Athletes · Team · Contact`), copy *"De technische opslag of toegang is noodzakelijk voor het leg"*, and `#E1E1E1` structural dividers.
