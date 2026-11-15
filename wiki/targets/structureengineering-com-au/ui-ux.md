# UI & UX Architecture: structureengineering-com-au

## Overview & Design Identity
- **Target**: `structureengineering-com-au` (**Structure Consulting Engineers · Structural Engineering Sydney**)
- **Production URL**: [https://structureengineering.com.au/](https://structureengineering.com.au/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#ffffff` ink, `#F5F5F5` accent)
- **Summary**: Specialists in structural engineering in Sydney, we work across a range of industries from residential to commercial, remedial, governmen...
- **Total Clean CSS Variables Extracted**: `5` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SequelSans`
- **Body Font Stack**: `PPFraktionMono`
- **Monospace / Technical Font Stack**: `PPFraktionMono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `.h2` (`font-size: 3.7em`, `line-height: 1`)
- **Body Copy**: rule `p` (`font-size: 16px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#B9B36D` | `var(--color-gold)` in `:root` |
| **Interactive Accent / Highlight** | `#F5F5F5` | `var(--color-background-grey)` in `:root` |
| **Secondary / Muted Copy** | `#BEBEBE` | `var(--color-grey)` in `:root` |
| **Structural Hairline Border** | `#fff` | `.preloader { background-color: #fff }` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-gold` | `#B9B36D` | Brand / Palette Token |
| `--color-background-grey` | `#F5F5F5` | Canvas / Surface Token |
| `--color-grey` | `#BEBEBE` | Brand / Palette Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--swiper-navigation-color` | `black` | Brand / Palette Token |
| `--wp--preset--aspect-ratio--square` | `1` | Design System Custom Token |
| `--wp--preset--aspect-ratio--4-3` | `4/3` | Design System Custom Token |
| `--wp--preset--aspect-ratio--3-4` | `3/4` | Design System Custom Token |
| `--wp--preset--aspect-ratio--3-2` | `3/2` | Design System Custom Token |
| `--wp--preset--aspect-ratio--2-3` | `2/3` | Design System Custom Token |
| `--structureenginee-bg` | `#000` | Canvas Substrate (from `var(--color-black)` in `:root`) |
| `--structureenginee-ink` | `#ffffff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.top-nav> — `structureengineering-com-au`)**:
   - Landmark `<nav class="top-nav font-PPFraktionMono">` hosting `Structure Consulting Engineers · Str` navigation (`About · Company · Careers · People · Sectors`), DOM attributes (`data-section-background-color="background-color-black"`, `data-rocket-prefetch`, `data-rocket-preload`, `data-rocket-async="style"`), and stylesheet rule `html { scroll-behavior: smooth; }`.
2. **Hero Stage & Focal Lead (<section.section> — `A different approach to traditiona`)**:
   - Landmark `<section class="section section-topbannerhome">` presenting display lead `A different approach to traditional structural en...` and copy excerpt *"About Company Careers"* over `#000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section> — `See our work`)**:
   - Landmark `<section class="section section-intro">` rendering section `See our work` with copy *"Sectors Residential Commercial Public Art"*, asset references (`www.googletagmanager.com`, `SequelSans-Medium.woff2`, `PPFraktionMono-Regular.woff2`, `s.svg`), and grid rule `.bounce { animation: bounce 2s linear 4s infinite alternate; }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Latest work`)**:
   - Landmark `<section class="section section-spread">` framing `Latest work` and `Northbridge House II` (*"Let's build something exceptional."*) with `#B9B36D` surface cards, `#F5F5F5` accents, and `.fadein { animation: fadein 0.5s; }`.
5. **Colophon & Global Directory Footer (<footer.preloadergone> — `https://structureengineering.com.au/`)**:
   - Landmark `<footer class="preloadergone">` anchoring `Structure Consulting Engineers ·` footer links (`About · Company · Careers · People · Sectors`), copy *"Let's build something exceptional"*, and `#fff` structural dividers.
