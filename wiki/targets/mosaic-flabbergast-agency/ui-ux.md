# UI & UX Architecture: mosaic-flabbergast-agency

## Overview & Design Identity
- **Target**: `mosaic-flabbergast-agency` (**Mosaic – Split & Back Up Your Seed Phrase**)
- **Production URL**: [https://mosaic.flabbergast.agency](https://mosaic.flabbergast.agency)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#4b4b4b`)
- **Summary**: Back up your seed phrase or password by splitting it between friends you trust. Any 3 of 5 shares recover it; fewer reveal nothing. No se...
- **Total Clean CSS Variables Extracted**: `67` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PixelOperator`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: "PixelOperator", ui-monospace, monospace`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(26 * var(--u)`, `clamp(36 * var(--u)`)
- **Body Copy**: CSS variables `--faq-body: #9d9d9d`
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | `var(--color-ink)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6b6b6b` | `var(--color-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#4b4b4b` | `var(--color-rule)` in `:root` |
| **Secondary / Muted Copy** | `#8b7bf7` | `var(--color-accent)` in `:root` |
| **Structural Hairline Border** | `#ff6b5b` | `var(--noise)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--ease-in` | `cubic-bezier(.4, 0, 1, 1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-ink` | `#121212` | Typography Ink Token |
| `--color-paper` | `#fff` | Canvas / Surface Token |
| `--color-muted` | `#6b6b6b` | Brand / Palette Token |
| `--color-rule` | `#4b4b4b` | Brand / Palette Token |
| `--color-accent` | `#8b7bf7` | Brand / Palette Token |
| `--font-display` | `"PixelOperator", ui-monospace, monospace` | Typography / Scale Token |
| `--spacing-gutter` | `calc(20 * var(--u))` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `mosaic-flabbergast-agency`)**:
   - Landmark `<header class="site-header site-header--centered">` hosting `Mosaic – Split & Back Up Your Seed P` navigation (`Technology · Guides · Developers · Roadmap · Download`), DOM attributes (`data-astro-cid-tfd3xvz2`, `data-astro-cid-nen7h5rs`, `data-reveal`, `data-tone-probe`), and stylesheet rule `.loader { display: none !important; }`.
2. **Hero Stage & Focal Lead (<section.features> — `Split and back up your seed phrase`)**:
   - Landmark `<section class="features">` presenting display lead `Split and back up your seed phrase` and copy excerpt *"Type in what you need to keep — a wallet’s seed phrase, a passwor"* over `#121212` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.chapter> — `Add a seed phrase or password`)**:
   - Landmark `<article class="chapter">` rendering section `Add a seed phrase or password` with copy *"Mosaic splits it with Shamir’s Secret Sharing, a scheme published"*, asset references (`favicon.ico`, `favicon-32.png`, `favicon-16.png`, `favicon.svg`), and grid rule `.rules__line { transform: scaleY(1) !important; }`.
4. **Interactive Detail & Feature Matrix (<article.chapter> — `Split it between friends you trust`)**:
   - Landmark `<article class="chapter">` framing `Split it between friends you trust` and `Need only a few shares to access it` (*"Explore the technology"*) with `#6b6b6b` surface cards, `#4b4b4b` accents, and `html.is-loading body { overflow: auto !important; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://mosaic.flabbergast.agency`)**:
   - Landmark `<footer class="footer">` anchoring `Mosaic – Split & Back Up Your Se` footer links (`Technology · Guides · Developers · Roadmap · Download`), copy *"Hand one share to each person, in person: they scan it from "*, and `#ff6b5b` structural dividers.
