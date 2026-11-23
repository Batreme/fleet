---
title: "UI & UX Architecture: annnimate-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: annnimate-com

## Overview & Design Identity
- **Target**: `annnimate-com` (**GSAP Motion Components for React & Vue · Annnimate**)
- **Production URL**: [https://annnimate.com](https://annnimate.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#b3fca0` / `#ca4417`)
- **Summary**: Production GSAP motion components for React and Vue. Every component is built to the standard we ship for real brands. By Good Fella.
- **Total Clean CSS Variables Extracted**: `453` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `geistSans`
- **Body Font Stack**: `geistSans Fallback`
- **Monospace / Technical Font Stack**: `geistMono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `,.h1` (`font-size: var(--font-size-4xl)`, `line-height: 1.2`, `letter-spacing: -.04em`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `,.h2` (`font-size: var(--font-size-2xl)`, `line-height: 1.2`, `letter-spacing: -.03em`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-size-base: clamp(1rem,.95rem + .25vw,1.125rem)`
- **Metadata & Labels**: CSS variables `--font-geist-mono: "geistMono", "geistMono Fallback"`, `--ga-label: clamp(18px, 1.4vw, 28px)`, `--font-mono: var(--font-geist-mono),"SF Mono",Monaco,"Cascadia Code",monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#b3fca0` | live computed `meta-theme-color` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | `var(--foreground)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f2f2ef` | `var(--ga-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ca4417` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#696869` | `var(--foreground-muted)` in `:root` |
| **Structural Hairline Border** | `#d4d4d4` | `var(--surface-border)` in `:root` |
| **Variable Token (`--ga-tile`)** | `#fafaf8` | `var(--ga-tile)` in `:root` |
| **Variable Token (`--ga-tile-2`)** | `#e8e8e4` | `var(--ga-tile-2)` in `:root` |
| **Variable Token (`--ga-fg`)** | `#141314` | `var(--ga-fg)` in `:root` |
| **Variable Token (`--ga-fg-soft`)** | `#9a9a96` | `var(--ga-fg-soft)` in `:root` |
| **Variable Token (`--ga-focus`)** | `#101010` | `var(--ga-focus)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist-sans` | `"geistSans", "geistSans Fallback"` | Typography / Scale Token |
| `--font-geist-mono` | `"geistMono", "geistMono Fallback"` | Typography / Scale Token |
| `--font-aktiv` | `"aktivGrotesk", "aktivGrotesk Fallback"` | Typography / Scale Token |
| `--font-handwritten` | `"shadowsIntoLight", "shadowsIntoLight Fallback"` | Typography / Scale Token |
| `--ga-bg` | `#f2f2ef` | Canvas / Surface Token |
| `--ga-tile` | `#fafaf8` | Color / Atmospheric Token |
| `--ga-tile-2` | `#e8e8e4` | Color / Atmospheric Token |
| `--ga-ink` | `#fafaf8` | Typography Ink Token |
| `--ga-fg` | `#141314` | Typography Ink Token |
| `--ga-fg-soft` | `#9a9a96` | Typography Ink Token |
| `--ga-fg-dim` | `#9a9a96` | Typography Ink Token |
| `--ga-focus` | `#1010104d` | Color / Atmospheric Token |
| `--ga-margin` | `clamp(20px, 2.8vw, 48px)` | Layout / Spatial Grid Token |
| `--ga-gutter` | `clamp(12px, 1.4vw, 24px)` | Layout / Spatial Grid Token |
| `--ga-label` | `clamp(18px, 1.4vw, 28px)` | Dimension / Scale Token |
| `--angle` | `0deg` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.v2-header> — `annnimate-com`)**:
   - Landmark `<header class="v2-header inset-x-0">` (`1440px`) hosting `GSAP Motion Components for React & V` navigation (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.QRhTIa_className { font-family:geistSans,geistSans Fallback }`.
2. **Hero Stage & Focal Lead (<section.bg-background> — `Give any site award‑level animatio`)**:
   - Landmark `<section class="bg-background pt-112">` presenting display lead `Give any site award‑level animation in minutes.` and copy excerpt *"Give any site award‑level"* over `#b3fca0` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.pt-64> — `Try it before you copy it.`)**:
   - Landmark `<section class="bg-background pt-64">` rendering section `Try it before you copy it.` with copy *"animation in minutes."*, asset references (`teaser-poster.jpg`, `edoardo_avatar.avif`, `lukas_avatar.avif`, `matthew_avatar.avif`), and grid rule `.QRhTIa_variable { --font-geist-sans:"geistSans", "geistSans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-64> — `Client-ready the moment you paste `)**:
   - Landmark `<section class="bg-background py-64">` framing `Client-ready the moment you paste it.` and `Motion that wins the pitch` (*"The same GSAP animations we build for Coca-Cola and Powerade, rea"*) with `#f2f2ef` surface cards, `#ca4417` accents, and `.mNpjDG_className { font-family:geistMono,geistMono Fallback }`.
5. **Colophon & Global Directory Footer (<footer.annnimate-footer> — `https://annnimate.com`)**:
   - Landmark `<footer class="annnimate-footer bg-background">` anchoring `GSAP Motion Components for React` footer links (`Library Library · Kits Kits New · Learn Learn · Docs Docs · Pricing Pricing`), copy *"Get access -25% Get access -25%"*, and `#d4d4d4` structural dividers.
