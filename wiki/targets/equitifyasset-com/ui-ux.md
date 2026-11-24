---
title: "UI & UX Architecture: equitifyasset-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: equitifyasset-com

## Overview & Design Identity
- **Target**: `equitifyasset-com` (**EquitiFy Assets · Home**)
- **Production URL**: [https://equitifyasset.com/](https://equitifyasset.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fbfbfb` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: We source off-market commercial property, run the acquisition end to end, and hand you 100% ownership. No syndicates, no partners.
- **Total Clean CSS Variables Extracted**: `96` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aspekta Variable Variable`
- **Body Font Stack**: `Aspekta Variable Variable Placeholder`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78.88px`, `line-height: 78.88px`, `font-weight: 400`, `letter-spacing: -2.3664px`); rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1em`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`, `letter-spacing: -1.92px`); rule `h2` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.1em`, `letter-spacing: -.04em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.3em`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fbfbfb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#c83e07` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `var(--border-color)` in `:root` |
| **Variable Token (`--token-f277370d-904c-4e87-88c6-49451f154e33`)** | `#d1ff00` | `var(--token-f277370d-904c-4e87-88c6-49451f154e33)` in `:root` |
| **Variable Token (`--token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f`)** | `#f4f4e8` | `var(--token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f)` in `:root` |
| **Variable Token (`--token-82d92470-f077-4c9d-9673-709d01132847`)** | `#534f4d` | `var(--token-82d92470-f077-4c9d-9673-709d01132847)` in `:root` |
| **Variable Token (`--token-1486dbb4-cc20-4852-a20d-db81362153cb`)** | `#bcbcbc` | `var(--token-1486dbb4-cc20-4852-a20d-db81362153cb)` in `:root` |
| **Variable Token (`--token-08d07ee3-fce8-41f2-9d02-9c41009dd49d`)** | `#3d3d3d` | `var(--token-08d07ee3-fce8-41f2-9d02-9c41009dd49d)` in `:root` |
| **Variable Token (`--token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284`)** | `#1c1e19` | `var(--token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284)` in `:root` |
| **Variable Token (`--token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3`)** | `#ffffed` | `var(--token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3)` in `:root` |
| **Variable Token (`--token-5e7f03a9-6226-4578-8399-febb83abe7c0`)** | `#050505` | `var(--token-5e7f03a9-6226-4578-8399-febb83abe7c0)` in `:root` |
| **Variable Token (`--token-b22324d1-617e-4b7c-9516-d41489048918`)** | `#9c9c9c` | `var(--token-b22324d1-617e-4b7c-9516-d41489048918)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-e5145d68-ee3f-43dc-8638-41389fb43644` | `#e2e2e2` | Color / Atmospheric Token |
| `--token-f277370d-904c-4e87-88c6-49451f154e33` | `#d1ff00` | Color / Atmospheric Token |
| `--token-d33926f3-e1ef-47a7-a2fc-872ea608e7c8` | `#000` | Color / Atmospheric Token |
| `--token-33c8dbd0-eb94-4e90-8099-e7a3fee4ad2f` | `#f4f4e8` | Color / Atmospheric Token |
| `--token-82d92470-f077-4c9d-9673-709d01132847` | `#534f4d` | Color / Atmospheric Token |
| `--token-1486dbb4-cc20-4852-a20d-db81362153cb` | `#bcbcbc` | Color / Atmospheric Token |
| `--token-08d07ee3-fce8-41f2-9d02-9c41009dd49d` | `#3d3d3d` | Color / Atmospheric Token |
| `--token-6e62038c-0066-4a2a-9fbd-3ca05d5d5284` | `#1c1e19` | Color / Atmospheric Token |
| `--token-27d215b1-9859-4ed9-910b-49be7f89fc94` | `#fbfbfb` | Color / Atmospheric Token |
| `--token-52433e3c-3bdd-4e8f-b4eb-8bd6681644d3` | `#ffffed` | Color / Atmospheric Token |
| `--token-19fadcaa-97dd-4766-8f90-eb9a72bcc235` | `#c83e07` | Color / Atmospheric Token |
| `--token-a5e091a2-859c-44ea-91df-ecdc98f39d88` | `#f4f4e8` | Color / Atmospheric Token |
| `--token-1f8b4914-6c8e-4506-b0ec-24a02142f4ba` | `#d1ff00` | Color / Atmospheric Token |
| `--token-5e7f03a9-6226-4578-8399-febb83abe7c0` | `#050505` | Color / Atmospheric Token |
| `--token-b5be0a90-9b43-4c58-8ca5-f5dd60fafe9f` | `#bcbcbc` | Color / Atmospheric Token |
| `--token-b22324d1-617e-4b7c-9516-d41489048918` | `#9c9c9c26` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.framer-ebH8S> — `equitifyasset-com`)**:
   - Landmark `<header class="framer-ebH8S">` (`1440px`) hosting `EquitiFy Assets · Home` navigation (`Home · How We Work · Properties · about us · Contact Us`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<div.framer-7dSme> — `100%`)**:
   - Landmark `<div class="framer-7dSme">` presenting display lead `100%` and copy excerpt *"EquitiFy Assets sources off-market commercial properties built ar"* over `#fbfbfb` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.framer-b5Z7g> — `Tax Benefits`)**:
   - Landmark `<div class="framer-b5Z7g">` rendering section `Tax Benefits` with copy *"We run the deal end-to-end. You keep 100%."*, asset references (`suGqY6sVqYrEl8vVN4Ar3ufRvmw.png`, `p8gmopxLkGo6Ily14ZQSTHPOFo0.png`, `3TkAWwL2xbK4k3fwlVTZWqigw.png`, `script`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<div.framer-4qNhg> — `W h e r e C a p i t a l B e c o m `)**:
   - Landmark `<div class="framer-4qNhg">` framing `W h e r e C a p i t a l B e c o m e s O w n e r s...` and `Exclusive Access` (*"The best properties never reach a listing. Ours come through an o"*) with `#c83e07` surface cards, `#0000ee` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.framer-UGi5s> — `https://equitifyasset.com/`)**:
   - Landmark `<footer class="framer-UGi5s framer-m1Hmn">` anchoring `EquitiFy Assets · Home` footer links (`Home · How We Work · Properties · about us · Contact Us`), copy *"We buy the same properties we bring to you, in the same mark"*, and `#e2e2e2` structural dividers.
