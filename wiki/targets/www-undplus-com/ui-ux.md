# UI & UX Architecture: www-undplus-com

## Overview & Design Identity
- **Target**: `www-undplus-com` (**UNDPLUS — Brand Architecture & Spatial Design Studio**)
- **Production URL**: [https://www.undplus.com](https://www.undplus.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ca9df1` canvas, `#ffd650` ink, `#0daa75` accent)
- **Summary**: Studio for brand architecture, spatial design and live experiences. We build trade fair booths, brand spaces and installations from Berli...
- **Total Clean CSS Variables Extracted**: `29` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins Regular`
- **Body Font Stack**: `Poppins Black`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 108px`, `line-height: 1.1em`, `letter-spacing: 0em`, `font-weight: 700`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `108px`)
- **Body Copy**: rule `p` (`font-size: 13px`, `line-height: 1.6em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ca9df1` | `var(--token-832a9c22-d657-4637-89aa-cbcc712eb257)` in `:root` |
| **Primary Typography Ink** | `#ffd650` | `var(--token-d9ed1eb8-0c54-4136-bf85-5e5373c04bfa)` in `:root` |
| **Elevated Surface / Card Substrate** | `#93d4f2` | `var(--token-fb37ef9f-b04f-4314-9731-cff242a9823b)` in `:root` |
| **Interactive Accent / Highlight** | `#0daa75` | `var(--token-86e11354-2bd9-45a6-a3ed-8f01f856a058)` in `:root` |
| **Secondary / Muted Copy** | `#f3c6b1` | `var(--token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a)` in `:root` |
| **Structural Hairline Border** | `#f08fc7` | `var(--token-54b8b414-a4ad-4bad-a655-869fc0cbd561)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-832a9c22-d657-4637-89aa-cbcc712eb257` | `#ca9df1` | Color / Atmospheric Token |
| `--token-d9ed1eb8-0c54-4136-bf85-5e5373c04bfa` | `#ffd650` | Color / Atmospheric Token |
| `--token-fb37ef9f-b04f-4314-9731-cff242a9823b` | `#93d4f2` | Color / Atmospheric Token |
| `--token-86e11354-2bd9-45a6-a3ed-8f01f856a058` | `#0daa75` | Color / Atmospheric Token |
| `--token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a` | `#f3c6b1` | Color / Atmospheric Token |
| `--token-54b8b414-a4ad-4bad-a655-869fc0cbd561` | `#f08fc7` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |
| `--line-height` | `var(--framer-line-height)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.framer-dYpKI> — `www-undplus-com`)**:
   - Landmark `<header class="framer-dYpKI">` hosting `UNDPLUS — Brand Architecture & Spati` navigation (`Brand Architecture · Retail & Hospitality · Workplace & New Work`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.framer-ap504g> — `UNDPLUS Studio for brand experienc`)**:
   - Landmark `<section class="framer-ap504g">` presenting display lead `UNDPLUS Studio for brand experiences in real life...` and copy excerpt *"brand experiences in real life b r a n d e x p e r i e n c e s i "* over `#ca9df1` canvas and `#ffd650` ink.
3. **Primary Showcase & Content Grid (<section.framer-AYmJg> — `From concept to execution. Ideas b`)**:
   - Landmark `<section class="framer-AYmJg">` rendering section `From concept to execution. Ideas become spaces. S...` with copy *"brand experiences in real life"*, asset references (`cXo2Pf7EWgS5at03i8N3qhgZg.svg`, `S6PCFl3VKfoljDTPsWBO3MD8eps.svg`, `gtm.js`, `script`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<section.framer-3gfgd> — `360° FULL SERVICE`)**:
   - Landmark `<section class="framer-3gfgd">` framing `360° FULL SERVICE` and `Brand Architecture` (*"b r a n d e x p e r i e n c e s i n r e a l l i f e"*) with `#93d4f2` surface cards, `#0daa75` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-LFW7G> — `https://www.undplus.com`)**:
   - Landmark `<footer class="framer-LFW7G">` anchoring `UNDPLUS — Brand Architecture & S` footer links (`Brand Architecture · Retail & Hospitality · Workplace & New Work`), copy *"e x p e r i e n c e s"*, and `#f08fc7` structural dividers.
