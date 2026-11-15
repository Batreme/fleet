# UI & UX Architecture: www-barebonescollective-com

## Overview & Design Identity
- **Target**: `www-barebonescollective-com` (**Bare Bones Collective**)
- **Production URL**: [https://www.barebonescollective.com/](https://www.barebonescollective.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#333` accent)
- **Summary**: We are a creative agency that believes great brands are built through audacious work
- **Total Clean CSS Variables Extracted**: `1` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Oswald`
- **Body Font Stack**: `PT Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `a { background-color: #0000 }` |
| **Primary Typography Ink** | `#000` | `mark { color: #000 }` |
| **Elevated Surface / Card Substrate** | `#ff0` | `mark { background: #ff0 }` |
| **Interactive Accent / Highlight** | `#333` | `body { color: #333 }` |
| **Secondary / Muted Copy** | `#fff` | `body { background-color: #fff }` |
| **Structural Hairline Border** | `#3898ec` | `.w-button { background-color: #3898ec }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--www-barebonescol-bg` | `#0000` | Canvas Substrate (from `a { background-color: #0000 }`) |
| `--www-barebonescol-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--www-barebonescol-surface` | `#ff0` | Surface Substrate (stylesheet-derived) |
| `--www-barebonescol-accent` | `#333` | Interactive Accent (stylesheet-derived) |
| `--www-barebonescol-muted` | `#fff` | Secondary Ink (stylesheet-derived) |
| `--www-barebonescol-border` | `#3898ec` | Structural Border (stylesheet-derived) |
| `--www-barebonescol-container` | `940px` | Container Bound (stylesheet-derived) |
| `--www-barebonescol-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--www-barebonescol-pad` | `9px` | Lateral Padding (stylesheet-derived) |
| `--www-barebonescol-ease` | `cubic-bezier(.165,.84,.44,1)` | Primary Easing Function |
| `--www-barebonescol-radius` | `3px` | Corner Radius (stylesheet-derived) |
| `--www-barebonescol-fs-base` | `2em` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-barebonescollective-com`)**:
   - Landmark `<header class="w-mod-js">` hosting `Bare Bones Collective` navigation (`Menu · Work · Services · 360° Campaigns · films`), DOM attributes (`data-wf-domain="www.barebonescollecti..."`, `data-wf-page="68358a988d15891f5e5e5ab6"`, `data-wf-site="68358a988d15891f5e5e5aad"`, `data-w-id="21dd915e-a730-31e5-d8..."`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.menu_element> — `Bare`)**:
   - Landmark `<section class="menu_element">` presenting display lead `Bare` and copy excerpt *"influencer campaigns"* over `#0000` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.logo_element> — `Bones`)**:
   - Landmark `<section class="logo_element">` rendering section `Bones` with copy *"hello@barebonescollective.com"*, asset references (`cdn.prod.website-files.com`, `bare-bones-collective.webflow.sha...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-hero> — `COLLECTIVE`)**:
   - Landmark `<section class="section-hero">` framing `COLLECTIVE` and `CREATIVE AGENCY THAT BELIEVES GREAT BRANDS ARE BU...` (*"Bones"*) with `#ff0` surface cards, `#333` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-ptserif-n7-active> — `https://www.barebonescollective.com/`)**:
   - Landmark `<footer class="wf-ptserif-n7-active">` anchoring `Bare Bones Collective` footer links (`Menu · Work · Services · 360° Campaigns · films`), copy *"COLLECTIVE"*, and `#3898ec` structural dividers.
