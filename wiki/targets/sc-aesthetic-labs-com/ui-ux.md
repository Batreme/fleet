# UI & UX Architecture: sc-aesthetic-labs-com

## Overview & Design Identity
- **Target**: `sc-aesthetic-labs-com` (**Digital Systems for Visible Trust – S/C Lab**)
- **Production URL**: [https://sc-aesthetic-labs.com/](https://sc-aesthetic-labs.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#151616` canvas, `#f2f4f4` ink, `#171818` accent)
- **Summary**: Digital Systems for Visible Trust by S/C Lab. Public image, digital form and visible trust for serious brands, clinics and institutions.
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `AL Suisse`
- **Body Font Stack**: `AL Mono`
- **Monospace / Technical Font Stack**: `AL Mono`
- **Hero Display (`H1`)**: CSS variables `--hero-title-opacity: 0`, `--hero-title-y: 32px`, `--hero-title-blur: 0px`; rule `h1` (`font-size: clamp(48px, 5.6vw, 104px)`, `line-height: 1.02`, `letter-spacing: -0.02em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(30px, 2.45vw, 48px)`, `line-height: 1.12`, `font-weight: 400`)
- **Body Copy**: rule `body` (`font-weight: 400`)
- **Metadata & Labels**: CSS variables `--mono: "AL Mono", "SFMono-Regular", Consolas, monospace`, `--hero-label-y: 0px`, `--hero-label-opacity: 1`; rule `.mono` (`font-size: 12px`, `line-height: 16px`, `letter-spacing: 0`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#151616` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#f2f4f4` | `var(--white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1d1f1f` | `var(--off)` in `:root` |
| **Interactive Accent / Highlight** | `#171818` | `var(--soft)` in `:root` |
| **Secondary / Muted Copy** | `#1d1f20` | `var(--soft-2)` in `:root` |
| **Structural Hairline Border** | `#FF4D00` | `var(--accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#151616` | Canvas / Surface Token |
| `--ink` | `#151616` | Typography Ink Token |
| `--white` | `#f2f4f4` | Canvas / Surface Token |
| `--off` | `#1d1f1f` | Color / Atmospheric Token |
| `--soft` | `#171818` | Color / Atmospheric Token |
| `--soft-2` | `#1d1f20` | Color / Atmospheric Token |
| `--line-dark` | `rgba(247, 248, 248, 0.18)` | Canvas / Surface Token |
| `--accent` | `#FF4D00` | Brand / Palette Token |
| `--edge` | `40px` | Dimension / Scale Token |
| `--gutter` | `30px` | Layout / Spatial Grid Token |
| `--max` | `1760px` | Dimension / Scale Token |
| `--font` | `"AL Suisse", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--mono` | `"AL Mono", "SFMono-Regular", Consolas, monospace` | Typography / Scale Token |
| `--tight` | `-0.025em` | Dimension / Scale Token |
| `--image-matte-top` | `rgba(18, 19, 20, 0.18)` | Color / Atmospheric Token |
| `--image-matte-bottom` | `rgba(18, 19, 20, 0.42)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.page-hero> — `sc-aesthetic-labs-com`)**:
   - Landmark `<header class="page-hero poster-hero">` hosting `Digital Systems for Visible Trust – ` navigation (`S/C Aesthetic Labs · Approach · Practice · Notes · Contact`), DOM attributes (`data-final-text="S/C Aesthetic Labs"`, `data-final-text="Approach"`, `data-final-text="Practice"`, `data-final-text="Notes"`), and stylesheet rule `body { margin: 0; background: var(--paper); color: var(--white); font-weight: 4... }`.
2. **Hero Stage & Focal Lead (<section.what-grid> — `S/C Labs TM`)**:
   - Landmark `<section class="what-grid tone-graphite">` presenting display lead `S/C Labs TM` and copy excerpt *"S/C Aesthetic Labs"* over `#151616` canvas and `#f2f4f4` ink.
3. **Primary Showcase & Content Grid (<article.what-col> — `Opening`)**:
   - Landmark `<article class="what-col">` rendering section `Opening` with copy *"Public Image Digital Systems"*, asset references (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `site.css`), and grid rule `textarea { font-weight: 400; }`.
4. **Interactive Detail & Feature Matrix (<article.what-col> — `Public Image`)**:
   - Landmark `<article class="what-col">` framing `Public Image` and `Digital Form` (*"Visible Trust Surface Logic"*) with `#1d1f1f` surface cards, `#171818` accents, and `img { display: block; width: 100%; height: 100%; object-fit: cover; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://sc-aesthetic-labs.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Digital Systems for Visible Trus` footer links (`S/C Aesthetic Labs · Approach · Practice · Notes · Contact`), copy *"S/C Labs is an independent practice for brands whose public "*, and `#FF4D00` structural dividers.
