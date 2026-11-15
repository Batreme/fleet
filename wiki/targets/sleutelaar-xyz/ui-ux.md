# UI & UX Architecture: sleutelaar-xyz

## Overview & Design Identity
- **Target**: `sleutelaar-xyz` (**Hans Sleutelaar · Officiële website**)
- **Production URL**: [https://sleutelaar.xyz/](https://sleutelaar.xyz/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#f0e6db`)
- **Summary**: Digitaal archief over dichter, journalist en Nieuwe Stijl-oprichter Hans Sleutelaar (1935–2020). Gedichten, essays, foto's en bibliografie.
- **Total Clean CSS Variables Extracted**: `12` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ABC Monument Grotesk`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0d0d` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#009dd8` | `var(--color-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#f0e6db` | `var(--color-beige)` in `:root` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#0d0d0d` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-blue` | `#009dd8` | Brand / Palette Token |
| `--color-beige` | `#f0e6db` | Brand / Palette Token |
| `--z-index-filter-clone` | `20` | Elevation / Border Token |
| `--z-index-chrome` | `100` | Elevation / Border Token |
| `--gap-scale` | `1` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--sleutelaar-xyz-bg` | `#0d0d0d` | Canvas Substrate (from `var(--color-black)` in `:root`) |
| `--sleutelaar-xyz-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.uppercase> — `sleutelaar-xyz`)**:
   - Landmark `<header class="uppercase fixed">` hosting `Hans Sleutelaar · Officiële website` navigation (`Biografie · Index · Gedichten · Archief`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-engine="three.js r185"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.flex> — `Samen met`)**:
   - Landmark `<section class="flex flex-col">` presenting display lead `Samen met` and copy excerpt *"Hans Sleutelaar (22 september 1935 – 25 juni 2020). Dichter - Jou"* over `#0d0d0d` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.flex> — `Uitgevers en instituties`)**:
   - Landmark `<section class="flex flex-col">` rendering section `Uitgevers en instituties` with copy *"Voor het betere schrijfwerk Sleutelaar groeide op als enigs kind "*, asset references (`ABCMonumentGroteskTrial-Regular.otf`, `ABCMonumentGroteskTrial-Medium.otf`, `6b9a08feb31cdbce07aca8010c8613f21...`, `0.CvILTd3z.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Voor het betere schrijfwerk Sleute`)**:
   - Landmark `<section class="flex flex-col">` framing `Voor het betere schrijfwerk Sleutelaar groeide o` and `Hij bleef nauw betrokken bij het behoud, het red` (*"Hij bleef nauw betrokken bij het behoud, het redigeren en heruitg"*) with `#009dd8` surface cards, `#f0e6db` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.right-0> — `https://sleutelaar.xyz/`)**:
   - Landmark `<footer class="right-0">` anchoring `Hans Sleutelaar · Officiële webs` footer links (`Biografie · Index · Gedichten · Archief`), copy *"2018 International Film Festival Rotterdam (IFFR) - première"*, and `#000000` structural dividers.
