# UI & UX Architecture: rubenwalma-nl

## Overview & Design Identity
- **Target**: `rubenwalma-nl` (**Ruben Walma – Filmmaker & videoproductie Groningen**)
- **Production URL**: [https://rubenwalma.nl/](https://rubenwalma.nl/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#5766ab` / `#1D1D1D`)
- **Summary**: Filmmaker uit Groningen voor aftermovies, campagnes en creatieve videoproducties. Dynamische video’s met tempo, sfeer en een eigen stijl.
- **Total Clean CSS Variables Extracted**: `58` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Pacaembu`
- **Body Font Stack**: `max(calc(var(--size-font) * 1.6)`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2.66em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.35em`, `line-height: 1.3`)
- **Body Copy**: rule `p` (`font-size: calc(var(--size-font)*2)`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--size-font)`, `3.3em`, `2.5em`, `1.6em`, `4em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#5766ab` | `var(--primary)` in `:root` |
| **Primary Typography Ink** | `#121212` | `var(--black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--white)` in `:root` |
| **Interactive Accent / Highlight** | `#1D1D1D` | `var(--grey)` in `:root` |
| **Secondary / Muted Copy** | `#131313` | `var(--button-040-color)` in `:root` |
| **Structural Hairline Border** | `#efeeec` | `var(--button-040-color-arrow)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--primary` | `#5766ab` | Brand / Palette Token |
| `--black` | `#121212` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--grey` | `#1D1D1D` | Color / Atmospheric Token |
| `--size-container-ideal` | `390` | Layout / Spatial Grid Token |
| `--size-container-min` | `320px` | Layout / Spatial Grid Token |
| `--size-container-max` | `479px` | Layout / Spatial Grid Token |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container-max))` | Layout / Spatial Grid Token |
| `--size-unit` | `10` | Layout / Spatial Grid Token |
| `--grid-columns` | `4` | Layout / Spatial Grid Token |
| `--grid-gap` | `1em` | Layout / Spatial Grid Token |
| `--container-padding` | `2em` | Layout / Spatial Grid Token |
| `--roll-line` | `1.45` | Design System Custom Token |
| `--roll-trim` | `.225em` | Dimension / Scale Token |
| `--nav-contact-gap` | `calc(var(--size-font) * 1.2)` | Layout / Spatial Grid Token |
| `--nav-contact-font` | `max(calc(var(--size-font) * 1.6), calc(24px - var(--nav-contact-gap)))` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `rubenwalma-nl`)**:
   - Landmark `<header class="lenis">` hosting `Ruben Walma – Filmmaker & videoprodu` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-barba="wrapper"`, `data-scrolling-started="false"`, `data-scrolling-direction="up"`, `data-page-theme="light"`), and stylesheet rule `root { --size-container-ideal:550;--size-container-min:480px;--size-container-m... }`.
2. **Hero Stage & Focal Lead (<main.logo> — `Videoproductie Groningen`)**:
   - Landmark `<main class="logo">` presenting display lead `Videoproductie Groningen` and copy excerpt *"Over Ruben Over Ruben"* over `#5766ab` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.menu-toggle> — `F i l m m a k e r u i t G r o n i `)**:
   - Landmark `<main class="menu-toggle">` rendering section `F i l m m a k e r u i t G r o n i n g e n u u t G...` with copy *"Projecten Projecten"*, asset references (`favicon-dark2.png`, `favicon-white.png`, `sitemap.xml`, `stream.mux.com`), and grid rule `selection { background-color:var(--primary);color:fff }`.
4. **Interactive Detail & Feature Matrix (<main.menu-toggle__label> — `Over Ruben`)**:
   - Landmark `<main class="menu-toggle__label">` framing `Over Ruben` and `info@rubenwalma.nl Klik om te kopiëren Gekopieer` (*"info@rubenwalma.nl Klik om te kopiëren Gekopieerd!"*) with `#fff` surface cards, `#1D1D1D` accents, and `html { background-color:var(--black);color:var(--white);scrollbar-gutter:stable... }`.
5. **Colophon & Global Directory Footer (<footer.hamburger> — `https://rubenwalma.nl/`)**:
   - Landmark `<footer class="hamburger">` anchoring `Ruben Walma – Filmmaker & videop` footer links (`Overview · Index · Archive · About · Contact`), copy *"info@rubenwalma.nl"*, and `#efeeec` structural dividers.
