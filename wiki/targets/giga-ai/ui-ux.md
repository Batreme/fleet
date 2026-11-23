---
title: "UI & UX Architecture: giga-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: giga-ai

## Overview & Design Identity
- **Target**: `giga-ai` (**Giga: AI support agents that improve your metrics**)
- **Production URL**: [https://giga.ai/](https://giga.ai/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0090ff`)
- **Summary**: Giga builds enterprise AI agents for customer support that resolve complex conversations across chat, voice, and email. Deployed in weeks...
- **Total Clean CSS Variables Extracted**: `1064` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Pixel Line`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 64px`, `font-weight: 400`); CSS variables `--display: inter, interExt, "InterVariable", system-ui, sans-serif`, `--text-4xl: 2rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 52.63px`, `line-height: 63.156px`, `font-weight: 400`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 2rem`, `line-height: 1.1`, `letter-spacing: var(--tracking-display)`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--gh-text-body: 1.125rem`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 13.5px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mono: "Geist Mono", ui-monospace, monospace`, `--key-mono: 400 11px/14px "Geist Mono", geistMono, monospace`, `--gh-text-meta: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#111c22` | `var(--gh-industry-surface)` in `:root` |
| **Interactive Accent / Highlight** | `#0090ff` | `var(--omni-cta)` in `:root` |
| **Secondary / Muted Copy** | `#6e6e6e` | `var(--gba-tool-use-chevron-fg)` in `:root` |
| **Structural Hairline Border** | `#2a2b2b` | `var(--gh-industry-border)` in `:root` (`rgb(232 237 239 / .18)`) |
| **Variable Token (`--orange`)** | `#ef5a00` | `var(--orange)` in `:root` |
| **Variable Token (`--key-face`)** | `#3b3b3e` | `var(--key-face)` in `:root` |
| **Variable Token (`--key-face`)** | `#2a2a2d` | `var(--key-face)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sans` | `"Geist", system-ui, sans-serif` | Typography / Scale Token |
| `--mono` | `"Geist Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--display` | `inter, interExt, "InterVariable", system-ui, sans-serif` | Dimension / Scale Token |
| `--text` | `inter, interExt, "InterVariable", system-ui, sans-serif` | Typography Ink Token |
| `--pixel` | `"Geist Pixel Line", "Geist Mono", monospace` | Design System Custom Token |
| `--orange` | `#ef5a00` | Color / Atmospheric Token |
| `--bar-h` | `calc(54px * max(1, var(--s, 1)))` | Dimension / Scale Token |
| `--key-radius` | `8px` | Elevation / Border Token |
| `--key-face` | `linear-gradient(123.37deg, #3b3b3e 13.97%, #2a2a2d 87.5%)` | Color / Atmospheric Token |
| `--key-edge` | `rgb(255 255 255 / .12)` | Color / Atmospheric Token |
| `--key-lit` | `inset 1px 1px 0 rgb(255 255 255 / .08)` | Color / Atmospheric Token |
| `--key-ink` | `rgb(232 237 239 / .88)` | Typography Ink Token |
| `--key-shadow` | `4px 6px 5px rgb(0 0 0 / .5), 2px 4px 2.5px rgb(0 0 0 / .6)` | Elevation / Border Token |
| `--key-shadow-down` | `1px 2px 2px rgb(0 0 0 / .5), 1px 1px 1px rgb(0 0 0 / .6)` | Elevation / Border Token |
| `--key-hover` | `brightness(1.12)` | Design System Custom Token |
| `--key-ring` | `1.5px solid rgb(232 237 239 / .6)` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.docked> — `giga-ai`)**:
   - Landmark `<header class="docked">` (`1440x86px`) hosting `Giga: AI support agents that improve` navigation (`Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`), DOM attributes (`data-theme="dark"`, `data-consent-region="gdpr"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `nter_8d8624c8-module__h29akW__cla... { font-family:inter }`.
2. **Hero Stage & Focal Lead (<section.banner-off> — `No time to wait.`)**:
   - Landmark `<section class="banner-off">` presenting display lead `No time to wait.` and copy excerpt *"AI AGENTS FOR CUSTOMER EXPERIENCE"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.hero-fixed> — `Giga agents are flexible.`)**:
   - Landmark `<section class="hero-fixed">` rendering section `Giga agents are flexible.` with copy *"AI Agents for Customer Experience"*, asset references (`geist_mono_400_latin-s.p.2qleaeww...`, `geist_pixel_line-s.p.1gvmpev-r-ty...`, `geist_sans_400-s.p.18rrztdh9mmoo....`, `geist_sans_500-s.p.08803r3rti4jl....`), and grid rule `inter_8d8624c8-module__h29akW__va... { --font-sans-source:"inter" }`.
4. **Interactive Detail & Feature Matrix (<section.gh-industries> — `See how Giga will improve your bus`)**:
   - Landmark `<section class="gh-industries">` framing `See how Giga will improve your business.` and `Freight & Logistics` (*"AI agents that resolve issues instantly across every channel and "*) with `#111c22` surface cards, `#0090ff` accents, and `erext_c8633ef-module__Fv8OZW__cla... { font-family:interExt,interExt Fallback }`.
5. **Colophon & Global Directory Footer (<footer.giga-cc> — `https://giga.ai/`)**:
   - Landmark `<footer class="giga-cc">` anchoring `Giga: AI support agents that imp` footer links (`Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`), copy *"try talking to our agent _"*, and `#2a2b2b` structural dividers.
