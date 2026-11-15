# UI & UX Architecture: kamdalej-sk_en

## Overview & Design Identity
- **Target**: `kamdalej-sk_en` (**Mastercard · Where Next**)
- **Production URL**: [https://kamdalej.sk/en](https://kamdalej.sk/en)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#FF671B` canvas, `#141413` ink, `#D6C4BB` accent)
- **Summary**: A digital tool helping people in Slovakia find better career opportunities by matching their skills with real labour market needs
- **Total Clean CSS Variables Extracted**: `149` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Mark Offc For MC`
- **Body Font Stack**: `Futura`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--fz-h1-mob: 40`, `--fz-h1: 64`; rule `.title` (`font-size: calc(var(--fz-body-xs) * 1px...`, `font-weight: var(--fw-medium)`)
- **Section Heading (`H2`)**: CSS variables `--fz-h2-mob: 36`, `--fz-h2: 52`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy**: CSS variables `--fz-body-xl-mob: 30`, `--fz-body-xl: 36`, `--fz-body-l-mob: 20`; rule `p` (`font-size: 14px`, `line-height: 20px`, `font-weight: var(--fw-normal)`)
- **Metadata & Labels**: rule `.label` (`font-size: calc(var(--fz-body-xs) * 1px...`, `line-height: 14px`, `font-weight: var(--fw-normal)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#FF671B` | `var(--orange)` in `:root` |
| **Primary Typography Ink** | `#882D00` | `var(--orangeh)` in `:root` |
| **Elevated Surface / Card Substrate** | `#C14000` | `var(--orange_wcag)` in `:root` |
| **Interactive Accent / Highlight** | `#D6C4BB` | `var(--orange_wcag_transparent)` in `:root` |
| **Secondary / Muted Copy** | `#141413` | `var(--gd)` in `:root` |
| **Structural Hairline Border** | `#F3EFEC` | `var(--gl)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--oki-base` | `4px` | Dimension / Scale Token |
| `--pad` | `calc(var(--oki-base) * 1)` | Layout / Spatial Grid Token |
| `--pad_x0` | `calc(var(--oki-base) * 0)` | Layout / Spatial Grid Token |
| `--pad_x1` | `calc(var(--oki-base) * 1)` | Layout / Spatial Grid Token |
| `--pad_x2` | `calc(var(--oki-base) * 2)` | Layout / Spatial Grid Token |
| `--pad_x3` | `calc(var(--oki-base) * 3)` | Layout / Spatial Grid Token |
| `--pad_x4` | `calc(var(--oki-base) * 4)` | Layout / Spatial Grid Token |
| `--pad_x5` | `calc(var(--oki-base) * 5)` | Layout / Spatial Grid Token |
| `--pad_x6` | `calc(var(--oki-base) * 6)` | Layout / Spatial Grid Token |
| `--pad_x7` | `calc(var(--oki-base) * 7)` | Layout / Spatial Grid Token |
| `--pad_x8` | `calc(var(--oki-base) * 8)` | Layout / Spatial Grid Token |
| `--pad_x9` | `calc(var(--oki-base) * 9)` | Layout / Spatial Grid Token |
| `--pad_x10` | `calc(var(--oki-base) * 10)` | Layout / Spatial Grid Token |
| `--pad_x11` | `calc(var(--oki-base) * 11)` | Layout / Spatial Grid Token |
| `--pad_x12` | `calc(var(--oki-base) * 12)` | Layout / Spatial Grid Token |
| `--pad_x13` | `calc(var(--oki-base) * 13)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.loaded> — `kamdalej-sk_en`)**:
   - Landmark `<header class="loaded">` hosting `Mastercard · Where Next` navigation (`Work Permit`), DOM attributes (`data-document-language="true"`, `data-domain-script="019c98a8-e583-7fb5-a6..."`, `data-v-app`, `data-v-a006813b`), and stylesheet rule `.flash { -webkit-animation-name:flash;animation-name:flash }`.
2. **Hero Stage & Focal Lead (<section.hero> — `WhereNext can you move forward pro`)**:
   - Landmark `<section class="hero heroMain">` presenting display lead `WhereNext can you move forward professionally?` and copy excerpt *"Tetiana (Ukraine) Former warehouse worker, now construction engin"* over `#FF671B` canvas and `#141413` ink.
3. **Primary Showcase & Content Grid (<section.heroForm> — `Powered by trusted partners`)**:
   - Landmark `<section class="heroForm">` rendering section `Powered by trusted partners` with copy *"Former warehouse worker,"*, asset references (`fav.svg`, `cdn.cookielaw.org`, `assets.adobedtm.com`, `otSDKStub.js`), and grid rule `.pulse { -webkit-animation-name:pulse;animation-name:pulse }`.
4. **Interactive Detail & Feature Matrix (<section.partners> — `Mastercard`)**:
   - Landmark `<section class="partners">` framing `Mastercard` and `IOM` (*"now construction engineer."*) with `#C14000` surface cards, `#D6C4BB` accents, and `.rubberBand { -webkit-animation-name:rubberBand;animation-name:rubberBand }`.
5. **Colophon & Global Directory Footer (<footer.aic> — `https://kamdalej.sk/en`)**:
   - Landmark `<footer class="aic">` anchoring `Mastercard · Where Next` footer links (`Work Permit`), copy *"Noura (Lebanon) Former call center agent, now Head of Reserv"*, and `#F3EFEC` structural dividers.
