---
title: "UI & UX Architecture: konkelectrical-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: konkelectrical-com

## Overview & Design Identity
- **Target**: `konkelectrical-com` (**Konk Electrical · Eastern Suburbs Electricians, Sydney**)
- **Production URL**: [https://konkelectrical.com/](https://konkelectrical.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0b0b0c` canvas, `#f6f3ec` ink, `#0068a0` accent)
- **Summary**: Electrical and automation specialists for high-end homes across Sydney's Eastern Suburbs. Lighting, smart home, data and audio visual, wi...
- **Total Clean CSS Variables Extracted**: `41` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 96.48px`, `line-height: 82.9728px`, `font-weight: 800`, `letter-spacing: -3.3768px`); CSS variables `--cc-font-display: 'Archivo', sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 118.4px`, `line-height: 101.824px`, `font-weight: 800`, `letter-spacing: -4.144px`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`); rule `p` (`font-size: clamp(1.02rem,1.25vw,1.16rem)`, `line-height: 1.7`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0b0c` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f6f3ec` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#121214` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0068a0` | `.sbi-feed-block-cta-btn { background: #0068a0 }` |
| **Secondary / Muted Copy** | `#808080` | live computed `hr` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#26262a` | `.kv { border-top: #26262a }` |
| **Variable Token (`--cc-bone`)** | `#f2f0eb` | `var(--cc-bone)` in `:root` |
| **Variable Token (`--cc-steel`)** | `#8c8a84` | `var(--cc-steel)` in `:root` |
| **Variable Token (`--cc-red`)** | `#c89446` | `var(--cc-red)` in `:root` |
| **Variable Token (`--cc-gold`)** | `#e7b96f` | `var(--cc-gold)` in `:root` |
| **Variable Token (`--ink-3`)** | `#17171a` | `var(--ink-3)` in `:root` |
| **Variable Token (`--brass-dim`)** | `#8a6733` | `var(--brass-dim)` in `:root` |
| **Variable Token (`--bronze`)** | `#5b4a33` | `var(--bronze)` in `:root` |
| **Variable Token (`--text`)** | `#e9e7e2` | `var(--text)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-ink` | `#0B0B0C` | Typography Ink Token |
| `--cc-bone` | `#F2F0EB` | Color / Atmospheric Token |
| `--cc-steel` | `#8C8A84` | Color / Atmospheric Token |
| `--cc-red` | `#C89446` | Color / Atmospheric Token |
| `--cc-gold` | `#E7B96F` | Color / Atmospheric Token |
| `--cc-font-display` | `'Archivo', sans-serif` | Typography / Scale Token |
| `--ink` | `#0b0b0c` | Typography Ink Token |
| `--ink-2` | `#121214` | Typography Ink Token |
| `--ink-3` | `#17171a` | Typography Ink Token |
| `--hair` | `#26262a` | Color / Atmospheric Token |
| `--paper` | `#f2f0eb` | Canvas / Surface Token |
| `--brass` | `#c89446` | Color / Atmospheric Token |
| `--brass-hi` | `#e7b96f` | Color / Atmospheric Token |
| `--brass-dim` | `#8a6733` | Color / Atmospheric Token |
| `--bronze` | `#5b4a33` | Color / Atmospheric Token |
| `--text` | `#e9e7e2` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hdr> — `konkelectrical-com`)**:
   - Landmark `<header class="hdr">` (`1440x90px`) hosting `Konk Electrical · Eastern Suburbs El` navigation (`Home · About · Electrical · Automation · Data & Networking`), DOM attributes (`data-section="header"`, `data-label="Header"`, `data-locked`, `data-header`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.tf> — `ELECTRICAL AND AUTOMATION`)**:
   - Landmark `<section class="tf">` presenting display lead `ELECTRICAL AND AUTOMATION` and copy excerpt *"From repairs and alterations to complete renovations, new builds "* over `#0b0b0c` canvas and `#f6f3ec` ink.
3. **Primary Showcase & Content Grid (<section.cc-page-home> — `Data & Networking`)**:
   - Landmark `<section class="cc-page-home">` rendering section `Data & Networking` with copy *"Effortless control"*, asset references (`xfavicon.png,qv=1793266697.pagesp...`, `A.fonts.css,,qv==1793266697+style...`, `xkonk-logo-white.png,qv=179326669... (Konk Electrical)`, `xkonk-logo-white.png,qv=179326669... (Konk Electrical)`), and grid rule `html { -webkit-text-size-adjust:100%;scroll-behavior:smooth }`.
4. **Interactive Detail & Feature Matrix (<section.konk-load> — `Audio Visual`)**:
   - Landmark `<section class="konk-load">` framing `Audio Visual` and `Send an enquiry` (*"Lighting, climate, security and entertainment through one intuiti"*) with `#121214` surface cards, `#0068a0` accents, and `video { display:block;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.ftr> — `https://konkelectrical.com/`)**:
   - Landmark `<footer class="ftr">` anchoring `Konk Electrical · Eastern Suburb` footer links (`Home · About · Electrical · Automation · Data & Networking`), copy *"Structured cabling and whole-home Wi-Fi that keeps every dev"*, and `#26262a` structural dividers.
