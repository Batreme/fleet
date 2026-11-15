# UI & UX Architecture: bennos-light-org

## Overview & Design Identity
- **Target**: `bennos-light-org` (**Benno's Light**)
- **Production URL**: [https://bennos-light.org/](https://bennos-light.org/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#9ca3af` / `#000000`)
- **Summary**: Benno Kern, one of only a few Holocaust survivors still alive in Austria, tells his heartbreaking story of survival in the latest experie...
- **Total Clean CSS Variables Extracted**: `43` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Acumin Pro Wide`
- **Body Font Stack**: `La Belle Aurore`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Primary Typography Ink** | `#000000` | `body { background-color: black }` (`#000000`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `body { color: white }` (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--colors-true-black` | `0,0,0` | Canvas / Surface Token |
| `--colors-true-white` | `255,255,255` | Canvas / Surface Token |
| `--colors-black` | `74,46,61` | Canvas / Surface Token |
| `--colors-white` | `244,235,214` | Canvas / Surface Token |
| `--colors-primary` | `74,46,61` | Brand / Palette Token |
| `--colors-secondary` | `244,235,214` | Brand / Palette Token |
| `--colors-accent` | `171,223,251` | Brand / Palette Token |
| `--colors-dark-beige` | `136,121,105` | Canvas / Surface Token |
| `--colors-mid-beige` | `202,192,168` | Brand / Palette Token |
| `--colors-themeClassnames-light` | `theme-light` | Canvas / Surface Token |
| `--colors-themeClassnames-dark` | `theme-dark` | Canvas / Surface Token |
| `--colors-THEME-COLORS-light-primary` | `244,235,214` | Canvas / Surface Token |
| `--colors-THEME-COLORS-light-secondary` | `74,46,61` | Canvas / Surface Token |
| `--colors-THEME-COLORS-dark-primary` | `74,46,61` | Canvas / Surface Token |
| `--colors-THEME-COLORS-dark-secondary` | `244,235,214` | Canvas / Surface Token |
| `--container-max-width` | `87.6923076923077vw` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.is-cookie-banner> — `bennos-light-org`)**:
   - Landmark `<header class="is-cookie-banner">` hosting `Benno's Light` navigation (`Cookiebot · Google · About · Privacy Policy · German`), DOM attributes (`data-version="1.1.0"`, `data-template="generaxion/cookiebot-..."`, `data-tone="neutral"`, `data-v-app`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:cur... }`.
2. **Hero Stage & Focal Lead (<div.is-visible-cookie-banner> — `Benno's Light`)**:
   - Landmark `<div class="is-visible-cookie-banner">` presenting display lead `Benno's Light` and copy excerpt *"This website uses cookies"* over `#9ca3af` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.is-visible-cookie-banner> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="is-visible-cookie-banner">` rendering section `Featured Work & Interactive Showcase` with copy *"We use cookies to personalise content and ads, to provide social "*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<div.is-visible-cookie-banner> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="is-visible-cookie-banner">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Allow all Allow all"*) with `#ffffff` surface cards, `#000000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.scrollbar-none> — `https://bennos-light.org/`)**:
   - Landmark `<footer class="scrollbar-none">` anchoring `Benno's Light` footer links (`Cookiebot · Google · About · Privacy Policy · German`), copy *"Show details Show details"*, and `#000000` structural dividers.
