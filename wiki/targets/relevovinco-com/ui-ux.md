# UI & UX Architecture: relevovinco-com

## Overview & Design Identity
- **Target**: `relevovinco-com` (**Relevo & Vinco — inkless packaging, pressed into the board**)
- **Production URL**: [https://relevovinco.com/](https://relevovinco.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#d4b08f` canvas, `#1f140b` ink, `#6b4c34` accent)
- **Summary**: Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, die-cut and fold raw board so a brand is something people fe...
- **Total Clean CSS Variables Extracted**: `29` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gabarito`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`)
- **Body Copy**: rule `p` (`font-size: clamp(26px,2.8vw,42px)`, `line-height: 1.12`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d4b08f` | `var(--color-1)` in `:root` |
| **Primary Typography Ink** | `#36261a` | `var(--color-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f7e8d2` | `var(--color-3)` in `:root` |
| **Interactive Accent / Highlight** | `#6b4c34` | `var(--color-4)` in `:root` |
| **Secondary / Muted Copy** | `#47331f` | `var(--color-5)` in `:root` |
| **Structural Hairline Border** | `#1f140b` | `var(--color-6)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-1` | `#d4b08f` | Brand / Palette Token |
| `--color-2` | `#36261a` | Brand / Palette Token |
| `--color-3` | `#f7e8d2` | Brand / Palette Token |
| `--color-4` | `#6b4c34` | Brand / Palette Token |
| `--color-5` | `#47331f` | Brand / Palette Token |
| `--color-6` | `#1f140b` | Brand / Palette Token |
| `--font-1` | `"Gabarito", "Gabarito Fallback", "Arial", sans-serif` | Typography / Scale Token |
| `--font-2` | `"Instrument Sans", "Instrument Sans Fallback", "Arial", sans-serif` | Typography / Scale Token |
| `--radius-1` | `6px` | Elevation / Border Token |
| `--radius-2` | `50%` | Elevation / Border Token |
| `--radius-3` | `clamp(18px, 2.4vw, 34px)` | Elevation / Border Token |
| `--shadow-7` | `1px 1px 0 color-mix(in srgb, var(--color-3) 75%, transparent)` | Elevation / Border Token |
| `--shadow-14` | `10px 16px 18px color-mix(in srgb, var(--color-6) 32%, transparent)` | Elevation / Border Token |
| `--space-1` | `clamp(20px, 6.5vw, 96px)` | Layout / Spatial Grid Token |
| `--space-2` | `clamp(96px, 15vh, 180px)` | Layout / Spatial Grid Token |
| `--hero-cap` | `min(16vh, 11.2vw)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `relevovinco-com`)**:
   - Landmark `<header class="lenis">` hosting `Relevo & Vinco — inkless packaging, ` navigation (`Finishes · Process · Work · Boards · Contact`), DOM attributes (`data-fonts`, `data-part="layers"`, `data-part="tokens"`, `data-part="base"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.relief-defs> — `Stand out. Press in.`)**:
   - Landmark `<section class="relief-defs">` presenting display lead `Stand out. Press in.` and copy excerpt *"Relevo & Vinco is an inkless packaging workshop in Porto. We embo"* over `#d4b08f` canvas and `#1f140b` ink.
3. **Primary Showcase & Content Grid (<section.relief-defs__shade> — `Ink fades. Foil peels. Pressure st`)**:
   - Landmark `<section class="relief-defs__shade">` rendering section `Ink fades. Foil peels. Pressure stays.` with copy *"Order a sample kit"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `gabarito-a94f9001.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.nav__bar> — `Six ways to say it without ink`)**:
   - Landmark `<section class="nav__bar">` framing `Six ways to say it without ink` and `Blind emboss` (*"Every box we make carries its brand in the board itself: raised w"*) with `#f7e8d2` surface cards, `#6b4c34` accents, and `img { display:block;max-width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://relevovinco.com/`)**:
   - Landmark `<footer class="m-text-3">` anchoring `Relevo & Vinco — inkless packagi` footer links (`Finishes · Process · Work · Boards · Contact`), copy *"Nothing to scuff off in transit and nothing to separate at t"*, and `#1f140b` structural dividers.
