# UI & UX Architecture: productionportugal-com

## Overview & Design Identity
- **Target**: `productionportugal-com` (**Production Portugal: Your trusted film production company in Portugal an...**)
- **Production URL**: [https://productionportugal.com/](https://productionportugal.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#6b6d79` / `#ff0080`)
- **Summary**: Dive into cinematic excellence with expert location scouting. Explore possibilities with Production Portugal - Your Trusted film producti...
- **Total Clean CSS Variables Extracted**: `23` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Grotesk Display Pro`
- **Body Font Stack**: `PP Eiko Italic`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#6b6d79` | `var(--_colours---color--grey--grey-100)` in `:root` |
| **Primary Typography Ink** | `#ff1972` | `var(--home__about__links-edge)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff0063` | `var(--_colours---brand)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0080` | `var(--base-bg)` in `:root` |
| **Secondary / Muted Copy** | `#ff126f` | `var(--blob-1)` in `:root` |
| **Structural Hairline Border** | `#a3003f` | `var(--blob-2)` in `:root` |
| **Variable Token (`--vignette`)** | `#590224d9` | `var(--vignette)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_colours---color--grey--grey-100` | `#6b6d79` | Brand / Palette Token |
| `--home__about__links-edge` | `#ff1972` | Typography Ink Token |
| `--_colours---brand` | `#ff0063` | Brand / Palette Token |
| `--psp-stage-height` | `var(--psp-viewport-height, 100dvh) !important` | Layout / Spatial Grid Token |
| `--psp-stage-bottom-inset` | `0px !important` | Dimension / Scale Token |
| `--psp-intro-height` | `100vh` | Layout / Spatial Grid Token |
| `--base-bg` | `#ff0080` | Canvas / Surface Token |
| `--blob-1` | `#ff126f` | Color / Atmospheric Token |
| `--blob-2` | `#a3003f` | Color / Atmospheric Token |
| `--vignette` | `#590224d9` | Color / Atmospheric Token |
| `--psp-viewport-height` | `100vh` | Layout / Spatial Grid Token |
| `--home-hero-project-progress` | `0%` | Dimension / Scale Token |
| `--home-brands-project-progress` | `0%` | Brand / Palette Token |
| `--psp-hover-x` | `0px` | Dimension / Scale Token |
| `--psp-hover-y` | `0px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `productionportugal-com`)**:
   - Landmark `<header class="header">` hosting `Production Portugal: Your trusted fi` navigation (`[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`), DOM attributes (`data-wf-domain="productionportugal.com"`, `data-wf-page="69f205b2a0439779a1d74754"`, `data-wf-site="69f205b0a0439779a1d746f7"`, `data-home-intro-title="Minute Maid"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.home__hero> — `We believe happiness—ours and your`)**:
   - Landmark `<section class="home__hero">` presenting display lead `We believe happiness—ours and yours—comes from cl...` and copy excerpt *"Hinge Can't Believe We Met on Hinge"* over `#6b6d79` canvas and `#a3003f` ink.
3. **Primary Showcase & Content Grid (<section.home__about> — `® we’re a leading Premium full-sca`)**:
   - Landmark `<section class="home__about">` rendering section `® we’re a leading Premium full-scale production s...` with copy *"Xfinity - We Love To Update"*, asset references (`cdn.prod.website-files.com`, `psp-6eb01f.webflow.shared.c80d7d9...`, `6a68884496439a79375f31d1_PSP-Logo...`, `6a688844292fe50b266154c7_PSP-Logo...`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.home__brands> — `Skip the Hesitation. Come Say Hi`)**:
   - Landmark `<section class="home__brands">` framing `Skip the Hesitation. Come Say Hi` and `Volkswagen Abt E-Line` (*"Volkswagen Abt E-Line"*) with `#ff0063` surface cards, `#ff0080` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://productionportugal.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Production Portugal: Your truste` footer links (`[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`), copy *"Uber - First Rides"*, and `#a3003f` structural dividers.
