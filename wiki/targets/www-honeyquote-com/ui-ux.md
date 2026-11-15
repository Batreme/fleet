# UI & UX Architecture: www-honeyquote-com

## Overview & Design Identity
- **Target**: `www-honeyquote-com` (**Compare Insurance Quotes Worth Trusting · HoneyQuote**)
- **Production URL**: [https://www.honeyquote.com/](https://www.honeyquote.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#ac512a` canvas, `#fff` ink, `#1b493d` accent)
- **Summary**: Compare quotes from 20+ carriers. Real licensed agents get you the best insurance quotes, straight answers, zero spam, and your credit sc...
- **Total Clean CSS Variables Extracted**: `235` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_typography---h1--font-size: 5rem`, `--_typography---h1--line-height: var(--_typography---font-height--small)`, `--_typography---h1--font-weight: var(--_typography---font-weight--normal)`; rule `h1` (`font-size: var(--_typography---h2--font-...`, `line-height: var(--_typography---h...`, `letter-spacing: var(--_typography---h...`, `font-weight: var(--_typogr...`)
- **Section Heading (`H2`)**: CSS variables `--_typography---h2--font-family: var(--_typography---font-family--primary)`, `--_typography---h2--font-size: 3rem`, `--_typography---h2--line-height: var(--_typography---font-height--small)`; rule `h2` (`font-size: var(--_typography---h3--font-...`, `line-height: var(--_typography---h...`, `letter-spacing: var(--_typography---h...`, `font-weight: var(--_typogr...`)
- **Body Copy**: CSS variables `--_typography---body--font-family: var(--_typography---font-family--secondary)`, `--_typography---body--font-size: var(--_typography---font--regular)`, `--_typography---body--line-height: var(--_typography---font-height--large)`; rule `p` (`font-size: var(--_typography---h4--font-...`, `line-height: var(--_typography---h...`, `letter-spacing: var(--_typography---h...`, `font-weight: var(--_typogr...`)
- **Metadata & Labels**: CSS variables `--_typography---body--letter-spacing: var(--_typography---letter-spacing--tight)`, `--_typography---h1--letter-spacing: var(--_typography---letter-spacing--tight)`, `--_typography---h2--letter-spacing: var(--_typography---letter-spacing--tight)`; rule `small` (`font-size: .75rem`, `line-height: 1.2`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ac512a` | `var(--amber)` in `:root` |
| **Primary Typography Ink** | `#f4ecde` | `var(--brand--ivory-nectar)` in `:root` |
| **Elevated Surface / Card Substrate** | `#276152` | `var(--brand--deep-cypress)` in `:root` |
| **Interactive Accent / Highlight** | `#1b493d` | `var(--brand--deep-cypress-dark)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--base-color-neutral--white)` in `:root` |
| **Structural Hairline Border** | `#fff0` | `var(--opacity--transparent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--background-color--background-primary` | `var(--brand--ivory-nectar)` | Canvas / Surface Token |
| `--_typography---body--font-family` | `var(--_typography---font-family--secondary)` | Typography / Scale Token |
| `--text-color--text-primary` | `var(--brand--midnight-pine)` | Typography Ink Token |
| `--_typography---body--font-size` | `var(--_typography---font--regular)` | Typography / Scale Token |
| `--_typography---body--line-height` | `var(--_typography---font-height--large)` | Typography / Scale Token |
| `--_typography---body--font-weight` | `var(--_typography---font-weight--medium)` | Typography / Scale Token |
| `--_typography---body--letter-spacing` | `var(--_typography---letter-spacing--tight)` | Typography / Scale Token |
| `--_typography---font-family--primary` | `"Instrument Serif",sans-serif` | Brand / Palette Token |
| `--_typography---h1--font-size` | `5rem` | Typography / Scale Token |
| `--_typography---h1--line-height` | `var(--_typography---font-height--small)` | Typography / Scale Token |
| `--_typography---h1--font-weight` | `var(--_typography---font-weight--normal)` | Typography / Scale Token |
| `--_typography---h1--letter-spacing` | `var(--_typography---letter-spacing--tight)` | Typography / Scale Token |
| `--_typography---h2--font-family` | `var(--_typography---font-family--primary)` | Typography / Scale Token |
| `--_typography---h2--font-size` | `3rem` | Typography / Scale Token |
| `--_typography---h2--line-height` | `var(--_typography---font-height--small)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav_content> — `www-honeyquote-com`)**:
   - Landmark `<nav class="nav_content w-nav-menu">` hosting `Compare Insurance Quotes Worth Trust` navigation (`Home Insurance · Flood Insurance · Condo Insurance · X insurance in Y`), DOM attributes (`data-wf-domain="www.honeyquote.com"`, `data-wf-page="6a21ae850094dc6f56f29bed"`, `data-wf-site="6a21ae820094dc6f56f29b98"`, `data-wf-intellimize-customer-id="117608328"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section_banner> — `Compare insurance quotes for cover`)**:
   - Landmark `<section class="section_banner">` presenting display lead `Compare insurance quotes for coverage that's ther...` and copy excerpt *"Want us to do the shopping for you? Call (561) 264-2614"* over `#ac512a` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.section_home-hero> — `The sweet spot for all things insu`)**:
   - Landmark `<section class="section_home-hero">` rendering section `The sweet spot for all things insurance.` with copy *"Mobile Home Insurance"*, asset references (`cdn.prod.website-files.com`, `honeyquote-v2.shared.e243b8f63.mi...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_coverage> — `What we cover`)**:
   - Landmark `<section class="section_coverage">` framing `What we cover` and `Personal Lines` (*"Want an expert to handle this?"*) with `#276152` surface cards, `#1b493d` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-inter-n8-active> — `https://www.honeyquote.com/`)**:
   - Landmark `<footer class="wf-inter-n8-active">` anchoring `Compare Insurance Quotes Worth T` footer links (`Home Insurance · Flood Insurance · Condo Insurance · X insurance in Y`), copy *"Home insurance in Florida"*, and `#fff0` structural dividers.
