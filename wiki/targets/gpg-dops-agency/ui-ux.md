# UI & UX Architecture: gpg-dops-agency

## Overview & Design Identity
- **Target**: `gpg-dops-agency` (**Garvinpromo**)
- **Production URL**: [https://gpg.dops.agency/](https://gpg.dops.agency/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#1051b4` accent)
- **Summary**: Welcome to Garvin Promotion Group, a leading provider of rebate management, spiffs, and loyalty incentive programs
- **Total Clean CSS Variables Extracted**: `48` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PPMori`
- **Body Font Stack**: `PPMori Semi Bold`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--vc-clr-primary)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--vc-clr-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#003c97` | `:before { background-color: #003c97 }` |
| **Interactive Accent / Highlight** | `#1051b4` | `:before { background-color: #1051b4 }` |
| **Secondary / Muted Copy** | `#f15928` | `:before { background-color: #f15928 }` |
| **Structural Hairline Border** | `#d3d3d3` | `:before { background-color: #d3d3d3 }` |
| **Variable Token (`--vc-clr-secondary`)** | `#090f207f` | `var(--vc-clr-secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--line` | `16px` | Dimension / Scale Token |
| `--height-mask` | `22px` | Layout / Spatial Grid Token |
| `--vc-clr-primary` | `#000` | Brand / Palette Token |
| `--vc-clr-secondary` | `#090f207f` | Brand / Palette Token |
| `--vc-clr-white` | `#fff` | Canvas / Surface Token |
| `--vc-icn-width` | `1.2em` | Layout / Spatial Grid Token |
| `--vc-nav-width` | `30px` | Layout / Spatial Grid Token |
| `--vc-nav-height` | `30px` | Layout / Spatial Grid Token |
| `--vc-nav-border-radius` | `0` | Layout / Spatial Grid Token |
| `--vc-nav-color` | `var(--vc-clr-primary)` | Brand / Palette Token |
| `--vc-nav-color-hover` | `var(--vc-clr-secondary)` | Brand / Palette Token |
| `--vc-nav-background` | `transparent` | Canvas / Surface Token |
| `--vc-pgn-width` | `12px` | Layout / Spatial Grid Token |
| `--vc-pgn-height` | `4px` | Layout / Spatial Grid Token |
| `--vc-pgn-margin` | `4px` | Layout / Spatial Grid Token |
| `--vc-pgn-border-radius` | `0` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `gpg-dops-agency`)**:
   - Landmark `<header class="header header--light">` hosting `Garvinpromo` navigation (`Services Services · About us About us · Let's Talk`), DOM attributes (`data-v-537c3597`, `data-v-5f87b270`, `data-v-05812e15`, `data-v-f8de3fbd`), and stylesheet rule `before { border-radius:50%;content:"";display:block;height:100%;left:0;position:a... }`.
2. **Hero Stage & Focal Lead (<section.carousel> — `Welcome to Garvin Promotion Group,`)**:
   - Landmark `<section class="carousel home-strategic__carousel">` presenting display lead `Welcome to Garvin Promotion Group, a leading prov...` and copy excerpt *"Garvin Promotion Group"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.carousel> — `Promotion strategy and development`)**:
   - Landmark `<section class="carousel">` rendering section `Promotion strategy and development` with copy *"Clients success Clients success"*, asset references (`garvinpromo.com`, `favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png`), and grid rule `hover .faq__item-question { color:898995 }`.
4. **Interactive Detail & Feature Matrix (<section.preloader--initial> — `Rebate fulfillment`)**:
   - Landmark `<section class="preloader--initial">` framing `Rebate fulfillment` and `Loyalty programs` (*"Garvin Promotion Group 10220 South 51st Street Phoenix, AZ 85044"*) with `#003c97` surface cards, `#1051b4` accents, and `hover .faq__item-cross { border-color:898995 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://gpg.dops.agency/`)**:
   - Landmark `<footer class="footer bg-dark">` anchoring `Garvinpromo` footer links (`Services Services · About us About us · Let's Talk`), copy *"Welcome to Garvin Promotion Group, a leading provider of reb"*, and `#d3d3d3` structural dividers.
