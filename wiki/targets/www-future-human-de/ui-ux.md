---
title: "UI & UX Architecture: www-future-human-de"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-future-human-de

## Overview & Design Identity
- **Target**: `www-future-human-de` (**FUTURE HUMAN · A Shared Year of Co-Creation & Presence**)
- **Production URL**: [https://www.future-human.de/](https://www.future-human.de/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff9ea` canvas, `#000000` ink, `#ffffff` accent)
- **Summary**: A one-year training for multidimensional coaching & co-creation. 8 modules, 16 participants, at Das HILLA near Kassel. Starts Oct 30, 2026.
- **Total Clean CSS Variables Extracted**: `30` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Spectral`
- **Body Font Stack**: `Plus Jakarta Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 36px`, `line-height: 36px`, `font-weight: 300`, `letter-spacing: -1.44px`); rule `h1` (`font-size: 32px`, `line-height: 110%`, `letter-spacing: -.04em`, `font-weight: 300`)
- **Section Heading (`H2`)**: observed font-size ladder: `36px`, `12px`, `18px`, `var(--font-size)`, `var(--framer-font-size)`
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 18px`, `line-height: 140%`, `letter-spacing: -.02em`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fff9ea` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fff9ea` | transparent/inherited card surface over live computed `body` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffffff` | `#__framer-editorbar-button { color: #ffffff }` |
| **Secondary / Muted Copy** | `#0099ff` | `.framer-S82Lr .framer-jkecn2 { color: #0099ff }` |
| **Structural Hairline Border** | `#0099ff` | hairline divider derived from `.framer-S82Lr .framer-jkecn2 { color: #0099ff }` |
| **Variable Token (`--token-5d91ee23-be21-4524-9b74-738a7ee13f13`)** | `#121212` | `var(--token-5d91ee23-be21-4524-9b74-738a7ee13f13)` in `:root` |
| **Variable Token (`--token-30996a26-1fe4-4007-9944-c80e3f142e44`)** | `#fffefc` | `var(--token-30996a26-1fe4-4007-9944-c80e3f142e44)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-0ae2222e-ae06-4270-a415-3dc68910790b` | `#fff9ea` | Color / Atmospheric Token |
| `--token-b6e76abb-dcfc-435b-9de5-4434133bc927` | `#fff9eacc` | Color / Atmospheric Token |
| `--token-5d91ee23-be21-4524-9b74-738a7ee13f13` | `#121212` | Color / Atmospheric Token |
| `--token-30996a26-1fe4-4007-9944-c80e3f142e44` | `#fffefc` | Color / Atmospheric Token |
| `--token-5f5766cb-e316-4651-8423-ae295a71112c` | `#fff` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |
| `--line-height` | `var(--framer-line-height)` | Typography / Scale Token |
| `--overflow-clip-fallback` | `hidden` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.framer-1m76co> — `www-future-human-de`)**:
   - Landmark `<nav class="framer-1m76co">` (`152x24px`) hosting `FUTURE HUMAN · A Shared Year of Co-C` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-16vyecu> — `THE FUTURE IS HUMAN.`)**:
   - Landmark `<section class="framer-16vyecu sct-room">` presenting display lead `THE FUTURE IS HUMAN.` and copy excerpt *"Die Welt braucht deine einzigartige Gabe."* over `#fff9ea` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.framer-1omsice> — `T H E F U T U R E I S H U M A N .`)**:
   - Landmark `<section class="framer-1omsice sct-room">` rendering section `T H E F U T U R E I S H U M A N .` with copy *"D i e W e l t b r a u c h t d e i n e e i n z i g a r t i g e G a"*, asset references (`GAHKwEi2fQdp0x0qCbx0ph5tnCs.png`, `fonts.gstatic.com`, `hls.min.js`, `script`), and grid rule `.hidden-181529u { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-i64cag> — `T h e M u l t i d i m e n s i o n `)**:
   - Landmark `<section class="framer-i64cag sct-room">` framing `T h e M u l t i d i m e n s i o n a l H u m a n` and `T h e C o l l e c t i v e F i e l d` (*"e i n z i g a r t i g e"*) with `#fff9ea` surface cards, `#ffffff` accents, and `.hidden-126ue0n { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-1818ei9> — `https://www.future-human.de/`)**:
   - Landmark `<footer class="framer-1818ei9">` anchoring `FUTURE HUMAN · A Shared Year of ` footer links (`Overview · Index · Archive · About · Contact`), copy *"M u l t i d i m e n s i o n a l"*, and `#0099ff` structural dividers.
