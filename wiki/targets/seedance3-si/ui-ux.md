---
title: "UI & UX Architecture: seedance3-si"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: seedance3-si

## Overview & Design Identity
- **Target**: `seedance3-si` (**Seedance 3.0 AI Video Generator: Make Videos from References**)
- **Production URL**: [https://seedance3.si/](https://seedance3.si/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#09090b` canvas, `#ffffff` ink, `#d3ff02` accent)
- **Summary**: Try Seedance 3.0 free online. Turn text, images, video clips, and audio into videos with sound. Keep faces the same and edit any part wit...
- **Total Clean CSS Variables Extracted**: `431` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Georgia`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 82.08px`, `line-height: 88.6464px`, `font-weight: 500`, `letter-spacing: -3.6936px`); CSS variables `--font-display: var(--font-home-heading)`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`; rule `h1` (`font-weight: 800`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 600`, `letter-spacing: -1.2px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: "Geist","Geist Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: clamp(16px,1.4vw,18px)`, `letter-spacing: .01em`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#09090b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a0a` | `var(--card-foreground)` in `:root` |
| **Interactive Accent / Highlight** | `#d3ff02` | `var(--theme-primary)` in `:root` |
| **Secondary / Muted Copy** | `#777970` | `var(--menu-muted)` in `:root` |
| **Structural Hairline Border** | `#2c2c32` | `var(--gem-line)` in `:root` |
| **Variable Token (`--primary`)** | `#171717` | `var(--primary)` in `:root` |
| **Variable Token (`--primary-foreground`)** | `#fafafa` | `var(--primary-foreground)` in `:root` |
| **Variable Token (`--secondary`)** | `#f5f5f5` | `var(--secondary)` in `:root` |
| **Variable Token (`--muted-foreground`)** | `#737373` | `var(--muted-foreground)` in `:root` |
| **Variable Token (`--destructive`)** | `#e40014` | `var(--destructive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#0a0a0a` | Typography Ink Token |
| `--card` | `#fff` | Color / Atmospheric Token |
| `--card-foreground` | `#0a0a0a` | Typography Ink Token |
| `--popover` | `#fff` | Color / Atmospheric Token |
| `--popover-foreground` | `#0a0a0a` | Typography Ink Token |
| `--primary` | `#171717` | Brand / Palette Token |
| `--primary-foreground` | `#fafafa` | Typography Ink Token |
| `--secondary` | `#f5f5f5` | Brand / Palette Token |
| `--secondary-foreground` | `#171717` | Typography Ink Token |
| `--muted` | `#f5f5f5` | Color / Atmospheric Token |
| `--muted-foreground` | `#737373` | Typography Ink Token |
| `--accent` | `#f5f5f5` | Brand / Palette Token |
| `--accent-foreground` | `#171717` | Typography Ink Token |
| `--destructive` | `#e40014` | Color / Atmospheric Token |
| `--destructive-foreground` | `#fff` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.tool-header> — `seedance3-si`)**:
   - Landmark `<header class="tool-header inset-x-0">` (`1440x57px`) hosting `Seedance 3.0 AI Video Generator: Mak` navigation (`Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.navigation-module__C5Mk9a__image... { width:min(380px,100vw - 32px) }`.
2. **Hero Stage & Focal Lead (<section.theme-gold> — `Seedance 3.0 AI Video Generator`)**:
   - Landmark `<section class="theme-gold">` presenting display lead `Seedance 3.0 AI Video Generator` and copy excerpt *"Seedance 3.0 Launch Sale: Get 50% off all yearly plans"* over `#09090b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.jsx-b8e54b4bef176a21> — `Seedance 3.0 Features`)**:
   - Landmark `<section class="jsx-b8e54b4bef176a21 generation-panel">` rendering section `Seedance 3.0 Features` with copy *"Create on Seedance 3.0 with an idea or a picture. Make a characte"*, asset references (`logo.png`, `712b6ac0fe98f484.css`, `7697b7c0cef68411.css`, `41592914de078ed4.css`), and grid rule `.navigation-module__C5Mk9a__eyebrow { align-items:center;gap:10px;margin:2px 2px 14px;display:flex }`.
4. **Interactive Detail & Feature Matrix (<section.py-14> — `Multi-Material Input`)**:
   - Landmark `<section class="py-14 text-white">` framing `Multi-Material Input` and `Precise Editing` (*"Click or drag to upload images, videos, or audio"*) with `#0a0a0a` surface cards, `#d3ff02` accents, and `vigation-module__C5Mk9a__eyebrow:... { content:"";background:var(--primary);border-radius:50%;width:5px;height:5px }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://seedance3.si/`)**:
   - Landmark `<footer class="flex">` anchoring `Seedance 3.0 AI Video Generator:` footer links (`Pricing`), copy *"— remaining today / 10"*, and `#2c2c32` structural dividers.
