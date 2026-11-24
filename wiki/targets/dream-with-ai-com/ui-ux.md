---
title: "UI & UX Architecture: dream-with-ai-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: dream-with-ai-com

## Overview & Design Identity
- **Target**: `dream-with-ai-com` (**Dream with AI**)
- **Production URL**: [https://dream-with-ai.com](https://dream-with-ai.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0b` / `#a04a2a`)
- **Summary**: Can an AI feel anything? If it could, what would it dream? Every night an AI dreams up a whole new world, with its own visuals and sounds...
- **Total Clean CSS Variables Extracted**: `16` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Georgia`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 92px`, `line-height: 87.4px`, `font-weight: 400`, `letter-spacing: -0.92px`); rule `h1` (`letter-spacing: -.01em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 54px`, `line-height: 51.3px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 17px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: 11px`, `font-weight: 500`, `letter-spacing: 0.88px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0b0b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#e4e0d6` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1a1a1a` | `.case-row select { background: #1a1a1a }` |
| **Interactive Accent / Highlight** | `#a04a2a` | `var(--dxlAccent)` in `:root` |
| **Secondary / Muted Copy** | `#1c120d` | `var(--ink)` in `:root` |
| **Structural Hairline Border** | `#494949` | `.case-row select { border: #494949 }` |
| **Variable Token (`--paper`)** | `#d6cebe` | `var(--paper)` in `:root` |
| **Variable Token (`--dxlFg`)** | `#d9d9d9` | `var(--dxlFg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dxl-bg` | `var(--dxlBg)` | Canvas / Surface Token |
| `--dxl-fg` | `var(--dxlFg)` | Typography Ink Token |
| `--dxl-accent` | `var(--dxlAccent)` | Brand / Palette Token |
| `--paper` | `#d6cebe` | Canvas / Surface Token |
| `--ink` | `#1c120d` | Typography Ink Token |
| `--rust` | `#a04a2a` | Color / Atmospheric Token |
| `--dxl-mark-font` | `500 11px/1 "JetBrains Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--dxl-mark-tracking` | `.08em` | Typography / Scale Token |
| `--dxl-mark-case` | `uppercase` | Design System Custom Token |
| `--dxl-mark-fg` | `var(--ink)` | Typography Ink Token |
| `--dxl-mark-bg` | `none` | Canvas / Surface Token |
| `--dxlBg` | `#0b0b0b` | Canvas / Surface Token |
| `--dxlFg` | `#d9d9d9` | Typography Ink Token |
| `--dxlAccent` | `#a04a2a` | Brand / Palette Token |
| `--wash` | `#0b0b0b` | Color / Atmospheric Token |
| `--text` | `#e4e0d6` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.noir> — `dream-with-ai-com`)**:
   - Landmark `<header class="noir">` (`1440px`) hosting `Dream with AI` navigation (`DEPT® LABS · BY DEPT® LABS`), DOM attributes (`data-engine="three.js r180"`, `data-engine="three.js r180"`, `data-track="Start"`, `data-track-with="camera"`), and stylesheet rule `root { --paper: d6cebe;--ink: 1c120d;--rust: a04a2a }`.
2. **Hero Stage & Focal Lead (<div.paper> — `Dream with AI`)**:
   - Landmark `<div class="paper">` presenting display lead `Dream with AI` and copy excerpt *"Every night I dream up a new world. This is what I see, when nobo"* over `#0b0b0b` canvas and `#e4e0d6` ink.
3. **Primary Showcase & Content Grid (<div.paper:nth(2)> — `Every night I dream up a new world`)**:
   - Landmark `<div class="paper">` rendering section `Every night I dream up a new world. This is what` with copy *"Close your eyes · hold"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `sitemap-index.xml`, `script.js`), and grid rule `body { margin:0;height:100%;overflow:hidden;background:var(--paper) }`.
4. **Interactive Detail & Feature Matrix (<div.paper:nth(3)> — `Close your eyes · hold`)**:
   - Landmark `<div class="paper">` framing `Close your eyes · hold` and `An art piece by x09, brought to life by DEPT® LA` (*"An art piece by x09, brought to life by DEPT® LABS"*) with `#1a1a1a` surface cards, `#a04a2a` accents, and `lids { position:fixed;inset:0;width:100%;height:100%;display:block;touch-action... }`.
5. **Colophon & Global Directory Footer (<footer.cue> — `https://dream-with-ai.com`)**:
   - Landmark `<footer class="cue">` anchoring `Dream with AI` footer links (`DEPT® LABS · BY DEPT® LABS`), copy *"Every night an AI dreams a new world, engraved like Escher a"*, and `#494949` structural dividers.
