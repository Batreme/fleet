# UI & UX Architecture: yuyafilmstudio-dev

## Overview & Design Identity
- **Target**: `yuyafilmstudio-dev` (**YUYA FILM STUDIO**)
- **Production URL**: [https://yuyafilmstudio.dev/](https://yuyafilmstudio.dev/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0a` / `#c9a96e`)
- **Summary**: Walk through YUYA FILM STUDIO — a working film company built from Yuya's real Video OS, projects and footage.
- **Total Clean CSS Variables Extracted**: `9` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Cormorant Garamond`
- **Monospace / Technical Font Stack**: `Courier Prime`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(30px,3.5vw,44px)`, `line-height: 1.06`, `letter-spacing: .12em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 9.5px`, `letter-spacing: .32em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: 21px`, `line-height: 1.38`)
- **Metadata & Labels**: CSS variables `--mono: "Courier Prime", "Courier New", monospace`; rule `small` (`font-size: 11px`, `letter-spacing: .01em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0b0a` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#f2ede4` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a39e94` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#c9a96e` | `var(--gold)` in `:root` |
| **Secondary / Muted Copy** | `#8c7650` | `var(--gold-dim)` in `:root` |
| **Structural Hairline Border** | `#e0402f` | `var(--rec)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0b0b0a` | Typography Ink Token |
| `--paper` | `#f2ede4` | Canvas / Surface Token |
| `--muted` | `#a39e94` | Color / Atmospheric Token |
| `--gold` | `#c9a96e` | Color / Atmospheric Token |
| `--gold-dim` | `#8c7650` | Color / Atmospheric Token |
| `--rec` | `#e0402f` | Color / Atmospheric Token |
| `--serif` | `"Cormorant Garamond", "Baskerville", Georgia, serif` | Typography / Scale Token |
| `--sans` | `"Inter", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--mono` | `"Courier Prime", "Courier New", monospace` | Typography / Scale Token |
| `--yuyafilmstudio-d-bg` | `#0b0b0a` | Canvas Substrate (from `var(--ink)` in `:root`) |
| `--yuyafilmstudio-d-ink` | `#f2ede4` | Primary Typography Ink (stylesheet-derived) |
| `--yuyafilmstudio-d-surface` | `#a39e94` | Surface Substrate (stylesheet-derived) |
| `--yuyafilmstudio-d-accent` | `#c9a96e` | Interactive Accent (stylesheet-derived) |
| `--yuyafilmstudio-d-muted` | `#8c7650` | Secondary Ink (stylesheet-derived) |
| `--yuyafilmstudio-d-border` | `#e0402f` | Structural Border (stylesheet-derived) |
| `--yuyafilmstudio-d-container` | `400px` | Container Bound (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bf-top> — `yuyafilmstudio-dev`)**:
   - Landmark `<header class="bf-top">` hosting `YUYA FILM STUDIO` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sdkn="@vercel/analytics"`, `data-sdkv="2.0.1"`, `data-engine="three.js r180"`, `data-k="KeyV"`), and stylesheet rule `gl { position:fixed;inset:0;width:100vw;height:100vh;display:block;outline:none }`.
2. **Hero Stage & Focal Lead (<section.brief> — `YUYA FILM STUDIO`)**:
   - Landmark `<section class="brief">` presenting display lead `YUYA FILM STUDIO` and copy excerpt *"VISITOR ACCESS / STUDIO TOUR"* over `#0b0b0a` canvas and `#f2ede4` ink.
3. **Primary Showcase & Content Grid (<section.bf-id> — `MOVE`)**:
   - Landmark `<section class="bf-id">` rendering section `MOVE` with copy *"Explore the studio, interact with the production process, and fol"*, asset references (`index-BGb4Src9.js`, `index-C-QYK-dA.css`, `script.js`), and grid rule `.hidden { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.bf-controls> — `EXPLORE`)**:
   - Landmark `<section class="bf-controls">` framing `EXPLORE` and `OBJECTS` (*"ENTER YUYA FILM STUDIO"*) with `#a39e94` surface cards, `#c9a96e` accents, and `button { font-family:var(--sans);cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.bf-foot> — `https://yuyafilmstudio.dev/`)**:
   - Landmark `<footer class="bf-foot">` anchoring `YUYA FILM STUDIO` footer links (`Overview · Index · Archive · About · Contact`), copy *"Pulling stills from the ÉCLAT edit…"*, and `#e0402f` structural dividers.
