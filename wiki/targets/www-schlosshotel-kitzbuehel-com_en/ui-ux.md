# UI & UX Architecture: www-schlosshotel-kitzbuehel-com_en

## Overview & Design Identity
- **Target**: `www-schlosshotel-kitzbuehel-com_en` (**Schlosshotel Kitzbühel – a premium experience**)
- **Production URL**: [https://www.schlosshotel-kitzbuehel.com/en](https://www.schlosshotel-kitzbuehel.com/en)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#300316` canvas, `#FFFFFF` ink, `#6e4e5b` accent)
- **Summary**: A beacon of elegance, exclusivity, and warmth – Schlosshotel Kitzbühel is a truly unparalleled retreat.
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Assistant`
- **Body Font Stack**: `lg`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`line-height: 1.2`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1em !important`, `line-height: 1.2`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: 12px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1rem,11.5vw,22.9em)`, `6.8em`, `4em`, `3.5em`, `2em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#300316` | `var(--dna-tldr-bg)` in `:root` |
| **Primary Typography Ink** | `#FFFFFF` | `var(--dna-tldr-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `var(--bl-trigger-text)` in `:root` |
| **Interactive Accent / Highlight** | `#6e4e5b` | `var(--bl-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#42041e` | `.MOD-Banner .MOD-Banner__frame { background-color: #42041e }` |
| **Structural Hairline Border** | `#fff` | `-OffersTeaser__item__request__w... { color: #fff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dna-tldr-bg` | `#300316` | Canvas / Surface Token |
| `--dna-tldr-text` | `#FFFFFF` | Typography Ink Token |
| `--dna-tldr-fs-desktop` | `2.1em` | Dimension / Scale Token |
| `--dna-tldr-fs-mobile` | `1.6em` | Dimension / Scale Token |
| `--track-width` | `52px` | Layout / Spatial Grid Token |
| `--track-height` | `28px` | Layout / Spatial Grid Token |
| `--thumb-size` | `23px` | Layout / Spatial Grid Token |
| `--thumb-gap` | `3px` | Layout / Spatial Grid Token |
| `--track-radius` | `999px` | Elevation / Border Token |
| `--vh` | `9px` | Layout / Spatial Grid Token |
| `--bl-size` | `40px` | Layout / Spatial Grid Token |
| `--bl-desktop-top` | `auto` | Design System Custom Token |
| `--bl-desktop-bottom` | `1.5em` | Dimension / Scale Token |
| `--bl-desktop-left` | `1.5em` | Dimension / Scale Token |
| `--bl-desktop-right` | `auto` | Design System Custom Token |
| `--bl-desktop-box-left` | `1.5em` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.SECT-Header> — `www-schlosshotel-kitzbuehel-com_en`)**:
   - Landmark `<header class="SECT-Header DNA-section">` hosting `Schlosshotel Kitzbühel – a premium e` navigation (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `from { transform:translateX(0) }`.
2. **Hero Stage & Focal Lead (<section.MOD-RoomsTeaser> — `Schlosshotel Kitzbühel`)**:
   - Landmark `<section class="MOD-RoomsTeaser DNA-module">` presenting display lead `Schlosshotel Kitzbühel` and copy excerpt *"Kitzbühel For families For sports enthusiasts For culture lovers "* over `#300316` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.MOD-OffersTeaser> — `Welcome to the threshold of the ex`)**:
   - Landmark `<section class="MOD-OffersTeaser DNA-module">` rendering section `Welcome to the threshold of the extraordinary` with copy *"For sports enthusiasts"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.MOD-Banner .MOD-Banner__outer { display:flex }`.
4. **Interactive Detail & Feature Matrix (<section.MOD-Text> — `For people of refined taste. For y`)**:
   - Landmark `<section class="MOD-Text DNA-module">` framing `For people of refined taste. For you.` and `Schlosshotel offers Not for all. But definitely f...` (*"For culture lovers"*) with `#000000` surface cards, `#6e4e5b` accents, and `.MOD-Banner .MOD-Banner__frame { padding:6.5em 0;flex:1;position:relative;background-color:42041e;overflo... }`.
5. **Colophon & Global Directory Footer (<footer.SECT-Footer> — `https://www.schlosshotel-kitzbuehel.com/en`)**:
   - Landmark `<footer class="SECT-Footer DNA-section">` anchoring `Schlosshotel Kitzbühel – a premi` footer links (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), copy *"Rooms and Suites Packages Inclusive services"*, and `#fff` structural dividers.
