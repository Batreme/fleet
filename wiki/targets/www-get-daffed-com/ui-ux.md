# UI & UX Architecture: www-get-daffed-com

## Overview & Design Identity
- **Target**: `www-get-daffed-com` (**Dafne Salvatori · Brand, design and marketing, Europe**)
- **Production URL**: [https://www.get-daffed.com/](https://www.get-daffed.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f8f6` canvas, `#111` ink, `#111` accent)
- **Summary**: Dafne Salvatori: Italian creative working across art direction, brand and marketing.
- **Total Clean CSS Variables Extracted**: `39` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Tight Variable`
- **Body Font Stack**: `Inter Tight Variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--step-0)`, `var(--step--1)`, `.875rem`, `var(--step-5)`, `var(--step-4)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--step-0)`, `var(--step--1)`, `.875rem`, `var(--step-5)`, `var(--step-4)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--step-0)`, `var(--step--1)`, `.875rem`, `var(--step-5)`, `var(--step-4)`)
- **Metadata & Labels**: rule `,.label` (`font-size: .875rem`, `line-height: 1.3`, `letter-spacing: -.01em`, `font-weight: 650`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f8f6` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#eeeeeb` | `var(--paper-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e4e4e0` | `var(--tissue)` in `:root` |
| **Interactive Accent / Highlight** | `#111` | `var(--ink)` in `:root` |
| **Secondary / Muted Copy** | `#474745` | `var(--ink-2)` in `:root` |
| **Structural Hairline Border** | `#6b6b66` | `var(--ink-3)` in `:root` |
| **Variable Token (`--line`)** | `#11111124` | `var(--line)` in `:root` |
| **Variable Token (`--line-strong`)** | `#1119` | `var(--line-strong)` in `:root` |
| **Variable Token (`--accent`)** | `#c3d0df` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-ink`)** | `#2d3b4d` | `var(--accent-ink)` in `:root` |
| **Variable Token (`--signal`)** | `#ff3d1f` | `var(--signal)` in `:root` |
| **Variable Token (`--red`)** | `#e10600` | `var(--red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#f8f8f6` | Canvas / Surface Token |
| `--paper-2` | `#eeeeeb` | Canvas / Surface Token |
| `--tissue` | `#e4e4e0` | Color / Atmospheric Token |
| `--ink` | `#111` | Typography Ink Token |
| `--ink-2` | `#474745` | Typography Ink Token |
| `--ink-3` | `#6b6b66` | Typography Ink Token |
| `--line` | `#11111124` | Color / Atmospheric Token |
| `--line-strong` | `#1119` | Color / Atmospheric Token |
| `--accent` | `#c3d0df` | Brand / Palette Token |
| `--accent-ink` | `#2d3b4d` | Typography Ink Token |
| `--signal` | `#ff3d1f` | Color / Atmospheric Token |
| `--red` | `#e10600` | Color / Atmospheric Token |
| `--margin` | `clamp(20px, 4vw, 56px)` | Layout / Spatial Grid Token |
| `--gutter` | `clamp(12px, 1.6vw, 24px)` | Layout / Spatial Grid Token |
| `--maxw` | `1680px` | Dimension / Scale Token |
| `--header-h` | `64px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-get-daffed-com`)**:
   - Landmark `<header class="site-header">` hosting `Dafne Salvatori · Brand, design and ` navigation (`Work · Side quests · How I work · About · Contact`), DOM attributes (`data-header`, `data-astro-cid-nen7h5rs`, `data-astro-cid-vjgwiq3r`, `data-drop`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Dafne S .`)**:
   - Landmark `<section class="hero">` presenting display lead `Dafne S .` and copy excerpt *"Brand, design and marketing. Made in Europe."* over `#f8f8f6` canvas and `#111` ink.
3. **Primary Showcase & Content Grid (<section.intro> — `Designer by training. Marketer by `)**:
   - Landmark `<section class="intro wrap">` rendering section `Designer by training. Marketer by trade. Builder...` with copy *"Head of Marketing at Advanced Biomedical Concept since January 20"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `sitemap-index.xml`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100%;scroll-behavior:smooth }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Now. Brand, website and evidence t`)**:
   - Landmark `<section class="section now">` framing `Now. Brand, website and evidence tools at ABC , a...` and `Selected work` (*"All work and archive →"*) with `#e4e4e0` surface cards, `#111` accents, and `canvas { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.get-daffed.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Dafne Salvatori · Brand, design ` footer links (`Work · Side quests · How I work · About · Contact`), copy *"ABC brand and digital A new website, live since June 2026, b"*, and `#6b6b66` structural dividers.
