---
title: "UI & UX Architecture: actl-me"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: actl-me

## Overview & Design Identity
- **Target**: `actl-me` (**ACTL — Arabian Community Tennis League**)
- **Production URL**: [https://actl.me/](https://actl.me/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a2952` / `#000080`)
- **Summary**: Find your next tennis match in Dubai. Discover the ACTL community, challenge players, follow your ranking and explore ACTL merchandise.
- **Total Clean CSS Variables Extracted**: `5` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Georgia`
- **Body Font Stack**: `montreal`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 118.08px`, `line-height: 122.803px`, `font-weight: 700`, `letter-spacing: -4.1328px`); rule `h1` (`font-size: clamp(60px,14vw,90px)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 93.6px`, `line-height: 97.344px`, `font-weight: 700`, `letter-spacing: -3.276px`); rule `,h2` (`line-height: 1.04`, `letter-spacing: -.035em`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-body: "montreal", "montreal Fallback"`; rule `p` (`font-size: 15px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: normal`, `font-weight: 400`); rule `small` (`font-size: 16px`, `letter-spacing: 0`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a2952` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ede6c4` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000080` | `body { background: navy }` (`#000080`) |
| **Interactive Accent / Highlight** | `#000080` | `.collection-colours button { color: navy }` (`#000080`) |
| **Secondary / Muted Copy** | `#8d251a` | `.checkout-error { color: #8d251a }` |
| **Structural Hairline Border** | `#6e7c84` | `.header-cta { border: #6e7c84 }` |
| **Variable Token (`--lime`)** | `#aaf136` | `var(--lime)` in `:root` |
| **Variable Token (`--paper`)** | `#f4f4f2` | `var(--paper)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--navy` | `#0a2952` | Layout / Spatial Grid Token |
| `--lime` | `#aaf136` | Color / Atmospheric Token |
| `--cream` | `#ede6c4` | Color / Atmospheric Token |
| `--paper` | `#f4f4f2` | Canvas / Surface Token |
| `--font-body` | `"montreal", "montreal Fallback"` | Typography / Scale Token |
| `--actl-me-bg` | `#0a2952` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--actl-me-ink` | `#ede6c4` | Primary Typography Ink (computed-derived) |
| `--actl-me-surface` | `#000080` | Surface Substrate (computed-derived) |
| `--actl-me-accent` | `#000080` | Interactive Accent (computed-derived) |
| `--actl-me-muted` | `#8d251a` | Secondary Ink (computed-derived) |
| `--actl-me-border` | `#6e7c84` | Structural Border (computed-derived) |
| `--actl-me-container` | `1440px` | Container Bound (computed-derived) |
| `--actl-me-gap` | `28px` | Grid Gutter (computed-derived) |
| `--actl-me-pad` | `26px` | Lateral Padding (computed-derived) |
| `--actl-me-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--actl-me-radius` | `30px` | Corner Radius (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `actl-me`)**:
   - Landmark `<header class="header">` (`1325x68px`) hosting `ACTL — Arabian Community Tennis Leag` navigation (`The league · The app · The shop · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r185"`, `data-reveal="true"`, `data-reveal="true"`), and stylesheet rule `real_ae148c7a-module__pSTb6W__cla... { font-family:montreal,montreal Fallback }`.
2. **Hero Stage & Focal Lead (<section.league> — `Find your people.`)**:
   - Landmark `<section class="league section">` presenting display lead `Find your people.` and copy excerpt *"Arabian Community Tennis League · Dubai"* over `#0a2952` canvas and `#ede6c4` ink.
3. **Primary Showcase & Content Grid (<section.app> — `Your kind of tennis.`)**:
   - Landmark `<section class="app section">` rendering section `Your kind of tennis.` with copy *"A shared court. A new rival. A reason to play again. Welcome to A"*, asset references (`NeueMontreal_Bold-s.p.1cs3sgkx_vm...`, `NeueMontreal_Regular-s.p.3qaxr7gv...`, `actl-logo.png`, `0xt1j8hd4-iqd.css`), and grid rule `treal_ae148c7a-module__pSTb6W__va... { --font-body:"montreal", "montreal Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.match-section> — `Less organising. More playing.`)**:
   - Landmark `<section class="match-section section">` framing `Less organising. More playing.` and `One more set? Always.` (*"More than the match"*) with `#000080` surface cards, `#000080` accents, and `root { --navy:0a2952;--lime:aaf136;--cream:ede6c4;--paper:f4f4f2 }`.
5. **Colophon & Global Directory Footer (<footer.header-cta> — `https://actl.me/`)**:
   - Landmark `<footer class="header-cta">` anchoring `ACTL — Arabian Community Tennis ` footer links (`The league · The app · The shop · Contact`), copy *"A little competition. A lot of community."*, and `#6e7c84` structural dividers.
