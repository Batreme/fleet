# UI & UX Architecture: recurziv-com

## Overview & Design Identity
- **Target**: `recurziv-com` (**Recurziv — Web & App Development Studio in Goa**)
- **Production URL**: [https://recurziv.com](https://recurziv.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#00d4ff` / `#fff`)
- **Summary**: A digital studio in Panaji, Goa building websites, e-commerce, and mobile apps since 2014 — designed and built in-house, iterated until t...
- **Total Clean CSS Variables Extracted**: `7` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gothic`
- **Body Font Stack**: `GothicBold`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.02rem,1.5vw,1.22rem)`, `letter-spacing: .01em`)
- **Body Copy**: rule `p` (`font-size: 1rem`, `line-height: 1.6`, `letter-spacing: 1px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `1.5rem`, `2rem`, `1.8rem`, `1rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#00d4ff` | `var(--accent)` in `:root` |
| **Primary Typography Ink** | `#04081a` | `var(--bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `.recursion { border-bottom: #000 }` |
| **Interactive Accent / Highlight** | `#fff` | `.recursion .recursion_wrapper h... { color: #fff }` |
| **Secondary / Muted Copy** | `#ffffff` | `ecursion .recursion_wrapper mai... { background: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#ff48c4` | `.recursion.recursion_1 ul { background-color: #ff48c4 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent` | `#00d4ff` | Brand / Palette Token |
| `--accent-dim` | `rgba(0, 212, 255, 0.18)` | Brand / Palette Token |
| `--accent-faint` | `rgba(0, 212, 255, 0.06)` | Brand / Palette Token |
| `--bg` | `#04081a` | Canvas / Surface Token |
| `--border` | `rgba(0, 212, 255, 0.13)` | Elevation / Border Token |
| `--panel-w` | `55vw` | Dimension / Scale Token |
| `--rz-l1-h` | `108px` | Elevation / Border Token |
| `--wp--preset--aspect-ratio--square` | `1` | Design System Custom Token |
| `--wp--preset--aspect-ratio--4-3` | `4/3` | Design System Custom Token |
| `--wp--preset--aspect-ratio--3-4` | `3/4` | Design System Custom Token |
| `--wp--preset--aspect-ratio--3-2` | `3/2` | Design System Custom Token |
| `--wp--preset--aspect-ratio--2-3` | `2/3` | Design System Custom Token |
| `--wp--preset--aspect-ratio--16-9` | `16/9` | Design System Custom Token |
| `--wp--preset--aspect-ratio--9-16` | `9/16` | Design System Custom Token |
| `--recurziv-com-bg` | `#00d4ff` | Canvas Substrate (from `var(--accent)` in `:root`) |
| `--recurziv-com-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.rzd-head> — `recurziv-com`)**:
   - Landmark `<header class="rzd-head">` hosting `Recurziv — Web & App Development Stu` navigation (`Recurziv · About Us · Services · Projects · Contact Us`), DOM attributes (`data-barba="wrapper"`, `data-rz-panel="mix"`, `data-layer1-consent-surface`, `data-rz-pulse-shown="1"`), and stylesheet rule `video { margin:0;padding:0;border:0;font-size:100%;font:inherit;text-decoration:... }`.
2. **Hero Stage & Focal Lead (<main.rz-consent-pending> — `before we begin — what should I ca`)**:
   - Landmark `<main class="rz-consent-pending">` presenting display lead `before we begin — what should I call you?` and copy excerpt *"allow experience analytics to help us understand which pages and "* over `#00d4ff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.rz-pre-choice> — `what we'd design for you`)**:
   - Landmark `<main class="rz-pre-choice">` rendering section `what we'd design for you` with copy *"please rotate your device"*, asset references (`favicon.ico`, `apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<main.rz-l1-bar> — `welcome to recurziv`)**:
   - Landmark `<main class="rz-l1-bar">` framing `welcome to recurziv` and `recurziv /rɪˈkəːrsɪv/` (*"this experience is designed for portrait."*) with `#000` surface cards, `#fff` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.rz-side-footer> — `https://recurziv.com`)**:
   - Landmark `<footer class="rz-side-footer">` anchoring `Recurziv — Web & App Development` footer links (`Recurziv · About Us · Services · Projects · Contact Us`), copy *"· design studies, not delivered projects"*, and `#ff48c4` structural dividers.
