# UI & UX Architecture: kelvin-8b-com

## Overview & Design Identity
- **Target**: `kelvin-8b-com` (**Kelvin — three nights of music, filmed in heat**)
- **Production URL**: [https://kelvin.8b.com/](https://kelvin.8b.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f1ede4` canvas, `#110d19` ink, `#2a5cff` accent)
- **Summary**: Kelvin is a three-night music festival filmed through thermal cameras and projected back into a former power station in Rotterdam. 23–25...
- **Total Clean CSS Variables Extracted**: `23` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Hubot Sans`
- **Body Font Stack**: `Kalnia`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.0625rem`, `clamp(1.85rem,5.2vw,5rem)`, `clamp(1.45rem,2.4vw,2.3rem)`, `0.75rem`, `clamp(1.1rem,1.45vw,1.32rem)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1ede4` | `var(--color-1)` in `:root` |
| **Primary Typography Ink** | `#110d19` | `var(--color-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2d18a8` | `var(--color-3)` in `:root` |
| **Interactive Accent / Highlight** | `#2a5cff` | `var(--color-4)` in `:root` |
| **Secondary / Muted Copy** | `#12c3e3` | `var(--color-5)` in `:root` |
| **Structural Hairline Border** | `#ffe000` | `var(--color-6)` in `:root` |
| **Variable Token (`--color-7`)** | `#ff7a00` | `var(--color-7)` in `:root` |
| **Variable Token (`--color-8`)** | `#ff2c46` | `var(--color-8)` in `:root` |
| **Variable Token (`--color-9`)** | `#ff42ad` | `var(--color-9)` in `:root` |
| **Variable Token (`--color-10`)** | `#5b5664` | `var(--color-10)` in `:root` |
| **Variable Token (`--color-11`)** | `#bcb6c6` | `var(--color-11)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-1` | `#f1ede4` | Brand / Palette Token |
| `--color-2` | `#110d19` | Brand / Palette Token |
| `--color-3` | `#2d18a8` | Brand / Palette Token |
| `--color-4` | `#2a5cff` | Brand / Palette Token |
| `--color-5` | `#12c3e3` | Brand / Palette Token |
| `--color-6` | `#ffe000` | Brand / Palette Token |
| `--color-7` | `#ff7a00` | Brand / Palette Token |
| `--color-8` | `#ff2c46` | Brand / Palette Token |
| `--color-9` | `#ff42ad` | Brand / Palette Token |
| `--color-10` | `#5b5664` | Brand / Palette Token |
| `--color-11` | `#bcb6c6` | Brand / Palette Token |
| `--font-1` | `"Hubot Sans", "Arial Narrow", Arial, sans-serif` | Typography / Scale Token |
| `--font-2` | `"Kalnia", Georgia, serif` | Typography / Scale Token |
| `--font-3` | `"Hubot Sans", "Kelvin Narrow", sans-serif` | Typography / Scale Token |
| `--space-1` | `clamp(16px, 3vw, 44px)` | Layout / Spatial Grid Token |
| `--space-2` | `clamp(88px, 11vw, 168px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `kelvin-8b-com`)**:
   - Landmark `<header class="lenis">` hosting `Kelvin — three nights of music, film` navigation (`Lineup · Nights · Archive · Visit`), DOM attributes (`data-8b-contract="4"`, `data-8b-part="fonts"`, `data-8b-part="layers"`, `data-8b-part="tokens"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.m-text> — `Kelvin K E L V I N`)**:
   - Landmark `<section class="m-text">` presenting display lead `Kelvin K E L V I N` and copy excerpt *"Kelvin Sound in heat · 2027"* over `#f1ede4` canvas and `#110d19` ink.
3. **Primary Showcase & Content Grid (<section.heat-defs> — `Every set is filmed in heat. The r`)**:
   - Landmark `<section class="heat-defs">` rendering section `Every set is filmed in heat. The room paints itself.` with copy *"Sound in heat · 2027"*, asset references (`images.unsplash.com`, `cdn.jsdelivr.net`, `fonts.gstatic.com`, `pe0rMIiULYxOvxVLbVwhEtCaBg.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.nav__brand> — `Six in the frame, forty‑one in the`)**:
   - Landmark `<section class="nav__brand">` framing `Six in the frame, forty‑one in the hall` and `Also in the hall` (*"Centrale Noord · Rotterdam"*) with `#2d18a8` surface cards, `#2a5cff` accents, and `html.lenis body { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://kelvin.8b.com/`)**:
   - Landmark `<footer class="m-text-3">` anchoring `Kelvin — three nights of music, ` footer links (`Lineup · Nights · Archive · Visit`), copy *"2027 · three nights"*, and `#ffe000` structural dividers.
