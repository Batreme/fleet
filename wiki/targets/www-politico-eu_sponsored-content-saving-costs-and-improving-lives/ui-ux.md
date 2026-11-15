# UI & UX Architecture: www-politico-eu_sponsored-content-saving-costs-and-improving-lives

## Overview & Design Identity
- **Target**: `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` (**Saving costs and improving lives – POLITICO**)
- **Production URL**: [https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/](https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#CCE5F4` ink, `#006ba1` accent)
- **Summary**: Visit the post for more.
- **Total Clean CSS Variables Extracted**: `326` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NSI`
- **Body Font Stack**: `Martina Plantijn fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-weight: var(--font-we...`)
- **Section Heading (`H2`)**: rule `h2` (`font-weight: var(--font-we...`)
- **Body Copy**: rule `p` (`font-size: var(--wp--custom--type-scale-...`, `line-height: var(--wp--custom--typ...`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: CSS variables `--wp--custom--animation--duration--small: 100ms`, `--wp--custom--animation--duration--extra-small: 50ms`, `--wp--custom--stroke--small: 1px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Interactive Accent / Highlight** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Secondary / Muted Copy** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Structural Hairline Border** | `#CCE5F4` | `var(--wp--custom--color--blue--100)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--card-image-ratio` | `3/2` | Design System Custom Token |
| `--button-padding-block` | `var(--wp--custom--spacing--6)` | Layout / Spatial Grid Token |
| `--button-padding-inline` | `var(--wp--custom--spacing--6)` | Layout / Spatial Grid Token |
| `--button-outline-color` | `var(--color-border)` | Brand / Palette Token |
| `--button-background-color` | `var(--color-background-inverse)` | Canvas / Surface Token |
| `--button-text-color` | `var(--color-text-inverse)` | Typography Ink Token |
| `--button-hover-background-color` | `var(--wp--custom--color--grey--800)` | Canvas / Surface Token |
| `--button-hover-text-color` | `var(--color-text-inverse)` | Typography Ink Token |
| `--button-focus-background-color` | `var(--color-background-inverse)` | Canvas / Surface Token |
| `--button-focus-text-color` | `var(--color-text-inverse)` | Typography Ink Token |
| `--button-active-background-color` | `var(--wp--custom--color--grey--800)` | Canvas / Surface Token |
| `--button-active-text-color` | `var(--color-text-inverse-50pc)` | Typography Ink Token |
| `--button-plain-background-color` | `transparent` | Canvas / Surface Token |
| `--button-plain-text-color` | `var(--color-text-primary)` | Typography Ink Token |
| `--button-plain-hover-text-color` | `var(--color-link)` | Typography Ink Token |
| `--button-plain-focus-text-color` | `var(--color-text-primary)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-politico-eu_sponsored-content-saving-costs-and-improving-lives`)**:
   - Landmark `<header class="header">` hosting `Saving costs and improving lives – P` navigation (`Europe · UK · France · Germany · Spain`), DOM attributes (`data-previous-scroll-y="-0px"`, `data-wp-strategy="async"`, `data-id="adlibScripts"`, `data-focus-first="false"`), and stylesheet rule `html { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
2. **Hero Stage & Focal Lead (<article.article> — `Our readers read next`)**:
   - Landmark `<article class="article article--no-top-margin">` presenting display lead `Our readers read next` and copy excerpt *"Skip to main content"* over `#7a00df` canvas and `#CCE5F4` ink.
3. **Primary Showcase & Content Grid (<article.article> — `US suggested Ukraine could give up`)**:
   - Landmark `<article class="article article--no-top-margin">` rendering section `US suggested Ukraine could give up Donbas for NAT...` with copy *"Policy areas Agriculture and Food Central Banker Competition and "*, asset references (`destination`, `favicon.ico`, `apple-touch-icon.png`, `favicon-32x32.png`), and grid rule `before { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<article.article> — `Finland rejects reported Russian d`)**:
   - Landmark `<article class="article article--no-top-margin">` framing `Finland rejects reported Russian demand to leave...` and `EU deal on Ukraine talks overshadows AI-focused s...` (*"Agriculture and Food"*) with `#007cba` surface cards, `#006ba1` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.article__footer-inline> — `https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/`)**:
   - Landmark `<footer class="article__footer-inline">` anchoring `Saving costs and improving lives` footer links (`Europe · UK · France · Germany · Spain`), copy *"Competition and Industrial Policy"*, and `#CCE5F4` structural dividers.
