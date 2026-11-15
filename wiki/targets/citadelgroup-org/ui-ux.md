# UI & UX Architecture: citadelgroup-org

## Overview & Design Identity
- **Target**: `citadelgroup-org` (**Citadel National Construction Group · Nationwide Construction**)
- **Production URL**: [https://citadelgroup.org/](https://citadelgroup.org/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7953e` / `#e3e3e4`)
- **Summary**: Citadel connects leading regional construction firms into one nationwide network, combining local expertise with national resources to de...
- **Total Clean CSS Variables Extracted**: `79` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Bebas Neue`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.6rem`, `.7rem`, `.8rem`, `1.2rem`, `1.5rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2.9rem,2.9vw,3.9rem)!im...`, `line-height: 1.02!important`)
- **Body Copy**: CSS variables `--font-citadel-body: "Montserrat", system-ui, sans-serif`; rule `p` (`font-size: .88rem`, `line-height: 1.35`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.6rem`, `.7rem`, `.8rem`, `1.2rem`, `1.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f7953e` | `var(--citadel-orange)` in `:root` |
| **Primary Typography Ink** | `#f87000` | `var(--citadel-dark-orange)` in `:root` |
| **Elevated Surface / Card Substrate** | `#818486` | `var(--citadel-medium-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#e3e3e4` | `var(--citadel-light-grey)` in `:root` |
| **Secondary / Muted Copy** | `#000000` | `var(--citadel-black)` in `:root` |
| **Structural Hairline Border** | `#e17e00` | `var(--color-brand-orange-hover)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--citadel-orange` | `#f7953e` | Color / Atmospheric Token |
| `--citadel-dark-orange` | `#f87000` | Canvas / Surface Token |
| `--citadel-medium-grey` | `#818486` | Color / Atmospheric Token |
| `--citadel-light-grey` | `#e3e3e4` | Canvas / Surface Token |
| `--citadel-black` | `#000000` | Canvas / Surface Token |
| `--color-brand-orange` | `var(--citadel-orange)` | Brand / Palette Token |
| `--color-brand-dark-orange` | `var(--citadel-dark-orange)` | Canvas / Surface Token |
| `--color-brand-orange-hover` | `#e17e00` | Brand / Palette Token |
| `--color-brand-black` | `var(--citadel-black)` | Canvas / Surface Token |
| `--color-brand-medium-grey` | `var(--citadel-medium-grey)` | Brand / Palette Token |
| `--color-brand-light-grey` | `var(--citadel-light-grey)` | Canvas / Surface Token |
| `--color-bg-dark` | `var(--citadel-black)` | Canvas / Surface Token |
| `--color-bg-light` | `var(--citadel-light-grey)` | Canvas / Surface Token |
| `--color-text-primary` | `var(--citadel-black)` | Typography Ink Token |
| `--color-accent` | `var(--citadel-orange)` | Brand / Palette Token |
| `--font-citadel-heading` | `"Montserrat", system-ui, sans-serif` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.citadel-site-header> — `citadelgroup-org`)**:
   - Landmark `<header class="citadel-site-header is-over-hero">` hosting `Citadel National Construction Group ` navigation (`About · Case Studies · Map · Principals`), DOM attributes (`data-wp-strategy="async"`, `data-loaded="true"`, `data-module="scrollspy-nav"`, `data-logo-cover-surface="hidden"`), and stylesheet rule `font-primary { font-family:var(--font-primary) }`.
2. **Hero Stage & Focal Lead (<section.citadel-hero> — `National Reach. Local Expertise.`)**:
   - Landmark `<section class="citadel-hero">` presenting display lead `National Reach. Local Expertise.` and copy excerpt *"Citadel Construction Group"* over `#f7953e` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.citadel-about> — `Serving Clients With National Need`)**:
   - Landmark `<section class="citadel-about">` rendering section `Serving Clients With National Needs` with copy *"Citadel National Construction Group leverages seven best-in-class"*, asset references (`www.googletagmanager.com`, `embed`, `theme-core.min.css`, `framework-md.min.css`), and grid rule `font-secondary { font-family:var(--font-secondary) }`.
4. **Interactive Detail & Feature Matrix (<section.citadel-partners> — `Seven firms. One connected constru`)**:
   - Landmark `<section class="citadel-partners flex">` framing `Seven firms. One connected construction network.` and `Case Studies` (*"L o c a l s t r e n g t h . N a t i o n a l s c a l e ."*) with `#818486` surface cards, `#e3e3e4` accents, and `font-open-sans { font-family:var(--font-base) }`.
5. **Colophon & Global Directory Footer (<footer.site-footer-meta> — `https://citadelgroup.org/`)**:
   - Landmark `<footer class="site-footer-meta">` anchoring `Citadel National Construction Gr` footer links (`About · Case Studies · Map · Principals`), copy *"L o c a l s t r e n g t h ."*, and `#e17e00` structural dividers.
