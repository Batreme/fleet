---
title: "UI & UX Architecture: ethiack-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ethiack-com

## Overview & Design Identity
- **Target**: `ethiack-com` (**Ethiack**)
- **Production URL**: [https://ethiack.com/](https://ethiack.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×1744px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b191b` / `#ff8000`)
- **Summary**: Ethiack is the Adversarial Exposure Validation platform. Hackian continuously tests your attack surface, validates exploitability with pr...
- **Total Clean CSS Variables Extracted**: `180` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `fk-grotesk-light`
- **Body Font Stack**: `fk-raster-blended`
- **Monospace / Technical Font Stack**: `fk-grotesk-mono-medium`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 58.05px`, `line-height: 58.05px`, `font-weight: 400`, `letter-spacing: -2.322px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 109.15px`, `line-height: 98.235px`, `font-weight: 400`, `letter-spacing: -4.366px`); rule `h2` (`font-size: 44px`, `line-height: 1.02`, `letter-spacing: -.03em`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: clamp(64px,55.81px + 100vw *...`, `line-height: 1em`, `letter-spacing: -.1em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); CSS variables `--mono: 'FK Grotesk Mono','fk-grotesk-mono',ui-monospace,monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b191b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#161003` | `var(--body-backgroundColor)` in `:root` |
| **Interactive Accent / Highlight** | `#ff8000` | `.fn-date-picker .pika-button:hover { background: #ff8000 }` |
| **Secondary / Muted Copy** | `#82988b` | `var(--color-muted-green-300)` in `:root` |
| **Structural Hairline Border** | `#23403f` | `var(--line)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-geral-yellow`)** | `#ffdea6` | `var(--color-geral-yellow)` in `:root` |
| **Variable Token (`--color-geral-red`)** | `#7c2329` | `var(--color-geral-red)` in `:root` |
| **Variable Token (`--color-semantic-informative-800`)** | `#1e40af` | `var(--color-semantic-informative-800)` in `:root` |
| **Variable Token (`--color-semantic-informative-200`)** | `#bfdbfe` | `var(--color-semantic-informative-200)` in `:root` |
| **Variable Token (`--color-semantic-danger-200`)** | `#fec8cc` | `var(--color-semantic-danger-200)` in `:root` |
| **Variable Token (`--color-semantic-danger-500`)** | `#de2d3b` | `var(--color-semantic-danger-500)` in `:root` |
| **Variable Token (`--color-semantic-danger-600`)** | `#d12332` | `var(--color-semantic-danger-600)` in `:root` |
| **Variable Token (`--color-semantic-warning-600`)** | `#fbbf24` | `var(--color-semantic-warning-600)` in `:root` |
| **Variable Token (`--color-infection-detected`)** | `#ff0015` | `var(--color-infection-detected)` in `:root` |
| **Variable Token (`--color-infection-identified`)** | `#ff9900` | `var(--color-infection-identified)` in `:root` |
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
   - Landmark `<header class="lenis">` (`1440x900px`) hosting `Ethiack` navigation (`Try Ethiack`), DOM attributes (`data-hubspot-styled-components`, `data-onloadfired="true"`, `data-website-id="9c5e0156-7850-40b6-91..."`, `data-onload`), and stylesheet rule `p em { font-size:2.1vw }`.
2. **Hero Stage & Focal Lead (<main.main> — `AI Offensive Security. Proven, Con`)**:
   - Landmark `<main class="main">` presenting display lead `AI Offensive Security. Proven, Continuous.` and copy excerpt *"Annual pentests give you a snapshot. Results arrive late, ranked "* over `#0b191b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.main:nth(2)> — `Autonomous. Relentless. Continuous`)**:
   - Landmark `<main class="main">` rendering section `Autonomous. Relentless. Continuous.` with copy *"R i s k v a l i d a t e d !"*, asset references (`analytics-browser-gtm-2.12.2-min....`, `cc.js`, `uwt.js`, `uc.js`), and grid rule `svg { height:clamp(80px,71.03px + 100vw * .023,110px) }`.
4. **Interactive Detail & Feature Matrix (<main.main:nth(3)> — `Pentesting without schedules, snap`)**:
   - Landmark `<main class="main">` framing `Pentesting without schedules, snapshots, or manua...` and `Complete visibility of your attack surface and su...` (*"X S S i n D a s h b o a r d"*) with `#161003` surface cards, `#ff8000` accents, and `svg path { fill:var(--carousel-logo-color,var(--color-muted-green-600)) }`.
5. **Colophon & Global Directory Footer (<footer.scene-container> — `https://ethiack.com/`)**:
   - Landmark `<footer class="scene-container">` anchoring `Ethiack` footer links (`Try Ethiack`), copy *"Ethiack is leading the future of proactive cybersecurity."*, and `#23403f` structural dividers.
