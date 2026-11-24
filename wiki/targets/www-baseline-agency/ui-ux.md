---
title: "UI & UX Architecture: www-baseline-agency"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-baseline-agency

## Overview & Design Identity
- **Target**: `www-baseline-agency` (**Baseline · Brand identity systems, designed and built**)
- **Production URL**: [https://www.baseline.agency/](https://www.baseline.agency/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`)
- **Summary**: Brand identity studio in Cluj-Napoca led by Victor Deaconu. Positioning, identity, rules and guidelines in 3 to 4 weeks, for brands that...
- **Total Clean CSS Variables Extracted**: `64` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 46.5333px`, `line-height: 44.2067px`, `font-weight: 700`, `letter-spacing: -1.396px`); CSS variables `--t-display: clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px))`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 53.48px`, `line-height: 53.48px`, `font-weight: 600`, `letter-spacing: -1.6044px`)
- **Body Copy**: live computed `body` (`font-size: 15.28px`, `line-height: 22.92px`, `font-weight: 400`); CSS variables `--t-body: clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px))`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15.28px`, `line-height: 18.145px`, `font-weight: 700`, `letter-spacing: -0.6112px`); CSS variables `--t-label: calc(14*1px)`, `--default-mono-font-family: var(--font-mono)`, `--about-small: clamp(calc(11 * 1px), .88vw, calc(24 * 1px))`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d0d0d0` | `:focus { background-color: #d0d0d0 }` |
| **Interactive Accent / Highlight** | `#000000` | `.S6Hkya_link:hover { color: #000000 }` |
| **Secondary / Muted Copy** | `#0d0d0d` | `:focus-visible { color: #0d0d0d }` |
| **Structural Hairline Border** | `#cecece` | `25 { border-color: #cecece }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#000` | Typography Ink Token |
| `--t-display` | `clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px))` | Dimension / Scale Token |
| `--t-heading` | `clamp(calc(24*1px),calc(22.9*1px) + .296vw,calc(28*1px))` | Typography Ink Token |
| `--t-body` | `clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px))` | Dimension / Scale Token |
| `--t-label` | `calc(14*1px)` | Dimension / Scale Token |
| `--edge` | `clamp(calc(17*1px),calc(14.5*1px) + .665vw,calc(26*1px))` | Dimension / Scale Token |
| `--gap` | `clamp(calc(16*1px),calc(13.2*1px) + .739vw,calc(26*1px))` | Layout / Spatial Grid Token |
| `--space-row` | `clamp(calc(48*1px),calc(34.7*1px) + 3.548vw,calc(96*1px))` | Layout / Spatial Grid Token |
| `--space-section` | `clamp(calc(96*1px),calc(72.7*1px) + 6.208vw,calc(180*1px))` | Layout / Spatial Grid Token |
| `--ink-light` | `0` | Canvas / Surface Token |
| `--duration-exit` | `.15s` | Motion / Easing Token |
| `--duration-enter` | `.21s` | Motion / Easing Token |
| `--duration-move` | `.4s` | Motion / Easing Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-inter-tight` | `"Inter Tight", "Inter Tight Fallback"` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-baseline-agency`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Baseline · Brand identity systems, d` navigation (`About > A b o u t`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.LINzvG_className { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.hero-drift> — `You got here with your brand worki`)**:
   - Landmark `<section class="hero-drift relative">` presenting display lead `You got here with your brand working against you....` and copy excerpt *"You've grown this far despite the brand and website built when yo"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `You've grown this far despite the `)**:
   - Landmark `<section class="relative text-white">` rendering section `You've grown this far despite the brand and webs` with copy *"Baseline B a s e l i n e Studio S t u d i o"*, asset references (`41q-9hyqnol8s.css`, `11vyltt-w7ouz.css`, `027ldshog-_ys.css`, `3ya-20k_dn7en.js`), and grid rule `.LINzvG_variable { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `Baseline B a s e l i n e Studio S `)**:
   - Landmark `<article class="flex flex-col">` framing `Baseline B a s e l i n e Studio S t u d i o` and `Baseline B a s e l i n e` (*"Baseline B a s e l i n e"*) with `#d0d0d0` surface cards, `#000000` accents, and `.PJ4aQa_className { font-family:Inter Tight,Inter Tight Fallback;font-style:normal;font-weig... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.baseline.agency/`)**:
   - Landmark `<footer class="relative w-full">` anchoring `Baseline · Brand identity system` footer links (`About > A b o u t`), copy *"Studio S t u d i o"*, and `#cecece` structural dividers.
