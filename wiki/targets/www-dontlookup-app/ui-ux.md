---
title: "UI & UX Architecture: www-dontlookup-app"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-dontlookup-app

## Overview & Design Identity
- **Target**: `www-dontlookup-app` (**Don't Look Up — a game about keeping everyone looking down**)
- **Production URL**: [https://www.dontlookup.app/](https://www.dontlookup.app/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3ef` / `#ffffff`)
- **Summary**: You are very rich, very tall, and standing on quite a lot of people. Keep them distracted and they keep paying. Let them look up, and the...
- **Total Clean CSS Variables Extracted**: `24` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Nunito`
- **Body Font Stack**: `Nunito`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `11px`, `15px`, `13px`, `10px`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `11px`, `15px`, `13px`, `10px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body: 'Nunito', ui-rounded, "SF Pro Rounded", system-ui, sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: 16.5px`, `font-weight: 600`, `letter-spacing: 0.11px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f3ef` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#14140f` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffffff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#8a5d02` | `#hud.is-warn .mtxt { color: #8a5d02 }` |
| **Structural Hairline Border** | `#e0dfdb` | `.mitem { border-top: #e0dfdb }` |
| **Variable Token (`--red`)** | `#c0342a` | `var(--red)` in `:root` |
| **Variable Token (`--convert`)** | `#9abeef` | `var(--convert)` in `:root` |
| **Variable Token (`--follow`)** | `#2b5a9b` | `var(--follow)` in `:root` |
| **Variable Token (`--y1`)** | `#f8e08a` | `var(--y1)` in `:root` |
| **Variable Token (`--y2`)** | `#f2c31a` | `var(--y2)` in `:root` |
| **Variable Token (`--y3`)** | `#c98f06` | `var(--y3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#f4f3ef` | Canvas / Surface Token |
| `--ink` | `#14140f` | Typography Ink Token |
| `--red` | `#c0342a` | Color / Atmospheric Token |
| `--btn-h` | `44px` | Dimension / Scale Token |
| `--convert` | `#9abeef` | Color / Atmospheric Token |
| `--follow` | `#2b5a9b` | Color / Atmospheric Token |
| `--y1` | `#f8e08a` | Color / Atmospheric Token |
| `--y2` | `#f2c31a` | Color / Atmospheric Token |
| `--y3` | `#c98f06` | Color / Atmospheric Token |
| `--btn-r` | `14px` | Dimension / Scale Token |
| `--body` | `'Nunito', ui-rounded, "SF Pro Rounded", system-ui, sans-serif` | Dimension / Scale Token |
| `--font` | `var(--body)` | Typography / Scale Token |
| `--hand` | `var(--body)` | Design System Custom Token |
| `--bw` | `2.5px` | Dimension / Scale Token |
| `--lift` | `5px` | Dimension / Scale Token |
| `--rail-n` | `8` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.is-title> — `www-dontlookup-app`)**:
   - Landmark `<header class="is-title">` (`1440px`) hosting `Don't Look Up — a game about keeping` navigation (`here`), DOM attributes (`data-engine="three.js r170"`, `data-id="ball"`, `data-cost="ball"`, `data-id="ball"`), and stylesheet rule `stage { position: fixed; inset: 0; }`.
2. **Hero Stage & Focal Lead (<div.is-asking> — `Don't Look Up — a game about keepi`)**:
   - Landmark `<div class="is-asking">` presenting display lead `Don't Look Up — a game about keeping everyone lo` and copy excerpt *"We count runs, not people. Anonymously, through Google Analytics,"* over `#f4f3ef` canvas and `#14140f` ink.
3. **Primary Showcase & Content Grid (<div.is-teaching> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="is-teaching">` rendering section `Featured Work & Interactive Showcase` with copy *"Keep your eye on the ball, not on the fees."*, asset references (`favicon.ico`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `stage canvas { display: block; touch-action: none; }`.
4. **Interactive Detail & Feature Matrix (<div.mcell> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="mcell">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Raise the fee Use +. This crowd will carry about 30%. Anything yo"*) with `#ffffff` surface cards, `#ffffff` accents, and `bubbles { position: fixed; inset: 0; pointer-events: none; overflow: hidden; }`.
5. **Colophon & Global Directory Footer (<footer.lbl> — `https://www.dontlookup.app/`)**:
   - Landmark `<footer class="lbl">` anchoring `Don't Look Up — a game about kee` footer links (`here`), copy *"Plant a distraction"*, and `#e0dfdb` structural dividers.
