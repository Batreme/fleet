---
title: "UI & UX Architecture: earthwallet-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: earthwallet-com

## Overview & Design Identity
- **Target**: `earthwallet-com` (**Earth Wallet — Real assets for unreal markets**)
- **Production URL**: [https://earthwallet.com/](https://earthwallet.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#03080d` / `#0000ff`)
- **Summary**: Financial claims can be created at will. Metal has to be found, dug and processed. Earth Wallet on hard assets, critical minerals and Can...
- **Total Clean CSS Variables Extracted**: `26` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gilroy`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 66.24px`, `line-height: 66.24px`, `font-weight: 500`, `letter-spacing: -2.9808px`); CSS variables `--font-display: Gilroy,Urbanist,sans-serif`; rule `h1` (`line-height: 1`, `letter-spacing: -.045em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 86.4px`, `font-weight: 600`, `letter-spacing: -0.8px`); rule `h2` (`font-size: clamp(27px,3.35vw,48px)`, `line-height: 1.1`, `letter-spacing: -.055em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 300`); CSS variables `--font-body: Poppins,sans-serif`; rule `p` (`font-size: clamp(24px,3.05vw,47px)`, `line-height: 1.4`, `letter-spacing: -1.2px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 21.6px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -1.188px`); rule `small` (`font-size: 12px`, `letter-spacing: 0`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#03080d` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#263848` | `.mineral-pin { background: #263848 }` |
| **Interactive Accent / Highlight** | `#0000ff` | `button:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#869599` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#2b3338` | `var(--line)` in `:root` (`rgba(202,223,229,.2)`) |
| **Variable Token (`--ink`)** | `#e7efef` | `var(--ink)` in `:root` |
| **Variable Token (`--ew-social-blue`)** | `#2496ff` | `var(--ew-social-blue)` in `:root` |
| **Variable Token (`--ew-social-blue-60`)** | `#7cc0ff` | `var(--ew-social-blue-60)` in `:root` |
| **Variable Token (`--ew-social-blue-20`)** | `#d3eaff` | `var(--ew-social-blue-20)` in `:root` |
| **Variable Token (`--ew-forest-green`)** | `#55d171` | `var(--ew-forest-green)` in `:root` |
| **Variable Token (`--ew-electric-yellow`)** | `#ffd600` | `var(--ew-electric-yellow)` in `:root` |
| **Variable Token (`--ew-gold`)** | `#ffa800` | `var(--ew-gold)` in `:root` |
| **Variable Token (`--ew-electric-violet`)** | `#691fdd` | `var(--ew-electric-violet)` in `:root` |
| **Variable Token (`--ew-electric-violet-60`)** | `#a579eb` | `var(--ew-electric-violet-60)` in `:root` |
| **Variable Token (`--ew-crimson`)** | `#e22d3f` | `var(--ew-crimson)` in `:root` |
| **Variable Token (`--ew-crimson-20`)** | `#f9d5d9` | `var(--ew-crimson-20)` in `:root` |
| **Variable Token (`--ew-moonlight-grey`)** | `#e6e9ed` | `var(--ew-moonlight-grey)` in `:root` |
| **Variable Token (`--ew-shuttle-gray`)** | `#a5acbb` | `var(--ew-shuttle-gray)` in `:root` |
| **Variable Token (`--ew-outer-space`)** | `#0f1726` | `var(--ew-outer-space)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#e7efef` | Typography Ink Token |
| `--muted` | `#869599` | Color / Atmospheric Token |
| `--line` | `rgba(202,223,229,.2)` | Color / Atmospheric Token |
| `--ew-social-blue` | `#2496FF` | Color / Atmospheric Token |
| `--ew-social-blue-60` | `#7CC0FF` | Color / Atmospheric Token |
| `--ew-social-blue-20` | `#D3EAFF` | Color / Atmospheric Token |
| `--ew-forest-green` | `#55D171` | Color / Atmospheric Token |
| `--ew-electric-yellow` | `#FFD600` | Color / Atmospheric Token |
| `--ew-gold` | `#FFA800` | Color / Atmospheric Token |
| `--ew-electric-violet` | `#691FDD` | Color / Atmospheric Token |
| `--ew-electric-violet-60` | `#A579EB` | Color / Atmospheric Token |
| `--ew-crimson` | `#E22D3F` | Color / Atmospheric Token |
| `--ew-crimson-20` | `#F9D5D9` | Color / Atmospheric Token |
| `--ew-moonlight-grey` | `#E6E9ED` | Canvas / Surface Token |
| `--ew-shuttle-gray` | `#A5ACBB` | Color / Atmospheric Token |
| `--ew-outer-space` | `#0F1726` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero-orbit> — `earthwallet-com`)**:
   - Landmark `<header class="hero-orbit">` (`1440x72px`) hosting `Earth Wallet — Real assets for unrea` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-frame-ms="1933.3"`, `data-scene-progress="3.0"`, `data-engine="three.js r160"`), and stylesheet rule `.survey-status { display:none }`.
2. **Hero Stage & Focal Lead (<section.orbit-ui> — `Lookat CanadafromABOVE`)**:
   - Landmark `<section class="orbit-ui">` presenting display lead `Lookat CanadafromABOVE` and copy excerpt *"04 / THE STOCKPILE"* over `#03080d` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.descent-copy> — `Look at Canada from ABOVE`)**:
   - Landmark `<section class="descent-copy">` rendering section `Look at Canada from ABOVE` with copy *"A CHANGE IN PERSPECTIVE"*, asset references (`site.webmanifest`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `.survey-heading h2 { font-size:clamp(27px,3.35vw,48px);line-height:1.1;letter-spacing:-.055em... }`.
4. **Interactive Detail & Feature Matrix (<section.cloud-copy> — `Not from the side.`)**:
   - Landmark `<section class="cloud-copy">` framing `Not from the side.` and `From the ground. Into our future.` (*"Look at Canada from"*) with `#263848` surface cards, `#0000ff` accents, and `.survey-subtitle { font-size:clamp(10px,1vw,14px);line-height:1.4;color:d5dfe8 }`.
5. **Colophon & Global Directory Footer (<footer.planet-rendered> — `https://earthwallet.com/`)**:
   - Landmark `<footer class="planet-rendered">` anchoring `Earth Wallet — Real assets for u` footer links (`Overview · Index · Archive · About · Contact`), copy *"An uninterrupted journey that begins in polar orbit and desc"*, and `#2b3338` structural dividers.
