---
title: "UI & UX Architecture: akaiito-ai"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: akaiito-ai

## Overview & Design Identity
- **Target**: `akaiito-ai` (**Akai Ito — Your twin dates millions. You go on one date.**)
- **Production URL**: [https://akaiito.ai](https://akaiito.ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ecebe5` / `#ff0000`)
- **Summary**: Akai Ito builds a digital twin of you. It goes on millions of first dates, lives ten thousand lives with your best match, then books one...
- **Total Clean CSS Variables Extracted**: `28` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 112.5px`, `line-height: 101.25px`, `font-weight: 500`, `letter-spacing: -6.1875px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 67.68px`, `font-weight: 500`, `letter-spacing: -3.6px`); rule `h2` (`font-size: clamp(44px, 6.4vw, 120px)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: .9375rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--mono: "Geist","Geist Fallback","Inter",system-ui,sans-serif`; rule `small` (`font-size: .74rem`, `line-height: 1.25`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ecebe5` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111113` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fbfaf7` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.btn.red { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#6f6e6a` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d2d1cc` | `var(--line)` in `:root` (`rgba(17,17,19,.12)`) |
| **Variable Token (`--red`)** | `#e4322b` | `var(--red)` in `:root` |
| **Variable Token (`--blue`)** | `#1a73e8` | `var(--blue)` in `:root` |
| **Variable Token (`--flesh`)** | `#f3c3a5` | `var(--flesh)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fit` | `1` | Design System Custom Token |
| `--paper` | `#ecebe5` | Canvas / Surface Token |
| `--ink` | `#111113` | Typography Ink Token |
| `--card` | `#fbfaf7` | Color / Atmospheric Token |
| `--red` | `#e4322b` | Color / Atmospheric Token |
| `--muted` | `#6f6e6a` | Color / Atmospheric Token |
| `--line` | `rgba(17,17,19,.12)` | Color / Atmospheric Token |
| `--blue` | `#1a73e8` | Color / Atmospheric Token |
| `--sans` | `"Geist","Geist Fallback","Inter",system-ui,-apple-system,sans-serif` | Typography / Scale Token |
| `--mono` | `"Geist","Geist Fallback","Inter",system-ui,sans-serif` | Typography / Scale Token |
| `--bg` | `#ecebe5` | Canvas / Surface Token |
| `--flesh` | `#f3c3a5` | Color / Atmospheric Token |
| `--dockH` | `6.4rem` | Dimension / Scale Token |
| `--navH` | `4.6rem` | Layout / Spatial Grid Token |
| `--ii` | `clamp(1.125rem, 2.4vw, 1.875rem)` | Dimension / Scale Token |
| `--tr` | `-.8deg` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.ahd> — `akaiito-ai`)**:
   - Landmark `<header class="ahd">` (`1440px`) hosting `Akai Ito — Your twin dates millions.` navigation (`Akai Ito · App · How it works · The model · Simulation`), DOM attributes (`data-slot="head"`, `data-d="-1"`, `data-d="1"`, `data-slot="body"`), and stylesheet rule `html { background:var(--paper);font-size:16px;overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<section.sec> — `Your twin dates millions. You go o`)**:
   - Landmark `<section class="sec opener">` presenting display lead `Your twin dates millions. You go on one date.` and copy excerpt *"Akai Ito is for grown-ups. Are you 18 or older?"* over `#ecebe5` canvas and `#111113` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `1 window awake on this block Every`)**:
   - Landmark `<section class="hero sec">` rendering section `1 window awake on this block Everyone you could l...` with copy *"Akai Ito · AI dating, by simulation"*, asset references (`icon.webp`, `favicon.png`, `apple-touch.png`, `phone.webp`), and grid rule `body { overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<section.appsec> — `Your twin lives in your pocket.`)**:
   - Landmark `<section class="sec appsec">` framing `Your twin lives in your pocket.` and `Act I · Right now You’ve swiped almost 4,000 times.` (*"Your twin dates millions."*) with `#fbfaf7` surface cards, `#ff0000` accents, and `stage { position:fixed;inset:0;width:100%;height:100%;display:block;z-index:0 }`.
5. **Colophon & Global Directory Footer (<footer.anim-off> — `https://akaiito.ai`)**:
   - Landmark `<footer class="anim-off">` anchoring `Akai Ito — Your twin dates milli` footer links (`Akai Ito · App · How it works · The model · Simulation`), copy *"You go on one date."*, and `#d2d1cc` structural dividers.
