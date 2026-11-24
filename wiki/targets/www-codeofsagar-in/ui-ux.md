---
title: "UI & UX Architecture: www-codeofsagar-in"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-codeofsagar-in

## Overview & Design Identity
- **Target**: `www-codeofsagar-in` (**Sagar K. Ghosh — Full-stack Developer & Designer**)
- **Production URL**: [https://www.codeofsagar.in/](https://www.codeofsagar.in/)
- **Final Redirected URL**: [https://codeofsagar.in/](https://codeofsagar.in/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#008000`)
- **Summary**: Websites and stores that sell, 3D people remember and automation that gives your team its time back, designed and built by Sagar K. Ghosh.
- **Total Clean CSS Variables Extracted**: `126` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `spaceGrotesk`
- **Body Font Stack**: `spaceGrotesk`
- **Monospace / Technical Font Stack**: `spaceMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 70.72px`, `line-height: 70.72px`, `font-weight: 400`, `letter-spacing: -2.1216px`); CSS variables `--font-display: var(--font-space-grotesk), ui-sans-serif, system-ui, sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 144px`, `line-height: 122.4px`, `font-weight: 300`, `letter-spacing: -3.6px`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 22.1px`, `font-weight: 700`, `letter-spacing: -0.085px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 22.1px`, `font-weight: 700`, `letter-spacing: -0.085px`); CSS variables `--type-meta: 700 .9rem / 1.3 var(--font-tech)`, `--ls-meta: .06em`, `--text-xs: .75rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f0f0f` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eeeae5` | `.project-transition-overlay { background: #eeeae5 }` |
| **Interactive Accent / Highlight** | `#008000` | `des button.AboutClutter-module_... { background: green }` (`#008000`) |
| **Secondary / Muted Copy** | `#262626` | `var(--ink-soft)` in `:root` |
| **Structural Hairline Border** | `#eeeeee` | `var(--line)` in `:root` (`0f0f0f12`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fs-text` | `1rem` | Typography Ink Token |
| `--fs-btn` | `var(--fs-text)` | Design System Custom Token |
| `--fs-head` | `var(--fs-text)` | Design System Custom Token |
| `--fw-text` | `700` | Typography Ink Token |
| `--fs-semi` | `clamp(1.5rem, 2.3vw, 2.6rem)` | Dimension / Scale Token |
| `--fs-title` | `clamp(2.2rem, 1rem + 3.8vw, 5rem)` | Dimension / Scale Token |
| `--type-text` | `var(--fw-text) var(--fs-text) / 1.3 var(--font-grotesk)` | Typography Ink Token |
| `--type-head` | `500 var(--fs-head) / 1.05 var(--font-grotesk)` | Typography / Scale Token |
| `--type-title` | `400 var(--fs-title) / 1 var(--font-grotesk)` | Typography / Scale Token |
| `--type-mtitle` | `700 clamp(2.25rem, 10.5vw, 3.25rem) / .95 var(--font-grotesk)` | Typography / Scale Token |
| `--ls-mtitle` | `-.06em` | Dimension / Scale Token |
| `--ls-text` | `-.005em` | Typography Ink Token |
| `--ls-head` | `-.02em` | Dimension / Scale Token |
| `--ls-title` | `-.03em` | Dimension / Scale Token |
| `--tt-text` | `none` | Typography Ink Token |
| `--page-x` | `clamp(1rem, 2vw, 2.5rem)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.NavBar-module__aMivtW__bar> — `www-codeofsagar-in`)**:
   - Landmark `<header class="NavBar-module__aMivtW__bar">` (`1372x56px`) hosting `Sagar K. Ghosh — Full-stack Develope` navigation (`H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`), DOM attributes (`data-nav-solid`, `data-lines-anim`, `data-sky="day"`, `data-dot="small"`), and stylesheet rule `host { --color-neutral-900:lab(7.78201% -.0000149012 0) }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Websites That Sell. AI That Never `)**:
   - Landmark `<section class="relative z-10">` presenting display lead `Websites That Sell. AI That Never Sleeps.` and copy excerpt *"I'm Sagar, a web developer. I design and build your website, your"* over `#ffffff` canvas and `#0f0f0f` ink.
3. **Primary Showcase & Content Grid (<section.grain-surface> — `Websites that sell. AI that never `)**:
   - Landmark `<section class="grain-surface home-titles">` rendering section `Websites that sell. AI that never sleeps.` with copy *"That's me, on my third coffee."*, asset references (`space_grotesk_latin_wght_normal-s...`, `space_mono_latin_400_normal-s.p.1...`, `space_mono_latin_700_normal-s.p.0...`, `36s0t0o8ux5as.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.bg-paper> — `S A G A R K . G H O S H`)**:
   - Landmark `<section class="bg-paper">` framing `S A G A R K . G H O S H` and `Get Found. Get Chosen. Get Bought.` (*"on my third coffee."*) with `#eeeae5` surface cards, `#008000` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.codeofsagar.in/`)**:
   - Landmark `<footer class="relative flex">` anchoring `Sagar K. Ghosh — Full-stack Deve` footer links (`H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`), copy *"Let's make it simple."*, and `#eeeeee` structural dividers.
