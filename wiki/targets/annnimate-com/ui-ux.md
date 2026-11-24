---
title: "UI & UX Architecture: annnimate-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: annnimate-com

## Overview & Design Identity
- **Target**: `annnimate-com` (**GSAP Motion Components for React & Vue · Annnimate**)
- **Production URL**: [https://annnimate.com](https://annnimate.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#141314` / `#fb460d`)
- **Summary**: Production GSAP motion components for React and Vue. Every component is built to the standard we ship for real brands. By Good Fella.
- **Total Clean CSS Variables Extracted**: `453` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `aktivGrotesk`
- **Body Font Stack**: `aktivGrotesk`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 59.298px`, `line-height: 59.298px`, `font-weight: 500`, `letter-spacing: -2.07543px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `,.h1` (`font-size: var(--font-size-4xl)`, `line-height: 1.2`, `letter-spacing: -.04em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 37.9102px`, `line-height: 42.649px`, `font-weight: 500`, `letter-spacing: -1.51641px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `,.h2` (`font-size: var(--font-size-2xl)`, `line-height: 1.2`, `letter-spacing: -.03em`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-size-base: clamp(1rem,.95rem + .25vw,1.125rem)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-geist-mono),"SF Mono",Monaco,"Cascadia Code",monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#141314` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#eeeeee` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#171717` | `var(--card-foreground)` in `:root` |
| **Interactive Accent / Highlight** | `#fb460d` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#696869` | `var(--foreground-muted)` in `:root` |
| **Structural Hairline Border** | `#121112` | `var(--border-muted)` in `:root` (`0000001a`) |
| **Variable Token (`--background`)** | `#fafafa` | `var(--background)` in `:root` |
| **Variable Token (`--card`)** | `#ffffff` | `var(--card)` in `:root` |
| **Variable Token (`--secondary`)** | `#f0f0f0` | `var(--secondary)` in `:root` |
| **Variable Token (`--secondary-muted`)** | `#e5e5e5` | `var(--secondary-muted)` in `:root` |
| **Variable Token (`--secondary-muted-foreground`)** | `#404040` | `var(--secondary-muted-foreground)` in `:root` |
| **Variable Token (`--surface`)** | `#ebebeb` | `var(--surface)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--v2-header-h` | `72px` | Layout / Spatial Grid Token |
| `--v2-header-gap` | `16px` | Layout / Spatial Grid Token |
| `--v2-sticky-top` | `24px` | Dimension / Scale Token |
| `--radius` | `.375rem` | Elevation / Border Token |
| `--background` | `#fafafa` | Canvas / Surface Token |
| `--foreground` | `#171717` | Typography Ink Token |
| `--card` | `#fff` | Color / Atmospheric Token |
| `--card-foreground` | `#171717` | Typography Ink Token |
| `--popover` | `#fff` | Color / Atmospheric Token |
| `--popover-foreground` | `#171717` | Typography Ink Token |
| `--secondary` | `#f0f0f0` | Brand / Palette Token |
| `--secondary-foreground` | `#171717` | Typography Ink Token |
| `--secondary-muted` | `#e5e5e5` | Brand / Palette Token |
| `--secondary-muted-foreground` | `#404040` | Typography Ink Token |
| `--surface` | `#ebebeb` | Canvas / Surface Token |
| `--surface-foreground` | `#171717` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.v2-header> — `annnimate-com`)**:
   - Landmark `<header class="v2-header inset-x-0">` (`1440x72px`) hosting `GSAP Motion Components for React & V` navigation (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `host { --glass-primary:color-mix(in srgb,var(--color-muted)70%,transparent) }`.
2. **Hero Stage & Focal Lead (<section.bg-background> — `Give any site award‑level animatio`)**:
   - Landmark `<section class="bg-background pt-112">` presenting display lead `Give any site award‑level animation in minutes.` and copy excerpt *"Give any site award‑level"* over `#141314` canvas and `#eeeeee` ink.
3. **Primary Showcase & Content Grid (<section.pt-64> — `Try it before you copy it.`)**:
   - Landmark `<section class="bg-background pt-64">` rendering section `Try it before you copy it.` with copy *"animation in minutes."*, asset references (`teaser-poster.jpg`, `edoardo_avatar.avif`, `lukas_avatar.avif`, `matthew_avatar.avif`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.py-64> — `Client-ready the moment you paste `)**:
   - Landmark `<section class="bg-background py-64">` framing `Client-ready the moment you paste it.` and `Motion that wins the pitch` (*"The same GSAP animations we build for Coca-Cola and Powerade, rea"*) with `#171717` surface cards, `#fb460d` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.annnimate-footer> — `https://annnimate.com`)**:
   - Landmark `<footer class="annnimate-footer bg-background">` anchoring `GSAP Motion Components for React` footer links (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), copy *"Get access -25% Get access -25%"*, and `#121112` structural dividers.
