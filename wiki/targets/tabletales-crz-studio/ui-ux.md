---
title: "UI & UX Architecture: tabletales-crz-studio"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: tabletales-crz-studio

## Overview & Design Identity
- **Target**: `tabletales-crz-studio` (**Table Tales by CRZ.STUDIO · Board Game Collection & Play Log**)
- **Production URL**: [https://tabletales.crz.studio/](https://tabletales.crz.studio/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#08335d` / `#0000ff`)
- **Summary**: Table Tales is a digital exhibition of board games as art: a curated collection and a living log of every night at the table. Designed an...
- **Total Clean CSS Variables Extracted**: `45` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `glowfor`
- **Body Font Stack**: `grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 144px`, `line-height: 144px`, `font-weight: 400`); CSS variables `--font-display: "display", "display Fallback"`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 219.846px`, `line-height: 197.861px`, `font-weight: 400`); rule `h2` (`font-size: clamp(56px,5.6vw,120px)`, `line-height: .92`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-body: clamp(16px, 1.25vw, 20px)`; rule `p` (`font-size: var(--text-body)`, `line-height: 1.35`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-label: clamp(12px, .9vw, 14px)`, `--text-small: clamp(14px, 1.04vw, 16px)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#08335d` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fdffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0000ff` | `body { background: blue }` (`#0000ff`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.AtWhqq_archiveLink { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#f7b538` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#0000ff` | `.J3CQ6a_ledger { border-top: #0000ff }` |
| **Variable Token (`--color-ochre`)** | `#c98f2e` | `var(--color-ochre)` in `:root` |
| **Variable Token (`--color-teal`)** | `#145a86` | `var(--color-teal)` in `:root` |
| **Variable Token (`--color-night`)** | `#010e1c` | `var(--color-night)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-blue` | `#08335d` | Brand / Palette Token |
| `--color-golden` | `#f7b538` | Brand / Palette Token |
| `--color-azure` | `#fdffff` | Brand / Palette Token |
| `--color-ochre` | `#c98f2e` | Brand / Palette Token |
| `--color-teal` | `#145a86` | Brand / Palette Token |
| `--color-night` | `#010e1c` | Brand / Palette Token |
| `--color-line-on-light` | `color-mix(in srgb, var(--color-blue) 22%, transparent)` | Canvas / Surface Token |
| `--color-line-on-dark` | `color-mix(in srgb, var(--color-azure) 22%, transparent)` | Canvas / Surface Token |
| `--color-muted-on-light` | `color-mix(in srgb, var(--color-blue) 62%, transparent)` | Canvas / Surface Token |
| `--color-muted-on-dark` | `color-mix(in srgb, var(--color-azure) 62%, transparent)` | Canvas / Surface Token |
| `--section-padding-inline` | `clamp(20px, 2.78vw, 64px)` | Layout / Spatial Grid Token |
| `--section-padding-block` | `clamp(72px, 8.33vw, 160px)` | Layout / Spatial Grid Token |
| `--measure-padding` | `clamp(0px, 18vw, 420px)` | Layout / Spatial Grid Token |
| `--space-2xs` | `4px` | Layout / Spatial Grid Token |
| `--space-xs` | `8px` | Layout / Spatial Grid Token |
| `--space-s` | `clamp(12px, 1.11vw, 16px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.LYh_OG_variable> — `tabletales-crz-studio`)**:
   - Landmark `<header class="LYh_OG_variable">` (`1440x97px`) hosting `Table Tales by CRZ.STUDIO · Board Ga` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `body { scrollbar-width:none;-ms-overflow-style:none;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.q_m67W_hero> — `TABLE TALES`)**:
   - Landmark `<section class="q_m67W_hero">` presenting display lead `TABLE TALES` and copy excerpt *"BOARD GAMES ARE ART MADE ALIVE BY THE HANDS THAT PLAY THEM"* over `#08335d` canvas and `#fdffff` ink.
3. **Primary Showcase & Content Grid (<section.uxasZq_variable> — `T a b l e T a l e s`)**:
   - Landmark `<section class="uxasZq_variable">` rendering section `T a b l e T a l e s` with copy *"Board games are art made alive by the hands that play them"*, asset references (`FoundersGrotesk_Bold-s.p.2z72oy2q...`, `FoundersGrotesk_BoldItalic-s.p.2h...`, `FoundersGrotesk_Light-s.p.03ydj7u...`, `FoundersGrotesk_LightItalic-s.p.2...`), and grid rule `html::-webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.O43udq_featured> — `Featured Games`)**:
   - Landmark `<section class="O43udq_featured">` framing `Featured Games` and `The play log` (*"Every game on this shelf began as a picture someone wanted to wal"*) with `#0000ff` surface cards, `#0000ff` accents, and `body::-webkit-scrollbar { display:none }`.
5. **Colophon & Global Directory Footer (<footer.tUdqrq_footer> — `https://tabletales.crz.studio/`)**:
   - Landmark `<footer class="tUdqrq_footer">` anchoring `Table Tales by CRZ.STUDIO · Boar` footer links (`Overview · Index · Archive · About · Contact`), copy *"Chosen for the worlds they build and the stories they leave "*, and `#0000ff` structural dividers.
