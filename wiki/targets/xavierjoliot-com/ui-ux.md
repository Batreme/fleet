---
title: "UI & UX Architecture: xavierjoliot-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: xavierjoliot-com

## Overview & Design Identity
- **Target**: `xavierjoliot-com` (**Xavier Joliot · Développeur Créatif**)
- **Production URL**: [https://xavierjoliot.com](https://xavierjoliot.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1c1730` / `#ffd23f`)
- **Summary**: Xavier Joliot, développeur créatif à Béziers : branding, UI/UX, stratégie, développement full-stack et mise en production. Disponible imm...
- **Total Clean CSS Variables Extracted**: `37` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Mono`
- **Body Font Stack**: `Space Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: observed font-size ladder: `15px`, `14.5px`, `13px`, `12px`, `1em`
- **Section Heading (`H2`)**: rule `h2` (`font-size: 22px`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`); rule `p` (`font-size: 13.5px`, `line-height: 1.65`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13px`, `line-height: 13px`, `font-weight: 600`, `letter-spacing: 1.82px`); CSS variables `--default-mono-font-family: var(--font-mono)`; rule `small` (`letter-spacing: .16em`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#1c1730` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f4ead9` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0b0907` | live computed `main` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffd23f` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ffd23f` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3a2f5e` | `var(--line)` in `:root` |
| **Variable Token (`--ok`)** | `#3ddc84` | `var(--ok)` in `:root` |
| **Variable Token (`--bg`)** | `#0d0a1a` | `var(--bg)` in `:root` |
| **Variable Token (`--scr`)** | `#110d20` | `var(--scr)` in `:root` |
| **Variable Token (`--dim`)** | `#9a8fb5` | `var(--dim)` in `:root` |
| **Variable Token (`--a1`)** | `#ff5a36` | `var(--a1)` in `:root` |
| **Variable Token (`--a3`)** | `#2ec4b6` | `var(--a3)` in `:root` |
| **Variable Token (`--a4`)** | `#e0366f` | `var(--a4)` in `:root` |
| **Variable Token (`--key`)** | `#d9d0e8` | `var(--key)` in `:root` |
| **Variable Token (`--keyt`)** | `#1d1630` | `var(--keyt)` in `:root` |
| **Variable Token (`--r0`)** | `#ffe066` | `var(--r0)` in `:root` |
| **Variable Token (`--r2`)** | `#ff9f3a` | `var(--r2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ok` | `#3ddc84` | Color / Atmospheric Token |
| `--bg` | `#0d0a1a` | Canvas / Surface Token |
| `--scr` | `#110d20` | Color / Atmospheric Token |
| `--ink` | `#f4ead9` | Typography Ink Token |
| `--dim` | `#9a8fb5` | Color / Atmospheric Token |
| `--a1` | `#ff5a36` | Color / Atmospheric Token |
| `--a2` | `#ffd23f` | Color / Atmospheric Token |
| `--a3` | `#2ec4b6` | Color / Atmospheric Token |
| `--a4` | `#e0366f` | Color / Atmospheric Token |
| `--line` | `#3a2f5e` | Color / Atmospheric Token |
| `--ch` | `#1c1730` | Color / Atmospheric Token |
| `--key` | `#d9d0e8` | Color / Atmospheric Token |
| `--keyt` | `#1d1630` | Color / Atmospheric Token |
| `--r0` | `#ffe066` | Color / Atmospheric Token |
| `--r1` | `#ffd23f` | Color / Atmospheric Token |
| `--r2` | `#ff9f3a` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top> — `xavierjoliot-com`)**:
   - Landmark `<header class="top">` (`1420x36px`) hosting `Xavier Joliot · Développeur Créatif` navigation (`FR · EN`), DOM attributes (`data-boot="off"`, `data-precedence="next"`, `data-label="Connexion"`, `data-n="1"`), and stylesheet rule `nded_fdf5727d-module__3a_gmq__cla... { font-family:Unbounded,Unbounded Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.screen> — `Xavier Joliot · Développeur Créati`)**:
   - Landmark `<section class="screen">` presenting display lead `Xavier Joliot · Développeur Créatif` and copy excerpt *"Je pense la marque, je conçois l'interface, je développe le produ"* over `#1c1730` canvas and `#f4ead9` ink.
3. **Primary Showcase & Content Grid (<section.screen:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="screen">` rendering section `Featured Work & Interactive Showcase` with copy *"3615 Développeur créatif"*, asset references (`0c8c4ded07fff55c-s.p.5c4452a7.woff2`, `1ccf8ef962b3f693-s.p.1edb596a.woff2`, `374a88ea0960b3d4-s.p.eb0a589c.woff2`, `8d05cfa5faa8406c-s.p.4adea45d.woff2`), and grid rule `unded_fdf5727d-module__3a_gmq__va... { --font-unbounded:"Unbounded","Unbounded Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.screen:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="screen">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"© 2026 Xavier Joliot"*) with `#0b0907` surface cards, `#ffd23f` accents, and `etch_f484a735-module__S-MHga__cla... { font-family:Chakra Petch,Chakra Petch Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.sp> — `https://xavierjoliot.com`)**:
   - Landmark `<footer class="sp">` anchoring `Xavier Joliot · Développeur Créa` footer links (`FR · EN`), copy *"Développement · Branding · UI/UX · Stratégie"*, and `#3a2f5e` structural dividers.
