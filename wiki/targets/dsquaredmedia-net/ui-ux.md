---
title: "UI & UX Architecture: dsquaredmedia-net"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: dsquaredmedia-net

## Overview & Design Identity
- **Target**: `dsquaredmedia-net` (**South Florida Marketing Agency · Branding, Web & AI · Dsquared Media**)
- **Production URL**: [https://dsquaredmedia.net](https://dsquaredmedia.net)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#07090d` / `#ff006d`)
- **Summary**: Dsquared Media is a boutique West Palm Beach marketing agency serving South Florida. Branding, web design, growth, and AI, built as one s...
- **Total Clean CSS Variables Extracted**: `87` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `jakarta`
- **Body Font Stack**: `jakarta`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 11px`, `line-height: 15.95px`, `font-weight: 700`, `letter-spacing: 1.54px`); rule `,h1` (`font-size: 62px`, `line-height: 1.05`, `letter-spacing: -.03em`, `font-weight: 600`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 76px`, `line-height: 74.48px`, `font-weight: 500`, `letter-spacing: -2.66px`); rule `,h2` (`font-size: clamp(32px,4vw,56px)`, `line-height: 1.04`, `letter-spacing: -.025em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.65`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-victor),ui-monospace,monospace`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 11px`, `line-height: 1.5`, `letter-spacing: .04em`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#07090d` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f1f1f1` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#111113` | `var(--color-surface)` in `:root` |
| **Interactive Accent / Highlight** | `#ff006d` | `var(--gradient-brand)` in `:root` |
| **Secondary / Muted Copy** | `#676977` | `var(--d2cal-muted)` in `:root` |
| **Structural Hairline Border** | `#16171b` | `var(--border-subtle)` in `:root` (`ffffff0f`) |
| **Variable Token (`--color-surface-2`)** | `#16161a` | `var(--color-surface-2)` in `:root` |
| **Variable Token (`--color-surface-raised`)** | `#0e0e13` | `var(--color-surface-raised)` in `:root` |
| **Variable Token (`--color-surface-card`)** | `#0c0d12` | `var(--color-surface-card)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-dim`)** | `#989898` | `var(--color-dim)` in `:root` |
| **Variable Token (`--color-text-80`)** | `#fffc` | `var(--color-text-80)` in `:root` |
| **Variable Token (`--color-text-60`)** | `#fff9` | `var(--color-text-60)` in `:root` |
| **Variable Token (`--color-blue`)** | `#5661ff` | `var(--color-blue)` in `:root` |
| **Variable Token (`--color-indigo`)** | `#4b39b4` | `var(--color-indigo)` in `:root` |
| **Variable Token (`--color-lavender`)** | `#a88fff` | `var(--color-lavender)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#07090d` | Canvas / Surface Token |
| `--color-surface` | `#111113` | Canvas / Surface Token |
| `--color-surface-2` | `#16161a` | Canvas / Surface Token |
| `--color-surface-raised` | `#0e0e13` | Canvas / Surface Token |
| `--color-surface-card` | `#0c0d12` | Canvas / Surface Token |
| `--color-text` | `#f1f1f1` | Typography Ink Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-dim` | `#989898` | Brand / Palette Token |
| `--color-text-80` | `#fffc` | Typography Ink Token |
| `--color-text-60` | `#fff9` | Typography Ink Token |
| `--color-text-50` | `#ffffff80` | Typography Ink Token |
| `--color-text-38` | `#ffffff61` | Typography Ink Token |
| `--color-blue` | `#5661ff` | Brand / Palette Token |
| `--color-indigo` | `#4b39b4` | Brand / Palette Token |
| `--color-lavender` | `#a88fff` | Brand / Palette Token |
| `--color-magenta` | `#ff006d` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cap-fw-head> — `dsquaredmedia-net`)**:
   - Landmark `<header class="cap-fw-head">` (`1440x362px`) hosting `South Florida Marketing Agency · Bra` navigation (`About · Services · Flex · The Hub · Work`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `awwwards { display:none }`.
2. **Hero Stage & Focal Lead (<section.hero> — `A SOUTH FLORIDA MARKETING AGENCY B`)**:
   - Landmark `<section class="hero hero-in">` presenting display lead `A SOUTH FLORIDA MARKETING AGENCY BUILT TO SHAPE Y...` and copy excerpt *"We live in a world shaped by perception."* over `#07090d` canvas and `#f1f1f1` ink.
3. **Primary Showcase & Content Grid (<section.statement> — `A South Florida marketing agency b`)**:
   - Landmark `<section class="statement">` rendering section `A South Florida marketing agency built to shape y...` with copy *"A full-service marketing agency in West Palm Beach, working with "*, asset references (`636a5ac981f94f8b-s.p.woff2`, `8d2bb7cdfa09b0c5-s.p.woff2`, `ee62220d3ef0f600.css`, `fc3610b87831099d.css`), and grid rule `.__className_0860af { font-family:jakarta,jakarta Fallback }`.
4. **Interactive Detail & Feature Matrix (<section.cap-fw> — `Branding, web, growth and AI, buil`)**:
   - Landmark `<section class="cap-fw anim">` framing `Branding, web, growth and AI, built as one system.` and `Graphic Design` (*"5.0 across 100+ client reviews"*) with `#111113` surface cards, `#ff006d` accents, and `.__variable_0860af { --font-jakarta:"jakarta","jakarta Fallback" }`.
5. **Colophon & Global Directory Footer (<footer.caf-footer> — `https://dsquaredmedia.net`)**:
   - Landmark `<footer class="caf-footer">` anchoring `South Florida Marketing Agency ·` footer links (`About · Services · Flex · The Hub · Work`), copy *"Over 15 years in South Florida and hundreds of trusted partn"*, and `#16171b` structural dividers.
