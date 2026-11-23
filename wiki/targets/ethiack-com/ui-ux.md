---
title: "UI & UX Architecture: ethiack-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: ethiack-com

## Overview & Design Identity
- **Target**: `ethiack-com` (**Ethiack**)
- **Production URL**: [https://ethiack.com/](https://ethiack.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b191b` / `#ff8000`)
- **Summary**: Ethiack is the Adversarial Exposure Validation platform. Hackian continuously tests your attack surface, validates exploitability with pr...
- **Total Clean CSS Variables Extracted**: `184` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `fk-grotesk-light`
- **Body Font Stack**: `fk-grotesk-regular`
- **Monospace / Technical Font Stack**: `fk-grotesk-mono-medium`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 58.05px`, `line-height: 58.05px`, `font-weight: 400`, `letter-spacing: -2.322px`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 33.45px`, `line-height: 36.795px`, `font-weight: 400`, `letter-spacing: -1.0035px`); rule `h2` (`font-size: 44px`, `line-height: 1.02`, `letter-spacing: -.03em`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: clamp(64px,55.81px + 100vw *...`, `line-height: 1em`, `letter-spacing: -.1em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.1px`); CSS variables `--mono: 'FK Grotesk Mono','fk-grotesk-mono',ui-monospace,monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b191b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff8000` | `.fn-date-picker .pika-button:hover { background: #ff8000 }` |
| **Secondary / Muted Copy** | `#82988b` | `var(--color-muted-green-300)` in `:root` |
| **Structural Hairline Border** | `#23403f` | `var(--line)` in `:root` |
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
   - Landmark `<main class="main">` presenting display lead `AI Offensive Security. Proven, Continuous.` and copy excerpt *"We use cookies to personalise content and ads, to provide social "* over `#0b191b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.main:nth(2)> — `Autonomous. Relentless. Continuous`)**:
   - Landmark `<main class="main">` rendering section `Autonomous. Relentless. Continuous.` with copy *"Annual pentests give you a snapshot. Results arrive late, ranked "*, asset references (`analytics-browser-gtm-2.12.2-min....`, `cc.js`, `uwt.js`, `uc.js`), and grid rule `focus-within { background-color:var(--newsletter-form-focusBgColor,rgb(from var(--color... }`.
4. **Interactive Detail & Feature Matrix (<main.main:nth(3)> — `Pentesting without schedules, snap`)**:
   - Landmark `<main class="main">` framing `Pentesting without schedules, snapshots, or manua...` and `Complete visibility of your attack surface and su...` (*"R i s k v a l i d a t e d !"*) with `#000000` surface cards, `#ff8000` accents, and `.newsletter-target form { align-items:center;display:flex;flex-direction:row;justify-content:space... }`.
5. **Colophon & Global Directory Footer (<footer.scene-container> — `https://ethiack.com/`)**:
   - Landmark `<footer class="scene-container">` anchoring `Ethiack` footer links (`Try Ethiack`), copy *"X S S i n D a s h b o a r d"*, and `#23403f` structural dividers.
