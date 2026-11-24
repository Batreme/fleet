---
title: "UI & UX Architecture: both-sides-the7eye-org-il_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: both-sides-the7eye-org-il_en

## Overview & Design Identity
- **Target**: `both-sides-the7eye-org-il_en` (**Extremists on Both Sides**)
- **Production URL**: [https://both-sides.the7eye.org.il/en/](https://both-sides.the7eye.org.il/en/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×3312px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fdfcff` / `#25d366`)
- **Summary**: We collected thousands of political actions carried out in public space over the past four years. Decide for yourself — who are the extre...
- **Total Clean CSS Variables Extracted**: `91` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Discordia`
- **Body Font Stack**: `Assistant`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 54px`, `font-weight: 400`); CSS variables `--se-cap-display: block`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 43.2px`, `font-weight: 400`); rule `.section-title` (`font-size: 36px`, `line-height: 1.2`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-body: 'Assistant', sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fdfcff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `age9-layout-v2 #page9ZoneAbove... { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#25d366` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#767676` | `var(--muted-ui)` in `:root` |
| **Structural Hairline Border** | `#e1e1e1` | `var(--line-light)` in `:root` |
| **Variable Token (`--ink`)** | `#111111` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#FDFCFF` | Canvas / Surface Token |
| `--card-w` | `min(456px, 100vw - 48px)` | Dimension / Scale Token |
| `--card-top` | `4.4vh` | Dimension / Scale Token |
| `--ink` | `#111` | Typography Ink Token |
| `--ink-soft` | `rgba(0, 0, 0, 0.81)` | Typography Ink Token |
| `--ink-note` | `rgba(0, 0, 0, 0.85)` | Typography Ink Token |
| `--muted-ui` | `#767676` | Color / Atmospheric Token |
| `--line-light` | `#E1E1E1` | Canvas / Surface Token |
| `--font-body` | `'Assistant', sans-serif` | Typography / Scale Token |
| `--font-title` | `'Discordia', serif` | Typography / Scale Token |
| `--font-ar` | `'IBM Plex Sans Arabic', 'Assistant', sans-serif` | Typography / Scale Token |
| `--ui-fade-ms` | `180ms` | Motion / Timing Token |
| `--tray-ms` | `.85s` | Motion / Timing Token |
| `--tray-ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--fade-ms` | `.35s` | Motion / Timing Token |
| `--p9-pop-ms` | `280ms` | Motion / Timing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lang-wrap> — `both-sides-the7eye-org-il_en`)**:
   - Landmark `<nav class="lang-wrap">` (`57x28px`) hosting `Extremists on Both Sides` navigation (`עברית · English · العربية`), DOM attributes (`data-page="0"`, `data-page="1"`, `data-page="2"`, `data-page="3"`), and stylesheet rule `html { touch-action: pan-x pan-y; }`.
2. **Hero Stage & Focal Lead (<section.text-section> — `Extremists on Both Sides`)**:
   - Landmark `<section class="text-section">` presenting display lead `Extremists on Both Sides` and copy excerpt *"The project shows 14,877 documented political actions that took p"* over `#fdfcff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.text-section:nth(2)> — `In recent years, Israeli citizens `)**:
   - Landmark `<section class="text-section">` rendering section `In recent years, Israeli citizens have become div...` with copy *"An analysis of political activity across Israel’s political camps"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`), and grid rule `body { background: var(--bg); }`.
4. **Interactive Detail & Feature Matrix (<section.text-section:nth(3)> — `Both camps include groups that bri`)**:
   - Landmark `<section class="text-section">` framing `Both camps include groups that bring their politi...` and `Because of their on-the-ground activity, these gr...` (*"Hover over a square to view the event description and scale."*) with `#ffffff` surface cards, `#25d366` accents, and `after { -webkit-user-select: none !important; user-select: none !important; -web... }`.
5. **Colophon & Global Directory Footer (<footer.page0-dots-overlay> — `https://both-sides.the7eye.org.il/en/`)**:
   - Landmark `<footer class="page0-dots-overlay">` anchoring `Extremists on Both Sides` footer links (`עברית · English · العربية`), copy *"Press and hold a square to view the event description and sc"*, and `#e1e1e1` structural dividers.
