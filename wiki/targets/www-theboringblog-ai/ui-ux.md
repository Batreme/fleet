---
title: "UI & UX Architecture: www-theboringblog-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-theboringblog-ai

## Overview & Design Identity
- **Target**: `www-theboringblog-ai` (**The Boring Blog — art, engineering and AI**)
- **Production URL**: [http://www.theboringblog.ai/](http://www.theboringblog.ai/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)
- **Summary**: Boring stuff about art, engineering, AI, and the little things that rarely make noise.
- **Total Clean CSS Variables Extracted**: `427` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Fraunces`
- **Body Font Stack**: `GeistSans`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 84.8px`, `line-height: 84.8px`, `font-weight: 400`, `letter-spacing: -2.3744px`); CSS variables `--font-display: "Fraunces", "Fraunces Fallback"`, `--text-display-sm: 1.75rem`, `--text-display-sm--line-height: 1.15`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: clamp(1.7rem,5vw,2.7rem)`, `line-height: 1.06`, `letter-spacing: -.024em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: -0.24px`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: 1.6`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: -0.24px`); CSS variables `--font-mono: var(--font-geist-mono), ui-monospace, "SF Mono", "Cascadia Code", monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`; rule `small` (`font-size: inherit`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0b0a06` | `var(--color-ink-950)` in `:root` |
| **Elevated Surface / Card Substrate** | `#faf8f2` | `var(--paper-day)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.track__keys button:active { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#818077` | `var(--color-ink-500)` in `:root` |
| **Structural Hairline Border** | `#ddd9cb` | `var(--line-day)` in `:root` |
| **Variable Token (`--color-context-figure`)** | `#d4d4d4` | `var(--color-context-figure)` in `:root` |
| **Variable Token (`--color-avatar-pink`)** | `#f9c2db` | `var(--color-avatar-pink)` in `:root` |
| **Variable Token (`--color-avatar-pink-text`)** | `#36222b` | `var(--color-avatar-pink-text)` in `:root` |
| **Variable Token (`--color-avatar-purple`)** | `#d7ccfe` | `var(--color-avatar-purple)` in `:root` |
| **Variable Token (`--color-avatar-purple-text`)** | `#2a2538` | `var(--color-avatar-purple-text)` in `:root` |
| **Variable Token (`--color-avatar-red`)** | `#ffc3c1` | `var(--color-avatar-red)` in `:root` |
| **Variable Token (`--color-avatar-red-text`)** | `#382222` | `var(--color-avatar-red-text)` in `:root` |
| **Variable Token (`--color-avatar-blue`)** | `#bcd8f5` | `var(--color-avatar-blue)` in `:root` |
| **Variable Token (`--color-avatar-blue-text`)** | `#1b2a3a` | `var(--color-avatar-blue-text)` in `:root` |
| **Variable Token (`--color-avatar-coral`)** | `#fdc6af` | `var(--color-avatar-coral)` in `:root` |
| **Variable Token (`--color-avatar-coral-text`)** | `#37231a` | `var(--color-avatar-coral-text)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--omnibar-width` | `calc(var(--spacing) * 140)` | Layout / Spatial Grid Token |
| `--omnibar-bar` | `calc(var(--spacing) * 10 + var(--stroke-hairline) * 2)` | Design System Custom Token |
| `--radius-swatch` | `var(--radius-xs)` | Brand / Palette Token |
| `--radius-chrome` | `calc(var(--radius-control) + .25rem)` | Elevation / Border Token |
| `--color-context-figure` | `#d4d4d4` | Typography Ink Token |
| `--lightningcss-light` | `initial` | Canvas / Surface Token |
| `--color-avatar-pink` | `#f9c2db` | Typography Ink Token |
| `--color-avatar-pink-text` | `#36222b` | Typography Ink Token |
| `--color-avatar-purple` | `#d7ccfe` | Brand / Palette Token |
| `--color-avatar-purple-text` | `#2a2538` | Typography Ink Token |
| `--color-avatar-red` | `#ffc3c1` | Brand / Palette Token |
| `--color-avatar-red-text` | `#382222` | Typography Ink Token |
| `--color-avatar-blue` | `#bcd8f5` | Brand / Palette Token |
| `--color-avatar-blue-text` | `#1b2a3a` | Typography Ink Token |
| `--color-avatar-coral` | `#fdc6af` | Brand / Palette Token |
| `--color-avatar-coral-text` | `#37231a` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mast> — `www-theboringblog-ai`)**:
   - Landmark `<header class="mast">` (`1440x97px`) hosting `The Boring Blog — art, engineering a` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `nces_3053e531-module__RZoG-q__cla... { font-family:Fraunces,Fraunces Fallback }`.
2. **Hero Stage & Focal Lead (<section.hero> — `The Boring Blog`)**:
   - Landmark `<section class="hero">` presenting display lead `The Boring Blog` and copy excerpt *"Boring stuff about art, engineering, AI, and the little things th"* over `#ffffff` canvas and `#0b0a06` ink.
3. **Primary Showcase & Content Grid (<section.hero:nth(2)> — `T h e n o t B o r i n g B l o g ?`)**:
   - Landmark `<section class="hero">` rendering section `T h e n o t B o r i n g B l o g ?` with copy *"T h e n o t B o r i n g B l o g ?"*, asset references (`2cu5yowomccdq.css`, `3njp7nmul3k7y.css`, `1g5rc0qzmf3ta.css`, `1l3760h_x0b06.css`), and grid rule `unces_3053e531-module__RZoG-q__va... { --font-display:"Fraunces", "Fraunces Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.hero:nth(3)> — `T h e n o t B o r i n g B l o g ?`)**:
   - Landmark `<section class="hero">` framing `T h e n o t B o r i n g B l o g ?` and `B o r i n g s t u f f a b o u t a r t , e n g i ` (*"B o r i n g s t u f f a b o u t a r t , e n g i n e e r i n g , A"*) with `#faf8f2` surface cards, `#ff0000` accents, and `sans_d5a4f12f-module__7QEr8W__cla... { font-family:GeistSans,GeistSans Fallback }`.
5. **Colophon & Global Directory Footer (<footer.hero__word> — `http://www.theboringblog.ai/`)**:
   - Landmark `<footer class="hero__word">` anchoring `The Boring Blog — art, engineeri` footer links (`Overview · Index · Archive · About · Contact`), copy *"e n g i n e e r i n g ,"*, and `#ddd9cb` structural dividers.
