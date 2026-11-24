---
title: "UI & UX Architecture: davidcata-com_en-musica"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: davidcata-com_en-musica

## Overview & Design Identity
- **Target**: `davidcata-com_en-musica` (**Music — “Queridos todos:” and “Origen”, by David Catá**)
- **Production URL**: [https://davidcata.com/en/musica/](https://davidcata.com/en/musica/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f2eee7` / `#cc8b3d`)
- **Summary**: The music of David Catá: his new album “Queridos todos:” (20 November 2026), pre-order signed and dedicated, and the instrumental album “...
- **Total Clean CSS Variables Extracted**: `12` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Fraunces`
- **Body Font Stack**: `Karla`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 168px`, `line-height: 151.2px`, `font-weight: 300`, `letter-spacing: -7.56px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 83.2px`, `line-height: 81.536px`, `font-weight: 300`, `letter-spacing: -3.744px`); rule `h2` (`font-size: 1.55rem`, `line-height: 1.15`, `letter-spacing: -.02em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 15px`, `line-height: 1.75`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f2eee7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#18110b` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#cc8b3d` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#cc8b3d` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#cc8b3d` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d1cdc7` | `15 { border-color: #d1cdc7 }` |
| **Variable Token (`--tinta-pluma`)** | `#1f3a78` | `var(--tinta-pluma)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--f-titular` | `"Fraunces",Georgia,serif` | Dimension / Scale Token |
| `--f-texto` | `"Karla",system-ui,sans-serif` | Typography Ink Token |
| `--papel` | `242 238 231` | Design System Custom Token |
| `--sala` | `10 9 8` | Design System Custom Token |
| `--hilo` | `158 43 37` | Design System Custom Token |
| `--renglon` | `2.25rem` | Dimension / Scale Token |
| `--tinta-pluma` | `#1f3a78` | Canvas / Surface Token |
| `--f-mano` | `"Caveat","Caveat Fallback"` | Design System Custom Token |
| `--marca` | `29, 185, 84` | Design System Custom Token |
| `--movil` | `0% 50%` | Dimension / Scale Token |
| `--pos` | `50% 50%` | Dimension / Scale Token |
| `--acento` | `204, 139, 61` | Design System Custom Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--davidcata-com-en-bg` | `#f2eee7` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--davidcata-com-en-ink` | `#18110b` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mundo-calido> — `davidcata-com_en-musica`)**:
   - Landmark `<header class="mundo-calido mundo-musica">` (`1440x80px`) hosting `Music — “Queridos todos:” and “Orige` navigation (`In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-website-id="d67277cc-b293-4b3e-b2..."`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.h-hero> — `Queridos todos:`)**:
   - Landmark `<section class="h-hero relative">` presenting display lead `Queridos todos:` and copy excerpt *"DAVID CATÁ · NEW ALBUM · 20.11.2026"* over `#f2eee7` canvas and `#18110b` ink.
3. **Primary Showcase & Content Grid (<section.overflow-clip> — `His theme in “Arriba Tutto”`)**:
   - Landmark `<section class="overflow-clip pb-14">` rendering section `His theme in “Arriba Tutto”` with copy *"Queridos todos: New album · 20.11.2026"*, asset references (`6ba5f591ae6c56f6-s.p.woff2`, `af4bf8399d1aacdf-s.p.woff2`, `b7ae23d8a9c319da-s.p.woff2`, `cd-queridos-limpio-240.webp`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.border-t> — `Three ways to experience it`)**:
   - Landmark `<section class="border-t py-20">` framing `Three ways to experience it` and `Two albums. One memory.` (*"New album · 20.11.2026"*) with `#cc8b3d` surface cards, `#cc8b3d` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-papel> — `https://davidcata.com/en/musica/`)**:
   - Landmark `<footer class="bg-papel text-tinta">` anchoring `Music — “Queridos todos:” and “O` footer links (`In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`), copy *"Origen Album · 2023"*, and `#d1cdc7` structural dividers.
