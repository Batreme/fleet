---
title: "UI & UX Architecture: nader-io"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: nader-io

## Overview & Design Identity
- **Target**: `nader-io` (**Nader Cserny**)
- **Production URL**: [https://nader.io](https://nader.io)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f6f6` canvas, `#0a0a0a` ink, `#ef4025` accent)
- **Summary**: Product leader specializing in agentic AI systems and blockchain tools. Founder, builder, and advisor, from strategy to shipped code.
- **Total Clean CSS Variables Extracted**: `75` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter-1977dbd7896d9b1f`
- **Body Font Stack**: `Inter-1977dbd7896d9b1f`
- **Monospace / Technical Font Stack**: `JetBrains Mono-7037818b06159deb`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 52px`, `line-height: 54.6px`, `font-weight: 800`, `letter-spacing: -1.82px`); CSS variables `--text-display: clamp(3.25rem, 11vw, 6.5rem)`, `--text-display--line-height: .95`, `--text-display--letter-spacing: -.04em`; rule `h1` (`font-size: clamp(40px,5.5vw,70px)`, `line-height: 1.1`, `letter-spacing: -.04em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 36px`, `font-weight: 800`, `letter-spacing: -1.6px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: .8125rem`, `line-height: 1.35`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: .9375rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-jetbrains-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f6f6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a0a0a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--menu-surface)` in `:root` |
| **Interactive Accent / Highlight** | `#ef4025` | `.pc-face-buttons button { background: #ef4025 }` |
| **Secondary / Muted Copy** | `#8a8a8a` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5e5e5` | `var(--color-rule)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-inter)` | Typography / Scale Token |
| `--font-mono` | `var(--font-jetbrains-mono)` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `nader-io`)**:
   - Landmark `<header class="site-header mb-12">` (`1104x48px`) hosting `Nader Cserny` navigation (`Poster Live · Quiet Edition · Kunsthalle Edition · Chaos Edition · Cinquanta Edition`), DOM attributes (`data-site="nader.io"`, `data-edition-menu`, `data-astro-cid-ylg3fdu2`, `data-astro-cid-lcdefpme`), and stylesheet rule `focus-visible { background-color:color-mix(in srgb, var(--menu-ink,var(--color-ink)) 8%,... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Hi, I’m Nader. Hi I’m Nader`)**:
   - Landmark `<section class="home-hero">` presenting display lead `Hi, I’m Nader. Hi I’m Nader` and copy excerpt *"Product · Design · Code"* over `#f6f6f6` canvas and `#0a0a0a` ink.
3. **Primary Showcase & Content Grid (<section.home-section> — `Shipping AI workflows`)**:
   - Landmark `<section class="home-section">` rendering section `Shipping AI workflows` with copy *"Analytical product guy. I help teams ship agentic AI products and"*, asset references (`favicon.svg`, `favicon.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `hover { color:var(--color-accent) }`.
4. **Interactive Detail & Feature Matrix (<article.home-cap> — `Scaling blockchain dApps`)**:
   - Landmark `<article class="home-cap">` framing `Scaling blockchain dApps` and `Leading 0-to-1 products` (*"Quit talking. Start doing."*) with `#ffffff` surface cards, `#ef4025` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://nader.io`)**:
   - Landmark `<footer class="site-footer mt-20">` anchoring `Nader Cserny` footer links (`Poster Live · Quiet Edition · Kunsthalle Edition · Chaos Edition · Cinquanta Edition`), copy *"Agentic workflows, LLM integrations, skills and tools for AI"*, and `#e5e5e5` structural dividers.
