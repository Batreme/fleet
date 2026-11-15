# UI & UX Architecture: www-fixchocolatier-com

## Overview & Design Identity
- **Target**: `www-fixchocolatier-com` (**FIX Dessert Chocolatier · The Original Dubai Chocolate**)
- **Production URL**: [https://www.fixchocolatier.com/](https://www.fixchocolatier.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#3a1402` / `#000`)
- **Summary**: Discover FIX Dessert Chocolatier, the original Dubai chocolate bar. Shop our viral kunafa, pistachio and pecan bars. Order daily on Careem.
- **Total Clean CSS Variables Extracted**: `16` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `sharpSans`
- **Body Font Stack**: `sharpSans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: 9rem`, `line-height: 1`, `letter-spacing: 0`, `font-weight: 800`)
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: 6rem`, `line-height: 1`, `letter-spacing: 0`, `font-weight: 800`)
- **Body Copy**: rule `p` (`font-size: 3rem`, `line-height: 1`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.8rem`, `.944rem`, `20px`, `12px`, `1.44rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3a1402` | `var(--bg-color)` in `:root` |
| **Primary Typography Ink** | `#742f3d` | `var(--shadow-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ccc` | `tepicker__month-year-read-view-... { border: #ccc }` |
| **Interactive Accent / Highlight** | `#000` | `.react-datepicker { color: #000 }` |
| **Secondary / Muted Copy** | `#fff` | `.react-datepicker { background-color: #fff }` |
| **Structural Hairline Border** | `#aeaeae` | `.react-datepicker { border: #aeaeae }` |
| **Variable Token (`--hover-bg-color`)** | `#3a140280` | `var(--hover-bg-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sharpsans` | `"sharpSans", "sharpSans Fallback"` | Typography / Scale Token |
| `--font-sydney` | `"sydney", Segoe UI` | Typography / Scale Token |
| `--bg-color` | `#3a1402` | Canvas / Surface Token |
| `--dot-color` | `white` | Brand / Palette Token |
| `--hover-bg-color` | `#3a140280` | Canvas / Surface Token |
| `--inactive-opacity` | `0` | Design System Custom Token |
| `--marquee-duration` | `3s` | Motion / Easing Token |
| `--marquee-easing` | `cubic-bezier(.05,0,.95,1)` | Motion / Easing Token |
| `--shadow-color` | `#742f3d` | Brand / Palette Token |
| `--switch-translate` | `3.99rem` | Dimension / Scale Token |
| `--t-duration` | `2s` | Motion / Easing Token |
| `--original-font-size` | `10px` | Typography / Scale Token |
| `--page-bg` | `rgb(98, 53, 41)` | Canvas / Surface Token |
| `--bg-gradient` | `none` | Canvas / Surface Token |
| `--bg-noise` | `none` | Canvas / Surface Token |
| `--scrim-rgb` | `98, 53, 41` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `www-fixchocolatier-com`)**:
   - Landmark `<header class="pointer-events-none absolute">` hosting `FIX Dessert Chocolatier · The Origin` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-engine="three.js r181"`), and stylesheet rule `sans_96245405-module__S_0vUq__cla... { font-family:sharpSans,sharpSans Fallback }`.
2. **Hero Stage & Focal Lead (<main.home-main> — `Can’t get Knafeh of it™`)**:
   - Landmark `<main class="home-main relative">` presenting display lead `Can’t get Knafeh of it™` and copy excerpt *"Collections Hero Bars Midnight Edition Bars Gifting & Sharing Lim"* over `#3a1402` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.home-main> — `CATCH ME IF PECAN`)**:
   - Landmark `<main class="home-main relative">` rendering section `CATCH ME IF PECAN` with copy *"Midnight Edition Bars"*, asset references (`SharpSansNo1_Extrabold-s.p.17c.ux...`, `SharpSansNo1_Semibold-s.p.141-gcw...`, `SydneyAlternate_Regular.p.0-s3cp4...`, `0~ky31xm0y.v6.css`), and grid rule `psans_96245405-module__S_0vUq__va... { --font-sharpsans:"sharpSans", "sharpSans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.home-main> — `BUTTER TO BE SAFE THAN SALTY`)**:
   - Landmark `<main class="home-main relative">` framing `BUTTER TO BE SAFE THAN SALTY` and `PICK UP A PRETZEL` (*"Limited Edition Bars"*) with `#ccc` surface cards, `#000` accents, and `dney_ed2b677e-module__XJDjNq__cla... { font-family:sydney,Segoe UI }`.
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://www.fixchocolatier.com/`)**:
   - Landmark `<footer class="fixed">` anchoring `FIX Dessert Chocolatier · The Or` footer links (`Overview · Index · Archive · About · Contact`), copy *"The Original Dubai Chocolate"*, and `#aeaeae` structural dividers.
