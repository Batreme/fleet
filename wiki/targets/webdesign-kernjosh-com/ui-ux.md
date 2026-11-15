# UI & UX Architecture: webdesign-kernjosh-com

## Overview & Design Identity
- **Target**: `webdesign-kernjosh-com` (**Josh Kern**)
- **Production URL**: [https://webdesign.kernjosh.com](https://webdesign.kernjosh.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f1e6` / `#3f3f3f`)
- **Summary**: Josh Kern - webdesign and dev. Some work, info, and how to get in touch.
- **Total Clean CSS Variables Extracted**: `64` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `UglyDave`
- **Body Font Stack**: `Outfit`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--about-font-display: "UglyDave", cursive`; rule `h1` (`font-size: clamp(.9rem,1.7vmin,1.1rem)`, `line-height: 1.75`, `font-weight: inherit`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `1.075rem`, `1.15rem`, `.75rem`, `34px`)
- **Body Copy**: CSS variables `--about-font-body: "DM Sans", sans-serif`
- **Metadata & Labels**: CSS variables `--about-font-label: "DM Sans", sans-serif`, `--about-label-size: .98rem`, `--about-label-tracking: -.005em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f1e6` | `var(--base-100)` in `:root` |
| **Primary Typography Ink** | `#e0dfd7` | `var(--base-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5f5f5f` | `var(--base-300)` in `:root` |
| **Interactive Accent / Highlight** | `#3f3f3f` | `var(--base-350)` in `:root` |
| **Secondary / Muted Copy** | `#0c0908` | `var(--base-400)` in `:root` |
| **Structural Hairline Border** | `#e6dfd0` | `var(--kuli-ground)` in `:root` |
| **Variable Token (`--buy-bg`)** | `#2a1d15` | `var(--buy-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-100` | `#f5f1e6` | Color / Atmospheric Token |
| `--base-200` | `#e0dfd7` | Color / Atmospheric Token |
| `--base-300` | `#5f5f5f` | Color / Atmospheric Token |
| `--base-350` | `#3f3f3f` | Color / Atmospheric Token |
| `--base-400` | `#0c0908` | Color / Atmospheric Token |
| `--kuli-pad-top` | `clamp(8.5rem, 18vh, 11.5rem)` | Layout / Spatial Grid Token |
| `--kuli-thumb-h` | `clamp(3rem, 7vh, 4.5rem)` | Dimension / Scale Token |
| `--kuli-ground` | `#e6dfd0` | Color / Atmospheric Token |
| `--kuli-line-h` | `9px` | Dimension / Scale Token |
| `--buy-bg` | `#2a1d15` | Canvas / Surface Token |
| `--kuli-box-ink` | `6px` | Typography Ink Token |
| `--kuli-phone-ratio` | `720 / 1278` | Design System Custom Token |
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--ease-spring` | `cubic-bezier(.34, 1.56, .64, 1)` | Motion / Easing Token |
| `--frame-w` | `min(calc(62vh * 16 / 10), 88vw)` | Dimension / Scale Token |
| `--enter-op` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `webdesign-kernjosh-com`)**:
   - Landmark `<nav class="nav">` hosting `Josh Kern` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-landscape="primary"`, `data-back-pill`, `data-back-arrow-path`, `data-work-open`), and stylesheet rule `selection { color:0a0a0a;background:fff19a }`.
2. **Hero Stage & Focal Lead (<section.desk> — `Hey my name is Josh and I cool web`)**:
   - Landmark `<section class="desk">` presenting display lead `Hey my name is Josh and I cool websites :)` and copy excerpt *"c e d r i c c a r r . c o m"* over `#f5f1e6` canvas and `#0c0908` ink.
3. **Primary Showcase & Content Grid (<section.work-stage> — `Getting to know you`)**:
   - Landmark `<section class="work-stage">` rendering section `Getting to know you` with copy *"C l i c k t o o p e n p r o j e c t"*, asset references (`favicon.png`, `apple-touch-icon.png`, `challenges.cloudflare.com`, `main-CwptEoZ4.js`), and grid rule `font-face { font-family:Outfit;src:url(/assets/Outfit-Variable-D6ftewdU.woff2)format... }`.
4. **Interactive Detail & Feature Matrix (<section.process-shell> — `Designing the site`)**:
   - Landmark `<section class="process-shell">` framing `Designing the site` and `Building the site` (*"1 Getting to know you I ask a lot of questions because I want the"*) with `#5f5f5f` surface cards, `#3f3f3f` accents, and `root { --base-100:f5f1e6;--base-200:e0dfd7;--base-300:5f5f5f;--base-350:3f3f3f;... }`.
5. **Colophon & Global Directory Footer (<footer.legal-footer> — `https://webdesign.kernjosh.com`)**:
   - Landmark `<footer class="legal-footer">` anchoring `Josh Kern` footer links (`Overview · Index · Archive · About · Contact`), copy *"I ask a lot of questions because I want the website to feel "*, and `#e6dfd0` structural dividers.
