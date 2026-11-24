---
title: "UI & UX Architecture: www-zrk-technology"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-zrk-technology

## Overview & Design Identity
- **Target**: `www-zrk-technology` (**Shahed interceptor with auto-guidance · Zirka**)
- **Production URL**: [https://www.zrk.technology/](https://www.zrk.technology/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#050505` / `#ffa500`)
- **Summary**: Ukrainian interceptor drone Zirka for defeating UAV threats. Automatic target tracking, combat-proven technology, and an airspeed twice t...
- **Total Clean CSS Variables Extracted**: `7` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter display`
- **Body Font Stack**: `Inter display`
- **Monospace / Technical Font Stack**: `Geist mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 63.36px`, `font-weight: 500`, `letter-spacing: -3.6px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 63.36px`, `font-weight: 500`, `letter-spacing: -3.6px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#050505` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#dddddd` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#ffa500` | `.nav-link:hover { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#333333` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--orange`)** | `#fc4f00` | `var(--orange)` in `:root` |

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
| `--www-zrk-technolo-bg` | `#050505` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-zrk-technolo-ink` | `#dddddd` | Primary Typography Ink (computed-derived) |
| `--www-zrk-technolo-surface` | `#222222` | Surface Substrate (computed-derived) |
| `--www-zrk-technolo-accent` | `#ffa500` | Interactive Accent (computed-derived) |
| `--www-zrk-technolo-muted` | `#333333` | Secondary Ink (computed-derived) |
| `--www-zrk-technolo-border` | `#3898ec` | Structural Border (computed-derived) |
| `--www-zrk-technolo-container` | `97.7778rem` | Container Bound (computed-derived) |
| `--www-zrk-technolo-gap` | `16px` | Grid Gutter (computed-derived) |
| `--www-zrk-technolo-pad` | `15.984px` | Lateral Padding (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-zrk-technology`)**:
   - Landmark `<header class="header">` (`1440x96px`) hosting `Shahed interceptor with auto-guidanc` navigation (`EN · ua · Threat · Features · Effectiveness`), DOM attributes (`data-wf-domain="www.zrk.technology"`, `data-wf-page="6a6b45050da8002d7ece655a"`, `data-wf-site="6a6b45050da8002d7ece655c"`, `data-w-id="ede80d56-8c0e-ad0b-36..."`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<main.main> — `Zirka is a Shahed interceptor with`)**:
   - Landmark `<main class="main">` presenting display lead `Zirka is a Shahed interceptor with auto-guidance` and copy excerpt *"i n t e r c e p t o r"* over `#050505` canvas and `#dddddd` ink.
3. **Primary Showcase & Content Grid (<main.main:nth(2)> — `Z i r k a i s a S h a h e d i n t `)**:
   - Landmark `<main class="main">` rendering section `Z i r k a i s a S h a h e d i n t e r c e p t o r...` with copy *"a u t o - g u i d a n c e"*, asset references (`cdn.prod.website-files.com`, `zirka-awwwards.webflow.shared.2f0...`, `6a4281712b40a844defb5fdd_180x180.png`, `6a1573e5debd7fd87a125ab4_180x180.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<main.main:nth(3)> — `A l l U k r a i n i a n i n t e r `)**:
   - Landmark `<main class="main">` framing `A l l U k r a i n i a n i n t e r c e p t i o n e...` and `F i r s t s t r i k e s o n U k r a i n e` (*"i n t e r c e p t i o n"*) with `#222222` surface cards, `#ffa500` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer-2> — `https://www.zrk.technology/`)**:
   - Landmark `<footer class="footer-2">` anchoring `Shahed interceptor with auto-gui` footer links (`EN · ua · Threat · Features · Effectiveness`), copy *"e x p e r i e n c e"*, and `#3898ec` structural dividers.
