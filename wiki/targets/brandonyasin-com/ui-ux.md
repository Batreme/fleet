# UI & UX Architecture: brandonyasin-com

## Overview & Design Identity
- **Target**: `brandonyasin-com` (**Brandon Yasin — Creative Director & Designer**)
- **Production URL**: [https://brandonyasin.com](https://brandonyasin.com)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111` canvas, `#fff` ink, `#fff` accent)
- **Summary**: Brand, digital and spatial design within lifestyle and luxury. AI scales the production, not the craft. Based in Denmark, working globally.
- **Total Clean CSS Variables Extracted**: `18` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Unica Pro`
- **Body Font Stack**: `Helvetica Now Variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `4.8rem`, `9rem`, `6.26vw`, `clamp(28px,3.125vw,32px)`, `3.34vw`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `4.8rem`, `9rem`, `6.26vw`, `clamp(28px,3.125vw,32px)`, `3.34vw`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `4.8rem`, `9rem`, `6.26vw`, `clamp(28px,3.125vw,32px)`, `3.34vw`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `4.8rem`, `9rem`, `6.26vw`, `clamp(28px,3.125vw,32px)`, `3.34vw`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111` | `var(--color-main)` in `:root` |
| **Primary Typography Ink** | `#f8f6f2` | `var(--color-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#263b1c` | `var(--color-green)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `:before { border: #fff }` |
| **Secondary / Muted Copy** | `#0000` | `html { color: #0000 }` |
| **Structural Hairline Border** | `#000` | `.img-wrap:after { background-color: #000 }` |
| **Variable Token (`--selection-bg`)** | `#44300033` | `var(--selection-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-main` | `#111` | Brand / Palette Token |
| `--color-bg` | `#f8f6f2` | Canvas / Surface Token |
| `--selection-color` | `#111` | Brand / Palette Token |
| `--selection-bg` | `#44300033` | Canvas / Surface Token |
| `--focus-bg` | `var(--color-main)` | Canvas / Surface Token |
| `--focus-color` | `var(--color-bg)` | Brand / Palette Token |
| `--lvh` | `1vh` | Layout / Spatial Grid Token |
| `--svh` | `1vh` | Layout / Spatial Grid Token |
| `--img-over-opacity` | `0` | Design System Custom Token |
| `--bg-brightness` | `1` | Canvas / Surface Token |
| `--size` | `1168` | Layout / Spatial Grid Token |
| `--cut` | `100%` | Dimension / Scale Token |
| `--color-green` | `#263b1c` | Brand / Palette Token |
| `--line-x` | `0px` | Dimension / Scale Token |
| `--line-w` | `0` | Design System Custom Token |
| `--before-w` | `.9` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `brandonyasin-com`)**:
   - Landmark `<header class="header font-body-12">` hosting `Brandon Yasin — Creative Director & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hid="initial-time-theme"`, `data-v-b4d4802c`, `data-slug="/archive"`, `data-menu-title-lag`), and stylesheet rule `last-child { margin-bottom:0 }`.
2. **Hero Stage & Focal Lead (<section.container> — `archive`)**:
   - Landmark `<section class="container archive-container">` presenting display lead `archive` and copy excerpt *"Brandon Brandon Yasin Yasin Brandon Awwwards Site of the day SOTD"* over `#111` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.header> — `I build refined brands and experie`)**:
   - Landmark `<section class="header about-header">` rendering section `I build refined brands and experiences across dig...` with copy *"Brandon Awwwards Site of the day SOTD Yasin Site of the day SOTD "*, asset references (`entry.Di9rGxLO.css`, `useSeo.HvQkUdpq.css`, `PageTitle.DBPCFnbI.css`, `about.D7v35ChA.css`), and grid rule `focus-visible { background-color:var(--focus-bg);color:var(--focus-color);outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.holder> — `my signature approach is guided by`)**:
   - Landmark `<section class="holder">` framing `my signature approach is guided by core values` and `established design process tried and tested on sm...` (*"Brandon Awwwards Site of the day SOTD"*) with `#263b1c` surface cards, `#fff` accents, and `before { height:.07vw }`.
5. **Colophon & Global Directory Footer (<footer.menu-tile> — `https://brandonyasin.com`)**:
   - Landmark `<footer class="menu-tile">` anchoring `Brandon Yasin — Creative Directo` footer links (`Overview · Index · Archive · About · Contact`), copy *"Site of the day SOTD"*, and `#000` structural dividers.
