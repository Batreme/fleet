---
title: "UI & UX Architecture: helmetverse-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: helmetverse-ai

## Overview & Design Identity
- **Target**: `helmetverse-ai` (**Helmetverse · Design yours**)
- **Production URL**: [https://helmetverse.ai/](https://helmetverse.ai/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f4f1` / `#00d2aa`)
- **Summary**: Type a prompt. The team rides what you imagine.
- **Total Clean CSS Variables Extracted**: `193` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `G42 Sans`
- **Body Font Stack**: `G42 Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 194.4px`, `line-height: 213.84px`, `font-weight: 900`, `letter-spacing: -7.776px`); CSS variables `--text-display: 60px`, `--text-h1: 48px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 30.6px`, `font-weight: 900`, `letter-spacing: -1.44px`); CSS variables `--text-h2: 36px`; rule `h2` (`font-size: 15px`, `line-height: 1.3`, `letter-spacing: .02em`, `font-weight: 900`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--text-body-lg: 18px`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: "G42 Sans", "Space Grotesk", sans-serif`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f4f1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#2a312b` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#00d2aa` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00d2aa` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#00d2aa` | `var(--color-secondary)` in `:root` |
| **Structural Hairline Border** | `#ede9e4` | `var(--color-border-light)` in `:root` |
| **Variable Token (`--color-accent-deep`)** | `#00baa0` | `var(--color-accent-deep)` in `:root` |
| **Variable Token (`--color-yellow`)** | `#f2ff5a` | `var(--color-yellow)` in `:root` |
| **Variable Token (`--color-blue`)** | `#0c56ff` | `var(--color-blue)` in `:root` |
| **Variable Token (`--color-surface-light`)** | `#ffffff` | `var(--color-surface-light)` in `:root` |
| **Variable Token (`--color-border2-light`)** | `#e5e7eb` | `var(--color-border2-light)` in `:root` |
| **Variable Token (`--color-bg-dark`)** | `#15161b` | `var(--color-bg-dark)` in `:root` |
| **Variable Token (`--color-surface-dark`)** | `#1c2620` | `var(--color-surface-dark)` in `:root` |
| **Variable Token (`--color-border-dark`)** | `#2a3830` | `var(--color-border-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-primary` | `#2a312b` | Brand / Palette Token |
| `--color-accent` | `#00d2aa` | Brand / Palette Token |
| `--color-accent-deep` | `#00baa0` | Brand / Palette Token |
| `--color-yellow` | `#f2ff5a` | Brand / Palette Token |
| `--color-blue` | `#0c56ff` | Brand / Palette Token |
| `--color-bg-light` | `#f7f4f1` | Canvas / Surface Token |
| `--color-surface-light` | `#fff` | Canvas / Surface Token |
| `--color-border-light` | `#ede9e4` | Canvas / Surface Token |
| `--color-border2-light` | `#e5e7eb` | Canvas / Surface Token |
| `--color-bg-dark` | `#15161b` | Canvas / Surface Token |
| `--color-surface-dark` | `#1c2620` | Canvas / Surface Token |
| `--color-border-dark` | `#2a3830` | Canvas / Surface Token |
| `--color-text-primary-light` | `#2a312b` | Canvas / Surface Token |
| `--color-text-secondary-light` | `#2a312b99` | Canvas / Surface Token |
| `--color-text-primary-dark` | `#f7f4f1` | Canvas / Surface Token |
| `--color-text-secondary-dark` | `#f7f4f18c` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.jsx-25f90e9ce2076406> — `helmetverse-ai`)**:
   - Landmark `<nav class="jsx-25f90e9ce2076406 overflow-hidden">` (`367x12px`) hosting `Helmetverse · Design yours` navigation (`Home · Gallery · AI Studio · Leaderboard · About`), DOM attributes (`data-paper-shader`, `data-precedence="next"`, `data-precedence="next"`, `data-styled-jsx`), and stylesheet rule `.PhoneInput { align-items:center;display:flex }`.
2. **Hero Stage & Focal Lead (<main.bg-bg-dark> — `HELMETVERSE`)**:
   - Landmark `<main class="bg-bg-dark text-text-primary-dark">` presenting display lead `HELMETVERSE` and copy excerpt *"Submissions and voting are officially closed. Explore this year’s"* over `#f7f4f1` canvas and `#2a312b` ink.
3. **Primary Showcase & Content Grid (<main.text-text-primary-dark> — `DESIGN WITHOUT LIMITS`)**:
   - Landmark `<main class="bg-bg-dark text-text-primary-dark">` rendering section `DESIGN WITHOUT LIMITS` with copy *"H E L M E T V E R S E"*, asset references (`6577f91f-ad74-4868-93e8-13027534a...`, `79d7fc46-0103-4a7f-b9f7-d1012c6fa...`, `98da8316-c3f4-4946-adb6-727aa17a0...`, `b241f184-7659-4fb4-bdb4-cdf53d1fc...`), and grid rule `.PhoneInputInput { flex:1;min-width:0 }`.
4. **Interactive Detail & Feature Matrix (<main.relative> — `A GLOBAL COMPETITION FOR THE MOST `)**:
   - Landmark `<main class="bg-bg-dark text-text-primary-dark">` framing `A GLOBAL COMPETITION FOR THE MOST CREATIVE MINDS` and `FEATURED HELMET DESIGNS` (*"Win a trip to Abu Dhabi"*) with `#00d2aa` surface cards, `#00d2aa` accents, and `.PhoneInputCountryIcon--square { width:var(--PhoneInputCountryFlag-height) }`.
5. **Colophon & Global Directory Footer (<footer.text-text-primary-dark> — `https://helmetverse.ai/`)**:
   - Landmark `<footer class="text-text-primary-dark">` anchoring `Helmetverse · Design yours` footer links (`Home · Gallery · AI Studio · Leaderboard · About`), copy *"THE DESIGNS ARE IN. NOW YOU DECIDE WHO WINS."*, and `#ede9e4` structural dividers.
