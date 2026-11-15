# UI & UX Architecture: ethiack-com

## Overview & Design Identity
- **Target**: `ethiack-com` (**Ethiack**)
- **Production URL**: [https://ethiack.com/](https://ethiack.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#7c2329`)
- **Summary**: Ethiack is the Adversarial Exposure Validation platform. Hackian continuously tests your attack surface, validates exploitability with pr...
- **Total Clean CSS Variables Extracted**: `167` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Mono`
- **Body Font Stack**: `fk-grotesk-light`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(18px,16.05px + 100vw * .005...`, `1.2vw`, `500px`, `12px`, `clamp(13px,12.61px + 100vw * .001...`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(18px,16.05px + 100vw * .005...`, `1.2vw`, `500px`, `12px`, `clamp(13px,12.61px + 100vw * .001...`)
- **Body Copy**: CSS variables `--body-backgroundColor: #161003`; rule `p` (`font-size: 12px`, `line-height: 1.1em`, `letter-spacing: 0`)
- **Metadata & Labels**: CSS variables `--menu-light-button-label-color: var(--color-bright-green-500)`, `--menu-dark-button-label-color: var(--color-deep-green-500)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffdea6` | `var(--color-geral-yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#7c2329` | `var(--color-geral-red)` in `:root` |
| **Secondary / Muted Copy** | `#1e40af` | `var(--color-semantic-informative-800)` in `:root` |
| **Structural Hairline Border** | `#bfdbfe` | `var(--color-semantic-informative-200)` in `:root` |
| **Variable Token (`--color-semantic-danger-200`)** | `#fec8cc` | `var(--color-semantic-danger-200)` in `:root` |
| **Variable Token (`--color-semantic-danger-500`)** | `#de2d3b` | `var(--color-semantic-danger-500)` in `:root` |
| **Variable Token (`--color-semantic-danger-600`)** | `#d12332` | `var(--color-semantic-danger-600)` in `:root` |
| **Variable Token (`--color-semantic-warning-600`)** | `#fbbf24` | `var(--color-semantic-warning-600)` in `:root` |
| **Variable Token (`--color-infection-detected`)** | `#ff0015` | `var(--color-infection-detected)` in `:root` |
| **Variable Token (`--color-infection-identified`)** | `#f90` | `var(--color-infection-identified)` in `:root` |
| **Variable Token (`--color-muted-green-50`)** | `#e8ecea` | `var(--color-muted-green-50)` in `:root` |
| **Variable Token (`--color-muted-green-100`)** | `#cdd5d0` | `var(--color-muted-green-100)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-geral-black` | `#000` | Canvas / Surface Token |
| `--color-geral-white` | `#fff` | Canvas / Surface Token |
| `--color-geral-yellow` | `#ffdea6` | Brand / Palette Token |
| `--color-geral-red` | `#7c2329` | Brand / Palette Token |
| `--color-semantic-informative-800` | `#1e40af` | Brand / Palette Token |
| `--color-semantic-informative-200` | `#bfdbfe` | Brand / Palette Token |
| `--color-semantic-danger-200` | `#fec8cc` | Brand / Palette Token |
| `--color-semantic-danger-500` | `#de2d3b` | Brand / Palette Token |
| `--color-semantic-danger-600` | `#d12332` | Brand / Palette Token |
| `--color-semantic-warning-600` | `#fbbf24` | Brand / Palette Token |
| `--color-infection-detected` | `#ff0015` | Brand / Palette Token |
| `--color-infection-identified` | `#f90` | Brand / Palette Token |
| `--color-muted-green-50` | `#e8ecea` | Brand / Palette Token |
| `--color-muted-green-100` | `#cdd5d0` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `ethiack-com`)**:
   - Landmark `<header class="lenis">` hosting `Ethiack` navigation (`Try Ethiack`), DOM attributes (`data-hubspot-styled-components`, `data-onloadfired="true"`, `data-website-id="9c5e0156-7850-40b6-91..."`, `data-onload`), and stylesheet rule `svg path { fill:var(--buttonIcon-iconColor,var(--color-muted-green-400));transition... }`.
2. **Hero Stage & Focal Lead (<main.main> — `AI Offensive Security. Proven, Con`)**:
   - Landmark `<main class="main">` presenting display lead `AI Offensive Security. Proven, Continuous.` and copy excerpt *"Annual pentests give you a snapshot. Results arrive late, ranked "* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.main> — `Autonomous. Relentless. Continuous`)**:
   - Landmark `<main class="main">` rendering section `Autonomous. Relentless. Continuous.` with copy *"L e a k e d C r e d e n t i a l s D e t e c t e d"*, asset references (`gtm.js`, `v2.js`, `entry.zScR8SkK.css`, `index.D9o0If2e.css`), and grid rule `svg { height:56px;position:relative;width:56px;z-index:5 }`.
4. **Interactive Detail & Feature Matrix (<main.main> — `Pentesting without schedules, snap`)**:
   - Landmark `<main class="main">` framing `Pentesting without schedules, snapshots, or manua...` and `See` (*"R i s k v a l i d a t e d !"*) with `#ffdea6` surface cards, `#7c2329` accents, and `hover { background-color:transparent }`.
5. **Colophon & Global Directory Footer (<footer.scene-container> — `https://ethiack.com/`)**:
   - Landmark `<footer class="scene-container">` anchoring `Ethiack` footer links (`Try Ethiack`), copy *"X S S i n D a s h b o a r d"*, and `#bfdbfe` structural dividers.
