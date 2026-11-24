---
title: "UI & UX Architecture: verasfawaz-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: verasfawaz-com

## Overview & Design Identity
- **Target**: `verasfawaz-com` (**Véras Fawaz**)
- **Production URL**: [https://verasfawaz.com](https://verasfawaz.com)
- **Final Redirected URL**: [https://www.verasfawaz.com/](https://www.verasfawaz.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080808` / `#cbbfa9`)
- **Summary**: Véras Fawaz © 1993 - 2026
- **Total Clean CSS Variables Extracted**: `122` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Studio Sans`
- **Body Font Stack**: `Studio Sans`
- **Monospace / Technical Font Stack**: `Studio Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--ui-title)`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 22px`, `line-height: 1.2`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: normal`, `font-weight: 400`); CSS variables `--meta: 13px`, `--type-mono: 'Studio Sans',Arial,sans-serif`, `--ui-meta: 12px`; rule `small` (`letter-spacing: 0`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#24292b` | `var(--panel-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#cbbfa9` | `.lynch-letter header button { color: #cbbfa9 }` |
| **Secondary / Muted Copy** | `#6a7173` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#2d2d2d` | `var(--review-rule)` in `:root` (`ffffff26`) |
| **Variable Token (`--hair`)** | `#272d27` | `var(--hair)` in `:root` |
| **Variable Token (`--paper`)** | `#f7f7f2` | `var(--paper)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#24292b` | Typography Ink Token |
| `--muted` | `#6a7173` | Color / Atmospheric Token |
| `--hair` | `#272d2723` | Color / Atmospheric Token |
| `--ui-space` | `32px` | Layout / Spatial Grid Token |
| `--edge-bottom` | `max(18px,env(safe-area-inset-bottom))` | Dimension / Scale Token |
| `--title` | `30px` | Dimension / Scale Token |
| `--action` | `15px` | Dimension / Scale Token |
| `--meta` | `13px` | Dimension / Scale Token |
| `--panel-bottom` | `160px` | Dimension / Scale Token |
| `--paper` | `#f7f7f2` | Canvas / Surface Token |
| `--panel-ink` | `#24292b` | Typography Ink Token |
| `--studio-safe-top` | `max(env(safe-area-inset-top,0px),var(--host-safe-top,0px))` | Dimension / Scale Token |
| `--studio-safe-bottom` | `max(env(safe-area-inset-bottom,0px),var(--host-safe-bottom,0px))` | Dimension / Scale Token |
| `--type-sans` | `'Studio Sans',Arial,sans-serif` | Typography / Scale Token |
| `--type-mono` | `'Studio Sans',Arial,sans-serif` | Typography / Scale Token |
| `--ui-font` | `var(--type-sans)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.studio-power-pending> — `verasfawaz-com`)**:
   - Landmark `<header class="studio-power-pending">` (`1376x44px`) hosting `Véras Fawaz` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-entrance-light="day"`, `data-entrance="loading"`, `data-studio-ready="true"`, `data-arrival="waiting"`), and stylesheet rule `studio-index-popup { --window-milk:rgba(255,255,255,.68); }`.
2. **Hero Stage & Focal Lead (<section.temporary-panel> — `Véras Fawaz`)**:
   - Landmark `<section class="temporary-panel">` presenting display lead `Véras Fawaz` and copy excerpt *"Skip to the archive"* over `#080808` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.studio-ui> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="studio-ui">` rendering section `Featured Work & Interactive Showcase` with copy *"PLEASE TOUCH EVERYTHING"*, asset references (`IBMPlexMono-Regular.woff2`, `wide-blackout.webp`, `startup-input-game-exit-20261018.js`, `apple-touch-icon.png`), and grid rule `span { font-family:'Studio Mono',monospace!important; font-size:11px!important; }`.
4. **Interactive Detail & Feature Matrix (<section.compact-music-ui> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="compact-music-ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Véras Fawaz © 1993 - 2026"*) with `#24292b` surface cards, `#cbbfa9` accents, and `.music-dock-glyph { display:flex;align-items:center;justify-content:center;transform-origin:... }`.
5. **Colophon & Global Directory Footer (<footer.context-footer-ui> — `https://verasfawaz.com`)**:
   - Landmark `<footer class="context-footer-ui">` anchoring `Véras Fawaz` footer links (`Overview · Index · Archive · About · Contact`), copy *"This room needs JavaScript. Visit Films , Music , Book or Ga"*, and `#2d2d2d` structural dividers.
