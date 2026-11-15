# UI & UX Architecture: earthwallet-com

## Overview & Design Identity
- **Target**: `earthwallet-com` (**Earth Wallet — Real assets for unreal markets**)
- **Production URL**: [https://earthwallet.com/](https://earthwallet.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#2496FF` / `#55D171`)
- **Summary**: Financial claims can be created at will. Metal has to be found, dug and processed. Earth Wallet on hard assets, critical minerals and Can...
- **Total Clean CSS Variables Extracted**: `26` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gilroy`
- **Body Font Stack**: `Urbanist`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: Gilroy,Urbanist,sans-serif`; rule `h1` (`line-height: 1`, `letter-spacing: -.045em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`line-height: 1.08`)
- **Body Copy**: CSS variables `--font-body: Poppins,sans-serif`; rule `body` (`font-weight: 300`)
- **Metadata & Labels**: rule `small` (`font-size: 11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#2496FF` | `var(--ew-social-blue)` in `:root` |
| **Primary Typography Ink** | `#7CC0FF` | `var(--ew-social-blue-60)` in `:root` |
| **Elevated Surface / Card Substrate** | `#D3EAFF` | `var(--ew-social-blue-20)` in `:root` |
| **Interactive Accent / Highlight** | `#55D171` | `var(--ew-forest-green)` in `:root` |
| **Secondary / Muted Copy** | `#FFD600` | `var(--ew-electric-yellow)` in `:root` |
| **Structural Hairline Border** | `#FFA800` | `var(--ew-gold)` in `:root` |
| **Variable Token (`--ew-electric-violet`)** | `#691FDD` | `var(--ew-electric-violet)` in `:root` |
| **Variable Token (`--ew-electric-violet-60`)** | `#A579EB` | `var(--ew-electric-violet-60)` in `:root` |
| **Variable Token (`--ew-crimson`)** | `#E22D3F` | `var(--ew-crimson)` in `:root` |
| **Variable Token (`--ew-crimson-20`)** | `#F9D5D9` | `var(--ew-crimson-20)` in `:root` |
| **Variable Token (`--ew-moonlight-grey`)** | `#E6E9ED` | `var(--ew-moonlight-grey)` in `:root` |
| **Variable Token (`--ew-shuttle-gray`)** | `#A5ACBB` | `var(--ew-shuttle-gray)` in `:root` |
| **Variable Token (`--ew-outer-space`)** | `#0F1726` | `var(--ew-outer-space)` in `:root` |
| **Variable Token (`--ew-outer-space-80`)** | `#3F4551` | `var(--ew-outer-space-80)` in `:root` |
| **Variable Token (`--ew-outer-space-60`)** | `#6F747D` | `var(--ew-outer-space-60)` in `:root` |
| **Variable Token (`--ew-outer-space-20`)** | `#CFD1D4` | `var(--ew-outer-space-20)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ew-social-blue` | `#2496FF` | Color / Atmospheric Token |
| `--ew-social-blue-60` | `#7CC0FF` | Color / Atmospheric Token |
| `--ew-social-blue-20` | `#D3EAFF` | Color / Atmospheric Token |
| `--ew-forest-green` | `#55D171` | Color / Atmospheric Token |
| `--ew-electric-yellow` | `#FFD600` | Color / Atmospheric Token |
| `--ew-gold` | `#FFA800` | Color / Atmospheric Token |
| `--ew-electric-violet` | `#691FDD` | Color / Atmospheric Token |
| `--ew-electric-violet-60` | `#A579EB` | Color / Atmospheric Token |
| `--ew-crimson` | `#E22D3F` | Color / Atmospheric Token |
| `--ew-crimson-20` | `#F9D5D9` | Color / Atmospheric Token |
| `--ew-moonlight-grey` | `#E6E9ED` | Canvas / Surface Token |
| `--ew-shuttle-gray` | `#A5ACBB` | Color / Atmospheric Token |
| `--ew-outer-space` | `#0F1726` | Layout / Spatial Grid Token |
| `--ew-outer-space-80` | `#3F4551` | Layout / Spatial Grid Token |
| `--ew-outer-space-60` | `#6F747D` | Layout / Spatial Grid Token |
| `--ew-outer-space-20` | `#CFD1D4` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero-orbit> — `earthwallet-com`)**:
   - Landmark `<header class="hero-orbit">` hosting `Earth Wallet — Real assets for unrea` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-frame-ms="7232.6"`, `data-scene-progress="0.0"`, `data-engine="three.js r160"`), and stylesheet rule `font-face { font-family:Gilroy;src:local('Gilroy-Medium'),local('Gilroy Medium');fon... }`.
2. **Hero Stage & Focal Lead (<section.orbit-ui> — `Look at Canada from ABOVE`)**:
   - Landmark `<section class="orbit-ui">` presenting display lead `Look at Canada from ABOVE` and copy excerpt *"A CHANGE IN PERSPECTIVE"* over `#2496FF` canvas and `#D3EAFF` ink.
3. **Primary Showcase & Content Grid (<section.descent-copy> — `Not from the side.`)**:
   - Landmark `<section class="descent-copy">` rendering section `Not from the side.` with copy *"Look at Canada from"*, asset references (`site.webmanifest`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `body { font-family:var(--font-body);font-weight:300 }`.
4. **Interactive Detail & Feature Matrix (<section.cloud-copy> — `From the ground. Into our future.`)**:
   - Landmark `<section class="cloud-copy">` framing `From the ground. Into our future.` and `The world’s demand for critical minerals is outpa...` (*"An uninterrupted journey that begins in polar orbit and descends "*) with `#D3EAFF` surface cards, `#55D171` accents, and `.ending-chart h3 { font-family:var(--font-display);font-weight:600;letter-spacing:-.01em }`.
5. **Colophon & Global Directory Footer (<footer.planet-rendered> — `https://earthwallet.com/`)**:
   - Landmark `<footer class="planet-rendered">` anchoring `Earth Wallet — Real assets for u` footer links (`Overview · Index · Archive · About · Contact`), copy *"Forty years of exporting raw concentrate and importing the f"*, and `#FFA800` structural dividers.
