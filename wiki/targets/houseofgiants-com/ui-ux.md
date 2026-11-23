---
title: "UI & UX Architecture: houseofgiants-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: houseofgiants-com

## Overview & Design Identity
- **Target**: `houseofgiants-com` (**House of Giants · Product engineering partner**)
- **Production URL**: [https://houseofgiants.com](https://houseofgiants.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#000000` accent)
- **Summary**: House of Giants designs and builds software products. We help you work out what to build, build it, and keep improving it.
- **Total Clean CSS Variables Extracted**: `188` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo Black`
- **Body Font Stack**: `IBM Plex Sans`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 111.387px`, `line-height: 98.021px`, `font-weight: 400`, `letter-spacing: -4.4555px`); CSS variables `--font-hog-display: "Newsreader", Georgia, serif`, `--text-5xl: 3rem`, `--text-5xl--line-height: 1`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 70.4px`, `font-weight: 400`, `letter-spacing: -3.4px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: var(--text-title-sm)`, `line-height: var(--text-title-sm--...`, `letter-spacing: var(--text-title-sm--...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-hog-body: "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-hog-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | `body` default contrast ink (`#000000`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | transparent/inherited card surface over live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#000000` | `body` default contrast ink (`#000000`) |
| **Secondary / Muted Copy** | `#000000` | secondary opacity step of `body` default contrast ink (`#000000`) |
| **Structural Hairline Border** | `#000000` | hairline divider derived from secondary opacity step of `body` default contrast ink (`#000000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--asset-logo-full` | `url(/brand/logo.svg)` | Design System Custom Token |
| `--asset-logo-mark` | `url(/brand/g.svg)` | Design System Custom Token |
| `--asset-logo-word` | `url(/brand/giants.svg)` | Design System Custom Token |
| `--asset-menu` | `url(/brand/menu.svg)` | Design System Custom Token |
| `--asset-work-cursor` | `url(/brand/subtract-cursor.svg)` | Design System Custom Token |
| `--font-hog-display` | `"Newsreader", Georgia, serif` | Typography / Scale Token |
| `--font-hog-impact` | `"Archivo Black", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-hog-body` | `"IBM Plex Sans", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-hog-eyebrow` | `"BN Blacklettra", serif` | Typography / Scale Token |
| `--paper` | `oklch(94.54% .0499 79.86)` | Canvas / Surface Token |
| `--surface` | `oklch(95.6% .043 82)` | Canvas / Surface Token |
| `--ink` | `oklch(24.2% .043 128)` | Typography Ink Token |
| `--ink-soft` | `oklch(48.5% .036 126)` | Typography Ink Token |
| `--moss` | `oklch(51.23% .0541 122.49)` | Color / Atmospheric Token |
| `--moss-dark` | `oklch(43.54% .0512 122.64)` | Canvas / Surface Token |
| `--moss-deep` | `oklch(33.03% .031 120.72)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-navigation> — `houseofgiants-com`)**:
   - Landmark `<header class="site-navigation inset-x-0">` (`1440x61px`) hosting `House of Giants · Product engineerin` navigation (`Work · How we decide · Services · Pricing · About`), DOM attributes (`data-precedence="default"`, `data-precedence="default"`, `data-status="active"`, `data-footprint-ready`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `BIG IDEAS. SERIOUS SOFTWARE.`)**:
   - Landmark `<section class="home-hero pt-10">` presenting display lead `BIG IDEAS. SERIOUS SOFTWARE.` and copy excerpt *"We build software, systems and processes for teams that are sick "* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.home-selected-work> — `Big Ideas. Serious Software.`)**:
   - Landmark `<section class="home-selected-work bg-moss">` rendering section `Big Ideas. Serious Software.` with copy *"We've worked with hundreds of amazing brands over the years. Thes"*, asset references (`thing-walk.svg`, `thing-tufts.svg`, `boulder.svg`, `thing-footprint-right.svg`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.home-process> — `The Living Proof`)**:
   - Landmark `<section class="home-process overflow-clip">` framing `The Living Proof` and `Booking system app` (*"PebbleSpaces Booking system app The prototype we inherited was ha"*) with `#ffffff` surface cards, `#000000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://houseofgiants.com`)**:
   - Landmark `<footer class="site-footer">` anchoring `House of Giants · Product engine` footer links (`Work · How we decide · Services · Pricing · About`), copy *"The prototype we inherited was half-built and the first loca"*, and `#000000` structural dividers.
