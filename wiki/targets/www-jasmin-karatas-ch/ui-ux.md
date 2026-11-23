---
title: "UI & UX Architecture: www-jasmin-karatas-ch"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-jasmin-karatas-ch

## Overview & Design Identity
- **Target**: `www-jasmin-karatas-ch` (**Jasmin Deniz Karatas – Product Designer, Gamification Specialist & Keyno...**)
- **Production URL**: [http://www.jasmin-karatas.ch](http://www.jasmin-karatas.ch)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#fea0c0`)
- **Summary**: Jasmin Deniz Karatas (JayKay): product designer, gamification specialist and keynote speaker. Keynotes, workshops and books on gaming the...
- **Total Clean CSS Variables Extracted**: `91` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `larsseit`
- **Body Font Stack**: `interphases`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 57.6px`, `line-height: 58.752px`, `font-weight: 700`, `letter-spacing: -2.304px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171717` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e8d8ba` | `.bg-paper { background-color: #e8d8ba }` |
| **Interactive Accent / Highlight** | `#fea0c0` | `var(--color-primary-100)` in `:root` |
| **Secondary / Muted Copy** | `#9fb0e2` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#c8c2bd` | `30 { border-color: #c8c2bd }` |
| **Variable Token (`--color-emerald-300`)** | `#5ee9b5` | `var(--color-emerald-300)` in `:root` |
| **Variable Token (`--color-emerald-400`)** | `#00d294` | `var(--color-emerald-400)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gutter` | `clamp(1.75rem, 7vw, 8rem)` | Layout / Spatial Grid Token |
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#171717` | Typography Ink Token |
| `--font-larsseit` | `"larsseit", "larsseit Fallback"` | Typography / Scale Token |
| `--font-interphases` | `"interphases", "interphases Fallback"` | Typography / Scale Token |
| `--font-wanted-serif` | `"Tinos", "Tinos Fallback"` | Typography / Scale Token |
| `--font-wanted-condensed` | `"Stint Ultra Condensed", "Stint Ultra Condensed Fallback"` | Typography / Scale Token |
| `--font-wanted-bounty` | `"Questrial", "Questrial Fallback"` | Typography / Scale Token |
| `--font-wanted-fine` | `"Oswald", "Oswald Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-interphases), sans-serif` | Typography / Scale Token |
| `--color-emerald-300` | `#5ee9b5` | Brand / Palette Token |
| `--color-emerald-400` | `#00d294` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xs` | `20rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-jasmin-karatas-ch`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x96px`) hosting `Jasmin Deniz Karatas – Product Desig` navigation (`Privacy · Imprint`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.relative> — `JAYKAY – Jasmin Deniz Karatas`)**:
   - Landmark `<section class="relative">` presenting display lead `JAYKAY – Jasmin Deniz Karatas` and copy excerpt *"04 Content Creation"* over `#ffffff` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<section.h-svh> — `04 Content Creation`)**:
   - Landmark `<section class="h-svh px-page">` rendering section `04 Content Creation` with copy *"Product Designer, Gamification Specialist & Keynote Speaker"*, asset references (`2f19417f17ff8e58-s.p.3gn-3bwpf0f0...`, `581c3ae769a58b7e-s.p.2ow53ya-6whs...`, `96cd250007373f76-s.p.13j832optq1i...`, `Larsseit_Bold-s.p.3wzp25uvg6vh4.w...`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.px-page> — `Product Designer, Gamification Spe`)**:
   - Landmark `<section class="h-svh px-page">` framing `Product Designer, Gamification Specialist & Keyn` and `Start voyage ENTER` (*"Start voyage ENTER"*) with `#e8d8ba` surface cards, `#fea0c0` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.overflow-clip> — `http://www.jasmin-karatas.ch`)**:
   - Landmark `<footer class="overflow-clip bg-navy-900">` anchoring `Jasmin Deniz Karatas – Product D` footer links (`Privacy · Imprint`), copy *"Not in the mood for games? Simple Website Version →"*, and `#c8c2bd` structural dividers.
