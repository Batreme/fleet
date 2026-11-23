---
title: "UI & UX Architecture: dark-moon-org"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: dark-moon-org

## Overview & Design Identity
- **Target**: `dark-moon-org` (**Darkmoon: Autonomous AI Penetration Testing Platform**)
- **Production URL**: [https://dark-moon.org/](https://dark-moon.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#f97316` accent)
- **Summary**: Darkmoon is an open-source, AI-powered autonomous penetration testing platform. 50 specialized AI agents covering web, cloud, identity, C...
- **Total Clean CSS Variables Extracted**: `387` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `googleSans`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `Google Sans Code`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--dm-display: clamp(3.25rem,7.8vw,7.75rem)`, `--m-display: clamp(3.5rem,calc(2rem + 8.2vw),4.5rem)`, `--m-h1: clamp(2.25rem,calc(1.25rem + 5.13vw),2.75rem)`; rule `h1` (`font-size: min(var(--m-h1),calc((100vw -...`, `line-height: .95`, `letter-spacing: -.02em`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 28px`, `line-height: 30.8px`, `font-weight: 500`, `letter-spacing: -0.56px`); rule `h2` (`letter-spacing: -.01em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--dm-body: clamp(1rem,1.11vw,1.125rem)`, `--dm-body-lh: 1.45`, `--text-base: 1rem`; rule `p` (`font-size: .9375rem`, `line-height: 1.4`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--dm-label: .78rem`, `--font-mono: var(--font-code)`, `--text-xs: .75rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#151515` | `var(--dm-card)` in `:root` |
| **Interactive Accent / Highlight** | `#f97316` | `.dm-main .dm-badge--high:before { background: #f97316 }` |
| **Secondary / Muted Copy** | `#9a9aa6` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#5c6168` | `var(--dc-line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--radius` | `15px` | Elevation / Border Token |
| `--background` | `#000` | Canvas / Surface Token |
| `--dm-gutter` | `clamp(.75rem,1.6vw,1.75rem)` | Layout / Spatial Grid Token |
| `--dm-inset` | `clamp(1rem,4.5vw,6rem)` | Dimension / Scale Token |
| `--dm-page-x` | `clamp(1rem,2.22vw,2.25rem)` | Dimension / Scale Token |
| `--dm-card` | `#151515` | Color / Atmospheric Token |
| `--dm-line` | `#ffffff42` | Color / Atmospheric Token |
| `--dm-card-line` | `#ffffff2e` | Color / Atmospheric Token |
| `--dm-card-radius` | `.5rem` | Elevation / Border Token |
| `--dm-card-gap` | `clamp(1rem,1.25vw,1.25rem)` | Layout / Spatial Grid Token |
| `--dm-section-top` | `clamp(1.5rem,2.22vw,2.25rem)` | Dimension / Scale Token |
| `--dm-section-bottom` | `clamp(6rem,17.8vw,17.75rem)` | Dimension / Scale Token |
| `--dm-stack-gap` | `clamp(4rem,13vw,13rem)` | Layout / Spatial Grid Token |
| `--dm-display` | `clamp(3.25rem,7.8vw,7.75rem)` | Dimension / Scale Token |
| `--dm-statement` | `clamp(1.75rem,3.33vw,3.35rem)` | Dimension / Scale Token |
| `--dm-h3` | `clamp(1.5rem,2.22vw,2.25rem)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Persistent Left Sidebar Navigation (<nav.ml-1> — `188×598px` at `x=12`)**:
   - Fixed/sticky left rail `<nav class="ml-1 hidden">` (`188px` wide) paired with top bar `<header class="inset-x-0 top-0">` hosting `Darkmoon: Autonomous AI Penetr` navigation (`Product · Attack paths · Pricing · Docs · Blog`), DOM attributes (`data-route-lang="en"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and rule `gl-l { display:block }`.
2. **Hero Stage & Focal Lead (<section.dm-hero> — `Darkmoon, Autonomous AI Penetratio`)**:
   - Landmark `<section class="dm-hero w6">` inside `1429px` main stage presenting display lead `Darkmoon, Autonomous AI Penetration Testing Platform` and copy excerpt *"AUTONOMOUS, CONTINUOUS PENETRATION TESTING"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.scroll-mt-24> — `Attack surface camp_20260426_3d2f `)**:
   - Landmark `<section class="scroll-mt-24 overflow-clip">` rendering section `Attack surface camp_20260426_3d2f · 26 Apr 2026` with copy *"Autonomous, continuous penetration testing"*, asset references (`eafabf029ad39a43-s.p.woff2`, `3d4d48715202a72c.css`, `6e008cfa72251405.css`, `e824d722814de74c.css`), and grid rule `.gl-host { isolation:isolate }`.
4. **Interactive Detail & Feature Matrix (<section.dc> — `Not a scanner. An autonomous secur`)**:
   - Landmark `<section class="dc dc--default">` framing `Not a scanner. An autonomous security conductor.` and `Darkmoon + Splunk: Send AI Pentest Findings to Yo...` (*"Autonomous, continuous"*) with `#151515` surface cards, `#f97316` accents, and `.gl-host.gl-static { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://dark-moon.org/`)**:
   - Landmark `<footer class="relative bg-white">` anchoring `Darkmoon: Autonomous AI Penetrat` footer links (`Product · Attack paths · Pricing · Docs · Blog`), copy *"penetration testing"*, and `#5c6168` structural dividers.
