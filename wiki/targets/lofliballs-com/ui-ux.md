---
title: "UI & UX Architecture: lofliballs-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lofliballs-com

## Overview & Design Identity
- **Target**: `lofliballs-com` (**LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli**)
- **Production URL**: [http://lofliballs.com](http://lofliballs.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fafeff` / `#f4da40`)
- **Summary**: LoFli Balls are weighted training tools with emulated stitching to mimic the feel of a real ball. Flying about half the distance of a sta...
- **Total Clean CSS Variables Extracted**: `196` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Alumni Sans`
- **Body Font Stack**: `Assistant`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 259.2px`, `line-height: 168.48px`, `font-weight: 700`, `letter-spacing: -7.776px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 63.36px`, `line-height: 57.024px`, `font-weight: 900`, `letter-spacing: -2.5344px`); rule `h2` (`font-size: calc(var(--kl-reviews-reviews...`, `line-height: 122%`, `font-weight: calc(var(--kl...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--gw-ball-body: var(--bg-brand)`, `--font-body: Assistant, sans-serif`; rule `p` (`font-size: medium`, `line-height: normal`, `letter-spacing: normal`, `font-weight: normal`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fafeff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#101820` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--jdgm-snippet-card-color)` in `:root` |
| **Interactive Accent / Highlight** | `#f4da40` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#7b7b7b` | `var(--jdgm-snippet-lighter-text-color)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `.gw-path__reveal { stroke: #ffffff }` |
| **Variable Token (`--color-yellow-5`)** | `#fdfbee` | `var(--color-yellow-5)` in `:root` |
| **Variable Token (`--color-yellow-50`)** | `#f8f4d9` | `var(--color-yellow-50)` in `:root` |
| **Variable Token (`--color-yellow-100`)** | `#f6eec2` | `var(--color-yellow-100)` in `:root` |
| **Variable Token (`--color-yellow-200`)** | `#f5e9a9` | `var(--color-yellow-200)` in `:root` |
| **Variable Token (`--color-yellow-300`)** | `#f4e48d` | `var(--color-yellow-300)` in `:root` |
| **Variable Token (`--color-yellow-400`)** | `#f4df6c` | `var(--color-yellow-400)` in `:root` |
| **Variable Token (`--color-yellow-600`)** | `#c9940d` | `var(--color-yellow-600)` in `:root` |
| **Variable Token (`--color-yellow-700`)** | `#8e5a0b` | `var(--color-yellow-700)` in `:root` |
| **Variable Token (`--color-yellow-800`)** | `#5d3309` | `var(--color-yellow-800)` in `:root` |
| **Variable Token (`--color-yellow-900`)** | `#361c08` | `var(--color-yellow-900)` in `:root` |
| **Variable Token (`--color-cyan-5`)** | `#f1fdff` | `var(--color-cyan-5)` in `:root` |
| **Variable Token (`--color-cyan-50`)** | `#d4edf5` | `var(--color-cyan-50)` in `:root` |
| **Variable Token (`--color-cyan-100`)** | `#b8e2ef` | `var(--color-cyan-100)` in `:root` |
| **Variable Token (`--color-cyan-200`)** | `#9bd8ea` | `var(--color-cyan-200)` in `:root` |
| **Variable Token (`--color-cyan-300`)** | `#7bcee7` | `var(--color-cyan-300)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-yellow-5` | `#FDFBEE` | Brand / Palette Token |
| `--color-yellow-50` | `#F8F4D9` | Brand / Palette Token |
| `--color-yellow-100` | `#F6EEC2` | Brand / Palette Token |
| `--color-yellow-200` | `#F5E9A9` | Brand / Palette Token |
| `--color-yellow-300` | `#F4E48D` | Brand / Palette Token |
| `--color-yellow-400` | `#F4DF6C` | Brand / Palette Token |
| `--color-yellow-500` | `#F4DA40` | Brand / Palette Token |
| `--color-yellow-600` | `#C9940D` | Brand / Palette Token |
| `--color-yellow-700` | `#8E5A0B` | Brand / Palette Token |
| `--color-yellow-800` | `#5D3309` | Brand / Palette Token |
| `--color-yellow-900` | `#361C08` | Brand / Palette Token |
| `--color-cyan-5` | `#F1FDFF` | Brand / Palette Token |
| `--color-cyan-50` | `#D4EDF5` | Brand / Palette Token |
| `--color-cyan-100` | `#B8E2EF` | Brand / Palette Token |
| `--color-cyan-200` | `#9BD8EA` | Brand / Palette Token |
| `--color-cyan-300` | `#7BCEE7` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.gw-header> — `lofliballs-com`)**:
   - Landmark `<header class="gw-header gw-header--dark">` (`1440x65px`) hosting `LoFli Balls—Innovative Training Tool` navigation (`Shop · Shop All · LoFli Baseball · LoFli Softball · About`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="77292208214"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `SWING HARD FLY LOW`)**:
   - Landmark `<section class="shopify-section">` presenting display lead `SWING HARD FLY LOW` and copy excerpt *"HITS LIKE A REAL BALL, BUT TRAVELS ABOUT HALF AS FAR."* over `#fafeff` canvas and `#101820` ink.
3. **Primary Showcase & Content Grid (<section.gw-hero> — `Swing hard Fly low`)**:
   - Landmark `<section class="gw-hero color-scheme-1">` rendering section `Swing hard Fly low` with copy *"Hits like a real ball, but travels about half as far."*, asset references (`destination`, `1129077949490951`, `fbevents.js`, `lofli-favicon.png`), and grid rule `.gw-type-h1 { font-size:calc(1rem * var(--type-scale) * var(--type-scale) * var(--type... }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section:nth(2)> — `Less Chasing. More Hitting.`)**:
   - Landmark `<section class="shopify-section">` framing `Less Chasing. More Hitting.` and `Made For The Whole Game.` (*"We built the LoFli ball to fly like a real baseball when thrown a"*) with `#ffffff` surface cards, `#f4da40` accents, and `.gw-type-h2 { font-size:calc(1rem * var(--type-scale) * var(--type-scale)) }`.
5. **Colophon & Global Directory Footer (<footer.gw-footer> — `http://lofliballs.com`)**:
   - Landmark `<footer class="gw-footer gw-footer--black">` anchoring `LoFli Balls—Innovative Training ` footer links (`Shop · Shop All · LoFli Baseball · LoFli Softball · About`), copy *"Not just for hitting. LoFli has the weight of a real ball, w"*, and `#ffffff` structural dividers.
