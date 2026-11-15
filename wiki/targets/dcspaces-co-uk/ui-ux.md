# UI & UX Architecture: dcspaces-co-uk

## Overview & Design Identity
- **Target**: `dcspaces-co-uk` (**Chorley Builders · Extensions & Renovations · DC Carpentry**)
- **Production URL**: [https://dcspaces.co.uk/](https://dcspaces.co.uk/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#14161A` canvas, `#FFFFFF` ink, `#F2F1ED` accent)
- **Summary**: Family-run builders in Chorley. House extensions, wall and chimney breast removals, kitchens and bespoke staircases across Lancashire. Fr...
- **Total Clean CSS Variables Extracted**: `29` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--cc-font-display: 'Satoshi', system-ui, sans-serif`; rule `h1` (`font-size: clamp(2.6rem, 5.6vw, 4.6rem)`, `line-height: 1`, `letter-spacing: -.045em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.5rem, 2.4vw, 2.1rem)`)
- **Body Copy**: CSS variables `--cc-font-body: 'Satoshi', system-ui, sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `.76rem`, `clamp(2.7rem, 6.4vw, 5rem)`, `clamp(2.1rem, 4.4vw, 3.5rem)`, `clamp(1.6rem, 2.6vw, 2.2rem)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#14161A` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#4A5058` | `var(--ink-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#767D86` | `var(--ink-3)` in `:root` |
| **Interactive Accent / Highlight** | `#F2F1ED` | `var(--paper)` in `:root` |
| **Secondary / Muted Copy** | `#E8E6E0` | `var(--paper-2)` in `:root` |
| **Structural Hairline Border** | `#FFFFFF` | `var(--white)` in `:root` |
| **Variable Token (`--brand`)** | `#2e432f` | `var(--brand)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#14161A` | Typography Ink Token |
| `--ink-2` | `#4A5058` | Typography Ink Token |
| `--ink-3` | `#767D86` | Typography Ink Token |
| `--paper` | `#F2F1ED` | Canvas / Surface Token |
| `--paper-2` | `#E8E6E0` | Canvas / Surface Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--line` | `rgba(20,22,26,.09)` | Color / Atmospheric Token |
| `--line-2` | `rgba(20,22,26,.16)` | Color / Atmospheric Token |
| `--r-xl` | `32px` | Dimension / Scale Token |
| `--r-sm` | `16px` | Dimension / Scale Token |
| `--gut` | `24px` | Dimension / Scale Token |
| `--max` | `1340px` | Dimension / Scale Token |
| `--shadow` | `0 1px 2px rgba(20,22,26,.04), 0 10px 30px -14px rgba(20,22,26,.14)` | Elevation / Border Token |
| `--shadow-lg` | `0 2px 6px rgba(20,22,26,.05), 0 30px 70px -28px rgba(20,22,26,.30)` | Elevation / Border Token |
| `--ease` | `cubic-bezier(.22,.61,.36,1)` | Motion / Easing Token |
| `--brand` | `#2e432f` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hdr> — `dcspaces-co-uk`)**:
   - Landmark `<header class="hdr">` hosting `Chorley Builders · Extensions & Reno` navigation (`Home · About · All services · Extensions · Projects`), DOM attributes (`data-carousel`, `data-dir="prev"`, `data-dir="next"`, `data-dir="prev"`), and stylesheet rule `font-face { font-family: "Satoshi"; src: url("../fonts/satoshi-400.woff2") format("w... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building & Renovation Specialists `)**:
   - Landmark `<section class="hero is-ready">` presenting display lead `Building & Renovation Specialists Across Chorley...` and copy excerpt *"Structural walls and chimney breasts"* over `#14161A` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.opening> — `Everything your house needs, from `)**:
   - Landmark `<section class="opening">` rendering section `Everything your house needs, from one team` with copy *"Kitchen renovations and fitting"*, asset references (`favicon.png`, `apple-touch-icon.png`, `satoshi-900.woff2`, `satoshi-400.woff2`), and grid rule `after { box-sizing: border-box; }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Home Extensions`)**:
   - Landmark `<section class="section">` framing `Home Extensions` and `Loft Conversions` (*"Bespoke carpentry and staircases"*) with `#767D86` surface cards, `#F2F1ED` accents, and `html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }`.
5. **Colophon & Global Directory Footer (<footer.ftr> — `https://dcspaces.co.uk/`)**:
   - Landmark `<footer class="ftr">` anchoring `Chorley Builders · Extensions & ` footer links (`Home · About · All services · Extensions · Projects`), copy *"Crafting unique spaces"*, and `#FFFFFF` structural dividers.
