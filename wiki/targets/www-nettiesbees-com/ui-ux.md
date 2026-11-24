---
title: "UI & UX Architecture: www-nettiesbees-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-nettiesbees-com

## Overview & Design Identity
- **Target**: `www-nettiesbees-com` (**Raw Local Honey in Rochester, MA · Nettie's Bees**)
- **Production URL**: [https://www.nettiesbees.com/](https://www.nettiesbees.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f9f3e3` / `#e4a62f`)
- **Summary**: Raw, unfiltered honey from South Coast Massachusetts hives. Visit our self-serve Honey House in Rochester, MA for seasonal honey, hot hon...
- **Total Clean CSS Variables Extracted**: `77` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Boska`
- **Body Font Stack**: `General Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 128px`, `line-height: 115.2px`, `font-weight: 500`, `letter-spacing: -3.84px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.48px`, `line-height: 63.504px`, `font-weight: 500`, `letter-spacing: -1.2096px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9f3e3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#2b1a0e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2b1a0e` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#e4a62f` | `var(--color-amber)` in `:root` |
| **Secondary / Muted Copy** | `#2b1a0e` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dad2c3` | `var(--color-line)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--t1` | `.22s` | Motion / Timing Token |
| `--t2` | `.6s` | Motion / Timing Token |
| `--t3` | `1.2s` | Motion / Timing Token |
| `--bg` | `var(--color-cream)` | Canvas / Surface Token |
| `--fg` | `var(--color-ink)` | Typography Ink Token |
| `--line` | `var(--color-line)` | Design System Custom Token |
| `--accent` | `var(--color-amber)` | Brand / Palette Token |
| `--on-accent` | `var(--color-ink)` | Brand / Palette Token |
| `--pop` | `var(--color-cranberry)` | Design System Custom Token |
| `--focus` | `var(--color-ink)` | Design System Custom Token |
| `--honey` | `var(--color-amber)` | Design System Custom Token |
| `--gap` | `1.5rem` | Layout / Spatial Grid Token |
| `--lit` | `1` | Design System Custom Token |
| `--font-sans` | `"General Sans", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `www-nettiesbees-com`)**:
   - Landmark `<header class="top-0 z-40">` (`1440x69px`) hosting `Raw Local Honey in Rochester, MA · N` navigation (`Shop · Honey Journal · Swarm retrieval · Pollination · Events`), DOM attributes (`data-season="fall"`, `data-hour="13"`, `data-month="10"`, `data-daypart="day"`), and stylesheet rule `webkit-slider-runnable-track { background:0 0;height:100% }`.
2. **Hero Stage & Focal Lead (<section.hairline> — `Discover local honey`)**:
   - Landmark `<section class="hairline overflow-hidden">` presenting display lead `Discover local honey` and copy excerpt *"From hive to home, every jar of our raw honey captures the unique"* over `#f9f3e3` canvas and `#2b1a0e` ink.
3. **Primary Showcase & Content Grid (<section.stockists> — `Also on the shelf at`)**:
   - Landmark `<section class="stockists border-y">` rendering section `Also on the shelf at` with copy *"Cervelli's Farmstand (seasonal)"*, asset references (`favicon.png`, `apple-touch-icon.png`, `sitemap-index.xml`, `rss.xml`), and grid rule `moz-range-track { background:0 0;height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `From hive to home`)**:
   - Landmark `<section class="section">` framing `From hive to home` and `From light to dark` (*"The Nook Coffee Shop"*) with `#2b1a0e` surface cards, `#e4a62f` accents, and `focus-visible { outline:2px solid var(--color-ink);outline-offset:4px }`.
5. **Colophon & Global Directory Footer (<footer.theme-invert> — `https://www.nettiesbees.com/`)**:
   - Landmark `<footer class="theme-invert relative">` anchoring `Raw Local Honey in Rochester, MA` footer links (`Shop · Honey Journal · Swarm retrieval · Pollination · Events`), copy *"Dartmouth Total Fitness"*, and `#dad2c3` structural dividers.
