---
title: "UI & UX Architecture: andreas-vision"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: andreas-vision

## Overview & Design Identity
- **Target**: `andreas-vision` (**Andreas Kruszakin, growth-focused design engineer in Europe**)
- **Production URL**: [https://andreas.vision](https://andreas.vision)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f8f8fa` / `#00aaff`)
- **Summary**: I'm Andreas, a growth-focused design engineer who is design first and builds the system underneath. I make founders' products easy to get...
- **Total Clean CSS Variables Extracted**: `193` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `TRJN DaVinci`
- **Body Font Stack**: `Geist Variable`
- **Monospace / Technical Font Stack**: `Geist Mono Variable`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 132px`, `line-height: 147.84px`, `font-weight: 400`, `letter-spacing: -5.28px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 104.8px`, `line-height: 90.128px`, `font-weight: 500`, `letter-spacing: -1.048px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 21px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 16.2px`, `font-weight: 500`); CSS variables `--font-brand-mono: "Geist Mono Variable", ui-monospace, monospace`, `--label-icon-selected: inherit`, `--labels: 0`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f8fa` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00aaff` | `var(--link-visited)` in `:root` |
| **Secondary / Muted Copy** | `#808080` | live computed `hr` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e4` | `var(--line-hover)` in `:root` (`rgba(0, 0, 0, 0.09)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Typography / Scale Token |
| `--font-brand` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Brand / Palette Token |
| `--font-brand-serif` | `"Newsreader Variable", Georgia, serif` | Brand / Palette Token |
| `--font-brand-mono` | `"Geist Mono Variable", ui-monospace, monospace` | Brand / Palette Token |
| `--font-site` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Typography / Scale Token |
| `--font-site-highlight` | `"TRJN DaVinci", "Newsreader Variable", Georgia, serif` | Canvas / Surface Token |
| `--control-2xs` | `20px` | Dimension / Scale Token |
| `--control-xs` | `24px` | Dimension / Scale Token |
| `--control-sm` | `28px` | Dimension / Scale Token |
| `--control-md` | `32px` | Dimension / Scale Token |
| `--control-lg` | `36px` | Dimension / Scale Token |
| `--radius-control-sm` | `4px` | Elevation / Border Token |
| `--radius-control` | `8px` | Elevation / Border Token |
| `--radius-surface` | `12px` | Canvas / Surface Token |
| `--radius-card` | `16px` | Elevation / Border Token |
| `--focus-ring-width` | `1.5px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top> — `andreas-vision`)**:
   - Landmark `<header class="top">` (`688x26px`) hosting `Andreas Kruszakin, growth-focused de` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-selection-ink`, `data-emotion="css-global"`, `data-s`, `data-emotion="css-global"`), and stylesheet rule `root { height: 100%; margin: 0; }`.
2. **Hero Stage & Focal Lead (<section.e5sioty0> — `Designer who ships with vision Des`)**:
   - Landmark `<section class="e5sioty0 css-8jf4oe">` presenting display lead `Designer who ships with vision Design Engineer wh...` and copy excerpt *"I'm Andreas, making precise, joyful interfaces and the tools to b"* over `#f8f8fa` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.swap> — `Work`)**:
   - Landmark `<section class="swap css-1eowax1">` rendering section `Work` with copy *"Designer who ships with vision"*, asset references (`llms.txt`, `icon-192.png`, `favicon.ico`, `favicon.svg`), and grid rule `html { background: fff; }`.
4. **Interactive Detail & Feature Matrix (<section.css-1yyyvev> — `Designer who ships with vision`)**:
   - Landmark `<section class="swap css-1yyyvev">` framing `Designer who ships with vision` and `Design Engineer who ships growth` (*"Design Engineer who ships growth"*) with `#ffffff` surface cards, `#00aaff` accents, and `header { border-color: #e2e2e4; }`.
5. **Colophon & Global Directory Footer (<footer.css-za9d9j> — `https://andreas.vision`)**:
   - Landmark `<footer class="css-za9d9j e154gxt60">` anchoring `Andreas Kruszakin, growth-focuse` footer links (`Overview · Index · Archive · About · Contact`), copy *"Cheval Inbox Canvas Arrange Share 2. Inbox: crit and variant"*, and `#e2e2e4` structural dividers.
