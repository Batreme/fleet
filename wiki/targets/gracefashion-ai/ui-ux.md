---
title: "UI & UX Architecture: gracefashion-ai"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: gracefashion-ai

## Overview & Design Identity
- **Target**: `gracefashion-ai` (**KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai**)
- **Production URL**: [https://gracefashion.ai](https://gracefashion.ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#9ca3af` accent)
- **Summary**: KI-Modefotografie aus deinen eigenen Teilen: On-Model-Bilder, Kampagnen und Videos. Als Software oder als Service, rund 80 Prozent unter...
- **Total Clean CSS Variables Extracted**: `11` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-display: var(--font-sans)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 66px`, `line-height: 69.3px`, `font-weight: 500`, `letter-spacing: -2.244px`); rule `h2` (`font-size: clamp(21px,16.62px + 1.124vw,...`, `line-height: 1.15`, `letter-spacing: -.026em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 18px`, `line-height: 1.5`, `letter-spacing: -.011em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#737373` | `.blog-content ul li:before { background: #737373 }` |
| **Interactive Accent / Highlight** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Secondary / Muted Copy** | `#737373` | `.blog-content ol li::marker { color: #737373 }` |
| **Structural Hairline Border** | `#fba9a3` | `60 { border-color: #fba9a3 }` |
| **Variable Token (`--color-cool-gray`)** | `#808285` | `var(--color-cool-gray)` in `:root` |
| **Variable Token (`--color-light-gray`)** | `#d1d3d4` | `var(--color-light-gray)` in `:root` |
| **Variable Token (`--color-warm-gray`)** | `#a7a9ac` | `var(--color-warm-gray)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-cool-gray` | `#808285` | Brand / Palette Token |
| `--color-light-gray` | `#d1d3d4` | Canvas / Surface Token |
| `--color-warm-gray` | `#a7a9ac` | Brand / Palette Token |
| `--font-sans` | `var(--font-instrument-sans), "Instrument Sans", sans-serif` | Typography / Scale Token |
| `--font-display` | `var(--font-sans)` | Typography / Scale Token |
| `--orbit-frame` | `min(21vh, 16vw, 290px)` | Dimension / Scale Token |
| `--font-instrument-sans` | `"Instrument Sans", "Instrument Sans Fallback"` | Typography / Scale Token |
| `--font-space-grotesk` | `"Space Grotesk", "Space Grotesk Fallback"` | Typography / Scale Token |
| `--ai-mark-w` | `70vw` | Dimension / Scale Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--gracefashion-ai-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--gracefashion-ai-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.top-0> — `gracefashion-ai`)**:
   - Landmark `<nav class="top-0 left-0">` (`1440x56px`) hosting `KI-Fotostudio für Mode: Bilder ohne ` navigation (`Software · Service · Ratgeber · Team · Demo buchen`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`), and stylesheet rule `.vGn8MW_className { font-family:Instrument Sans,Instrument Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.page-surface> — `KI-Fotostudio für Modemarken: Soft`)**:
   - Landmark `<section class="page-surface px-8">` presenting display lead `KI-Fotostudio für Modemarken: Software und Servic...` and copy excerpt *"Models ohne Buchung."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-black> — `Du entscheidest, was die Welt sehe`)**:
   - Landmark `<section class="bg-black">` rendering section `Du entscheidest, was die Welt sehen und tragen soll.` with copy *"Du entscheidest, was die Welt"*, asset references (`237858b39a32779d-s.p.1ii7211jqpzi...`, `4cf231d25563e07b-s.p.3uuun_-7zsf1...`, `62f37606a5bd6f6f-s.p.3wn_q526zaol...`, `92b6de9cb55945e2-s.p.44ks8kcggj01...`), and grid rule `.vGn8MW_variable { --font-instrument-sans:"Instrument Sans", "Instrument Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.bg-neutral-900> — `Du entscheidest, was die Welt`)**:
   - Landmark `<section class="bg-neutral-900 relative">` framing `Du entscheidest, was die Welt` and `sehen und tragen soll.` (*"sehen und tragen soll."*) with `#737373` surface cards, `#9ca3af` accents, and `.wdTYSa_className { font-family:Space Grotesk,Space Grotesk Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://gracefashion.ai`)**:
   - Landmark `<footer class="relative text-white">` anchoring `KI-Fotostudio für Mode: Bilder o` footer links (`Software · Service · Ratgeber · Team · Demo buchen`), copy *"Aus deinem Produkt wird ein ganzes Shooting. In Minuten."*, and `#fba9a3` structural dividers.
