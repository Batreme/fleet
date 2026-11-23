---
title: "UI & UX Architecture: www-fieldrank-run"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-fieldrank-run

## Overview & Design Identity
- **Target**: `www-fieldrank-run` (**FieldRank: Trail and ultra rankings**)
- **Production URL**: [https://www.fieldrank.run](https://www.fieldrank.run)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×1266px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1e1d1a` ink, `#f1efea` accent)
- **Summary**: A season ranking of trail and ultra runners, built from race results. Overall and by distance.
- **Total Clean CSS Variables Extracted**: `89` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 57.12px`, `font-weight: 600`, `letter-spacing: -1.96px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1e1d1a` | `var(--foreground)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f1efea` | `var(--background)` in `:root` |
| **Interactive Accent / Highlight** | `#f1efea` | `var(--primary-foreground)` in `:root` |
| **Secondary / Muted Copy** | `#66635d` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#ddd9cf` | `var(--border)` in `:root` |
| **Variable Token (`--card`)** | `#faf9f6` | `var(--card)` in `:root` |
| **Variable Token (`--secondary`)** | `#e9e6df` | `var(--secondary)` in `:root` |
| **Variable Token (`--destructive`)** | `#e40014` | `var(--destructive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#f1efea` | Canvas / Surface Token |
| `--foreground` | `#1e1d1a` | Typography Ink Token |
| `--card` | `#faf9f6` | Color / Atmospheric Token |
| `--card-foreground` | `#1e1d1a` | Typography Ink Token |
| `--popover` | `#faf9f6` | Color / Atmospheric Token |
| `--popover-foreground` | `#1e1d1a` | Typography Ink Token |
| `--primary` | `#1e1d1a` | Brand / Palette Token |
| `--primary-foreground` | `#f1efea` | Typography Ink Token |
| `--secondary` | `#e9e6df` | Brand / Palette Token |
| `--secondary-foreground` | `#1e1d1a` | Typography Ink Token |
| `--muted` | `#e9e6df` | Color / Atmospheric Token |
| `--muted-foreground` | `#66635d` | Typography Ink Token |
| `--accent` | `#e9e6df` | Brand / Palette Token |
| `--accent-foreground` | `#1e1d1a` | Typography Ink Token |
| `--destructive` | `#e40014` | Color / Atmospheric Token |
| `--border` | `#ddd9cf` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `www-fieldrank-run`)**:
   - Landmark `<header class="top-0 z-40">` (`1440x57px`) hosting `FieldRank: Trail and ultra rankings` navigation (`Rankings · Races`), DOM attributes (`data-precedence="next"`, `data-site="KPVLKBUA"`, `data-auto="false"`, `data-slot="button"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
2. **Hero Stage & Focal Lead (<div.light> — `Trail and ultra rankings`)**:
   - Landmark `<div class="light">` presenting display lead `Trail and ultra rankings` and copy excerpt *"A season ranking of trail and ultra runners, built from race resu"* over `#ffffff` canvas and `#1e1d1a` ink.
3. **Primary Showcase & Content Grid (<div.min-h-screen> — `A season ranking of trail and ultr`)**:
   - Landmark `<div class="min-h-screen">` rendering section `A season ranking of trail and ultra runners, bui` with copy *"Season in progress"*, asset references (`2oz0lep7db5t2.css`, `0jvhpaew_uadu.js`, `script.js`, `19mx3mg6lkumu.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.bg-background> — `Season in progress`)**:
   - Landmark `<div class="bg-background">` framing `Season in progress` and `2026-11-15 · Santa Ynez, CA, USA · Short · 422 r` (*"2026-11-15 · Santa Ynez, CA, USA · Short · 422 results"*) with `#f1efea` surface cards, `#f1efea` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.text-foreground> — `https://www.fieldrank.run`)**:
   - Landmark `<footer class="text-foreground">` anchoring `FieldRank: Trail and ultra ranki` footer links (`Rankings · Races`), copy *"Santa Ynez, CA, USA"*, and `#ddd9cf` structural dividers.
