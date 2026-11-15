# UI & UX Architecture: mauricemoynihan-com

## Overview & Design Identity
- **Target**: `mauricemoynihan-com` (**Maurice Moynihan**)
- **Production URL**: [https://mauricemoynihan.com](https://mauricemoynihan.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#EFEDE6` / `#4c4a43`)
- **Summary**: Advertising creative director, Melbourne. A portfolio. Some of it won things. It also has an album, which hasn’t.
- **Total Clean CSS Variables Extracted**: `25` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Space Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(1.9rem,5.2vw,4.4rem)`, `line-height: 1.02`, `letter-spacing: -.02em`, `font-weight: 900`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2rem,7vw,5.2rem)`, `line-height: .92`, `letter-spacing: -.02em`, `font-weight: 900`)
- **Body Copy**: rule `body` (`font-size: 1.0625rem`, `line-height: 1.55`)
- **Metadata & Labels**: CSS variables `--mono: "Space Mono","Courier New",monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#EFEDE6` | `var(--bone)` in `:root` |
| **Primary Typography Ink** | `#E6E3D9` | `var(--bone-deep)` in `:root` |
| **Elevated Surface / Card Substrate** | `#161511` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#4c4a43` | `var(--ink-soft)` in `:root` |
| **Secondary / Muted Copy** | `#FFFFFF` | `var(--paper)` in `:root` |
| **Structural Hairline Border** | `#ff0000` | `::selection { background: red }` (`#ff0000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bone` | `#EFEDE6` | Color / Atmospheric Token |
| `--bone-deep` | `#E6E3D9` | Color / Atmospheric Token |
| `--ink` | `#161511` | Typography Ink Token |
| `--ink-soft` | `#4c4a43` | Typography Ink Token |
| `--red` | `#161511` | Color / Atmospheric Token |
| `--red-deep` | `#161511` | Color / Atmospheric Token |
| `--red-lift` | `#EFEDE6` | Color / Atmospheric Token |
| `--paper` | `#FFFFFF` | Canvas / Surface Token |
| `--sans` | `"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--mono` | `"Space Mono","Courier New",monospace` | Typography / Scale Token |
| `--serif` | `"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--pad` | `clamp(1rem, 3.4vw, 3rem)` | Layout / Spatial Grid Token |
| `--hair` | `1.5px solid var(--ink)` | Dimension / Scale Token |
| `--card` | `clamp(7rem,13.2vw,11.5rem)` | Dimension / Scale Token |
| `--shelf-pad` | `clamp(1rem,3vh,2.4rem)` | Layout / Spatial Grid Token |
| `--shelf` | `calc(var(--card) * 1.22 + var(--shelf-pad) + var(--nav-h) + 1.6rem + 1.8vw)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `mauricemoynihan-com`)**:
   - Landmark `<header class="nav nav--home">` hosting `Maurice Moynihan` navigation (`Advertising · adnauseum.ai · Music · About`), DOM attributes (`data-src="assets/koi/koi_a.webp"`, `data-src2="assets/koi/koi_b.webp"`, `data-panel`, `data-ink-top="0.7539"`), and stylesheet rule `html { scroll-behavior:smooth; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Maurice Moynihan`)**:
   - Landmark `<section class="hero">` presenting display lead `Maurice Moynihan` and copy excerpt *"Skip to the content"* over `#EFEDE6` canvas and `#161511` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Skip to the content`)**:
   - Landmark `<section class="hero">` rendering section `Skip to the content` with copy *"is a Creative Director, Songwriter and Governor of the Central Ba"*, asset references (`apple-touch-icon.png`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `video { max-width:100%;display:block; }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `is a Creative Director, Songwriter`)**:
   - Landmark `<section class="hero">` framing `is a Creative Director, Songwriter and Governor ` and `Governor of the Central Bank of Ireland` (*"Governor of the Central Bank of Ireland"*) with `#161511` surface cards, `#4c4a43` accents, and `selection { background:var(--red);color:var(--bone); }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://mauricemoynihan.com`)**:
   - Landmark `<footer class="footer">` anchoring `Maurice Moynihan` footer links (`Advertising · adnauseum.ai · Music · About`), copy *"01 Advertising Things that made people buy other things."*, and `#ff0000` structural dividers.
