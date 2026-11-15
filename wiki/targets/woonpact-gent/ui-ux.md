# UI & UX Architecture: woonpact-gent

## Overview & Design Identity
- **Target**: `woonpact-gent` (**Home - Woonpact**)
- **Production URL**: [https://woonpact.gent/](https://woonpact.gent/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#fff4e0` accent)
- **Summary**: Alles begint bij betaalbaar wonen. En waar doe je dat liever dan in Gent? De vraag werd groter dan het aanbod, waardoor Gent in een woonc...
- **Total Clean CSS Variables Extracted**: `252` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Satochi`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--text-extralarge)`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: var(--text-large)`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--text-baseline: clamp(1rem, 1.375vw, 1.375rem)`
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f8e6c4` | `var(--color-beige)` in `:root` |
| **Interactive Accent / Highlight** | `#fff4e0` | `var(--color-eggshell)` in `:root` |
| **Secondary / Muted Copy** | `#c9a96e` | `var(--color-sand)` in `:root` |
| **Structural Hairline Border** | `#e6f2fb` | `var(--color-sky)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Satochi", sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `1.5` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75 / 1.125)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |
| `--text-xl--line-height` | `calc(1.75 / 1.25)` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |
| `--text-2xl--line-height` | `calc(2 / 1.5)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-site-header> — `woonpact-gent`)**:
   - Landmark `<header class="c-site-header">` hosting `Home - Woonpact` navigation (`Open oproep · Nieuws · Partners · Agenda`), DOM attributes (`data-category="analytics"`, `data-category="analytics"`, `data-barba="wrapper"`, `data-page-theme="none"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.transition-fade> — `Bouwen aan betaalbaarheid`)**:
   - Landmark `<main class="transition-fade">` presenting display lead `Bouwen aan betaalbaarheid` and copy excerpt *"E v e n g e d u l d"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.transition-fade> — `Laatste updates`)**:
   - Landmark `<main class="transition-fade">` rendering section `Laatste updates` with copy *"Skip to main content"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.transition-fade> — `Eerste Woonpactpioniers dienen pro`)**:
   - Landmark `<main class="transition-fade">` framing `Eerste Woonpactpioniers dienen project in` and `Heb je grond of plannen voor wonen in Gent? Dien...` (*"Bouwen aan betaalbaarheid"*) with `#f8e6c4` surface cards, `#fff4e0` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.c-site-footer> — `https://woonpact.gent/`)**:
   - Landmark `<footer class="c-site-footer">` anchoring `Home - Woonpact` footer links (`Open oproep · Nieuws · Partners · Agenda`), copy *"Alles begint bij betaalbaar wonen. En waar doe je dat liever"*, and `#e6f2fb` structural dividers.
