---
title: "UI & UX Architecture: adamperlis-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: adamperlis-com

## Overview & Design Identity
- **Target**: `adamperlis-com` (**Adam Perlis — I design and build apps**)
- **Production URL**: [https://adamperlis.com](https://adamperlis.com)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#009dff`)
- **Summary**: Founder of Academy, formerly Head of Design at TIME and Head of UX at AKQA. I help founders and teams design, build and ship their apps.
- **Total Clean CSS Variables Extracted**: `83` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SF Pro Display`
- **Body Font Stack**: `SF Pro Display`
- **Monospace / Technical Font Stack**: `Geist Mono Variable`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`, `letter-spacing: -0.21px`); CSS variables `--font-mono: "Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#161615` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e4e4df` | `:hover { background-color: #e4e4df }` |
| **Interactive Accent / Highlight** | `#009dff` | `var(--color-glass)` in `:root` |
| **Secondary / Muted Copy** | `#8a8a85` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ebebe7` | `var(--color-rule)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-mono` | `"Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--container-5xl` | `64rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `adamperlis-com`)**:
   - Landmark `<header class="pointer-events-none inset-x-0">` (`1440x52px`) hosting `Adam Perlis — I design and build app` navigation (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), DOM attributes (`data-paper-shader`, `data-site-header`, `data-home`, `data-buddy-sound`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.wrap> — `Hello, I'm Adam. I design and buil`)**:
   - Landmark `<section class="wrap relative">` presenting display lead `Hello, I'm Adam. I design and build apps.` and copy excerpt *"He built me with Claude Code, Codex and a little bit of love. Mos"* over `#ffffff` canvas and `#161615` ink.
3. **Primary Showcase & Content Grid (<section.moment> — `He built me with Claude Code, Code`)**:
   - Landmark `<section class="moment py-12">` rendering section `He built me with Claude Code, Codex and a little` with copy *"I design and build apps."*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.place-items-center> — `I design and build apps.`)**:
   - Landmark `<section class="place-items-center grid">` framing `I design and build apps.` and `Fifteen years leading design for clients like Go` (*"Fifteen years leading design for clients like Google, Microsoft, "*) with `#e4e4df` surface cards, `#009dff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://adamperlis.com`)**:
   - Landmark `<footer class="wrap gap-4">` anchoring `Adam Perlis — I design and build` footer links (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), copy *"Formerly Head of Product Design at TIME, AKQA, B-Reel and BA"*, and `#ebebe7` structural dividers.
