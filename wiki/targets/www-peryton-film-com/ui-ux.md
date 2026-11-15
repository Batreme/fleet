# UI & UX Architecture: www-peryton-film-com

## Overview & Design Identity
- **Target**: `www-peryton-film-com` (**Werbefilm & Social Ads aus Gießen · Peryton Film**)
- **Production URL**: [https://www.peryton-film.com/](https://www.peryton-film.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#eae0d0` / `#0009`)
- **Summary**: Werbefilme, Imagefilme und Social Ads aus Gießen, von Mittelhessen bis Frankfurt. Über 200 Unternehmen vertrauen Peryton Film. Jetzt Erst...
- **Total Clean CSS Variables Extracted**: `71` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Ppmuseum`
- **Body Font Stack**: `Instrumentsans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `4rem`, `3rem`, `2.5rem`, `2rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `4rem`, `3rem`, `2.5rem`, `2rem`)
- **Body Copy**: CSS variables `--_typography---font-styles--body: Instrumentsans,Arial,sans-serif`, `--pery-font-body: Instrumentsans, Arial, sans-serif`
- **Metadata & Labels**: CSS variables `--_ui-styles---radius--small: .5rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#eae0d0` | `var(--color-scheme-1--text-light)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--_primitives---colors--white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ecc779` | `var(--color-scheme-1--accent)` in `:root` |
| **Interactive Accent / Highlight** | `#0009` | `var(--_primitives---opacity--neutral-darkest-60)` in `:root` |
| **Secondary / Muted Copy** | `#fff9` | `var(--_primitives---opacity--white-60)` in `:root` |
| **Structural Hairline Border** | `#fff6` | `var(--_primitives---opacity--white-40)` in `:root` |
| **Variable Token (`--color-scheme-1--border`)** | `#ffffff73` | `var(--color-scheme-1--border)` in `:root` |
| **Variable Token (`--shadow-border`)** | `#ecc77980` | `var(--shadow-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-scheme-1--background-dark` | `var(--color-scheme-1--brand-base)` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `Instrumentsans,Arial,sans-serif` | Typography / Scale Token |
| `--color-scheme-1--text-light` | `#eae0d0` | Canvas / Surface Token |
| `--_typography---font-styles--heading` | `Ppmuseum,Arial,sans-serif` | Typography Ink Token |
| `--color-scheme-1--text-dark` | `var(--color-scheme-1--brand-base)` | Canvas / Surface Token |
| `--_primitives---colors--white` | `#fff` | Canvas / Surface Token |
| `--color-scheme-1--border` | `#ffffff73` | Brand / Palette Token |
| `--color-scheme-1--accent` | `#ecc779` | Brand / Palette Token |
| `--_primitives---colors--neutral-darkest` | `black` | Canvas / Surface Token |
| `--_primitives---opacity--transparent` | `transparent` | Design System Custom Token |
| `--shadow-border` | `#ecc77980` | Elevation / Border Token |
| `--_primitives---opacity--neutral-darkest-60` | `#0009` | Canvas / Surface Token |
| `--_primitives---opacity--white-60` | `#fff9` | Canvas / Surface Token |
| `--_ui-styles---stroke--border-width` | `1px` | Layout / Spatial Grid Token |
| `--_ui-styles---radius--medium` | `1rem` | Elevation / Border Token |
| `--color-scheme-1--foreground` | `var(--_primitives---colors--neutral-lightest)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `www-peryton-film-com`)**:
   - Landmark `<nav class="bold-nav-full">` hosting `Werbefilm & Social Ads aus Gießen · ` navigation (`Home · Über Uns · Referenzen · Leistungen · Kontakt`), DOM attributes (`data-wf-domain="www.peryton-film.com"`, `data-wf-page="69ef0496c745ba2d70c01ce3"`, `data-wf-site="69ef0495c745ba2d70c01c8a"`, `data-website-id="6378536d-081a-43d7-a7..."`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.main-section> — `Mit Videomarketing vom Geheimtipp `)**:
   - Landmark `<section class="main-section overflow-hidden">` presenting display lead `Mit Videomarketing vom Geheimtipp zum` and copy excerpt *"Antrieb zünden Antrieb zünden"* over `#eae0d0` canvas and `#0009` ink.
3. **Primary Showcase & Content Grid (<section.main-section> — `HYPE`)**:
   - Landmark `<section class="main-section is-mask">` rendering section `HYPE` with copy *"Strategische Werbefilme und Social Ads aus Gießen, von Mittelhess"*, asset references (`cdn.prod.website-files.com`, `peryton-film.shared.c549ade3f.min...`, `peryton-film.69ef0496c745ba2d70c0...`, `69f9d75c7d46e2ad8d6fab7f_logo_fav...`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.main-section> — `Videomarketing`)**:
   - Landmark `<section class="main-section overflow-hidden">` framing `Videomarketing` and `Infrastruktur` (*"Unendliche Möglichkeiten."*) with `#ecc779` surface cards, `#0009` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.peryton-film.com/`)**:
   - Landmark `<footer class="footer-wrap">` anchoring `Werbefilm & Social Ads aus Gieße` footer links (`Home · Über Uns · Referenzen · Leistungen · Kontakt`), copy *"“Nicht zu vergleichen mit anderen Agenturen & Filmproduktion"*, and `#fff6` structural dividers.
