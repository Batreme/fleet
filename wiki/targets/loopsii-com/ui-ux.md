---
title: "UI & UX Architecture: loopsii-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: loopsii-com

## Overview & Design Identity
- **Target**: `loopsii-com` (**Loopsii: the all-in-one app for freelancers**)
- **Production URL**: [https://loopsii.com/](https://loopsii.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f0` / `#c4f041`)
- **Summary**: Loopsii is the all-in-one app for freelancers: CRM, project management, time tracking, AI notes from client calls and dictation. 14-day f...
- **Total Clean CSS Variables Extracted**: `158` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Saans VF-1156b2189454d62c`
- **Body Font Stack**: `Saans VF-1156b2189454d62c`
- **Monospace / Technical Font Stack**: `Geist Mono-c001706f58ecc7d6`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 12px`, `line-height: 12px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 21px`, `line-height: 29.4px`, `font-weight: 400`, `letter-spacing: -0.63px`); rule `h2` (`font-size: calc(28 * var(--spacing))`, `letter-spacing: -.01em`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 12px`, `font-weight: 400`); CSS variables `--font-body: var(--font-title)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 12px`, `font-weight: 400`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0f0` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.prose code { background: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#c4f041` | `var(--color-main)` in `:root` |
| **Secondary / Muted Copy** | `#8fd8ff` | `var(--tp-input-foreground-color)` in `:root` |
| **Structural Hairline Border** | `#d0d0d0` | `.nav_legal .nav_legal-socials { border-color: #d0d0d0 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-body` | `var(--font-title)` | Typography / Scale Token |
| `--dw` | `1920` | Design System Custom Token |
| `--dh` | `900` | Design System Custom Token |
| `--to-vh` | `var(--dh) * 100vh` | Layout / Spatial Grid Token |
| `--screen-h` | `100lvh` | Dimension / Scale Token |
| `--size-unit` | `16` | Layout / Spatial Grid Token |
| `--hand-scale` | `1.5` | Design System Custom Token |
| `--size-container-ideal` | `1920` | Layout / Spatial Grid Token |
| `--size-container-min` | `1200px` | Layout / Spatial Grid Token |
| `--size-container-max` | `2560px` | Layout / Spatial Grid Token |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container-max))` | Layout / Spatial Grid Token |
| `--ease` | `.8s cubic-bezier(.84, 0, .16, 1)` | Motion / Easing Token |
| `--fast-ease` | `.6s cubic-bezier(.84, 0, .16, 1)` | Motion / Easing Token |
| `--smooth` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Timing Token |
| `--color-ease` | `.4s ease-out` | Brand / Palette Token |
| `--multiplier` | `.2` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.is-loading> — `loopsii-com`)**:
   - Landmark `<header class="is-loading">` (`1440x872px`) hosting `Loopsii: the all-in-one app for free` navigation (`W h y L o o p s i i · F e a t u r e s · P r i c i n g`), DOM attributes (`data-transition="wrapper"`, `data-loader`, `data-module="NavMorph"`, `data-track="nav-logo"`), and stylesheet rule `root { --font-title:"Saans VF-1156b2189454d62c","Saans VF-1156b2189454d62c fall... }`.
2. **Hero Stage & Focal Lead (<section.intro> — `Loopsii, the all-in-one app for fr`)**:
   - Landmark `<section class="intro z-2">` presenting display lead `Loopsii, the all-in-one app for freelancers` and copy excerpt *"Every project follows a familiar loop. Loopsii keeps it moving, s"* over `#f0f0f0` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.distraction> — `The all-in-one app for freelancers`)**:
   - Landmark `<section class="distraction z-3">` rendering section `The all-in-one app for freelancers. Like a person...` with copy *"Too many things pulling you away"*, asset references (`f1306f12b629075b.woff2`, `fd3499837a53ca88.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `.v-text { writing-mode:vertical-lr }`.
4. **Interactive Detail & Feature Matrix (<section.app-demo> — `Loopsii helps freelance designers `)**:
   - Landmark `<section class="app-demo app-demo--pinned">` framing `Loopsii helps freelance designers and developers...` and `That's why Loopsii exists` (*"from the work that actually matters"*) with `#ffffff` surface cards, `#c4f041` accents, and `.display { font-size:calc(164 * var(--spacing));letter-spacing:-.02em;font-variatio... }`.
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://loopsii.com/`)**:
   - Landmark `<footer class="fixed">` anchoring `Loopsii: the all-in-one app for ` footer links (`W h y L o o p s i i · F e a t u r e s · P r i c i n g`), copy *"Forgot to start the timer"*, and `#d0d0d0` structural dividers.
