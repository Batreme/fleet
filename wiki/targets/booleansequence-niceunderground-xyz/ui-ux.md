---
title: "UI & UX Architecture: booleansequence-niceunderground-xyz"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: booleansequence-niceunderground-xyz

## Overview & Design Identity
- **Target**: `booleansequence-niceunderground-xyz` (**booleanSequence · generative art by niceunderground**)
- **Production URL**: [https://booleansequence.niceunderground.xyz/](https://booleansequence.niceunderground.xyz/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)
- **Summary**: booleanSequence by niceunderground: generative visuals built on two values and nothing else. A modern yin and yang of contrasts that swap...
- **Total Clean CSS Variables Extracted**: `10` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 196.663px`, `line-height: 157.33px`, `font-weight: 800`, `letter-spacing: -10.8165px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 518.4px`, `line-height: 383.616px`, `font-weight: 900`, `letter-spacing: -7.776px`); CSS variables `--rule-h2: clamp(2rem, 4.6vw, 5.6rem)`; rule `.h2` (`font-size: clamp(2.1rem,5vw,6rem)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); rule `p` (`font-size: clamp(15px,1.05vw,17px)`, `line-height: 1.4`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0000ff` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `var(--err)` in `:root` |
| **Secondary / Muted Copy** | `#0000ff` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#0000ff` | hairline divider derived from secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--err` | `#ff0000` | Color / Atmospheric Token |
| `--fd` | `"Archivo", "Helvetica Neue", Arial, sans-serif` | Dimension / Scale Token |
| `--fm` | `"JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace` | Design System Custom Token |
| `--pad` | `clamp(16px, 2.2vw, 40px)` | Layout / Spatial Grid Token |
| `--hud` | `clamp(30px, 2.4vw, 38px)` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(.7, 0, .2, 1)` | Motion / Easing Token |
| `--wp` | `.1em` | Dimension / Scale Token |
| `--rule-h2` | `clamp(2rem, 4.6vw, 5.6rem)` | Typography / Scale Token |
| `--pt` | `#0000ff` | Color / Atmospheric Token |
| `--pf` | `#ffffff` | Color / Atmospheric Token |
| `--booleansequence--bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--booleansequence--ink` | `#0000ff` | Primary Typography Ink (computed-derived) |
| `--booleansequence--surface` | `#0000ff` | Surface Substrate (computed-derived) |
| `--booleansequence--accent` | `#ff0000` | Interactive Accent (computed-derived) |
| `--booleansequence--muted` | `#0000ff` | Secondary Ink (computed-derived) |
| `--booleansequence--border` | `#0000ff` | Structural Border (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hud> — `booleansequence-niceunderground-xyz`)**:
   - Landmark `<header class="hud">` (`1377x35px`) hosting `booleanSequence · generative art by ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-live`, `data-magnetic`, `data-set="plus"`, `data-set="bin"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `boolean Sequence`)**:
   - Landmark `<section class="hero">` presenting display lead `boolean Sequence` and copy excerpt *"niceunderground generative visuals"* over `#ffffff` canvas and `#0000ff` ink.
3. **Primary Showcase & Content Grid (<section.statement> — `b o o l e a n S e q u e n c e`)**:
   - Landmark `<section class="statement">` rendering section `b o o l e a n S e q u e n c e` with copy *"generative visuals"*, asset references (`llms.txt`, `favicon.svg`, `favicon-32.png`, `favicon-48.png`), and grid rule `html { -webkit-text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.above> — `Seen from above, it looks like a s`)**:
   - Landmark `<section class="above">` framing `Seen from above, it looks like a society.` and `One rule, four verbs.` (*"A modern yin and yang. Two values, nothing else."*) with `#0000ff` surface cards, `#ff0000` accents, and `html.lenis body { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://booleansequence.niceunderground.xyz/`)**:
   - Landmark `<footer class="foot">` anchoring `booleanSequence · generative art` footer links (`Overview · Index · Archive · About · Contact`), copy *"click the field to send a wave through it tap the field to s"*, and `#0000ff` structural dividers.
