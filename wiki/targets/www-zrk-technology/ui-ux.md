# UI & UX Architecture: www-zrk-technology

## Overview & Design Identity
- **Target**: `www-zrk-technology` (**Shahed interceptor with auto-guidance · Zirka**)
- **Production URL**: [https://www.zrk.technology/](https://www.zrk.technology/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fc4f00` / `#0000`)
- **Summary**: Ukrainian interceptor drone Zirka for defeating UAV threats. Automatic target tracking, combat-proven technology, and an airspeed twice t...
- **Total Clean CSS Variables Extracted**: `7` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter display`
- **Body Font Stack**: `Geist mono`
- **Monospace / Technical Font Stack**: `Geist mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fc4f00` | `var(--orange)` in `:root` |
| **Primary Typography Ink** | `#050505` | `var(--black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ddd` | `var(--white)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `a { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#000` | `mark { color: #000 }` |
| **Structural Hairline Border** | `#ff0` | `mark { background: #ff0 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--orange` | `#fc4f00` | Color / Atmospheric Token |
| `--black` | `#050505` | Canvas / Surface Token |
| `--white` | `#ddd` | Canvas / Surface Token |
| `--bar` | `1px` | Dimension / Scale Token |
| `--gap` | `2.5px` | Layout / Spatial Grid Token |
| `--word` | `1` | Design System Custom Token |
| `--char` | `1` | Design System Custom Token |
| `--www-zrk-technolo-bg` | `#fc4f00` | Canvas Substrate (from `var(--orange)` in `:root`) |
| `--www-zrk-technolo-ink` | `#ff0` | Primary Typography Ink (stylesheet-derived) |
| `--www-zrk-technolo-surface` | `#ddd` | Surface Substrate (stylesheet-derived) |
| `--www-zrk-technolo-accent` | `#0000` | Interactive Accent (stylesheet-derived) |
| `--www-zrk-technolo-muted` | `#000` | Secondary Ink (stylesheet-derived) |
| `--www-zrk-technolo-border` | `#ff0` | Structural Border (stylesheet-derived) |
| `--www-zrk-technolo-container` | `940px` | Container Bound (stylesheet-derived) |
| `--www-zrk-technolo-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--www-zrk-technolo-pad` | `9px` | Lateral Padding (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-zrk-technology`)**:
   - Landmark `<header class="header">` hosting `Shahed interceptor with auto-guidanc` navigation (`EN · ua · Threat · Features · Effectiveness`), DOM attributes (`data-wf-domain="www.zrk.technology"`, `data-wf-page="6a6b45050da8002d7ece655a"`, `data-wf-site="6a6b45050da8002d7ece655c"`, `data-w-id="ede80d56-8c0e-ad0b-36..."`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<main.main> — `Z i r k a i s a S h a h e d i n t `)**:
   - Landmark `<main class="main">` presenting display lead `Z i r k a i s a S h a h e d i n t e r c e p t o r...` and copy excerpt *"i n t e r c e p t o r"* over `#fc4f00` canvas and `#ff0` ink.
3. **Primary Showcase & Content Grid (<main.main> — `A l l U k r a i n i a n i n t e r `)**:
   - Landmark `<main class="main">` rendering section `A l l U k r a i n i a n i n t e r c e p t i o n e...` with copy *"a u t o - g u i d a n c e"*, asset references (`cdn.prod.website-files.com`, `zirka-awwwards.webflow.shared.2f0...`, `6a4281712b40a844defb5fdd_180x180.png`, `6a1573e5debd7fd87a125ab4_180x180.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<main.main> — `F i r s t s t r i k e s o n U k r `)**:
   - Landmark `<main class="main">` framing `F i r s t s t r i k e s o n U k r a i n e` and `G e r a n - 2 : R u s s i a ’ s a d a p t a t i o...` (*"i n t e r c e p t i o n"*) with `#ddd` surface cards, `#0000` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer-2> — `https://www.zrk.technology/`)**:
   - Landmark `<footer class="footer-2">` anchoring `Shahed interceptor with auto-gui` footer links (`EN · ua · Threat · Features · Effectiveness`), copy *"e x p e r i e n c e"*, and `#ff0` structural dividers.
