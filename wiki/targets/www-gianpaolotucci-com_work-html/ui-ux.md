---
title: "UI & UX Architecture: www-gianpaolotucci-com_work-html"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-gianpaolotucci-com_work-html

## Overview & Design Identity
- **Target**: `www-gianpaolotucci-com_work-html` (**Gianpaolo Tucci — Creative Director, Berlin · AI-native experiences**)
- **Production URL**: [https://www.gianpaolotucci.com/work.html](https://www.gianpaolotucci.com/work.html)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×2484px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f1e7` / `#1f2bd6`)
- **Summary**: Gianpaolo Tucci is a Berlin-based creative director and experience design director shaping AI-native products, luxury digital experiences...
- **Total Clean CSS Variables Extracted**: `17` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`); CSS variables `--f-display: "Instrument Sans","Helvetica Neue",Helvetica,Arial,sans-serif`; rule `h1` (`font-size: clamp(72px,16vw,250px)`, `line-height: .84`, `letter-spacing: -.055em`, `font-weight: var(--hl-w)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 158.4px`, `line-height: 133.056px`, `font-weight: 500`, `letter-spacing: -8.712px`); rule `h2` (`font-size: clamp(64px,11vw,170px)`, `line-height: .84`, `letter-spacing: -.055em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 17px`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: 0.22px`); CSS variables `--f-mono: "DM Mono",ui-monospace,"SFMono-Regular",Menlo,monospace`; rule `.mono` (`font-size: 11px`, `letter-spacing: .02em`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f1e7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0d0d0c` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fbf9f4` | `.tcard { background: #fbf9f4 }` |
| **Interactive Accent / Highlight** | `#1f2bd6` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#ffffff` | `.cbar button { color: #ffffff }` |
| **Structural Hairline Border** | `#d5d1c8` | `.pst::before { border: #d5d1c8 }` |
| **Variable Token (`--mute`)** | `#6f6b62` | `var(--mute)` in `:root` |
| **Variable Token (`--faint`)** | `#beb9ac` | `var(--faint)` in `:root` |
| **Variable Token (`--sheet`)** | `#f8f5ee` | `var(--sheet)` in `:root` |
| **Variable Token (`--go`)** | `#13a35e` | `var(--go)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#F5F1E7` | Canvas / Surface Token |
| `--ink` | `#0D0D0C` | Typography Ink Token |
| `--mute` | `#6F6B62` | Color / Atmospheric Token |
| `--faint` | `#BEB9AC` | Color / Atmospheric Token |
| `--dot` | `#0D0D0C` | Color / Atmospheric Token |
| `--accent` | `#1F2BD6` | Brand / Palette Token |
| `--sheet` | `#F8F5EE` | Color / Atmospheric Token |
| `--f-display` | `"Instrument Sans","Helvetica Neue",Helvetica,Arial,sans-serif` | Design System Custom Token |
| `--f-serif` | `"Instrument Serif","Times New Roman",Georgia,serif` | Typography / Scale Token |
| `--f-dot` | `"Doto","DM Mono",ui-monospace,monospace` | Design System Custom Token |
| `--f-mono` | `"DM Mono",ui-monospace,"SFMono-Regular",Menlo,monospace` | Typography / Scale Token |
| `--ease` | `cubic-bezier(.22,1,.36,1)` | Motion / Easing Token |
| `--go` | `#13A35E` | Color / Atmospheric Token |
| `--pc` | `#13A35E` | Color / Atmospheric Token |
| `--hl-w` | `500` | Design System Custom Token |
| `--hl-wd` | `"wdth" 100` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.idx-head> — `www-gianpaolotucci-com_work-html`)**:
   - Landmark `<header class="idx-head">` (`1376x150px`) hosting `Gianpaolo Tucci — Creative Director,` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-go="work"`, `data-go="index"`, `data-go="about"`, `data-go="contact"`), and stylesheet rule `body { height:100% }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `Gianpaolo Tucci — Creative Directo`)**:
   - Landmark `<section class="sr-only">` presenting display lead `Gianpaolo Tucci — Creative Director, Berlin` and copy excerpt *"Gianpaolo Tucci is a Berlin-based creative director and experienc"* over `#f5f1e7` canvas and `#0d0d0c` ink.
3. **Primary Showcase & Content Grid (<section.boot> — `Selected work`)**:
   - Landmark `<section class="boot">` rendering section `Selected work` with copy *"This is not a portfolio. This is a timeline of a shift."*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `button { font:inherit;color:inherit;background:none;border:0;padding:0;cursor:poi... }`.
4. **Interactive Detail & Feature Matrix (<section.col> — `Versace Biggies`)**:
   - Landmark `<section class="col">` framing `Versace Biggies` and `Moncler City of Genius` (*"Versace Biggies 2024 · Creative direction · Global campaign. One "*) with `#fbf9f4` surface cards, `#1f2bd6` accents, and `img { max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.lcol> — `https://www.gianpaolotucci.com/work.html`)**:
   - Landmark `<footer class="lcol">` anchoring `Gianpaolo Tucci — Creative Direc` footer links (`Overview · Index · Archive · About · Contact`), copy *"2024 · Creative direction · Global campaign. One campaign ac"*, and `#d5d1c8` structural dividers.
