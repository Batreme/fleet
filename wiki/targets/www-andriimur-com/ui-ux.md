---
title: "UI & UX Architecture: www-andriimur-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-andriimur-com

## Overview & Design Identity
- **Target**: `www-andriimur-com` (**Andrii Mur**)
- **Production URL**: [https://www.andriimur.com/](https://www.andriimur.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#262626` canvas, `#ffffff` ink, `#829f62` accent)
- **Summary**: Andrii Mur – Ukrainian street & documentary photographer in Tallinn, Estonia. From the information mess to how it feels to be Alive in an...
- **Total Clean CSS Variables Extracted**: `138` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 800`, `letter-spacing: -1.2px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#262626` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `header` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `var(--pswp-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#829f62` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#9ca3af` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#4f4f4f` | `var(--pswp-icon-stroke-color)` in `:root` |
| **Variable Token (`--color-yellow-100`)** | `#fef9c2` | `var(--color-yellow-100)` in `:root` |
| **Variable Token (`--color-yellow-700`)** | `#a36100` | `var(--color-yellow-700)` in `:root` |
| **Variable Token (`--color-blue-500`)** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Variable Token (`--color-blue-800`)** | `#193cb8` | `var(--color-blue-800)` in `:root` |
| **Variable Token (`--color-slate-200`)** | `#e2e8f0` | `var(--color-slate-200)` in `:root` |
| **Variable Token (`--color-gray-50`)** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Variable Token (`--color-gray-100`)** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d1d5dc` | `var(--color-gray-300)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--z-page-background` | `-1` | Canvas / Surface Token |
| `--z-chrome` | `10` | Elevation / Border Token |
| `--z-overlay` | `15` | Elevation / Border Token |
| `--vf-dial-gutter` | `2.75rem` | Layout / Spatial Grid Token |
| `--vf-frame-max-w` | `min(calc(100cqh * 1.5), calc(100cqw - var(--vf-dial-gutter) * 2))` | Layout / Spatial Grid Token |
| `--vf-dial-inset` | `max(1rem, calc(50vw - 75svh - var(--vf-dial-gutter)))` | Dimension / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-yellow-100` | `#fef9c2` | Brand / Palette Token |
| `--color-yellow-700` | `#a36100` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-800` | `#193cb8` | Brand / Palette Token |
| `--color-slate-200` | `#e2e8f0` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5dc` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Persistent Left Sidebar Navigation (<nav.inset-0> — `364×772px` at `x=-388`)**:
   - Fixed/sticky left rail `<nav class="inset-0 items-end">` (`364px` wide) paired with top bar `<header class="top-0 gap-x-5">` hosting `Andrii Mur` navigation (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), DOM attributes (`data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Andrii Mur`)**:
   - Landmark `<section class="dark">` inside `1076px` main stage presenting display lead `Andrii Mur` and copy excerpt *"Black and White singles"* over `#262626` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.snap-showcase> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="snap-showcase">` rendering section `Featured Work & Interactive Showcase` with copy *"Tripod left at Home"*, asset references (`m2ak1cq3.api.sanity.io`, `6ab71d031fe7ae3b-s.p.141jscyq52bj...`, `80bb744e92754df7-s.p.2eihtoujcocl...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="flex">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Between duality of Space and Time"*) with `#000000` surface cards, `#829f62` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bottom-0> — `https://www.andriimur.com/`)**:
   - Landmark `<footer class="bottom-0 bg-neutral-900">` anchoring `Andrii Mur` footer links (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), copy *"a Quiet gaze from Within"*, and `#4f4f4f` structural dividers.
