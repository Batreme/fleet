# UI & UX Architecture: noho-ink

## Overview & Design Identity
- **Target**: `noho-ink` (**Noho**)
- **Production URL**: [https://noho.ink](https://noho.ink)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f1eee9` / `#0000`)
- **Summary**: E n e r g y u s a g e E n e r g y u s a g e
- **Total Clean CSS Variables Extracted**: `41` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Switzer`
- **Body Font Stack**: `Switzer Variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.h1` (`font-size: 7.292vw!important`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1eee9` | `var(--bg-page)` in `:root` |
| **Primary Typography Ink** | `#3c3c3c` | `var(--txt-main)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d7d1c7` | `var(--bg-switch)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `var(--transperent)` in `:root` |
| **Secondary / Muted Copy** | `#e7e2da` | `var(--bg-element)` in `:root` |
| **Structural Hairline Border** | `#cdc0b0` | `var(--bg-element-third)` in `:root` |
| **Variable Token (`--raven-black-40`)** | `#3c3c3c66` | `var(--raven-black-40)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--noho-slogan-lift` | `0px` | Dimension / Scale Token |
| `--bg-page` | `#f1eee9` | Canvas / Surface Token |
| `--txt-main` | `#3c3c3c` | Color / Atmospheric Token |
| `--bg-form-element` | `white` | Canvas / Surface Token |
| `--raven-black-100` | `#3c3c3c` | Canvas / Surface Token |
| `--bg-switch` | `#d7d1c7` | Canvas / Surface Token |
| `--bg-inner-switch` | `white` | Canvas / Surface Token |
| `--bg-btn-pm` | `#3c3c3c` | Canvas / Surface Token |
| `--txt-btn-pm` | `white` | Design System Custom Token |
| `--bg-btn-sc` | `white` | Canvas / Surface Token |
| `--txt-btn-sc` | `#3c3c3c` | Color / Atmospheric Token |
| `--bg-btn-big` | `#3c3c3c` | Canvas / Surface Token |
| `--txt-btn-big` | `white` | Design System Custom Token |
| `--transperent` | `#0000` | Color / Atmospheric Token |
| `--raven-black-40` | `#3c3c3c66` | Canvas / Surface Token |
| `--offbeat` | `#d7d1c7` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `noho-ink`)**:
   - Landmark `<header class="header section">` hosting `Noho` navigation (`A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`), DOM attributes (`data-wf-domain="noho-a7a5a8.webflow.io"`, `data-wf-page="667aaef1d0489a9d5183ef5d"`, `data-wf-site="667aaef1d0489a9d5183ef56"`, `data-wf-status="1"`), and stylesheet rule `html { height:auto;overflow-x:hidden;overflow-y:auto }`.
2. **Hero Stage & Focal Lead (<section.switch> — `“He ain’t heavy”`)**:
   - Landmark `<section class="switch">` presenting display lead `“He ain’t heavy”` and copy excerpt *"A b o u t A b o u t"* over `#f1eee9` canvas and `#3c3c3c` ink.
3. **Primary Showcase & Content Grid (<section.switch> — `“Not only do they look great, but `)**:
   - Landmark `<section class="switch">` rendering section `“Not only do they look great, but they are very c...` with copy *"P r i c e P r i c e"*, asset references (`webflow.shared.min.css`, `6a4e44ce6ee465198645089f_favicon-...`, `6a4e444d307c1e077753f979_favicon-...`, `6a4e44ceccf875bb9d22c7cd_favicon-...`), and grid rule `html ::selection { background-color:var(--bg-form-element);color:var(--text-form-element) }`.
4. **Interactive Detail & Feature Matrix (<section.hero-section-parent> — `Josh L`)**:
   - Landmark `<section class="hero-section-parent">` framing `Josh L` and `Why Lighty` (*"E n e r g y u s a g e E n e r g y u s a g e"*) with `#d7d1c7` surface cards, `#0000` accents, and `html ::-moz-selection { background-color:var(--bg-form-element);color:var(--text-form-element) }`.
5. **Colophon & Global Directory Footer (<footer.footer-parent> — `https://noho.ink`)**:
   - Landmark `<footer class="footer-parent">` anchoring `Noho` footer links (`A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`), copy *"Dark mode and reduce animation options allow you to save abo"*, and `#cdc0b0` structural dividers.
