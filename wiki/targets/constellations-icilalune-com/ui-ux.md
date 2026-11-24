---
title: "UI & UX Architecture: constellations-icilalune-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: constellations-icilalune-com

## Overview & Design Identity
- **Target**: `constellations-icilalune-com` (**Constellation(s) — Immersive virtual 3D art exhibitions**)
- **Production URL**: [https://constellations.icilalune.com/](https://constellations.icilalune.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×3312px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f8f8` canvas, `#111111` ink, `#ec3013` accent)
- **Summary**: Immersive virtual galleries: step into the worlds of AG Z, David Bartus, Palash Bag, Jonas Togo, Laura Meinhardt, François Glineur, Adam...
- **Total Clean CSS Variables Extracted**: `48` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Arimo`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 100.8px`, `line-height: 92.736px`, `font-weight: 800`, `letter-spacing: -3.024px`); rule `h1` (`font-size: 42px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 56px`, `line-height: 53.2px`, `font-weight: 800`, `letter-spacing: -1.12px`); rule `h2` (`font-size: 32px`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 23.25px`, `font-weight: 400`); CSS variables `--font-body: "Archivo", system-ui, sans-serif`; rule `body` (`font-size: 15px`, `line-height: 1.55`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 23.25px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f8f8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111111` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f2f2` | `var(--color-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ec3013` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#201e1d` | `var(--color-text)` in `:root` |
| **Structural Hairline Border** | `#201e1d` | `var(--color-divider)` in `:root` |
| **Variable Token (`--color-surface`)** | `#eae9e9` | `var(--color-surface)` in `:root` |
| **Variable Token (`--color-accent-2`)** | `#e15b47` | `var(--color-accent-2)` in `:root` |
| **Variable Token (`--color-neutral-100`)** | `#f8f4f4` | `var(--color-neutral-100)` in `:root` |
| **Variable Token (`--color-neutral-200`)** | `#eae7e7` | `var(--color-neutral-200)` in `:root` |
| **Variable Token (`--color-neutral-300`)** | `#d7d3d3` | `var(--color-neutral-300)` in `:root` |
| **Variable Token (`--color-neutral-400`)** | `#bab6b6` | `var(--color-neutral-400)` in `:root` |
| **Variable Token (`--color-neutral-500`)** | `#9b9797` | `var(--color-neutral-500)` in `:root` |
| **Variable Token (`--color-neutral-600`)** | `#7d7979` | `var(--color-neutral-600)` in `:root` |
| **Variable Token (`--color-neutral-700`)** | `#605d5d` | `var(--color-neutral-700)` in `:root` |
| **Variable Token (`--color-neutral-800`)** | `#444141` | `var(--color-neutral-800)` in `:root` |
| **Variable Token (`--color-neutral-900`)** | `#2d2b2b` | `var(--color-neutral-900)` in `:root` |
| **Variable Token (`--color-accent-100`)** | `#fff2ef` | `var(--color-accent-100)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#f3f2f2` | Canvas / Surface Token |
| `--color-surface` | `#eae9e9` | Canvas / Surface Token |
| `--color-text` | `#201e1d` | Typography Ink Token |
| `--color-accent` | `#ec3013` | Brand / Palette Token |
| `--color-accent-2` | `#e15b47` | Brand / Palette Token |
| `--color-divider` | `color-mix(in srgb, #201e1d 40%, transparent)` | Brand / Palette Token |
| `--color-neutral-100` | `#f8f4f4` | Brand / Palette Token |
| `--color-neutral-200` | `#eae7e7` | Brand / Palette Token |
| `--color-neutral-300` | `#d7d3d3` | Brand / Palette Token |
| `--color-neutral-400` | `#bab6b6` | Brand / Palette Token |
| `--color-neutral-500` | `#9b9797` | Brand / Palette Token |
| `--color-neutral-600` | `#7d7979` | Brand / Palette Token |
| `--color-neutral-700` | `#605d5d` | Brand / Palette Token |
| `--color-neutral-800` | `#444141` | Brand / Palette Token |
| `--color-neutral-900` | `#2d2b2b` | Brand / Palette Token |
| `--color-accent-100` | `#fff2ef` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sc-host> — `constellations-icilalune-com`)**:
   - Landmark `<header class="sc-host">` (`1440px`) hosting `Constellation(s) — Immersive virtual` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-dc-tpl="1"`, `data-dc-tpl="2"`, `data-dc-tpl="3"`, `data-sc-name="Root"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.sc-interp> — `Artists`)**:
   - Landmark `<section class="sc-interp">` presenting display lead `Artists` and copy excerpt *"Immersive virtual galleries: step into the worlds of AG Z, David "* over `#f8f8f8` canvas and `#111111` ink.
3. **Primary Showcase & Content Grid (<section.scp0> — `Immersive virtual galleries: step `)**:
   - Landmark `<section class="scp0">` rendering section `Immersive virtual galleries: step into the world` with copy *"AG Z — Ten Thousand Li · Travel and street photography, China"*, asset references (`manifest.webmanifest`, `favicon.svg`, `favicon-32.png`, `favicon-16.png`), and grid rule `body { background: var(--color-bg); color: var(--color-text); font-family: var(... }`.
4. **Interactive Detail & Feature Matrix (<section.scp1> — `AG Z — Ten Thousand Li · Travel an`)**:
   - Landmark `<section class="scp1">` framing `AG Z — Ten Thousand Li · Travel and street photo` and `David Bartus — From Above · Landscape and drone ` (*"David Bartus — From Above · Landscape and drone photography, Hung"*) with `#f3f2f2` surface cards, `#ec3013` accents, and `h4 { font-family: var(--font-heading); font-weight: var(--font-heading-weight); }`.
5. **Colophon & Global Directory Footer (<footer.scp2> — `https://constellations.icilalune.com/`)**:
   - Landmark `<footer class="scp2">` anchoring `Constellation(s) — Immersive vir` footer links (`Overview · Index · Archive · About · Contact`), copy *"Palash Bag — Still Water · Macro photography, India"*, and `#201e1d` structural dividers.
