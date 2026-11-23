---
title: "UI & UX Architecture: www-huxleysaga-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-huxleysaga-com

## Overview & Design Identity
- **Target**: `www-huxleysaga-com` (**Huxley · Home**)
- **Production URL**: [https://www.huxleysaga.com/](https://www.huxleysaga.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0000`)
- **Summary**: The HUXLEY® saga is an original sci-fi universe created by renowned concept artist Ben Mauro. Explore all the books, products, artwork an...
- **Total Clean CSS Variables Extracted**: `228` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NB Architekt Light`
- **Body Font Stack**: `NB Architekt Regular`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78.3014px`, `line-height: 70.4712px`, `font-weight: 300`, `letter-spacing: 1.6px`); rule `,h1` (`font-size: clamp(80px,80px + 0vw,80px)`, `line-height: 90%`, `letter-spacing: 1.6px`, `font-weight: 300`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 400`, `letter-spacing: 1.2px`); rule `,h2` (`font-size: clamp(32px,32px + 0vw,32px)`, `line-height: 100%`, `letter-spacing: 1.92px`, `font-weight: 300`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `,p` (`letter-spacing: 12%`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1a1a1a` | `.page-showcase .showcase-box--h { background: #1a1a1a }` |
| **Interactive Accent / Highlight** | `#ff0000` | `:root .--red { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#666666` | `:root .--grey2 { color: #666666 }` |
| **Structural Hairline Border** | `#ffffff` | `.cta>span { border-bottom: #ffffff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `#fff` | Canvas / Surface Token |
| `--white-0` | `hsla(0,0%,100%,0)` | Canvas / Surface Token |
| `--white-5` | `hsla(0,0%,100%,.05)` | Canvas / Surface Token |
| `--white-10` | `hsla(0,0%,100%,.1)` | Canvas / Surface Token |
| `--white-15` | `hsla(0,0%,100%,.15)` | Canvas / Surface Token |
| `--white-20` | `hsla(0,0%,100%,.2)` | Canvas / Surface Token |
| `--white-25` | `hsla(0,0%,100%,.25)` | Canvas / Surface Token |
| `--white-30` | `hsla(0,0%,100%,.3)` | Canvas / Surface Token |
| `--white-35` | `hsla(0,0%,100%,.35)` | Canvas / Surface Token |
| `--white-40` | `hsla(0,0%,100%,.4)` | Canvas / Surface Token |
| `--white-45` | `hsla(0,0%,100%,.45)` | Canvas / Surface Token |
| `--white-50` | `hsla(0,0%,100%,.5)` | Canvas / Surface Token |
| `--white-55` | `hsla(0,0%,100%,.55)` | Canvas / Surface Token |
| `--white-60` | `hsla(0,0%,100%,.6)` | Canvas / Surface Token |
| `--white-65` | `hsla(0,0%,100%,.65)` | Canvas / Surface Token |
| `--white-70` | `hsla(0,0%,100%,.7)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.e-nav> — `www-huxleysaga-com`)**:
   - Landmark `<header class="e-nav">` (`1440x39px`) hosting `Huxley · Home` navigation (`H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`), DOM attributes (`data-hid="gtm"`, `data-hid="gtm-noscript"`, `data-hid="no-js-style"`, `data-v-db217464`), and stylesheet rule `root { --white:fff }`.
2. **Hero Stage & Focal Lead (<section.s-banner-hero> — `10.23.26`)**:
   - Landmark `<section class="s-banner-hero">` presenting display lead `10.23.26` and copy excerpt *"A post-apocalyptic sci-fi universe"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.s-small-header> — `The HUXLEY® saga`)**:
   - Landmark `<section class="s-small-header">` rendering section `The HUXLEY® saga` with copy *"S c r o l l t o e x p l o r e"*, asset references (`gtm.js`, `entry.B21Z6f7r.css`, `SvgMask.Bd2uXaPf.css`, `LabelHighlight.DTuRQ1tQ.css`), and grid rule `root .--white { color:fff }`.
4. **Interactive Detail & Feature Matrix (<section.s-featured> — `An original sci-fi universe create`)**:
   - Landmark `<section class="s-featured">` framing `An original sci-fi universe created by renowned c...` and `STORY` (*"V I E W T H E O R A C L E"*) with `#1a1a1a` surface cards, `#ff0000` accents, and `root .--white-0 { color:fff0 }`.
5. **Colophon & Global Directory Footer (<footer.e-footer> — `https://www.huxleysaga.com/`)**:
   - Landmark `<footer class="e-footer layout-block">` anchoring `Huxley · Home` footer links (`H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`), copy *"V I E W H U X L E Y"*, and `#ffffff` structural dividers.
