---
title: "UI & UX Architecture: www-1centre-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-1centre-com

## Overview & Design Identity
- **Target**: `www-1centre-com` (**1Centre — Trade Credit Software for NZ & Australia**)
- **Production URL**: [https://www.1centre.com/](https://www.1centre.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fafbfa` / `#4ab0ff`)
- **Summary**: Trade credit software for suppliers in New Zealand and Australia: digital account applications, ID checks, credit decisions, 24/7 monitor...
- **Total Clean CSS Variables Extracted**: `87` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 55.6667px`, `line-height: 54.5533px`, `font-weight: 500`, `letter-spacing: -1.94833px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 86.4px`, `line-height: 84.672px`, `font-weight: 500`, `letter-spacing: -3.888px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fafbfa` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#101112` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f5f2` | `var(--color-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#4ab0ff` | `.btn-dots.btn-candy { background-color: #4ab0ff }` |
| **Secondary / Muted Copy** | `#9a9da0` | `var(--color-muted-2)` in `:root` |
| **Structural Hairline Border** | `#e7e9e8` | `var(--color-line)` in `:root` |
| **Variable Token (`--color-amber-500`)** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Variable Token (`--color-amber-700`)** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-archivo` | `"Archivo Black", "Archivo Black Fallback"` | Typography / Scale Token |
| `--dot-r` | `0px` | Dimension / Scale Token |
| `--qc-r` | `60%` | Dimension / Scale Token |
| `--qc-r2` | `70%` | Dimension / Scale Token |
| `--font-sans` | `var(--font-inter), ui-sans-serif, system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-4xl` | `2.25rem` | Typography Ink Token |
| `--text-4xl--line-height` | `calc(2.5 / 2.25)` | Typography Ink Token |
| `--text-5xl` | `3rem` | Typography Ink Token |
| `--text-5xl--line-height` | `1` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `www-1centre-com`)**:
   - Landmark `<header class="top-0 transition-colors">` (`1440x64px`) hosting `1Centre — Trade Credit Software for ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nimg="1"`, `data-dark="true"`), and stylesheet rule `nter_7b064e0d-module__MOT0tq__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Trade credit at scale, so you can `)**:
   - Landmark `<section class="relative overflow-hidden">` presenting display lead `Trade credit at scale, so you can focus on sales.` and copy excerpt *"1Centre helps businesses across all industries trade with trust. "* over `#fafbfa` canvas and `#101112` ink.
3. **Primary Showcase & Content Grid (<section.group> — `Build trade credit workflows on ev`)**:
   - Landmark `<section class="group border-y">` rendering section `Build trade credit workflows on everything your b...` with copy *"Trade credit at scale,"*, asset references (`5e4d537aaa9e154b-s.p.0g9-.3zp53cu...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `logo-mark.svg`, `mitre10.svg`), and grid rule `inter_7b064e0d-module__MOT0tq__va... { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-mt-20> — `Open trade accounts from the count`)**:
   - Landmark `<section class="scroll-mt-20 pb-16">` framing `Open trade accounts from the counter, the web, yo...` and `Write your own credit rules — and let them decide...` (*"so you can focus on sales."*) with `#f6f5f2` surface cards, `#4ab0ff` accents, and `lack_857642da-module__iF7jea__cla... { font-family:Archivo Black,Archivo Black Fallback;font-style:normal;font-... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.1centre.com/`)**:
   - Landmark `<footer class="relative overflow-hidden">` anchoring `1Centre — Trade Credit Software ` footer links (`Overview · Index · Archive · About · Contact`), copy *"1Centre helps businesses across all industries"*, and `#e7e9e8` structural dividers.
