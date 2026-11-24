---
title: "UI & UX Architecture: adamperlis-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: adamperlis-com

## Overview & Design Identity
- **Target**: `adamperlis-com` (**Adam Perlis — I design and build apps**)
- **Production URL**: [https://adamperlis.com](https://adamperlis.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×1744px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#efefeb`)
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
| **Elevated Surface / Card Substrate** | `#efefeb` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#efefeb` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#8a8a85` | live computed `footer` `color` (`computed_styles.json`) |
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
   - Landmark `<header class="pointer-events-none inset-x-0">` (`1440x52px`) hosting `Adam Perlis — I design and build app` navigation (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), DOM attributes (`data-paper-shader`, `data-intro`, `data-sound-toggle`, `data-sound-choice="on"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.wrap> — `Hello, I'm Adam. I design and buil`)**:
   - Landmark `<section class="wrap relative">` presenting display lead `Hello, I'm Adam. I design and build apps.` and copy excerpt *"I design and build apps."* over `#ffffff` canvas and `#161615` ink.
3. **Primary Showcase & Content Grid (<section.moment> — `I design and build apps.`)**:
   - Landmark `<section class="moment py-12">` rendering section `I design and build apps.` with copy *"He built me with Claude Code, Codex and a little bit of love. Mos"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.place-items-center> — `He built me with Claude Code, Code`)**:
   - Landmark `<section class="place-items-center grid">` framing `He built me with Claude Code, Codex and a little` and `# best with sound on` (*"# best with sound on"*) with `#efefeb` surface cards, `#efefeb` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://adamperlis.com`)**:
   - Landmark `<footer class="wrap gap-4">` anchoring `Adam Perlis — I design and build` footer links (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), copy *"Need to install the following packages:"*, and `#ebebe7` structural dividers.
