---
title: "UI & UX Architecture: clipdance-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: clipdance-ai

## Overview & Design Identity
- **Target**: `clipdance-ai` (**Seedance 2.0 - Free AI Video Generator · Text/Image to Video**)
- **Production URL**: [https://clipdance.ai](https://clipdance.ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×855px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#8a6b0d`)
- **Summary**: Create cinematic AI videos with Seedance 2.0. Text-to-video, image-to-video, native audio. The Seedance 2.0 AI video generator. Free to s...
- **Total Clean CSS Variables Extracted**: `287` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `fontInter`
- **Monospace / Technical Font Stack**: `Noto Sans Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 43.2px`, `font-weight: 800`, `letter-spacing: -1px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2 (largest visible desktop heading)` (`font-size: 40px`, `line-height: 1.2`, `font-weight: 600`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-noto-sans-mono)`, `--font-noto-sans-mono: "Noto Sans Mono", "Noto Sans Mono Fallback"`, `--text-xs: .75rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#18181b` | `var(--card-foreground)` in `:root` |
| **Interactive Accent / Highlight** | `#8a6b0d` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#71717a` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#e4e4e7` | `var(--border)` in `:root` |
| **Variable Token (`--background`)** | `#fafafa` | `var(--background)` in `:root` |
| **Variable Token (`--secondary`)** | `#f4f4f5` | `var(--secondary)` in `:root` |
| **Variable Token (`--secondary-foreground`)** | `#27272a` | `var(--secondary-foreground)` in `:root` |
| **Variable Token (`--destructive`)** | `#d92d20` | `var(--destructive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#fafafa` | Canvas / Surface Token |
| `--foreground` | `#18181b` | Typography Ink Token |
| `--card` | `#fff` | Color / Atmospheric Token |
| `--card-foreground` | `#18181b` | Typography Ink Token |
| `--popover` | `#fff` | Color / Atmospheric Token |
| `--popover-foreground` | `#18181b` | Typography Ink Token |
| `--primary` | `#8a6b0d` | Brand / Palette Token |
| `--primary-foreground` | `#fff` | Typography Ink Token |
| `--secondary` | `#f4f4f5` | Brand / Palette Token |
| `--secondary-foreground` | `#27272a` | Typography Ink Token |
| `--muted` | `#f4f4f5` | Color / Atmospheric Token |
| `--muted-foreground` | `#71717a` | Typography Ink Token |
| `--accent` | `#f4f4f5` | Brand / Palette Token |
| `--accent-foreground` | `#8a6b0d` | Typography Ink Token |
| `--destructive` | `#d92d20` | Color / Atmospheric Token |
| `--destructive-foreground` | `#fff` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Persistent Left Sidebar Navigation (<nav.max-w-max> — `206×607px` at `x=13`)**:
   - Fixed/sticky left rail `<nav class="max-w-max flex-1">` (`206px` wide) paired with top bar `<header class="inset-x-0 top-0">` hosting `Seedance 2.0 - Free AI Video G` navigation (`Seedance 2.5 · Blog · Pricing · My Creations`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-state="closed"`, `data-slot="sheet-trigger"`), and rule `nter_a1c1f49b-module__H0XvcG__cla... { font-family:fontInter,fontInter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Free Seedance 2.0 AI Video Generat`)**:
   - Landmark `<section class="relative w-full">` inside `1220px` main stage presenting display lead `Free Seedance 2.0 AI Video Generator` and copy excerpt *"Turn text and images into professional 1080p videos with synchron"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `GPT Image 2.5 Flare & Sunburst.`)**:
   - Landmark `<section class="w-full mx-auto">` rendering section `GPT Image 2.5 Flare & Sunburst.` with copy *"2026 · Seedance 2.0 Released"*, asset references (`3455abe1a79cd15c-s.p.2fxd9z3s4zhc...`, `InterVariable-s.p.2c0y96ae70xfx.w...`, `e8f2fbee2754df70-s.p.1dqa_6e_ad4s...`, `seedance.png`), and grid rule `inter_a1c1f49b-module__H0XvcG__va... { --font-inter:"fontInter", "fontInter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-5> — `Get Up to 8,000 Credits Every Mont`)**:
   - Landmark `<section class="py-5">` framing `Get Up to 8,000 Credits Every Month.` and `Popular AI Models` (*"Seedance 2.0 Fast-Portrait"*) with `#18181b` surface cards, `#8a6b0d` accents, and `rrat_84fd8339-module__Za0QWW__cla... { font-family:Montserrat,Montserrat Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://clipdance.ai`)**:
   - Landmark `<footer class="border-t">` anchoring `Seedance 2.0 - Free AI Video Gen` footer links (`Seedance 2.5 · Blog · Pricing · My Creations`), copy *"OpenAI's newest image model, both versions live. Five qualit"*, and `#e4e4e7` structural dividers.
