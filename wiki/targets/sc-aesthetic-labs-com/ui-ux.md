---
title: "UI & UX Architecture: sc-aesthetic-labs-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: sc-aesthetic-labs-com

## Overview & Design Identity
- **Target**: `sc-aesthetic-labs-com` (**Digital Systems for Visible Trust – S/C Lab**)
- **Production URL**: [https://sc-aesthetic-labs.com/](https://sc-aesthetic-labs.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#151616` canvas, `#f2f4f4` ink, `#ff4d00` accent)
- **Summary**: Digital Systems for Visible Trust by S/C Lab. Public image, digital form and visible trust for serious brands, clinics and institutions.
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `AL Mono`
- **Body Font Stack**: `AL Suisse`
- **Monospace / Technical Font Stack**: `AL Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60.48px`, `line-height: 60.48px`, `font-weight: 400`); CSS variables `--hero-title-opacity: 0`, `--hero-title-y: 32px`, `--hero-title-blur: 0px`; rule `h1` (`font-size: clamp(48px, 5.6vw, 104px)`, `line-height: 1.02`, `letter-spacing: -0.02em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 89.28px`, `line-height: 91.0656px`, `font-weight: 400`, `letter-spacing: -2.232px`); rule `h2` (`font-size: clamp(30px, 2.45vw, 48px)`, `line-height: 1.12`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `body` (`font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mono: "AL Mono", "SFMono-Regular", Consolas, monospace`, `--hero-label-y: 0px`, `--hero-label-opacity: 1`; rule `.mono` (`font-size: 12px`, `line-height: 16px`, `letter-spacing: 0`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#151616` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f2f4f4` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#696967` | `.type33-dots span { background: #696967 }` |
| **Interactive Accent / Highlight** | `#ff4d00` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ff4d00` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3e3f3f` | `var(--line-dark)` in `:root` (`rgba(247, 248, 248, 0.18)`) |
| **Variable Token (`--off`)** | `#1d1f1f` | `var(--off)` in `:root` |
| **Variable Token (`--soft`)** | `#171818` | `var(--soft)` in `:root` |
| **Variable Token (`--soft-2`)** | `#1d1f20` | `var(--soft-2)` in `:root` |

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
   - Landmark `<header class="page-hero poster-hero">` (`1440x2880px`) hosting `Digital Systems for Visible Trust – ` navigation (`S/C Aesthetic Labs · Approach · Practice · Notes · Contact`), DOM attributes (`data-final-text="S/C Aesthetic Labs"`, `data-final-text="Approach"`, `data-final-text="Practice"`, `data-final-text="Notes"`), and stylesheet rule `body { margin: 0; background: var(--paper); color: var(--white); font-weight: 4... }`.
2. **Hero Stage & Focal Lead (<section.what-grid> — `S/C LABSTM`)**:
   - Landmark `<section class="what-grid tone-graphite">` presenting display lead `S/C LABSTM` and copy excerpt *"S/C Aesthetic Labs designs identities, websites and digital exper"* over `#151616` canvas and `#f2f4f4` ink.
3. **Primary Showcase & Content Grid (<article.what-col> — `S/C Labs TM`)**:
   - Landmark `<article class="what-col">` rendering section `S/C Labs TM` with copy *"Public Image Digital Systems"*, asset references (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `site.css`), and grid rule `textarea { font-weight: 400; }`.
4. **Interactive Detail & Feature Matrix (<article.what-col:nth(2)> — `Public Image`)**:
   - Landmark `<article class="what-col">` framing `Public Image` and `Digital Form` (*"Visible Trust Surface Logic"*) with `#696967` surface cards, `#ff4d00` accents, and `img { display: block; width: 100%; height: 100%; object-fit: cover; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://sc-aesthetic-labs.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Digital Systems for Visible Trus` footer links (`S/C Aesthetic Labs · Approach · Practice · Notes · Contact`), copy *"Each project takes the shape the brand needs. Discuss a proj"*, and `#3e3f3f` structural dividers.
