# UI & UX Architecture: www-avara-band

## Overview & Design Identity
- **Target**: `www-avara-band` (**AVARA**)
- **Production URL**: [http://www.avara.band](http://www.avara.band)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#000000`)
- **Summary**: AVARA — an old Georgian word, the closest our language comes to punk. Band from Tbilisi.
- **Total Clean CSS Variables Extracted**: `38` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ff-brokenscript-bc-web`
- **Body Font Stack**: `novecento-sans-condensed`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(72px,18vw,200px)`, `11px`, `15px`, `clamp(60px,10vw,140px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(72px,18vw,200px)`, `11px`, `15px`, `clamp(60px,10vw,140px)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(72px,18vw,200px)`, `11px`, `15px`, `clamp(60px,10vw,140px)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(72px,18vw,200px)`, `11px`, `15px`, `clamp(60px,10vw,140px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#182833` | `var(--color-firefly)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `html { background-color: black }` (`#000000`) |
| **Secondary / Muted Copy** | `#ffffff` | `::-moz-selection { color: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#0009` | `:hover { background: #0009 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-family-inter-thin` | `Inter-Thin` | Typography / Scale Token |
| `--font-family-inter-light` | `Inter-Light` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-transparent` | `transparent` | Brand / Palette Token |
| `--color-firefly` | `#182833` | Brand / Palette Token |
| `--layout-grid-xxs` | `1.0416666667vw` | Layout / Spatial Grid Token |
| `--layout-grid-xxs-px` | `20px` | Layout / Spatial Grid Token |
| `--layout-grid-xs` | `2.0833333333vw` | Layout / Spatial Grid Token |
| `--layout-grid-xs-px` | `40px` | Layout / Spatial Grid Token |
| `--layout-grid-s` | `3.125vw` | Layout / Spatial Grid Token |
| `--layout-grid-s-px` | `60px` | Layout / Spatial Grid Token |
| `--layout-grid-m` | `4.1666666667vw` | Layout / Spatial Grid Token |
| `--layout-grid-m-px` | `80px` | Layout / Spatial Grid Token |
| `--layout-grid-l` | `5.2083333333vw` | Layout / Spatial Grid Token |
| `--layout-grid-l-px` | `100px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-avara-band`)**:
   - Landmark `<header class="lenis">` hosting `AVARA` navigation (`MOGONEBEBS`), DOM attributes (`data-v-app`, `data-v-6a59b94f`, `data-v-976b387d`, `data-v-be045427`), and stylesheet rule `.tk-ff-brokenscript-bc-web { font-family: "ff-brokenscript-bc-web",serif; }`.
2. **Hero Stage & Focal Lead (<div.lenis-stopped> — `AVARA`)**:
   - Landmark `<div class="lenis-stopped">` presenting display lead `AVARA` and copy excerpt *"is an old Georgian word, the closest"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.default-layout> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="default-layout">` rendering section `Featured Work & Interactive Showcase` with copy *"our language comes to punk ."*, asset references (`use.typekit.net`, `p.typekit.net`, `axe8qgi.css`, `entry.T26Jnyvf.css`), and grid rule `.tk-novecento-sans-condensed { font-family: "novecento-sans-condensed",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<div.app-header> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="app-header">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"our language comes to"*) with `#182833` surface cards, `#000000` accents, and `.tk-owners-wide { font-family: "owners-wide",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.flex-center> — `http://www.avara.band`)**:
   - Landmark `<footer class="flex-center">` anchoring `AVARA` footer links (`MOGONEBEBS`), copy *"It belongs to those who drift ,"*, and `#0009` structural dividers.
