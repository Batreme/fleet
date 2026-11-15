# UI & UX Architecture: ladolfinajumping-com

## Overview & Design Identity
- **Target**: `ladolfinajumping-com` (**La Dolfina Jumping. World class genetics, breed in Argentina**)
- **Production URL**: [https://ladolfinajumping.com/](https://ladolfinajumping.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fbe0b6` canvas, `#0d1620` ink, `#c7bcac` accent)
- **Summary**: We are dedicated to create the finest show jumping horses through our cutting-edge breeding program in Argentina by sourcing and importin...
- **Total Clean CSS Variables Extracted**: `12` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Marcellus`
- **Body Font Stack**: `Alpine Script`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: .25em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `clamp(32px,8vw,36px)`, `clamp(32px,8vw,48px)`, `clamp(32px,8vw,60px)`)
- **Body Copy**: rule `p` (`font-weight: 500`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `clamp(32px,8vw,36px)`, `clamp(32px,8vw,48px)`, `clamp(32px,8vw,60px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fbe0b6` | `var(--color-primary)` in `:root` |
| **Primary Typography Ink** | `#0a1b2e` | `var(--color-secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#be7e21` | `var(--color-tertiary)` in `:root` |
| **Interactive Accent / Highlight** | `#c7bcac` | `var(--color-quaternary)` in `:root` |
| **Secondary / Muted Copy** | `#475768` | `var(--color-p)` in `:root` |
| **Structural Hairline Border** | `#0d1620` | `var(--color-dark-strong)` in `:root` |
| **Variable Token (`--color-footer`)** | `#162638` | `var(--color-footer)` in `:root` |
| **Variable Token (`--form-brdr`)** | `#efe7dc` | `var(--form-brdr)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |
| **Variable Token (`--swiper-preloader-color`)** | `#fff` | `var(--swiper-preloader-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-primary` | `"Noto Sans Display", sans-serif` | Brand / Palette Token |
| `--font-secondary` | `"Alpine Script" !important` | Brand / Palette Token |
| `--font-tertiary` | `"Marcellus", "Dualis Lite", "Noto Sans Display", sans-serif` | Typography / Scale Token |
| `--color-primary` | `#fbe0b6` | Brand / Palette Token |
| `--color-secondary` | `#0a1b2e` | Brand / Palette Token |
| `--color-tertiary` | `#be7e21` | Brand / Palette Token |
| `--color-quaternary` | `#c7bcac` | Brand / Palette Token |
| `--color-form` | `rgb(175, 145, 95)` | Brand / Palette Token |
| `--color-p` | `#475768` | Brand / Palette Token |
| `--color-dark-strong` | `#0d1620` | Canvas / Surface Token |
| `--color-footer` | `#162638` | Brand / Palette Token |
| `--form-brdr` | `2px solid #efe7dc` | Color / Atmospheric Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--ladolfinajumping-bg` | `#fbe0b6` | Canvas Substrate (from `var(--color-primary)` in `:root`) |
| `--ladolfinajumping-ink` | `#0d1620` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `ladolfinajumping-com`)**:
   - Landmark `<header class="header has--bg-darken">` hosting `La Dolfina Jumping. World class gene` navigation (`Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`), DOM attributes (`data-speed="0.5"`, `data-transition="opacity-in"`, `data-speed="0.25"`, `data-transition="opacity-scale-in-group"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<article.loader> — `D e l i v e r i n g A c c e s s t `)**:
   - Landmark `<article class="loader">` presenting display lead `D e l i v e r i n g A c c e s s t o e x c e p t i...` and copy excerpt *"Tour & Championship Tour y Campeonatos"* over `#fbe0b6` canvas and `#0d1620` ink.
3. **Primary Showcase & Content Grid (<section.o-section> — `A n e x c l u s i v e b r a n d`)**:
   - Landmark `<section class="o-section c-brand">` rendering section `A n e x c l u s i v e b r a n d` with copy *"Tour & Championship"*, asset references (`289546863693632`, `fbevents.js`, `gtm.js`, `favicon.png`), and grid rule `html { height:auto;font-size:16px }`.
4. **Interactive Detail & Feature Matrix (<section.o-section> — `A d o l f o C a m b i a s o`)**:
   - Landmark `<section class="o-section c-breeding">` framing `A d o l f o C a m b i a s o` and `B r e e d i n g` (*"Tour y Campeonatos"*) with `#be7e21` surface cards, `#c7bcac` accents, and `html.lenis { height:auto;scroll-behavior:initial }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ladolfinajumping.com/`)**:
   - Landmark `<footer class="footer bg-white">` anchoring `La Dolfina Jumping. World class ` footer links (`Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`), copy *"Equipment Equipamiento Saddles Bridles Monturas Cabezadas"*, and `#0d1620` structural dividers.
