# UI & UX Architecture: belgradearbor-rs_en

## Overview & Design Identity
- **Target**: `belgradearbor-rs_en` (**Belgrade Arbor · Residential & Business Complex in New Belgrade**)
- **Production URL**: [https://belgradearbor.rs/en](https://belgradearbor.rs/en)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#fb2c36` / `#2e3a26`)
- **Summary**: Discover Belgrade Arbor - premium apartments and business spaces in New Belgrade. Explore residences, amenities, location, and availability.
- **Total Clean CSS Variables Extracted**: `61` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Work Sans`
- **Body Font Stack**: `Work Sans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `20rem`, `10rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `20rem`, `10rem`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdfbef` | `var(--color-vanilla)` in `:root` |
| **Interactive Accent / Highlight** | `#2e3a26` | `var(--color-pine-green)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--card)` in `:root` |
| **Structural Hairline Border** | `#0a0a0a` | `var(--card-foreground)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-workSans` | `"Work Sans", "Work Sans Fallback"` | Typography / Scale Token |
| `--font-editorialOld` | `"editorialOld", "editorialOld Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-workSans)` | Typography / Scale Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.mt-12> — `belgradearbor-rs_en`)**:
   - Landmark `<nav class="mt-12 flex">` hosting `Belgrade Arbor · Residential & Busin` navigation (`Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-cookieconsent="ignore"`), and stylesheet rule `sans_5fdc899b-module__sptEXa__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Belgrade Arbor`)**:
   - Landmark `<section class="relative">` presenting display lead `Belgrade Arbor` and copy excerpt *"3D Experience 3D Experience"* over `#fb2c36` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.introduction-mobile> — `The visual identity of Belgrade Ar`)**:
   - Landmark `<section class="introduction-mobile relative">` rendering section `The visual identity of Belgrade Arbor is defined...` with copy *"Residences Residences"*, asset references (`0p5o.wdb6s0x3.css`, `13l3zbj81552..css`, `0eqspdm2dt5_-.css`, `00u~npbo7.a04.js`), and grid rule `sans_5fdc899b-module__sptEXa__var... { --font-workSans:"Work Sans", "Work Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Belgrade Arbor isn't just another `)**:
   - Landmark `<section class="relative z-1">` framing `Belgrade Arbor isn't just another addition to the...` and `A N e w C h a p t e r i n P r e s t i g i o u s L...` (*"Retail Spaces Retail Spaces"*) with `#fdfbef` surface cards, `#2e3a26` accents, and `lold_a81ffa36-module__Y0KS7a__cla... { font-family:editorialOld,editorialOld Fallback }`.
5. **Colophon & Global Directory Footer (<footer.to-vanilla> — `https://belgradearbor.rs/en`)**:
   - Landmark `<footer class="to-vanilla relative">` anchoring `Belgrade Arbor · Residential & B` footer links (`Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`), copy *"Amenities Amenities"*, and `#0a0a0a` structural dividers.
