# UI & UX Architecture: jozue-fr

## Overview & Design Identity
- **Target**: `jozue-fr` (**Josué Pichot, freelance art director and photographer in Paris**)
- **Production URL**: [https://jozue.fr](https://jozue.fr)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111319` canvas, `#fff` ink, `#dcdbdb` accent)
- **Summary**: Paris-based freelance art director, photographer, director and product designer. 15+ years in advertising and digital. Available in-house...
- **Total Clean CSS Variables Extracted**: `104` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Grotesk Display`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`)
- **Body Copy**: rule `p` (`font-size: 2.3rem`, `line-height: 1.22`, `letter-spacing: .03em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111319` | `var(--pill-bg)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--roll-from)` in `:root` |
| **Elevated Surface / Card Substrate** | `#050507` | `var(--intro-signature-color)` in `:root` |
| **Interactive Accent / Highlight** | `#dcdbdb` | `var(--home-j-color)` in `:root` |
| **Secondary / Muted Copy** | `#f73326` | `var(--hint-color)` in `:root` |
| **Structural Hairline Border** | `#0000` | `button { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paletteCount` | `5` | Brand / Palette Token |
| `--title-delay` | `var(--home-title-delay)` | Motion / Easing Token |
| `--island-side` | `1.6rem` | Dimension / Scale Token |
| `--island-bottom` | `calc(1.6rem + env(safe-area-inset-bottom,0px))` | Dimension / Scale Token |
| `--island-bar` | `5.2rem` | Dimension / Scale Token |
| `--island-r` | `2.6rem` | Dimension / Scale Token |
| `--island-fs` | `1.5rem` | Dimension / Scale Token |
| `--island-count` | `3.6rem` | Dimension / Scale Token |
| `--signature-word-y` | `-35.8%` | Dimension / Scale Token |
| `--pill-bg` | `#111319` | Canvas / Surface Token |
| `--roll-from` | `#fff` | Color / Atmospheric Token |
| `--roll-to` | `#fff` | Color / Atmospheric Token |
| `--roll-ink` | `var(--pill-bg,#111319)` | Typography Ink Token |
| `--pagination-off` | `.25` | Design System Custom Token |
| `--pagination-dot` | `.4` | Design System Custom Token |
| `--pagination-bar` | `2.8` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.menu> — `jozue-fr`)**:
   - Landmark `<nav class="menu menu--site">` hosting `Josué Pichot, freelance art director` navigation (`About. · Works. · Contact. · Français.`), DOM attributes (`data-intro="done"`, `data-color="111319"`, `data-color="F73326"`, `data-title="About"`), and stylesheet rule `root { --paletteCount:5 }`.
2. **Hero Stage & Focal Lead (<article.homepage> — `a r t d i r e c t o r + p h o t o `)**:
   - Landmark `<article class="homepage">` presenting display lead `a r t d i r e c t o r + p h o t o g r a p h e r c...` and copy excerpt *"English. Français."* over `#111319` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.js-infos> — `selected works 18`)**:
   - Landmark `<section class="js-infos homepage__infos">` rendering section `selected works 18` with copy *"a r t d i r e c t o r + p h o t o g r a p h e r"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `jozue-logo-full.DpMZCk-F.svg`), and grid rule `.stop { overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.wrapper> — `let's talk`)**:
   - Landmark `<section class="wrapper wrapper--infos">` framing `let's talk` and `Awards & Archives` (*"a r t d i r e c t o r"*) with `#050507` surface cards, `#dcdbdb` accents, and `.transi { opacity:0;z-index:-1;width:100vw;height:100vh;display:flex;position:fixe... }`.
5. **Colophon & Global Directory Footer (<footer.transi> — `https://jozue.fr`)**:
   - Landmark `<footer class="transi">` anchoring `Josué Pichot, freelance art dire` footer links (`About. · Works. · Contact. · Français.`), copy *"+ p h o t o g r a p h e r"*, and `#0000` structural dividers.
