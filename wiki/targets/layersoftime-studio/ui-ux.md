---
title: "UI & UX Architecture: layersoftime-studio"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: layersoftime-studio

## Overview & Design Identity
- **Target**: `layersoftime-studio` (**LAYERS OF TIME — The show runs on our clock.**)
- **Production URL**: [https://layersoftime.studio/](https://layersoftime.studio/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#08090b` / `#8a9099`)
- **Summary**: LAYERS OF TIME is a show studio in Singapore. We design light, video and sound for live rooms, and we build the engine that keeps all of...
- **Total Clean CSS Variables Extracted**: `35` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Söhne`
- **Body Font Stack**: `Söhne`
- **Monospace / Technical Font Stack**: `Söhne Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 115.2px`, `line-height: 109.44px`, `font-weight: 500`, `letter-spacing: -4.032px`); CSS variables `--fs-h1: clamp(2.25rem, 5.5vw, 5.5rem)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 51.84px`, `line-height: 52.8768px`, `font-weight: 500`, `letter-spacing: -1.296px`); CSS variables `--fs-h2: clamp(1.75rem, 3.6vw, 3.5rem)`; rule `h2` (`font-size: var(--fs-h3)`, `letter-spacing: -.015em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--fs-body: 1.0625rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--fs-small: .9375rem`, `--fs-label: .75rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#08090b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#e9ecef` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0e1013` | `var(--panel)` in `:root` |
| **Interactive Accent / Highlight** | `#8a9099` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#8a9099` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#232527` | `var(--line)` in `:root` (`e9ecef1f`) |
| **Variable Token (`--panel-2`)** | `#14171b` | `var(--panel-2)` in `:root` |
| **Variable Token (`--faint`)** | `#767c85` | `var(--faint)` in `:root` |
| **Variable Token (`--signal`)** | `#d4178f` | `var(--signal)` in `:root` |
| **Variable Token (`--signal-live`)** | `#ff29c4` | `var(--signal-live)` in `:root` |
| **Variable Token (`--signal-fill`)** | `#8f0e66` | `var(--signal-fill)` in `:root` |
| **Variable Token (`--parallax`)** | `#22d3ee` | `var(--parallax)` in `:root` |
| **Variable Token (`--parsec`)** | `#a3e635` | `var(--parsec)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#08090b` | Canvas / Surface Token |
| `--panel` | `#0e1013` | Color / Atmospheric Token |
| `--panel-2` | `#14171b` | Color / Atmospheric Token |
| `--fg` | `#e9ecef` | Typography Ink Token |
| `--muted` | `#8a9099` | Color / Atmospheric Token |
| `--faint` | `#767c85` | Color / Atmospheric Token |
| `--line` | `#e9ecef1f` | Color / Atmospheric Token |
| `--line-strong` | `#e9ecef47` | Color / Atmospheric Token |
| `--signal` | `#d4178f` | Color / Atmospheric Token |
| `--signal-live` | `#ff29c4` | Color / Atmospheric Token |
| `--signal-fill` | `#8f0e66` | Color / Atmospheric Token |
| `--parallax` | `#22d3ee` | Color / Atmospheric Token |
| `--parsec` | `#a3e635` | Color / Atmospheric Token |
| `--ease` | `cubic-bezier(.22, .61, .36, 1)` | Motion / Easing Token |
| `--d-fast` | `.16s` | Motion / Timing Token |
| `--d-base` | `.32s` | Motion / Timing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `layersoftime-studio`)**:
   - Landmark `<header class="header">` (`1440x64px`) hosting `LAYERS OF TIME — The show runs on ou` navigation (`Work · Studio · Software · Log · Contact`), DOM attributes (`data-theme="dark"`, `data-astro-exec`, `data-header`, `data-astro-cid-nen7h5rs`), and stylesheet rule `.brand__mark { flex:none;width:17px;height:20px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `The show runs on our clock.`)**:
   - Landmark `<section class="hero">` presenting display lead `The show runs on our clock.` and copy excerpt *"The mark is a rig. Ten fixtures, replaying a night recorded throu"* over `#08090b` canvas and `#e9ecef` ink.
3. **Primary Showcase & Content Grid (<section.chapter> — `A show studio in Singapore that bu`)**:
   - Landmark `<section class="chapter chapter--light">` rendering section `A show studio in Singapore that builds the softwa...` with copy *"Your clock 22:54:01:21 EST"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `soehne-kraftig.woff2`, `soehne-buch.woff2`), and grid rule `hover { color:var(--fg) }`.
4. **Interactive Detail & Feature Matrix (<section.section-tight> — `Rooms we have run.`)**:
   - Landmark `<section class="section-tight">` framing `Rooms we have run.` and `Built on tour, between soundcheck and doors.` (*"Next night Singapore · Pasir Panjang Power Station · 4d 23h 05m"*) with `#0e1013` surface cards, `#8a9099` accents, and `.footer__mark { flex:none;width:44px;height:52px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://layersoftime.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `LAYERS OF TIME — The show runs o` footer links (`Work · Studio · Software · Log · Contact`), copy *"Singapore · Pasir Panjang Power Station · 4d 23h 05m"*, and `#232527` structural dividers.
