# UI & UX Architecture: dream-with-ai-com

## Overview & Design Identity
- **Target**: `dream-with-ai-com` (**Dream with AI**)
- **Production URL**: [https://dream-with-ai.com](https://dream-with-ai.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#d6cebe` / `#0b0b0b`)
- **Summary**: Can an AI feel anything? If it could, what would it dream? Every night an AI dreams up a whole new world, with its own visuals and sounds...
- **Total Clean CSS Variables Extracted**: `16` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: -.01em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `clamp(22px,2.8vw,32px)`, `17px`, `10px`, `2.25vw`)
- **Body Copy**: rule `p` (`font-size: 17px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `clamp(22px,2.8vw,32px)`, `17px`, `10px`, `2.25vw`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d6cebe` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#1c120d` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a04a2a` | `var(--rust)` in `:root` |
| **Interactive Accent / Highlight** | `#0b0b0b` | `var(--dxlBg)` in `:root` |
| **Secondary / Muted Copy** | `#d9d9d9` | `var(--dxlFg)` in `:root` |
| **Structural Hairline Border** | `#e4e0d6` | `var(--text)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dxl-mark-font` | `500 11px/1 "JetBrains Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--dxl-mark-tracking` | `.08em` | Typography / Scale Token |
| `--dxl-mark-case` | `uppercase` | Design System Custom Token |
| `--dxl-mark-fg` | `var(--ink)` | Typography Ink Token |
| `--dxl-mark-bg` | `none` | Canvas / Surface Token |
| `--paper` | `#d6cebe` | Canvas / Surface Token |
| `--ink` | `#1c120d` | Typography Ink Token |
| `--rust` | `#a04a2a` | Color / Atmospheric Token |
| `--dxl-bg` | `var(--dxlBg)` | Canvas / Surface Token |
| `--dxl-fg` | `var(--dxlFg)` | Typography Ink Token |
| `--dxl-accent` | `var(--dxlAccent)` | Brand / Palette Token |
| `--dxlBg` | `#0b0b0b` | Canvas / Surface Token |
| `--dxlFg` | `#d9d9d9` | Typography Ink Token |
| `--dxlAccent` | `#a04a2a` | Brand / Palette Token |
| `--wash` | `#0b0b0b` | Color / Atmospheric Token |
| `--text` | `#e4e0d6` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.noir> — `dream-with-ai-com`)**:
   - Landmark `<header class="noir">` hosting `Dream with AI` navigation (`DEPT® LABS · BY DEPT® LABS`), DOM attributes (`data-engine="three.js r180"`, `data-engine="three.js r180"`, `data-track="Start"`, `data-track-with="camera"`), and stylesheet rule `root { --paper: d6cebe;--ink: 1c120d;--rust: a04a2a }`.
2. **Hero Stage & Focal Lead (<div.paper> — `Dream with AI`)**:
   - Landmark `<div class="paper">` presenting display lead `Dream with AI` and copy excerpt *"Close your eyes · hold"* over `#d6cebe` canvas and `#0b0b0b` ink.
3. **Primary Showcase & Content Grid (<div.paper> — `How to dream`)**:
   - Landmark `<div class="paper">` rendering section `How to dream` with copy *"An art piece by x09, brought to life by DEPT® LABS"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `sitemap-index.xml`, `script.js`), and grid rule `body { margin:0;height:100%;overflow:hidden;background:var(--paper) }`.
4. **Interactive Detail & Feature Matrix (<div.paper> — `Your camera`)**:
   - Landmark `<div class="paper">` framing `Your camera` and `Every night an AI dreams a new world, engraved l` (*"Every night an AI dreams a new world, engraved like Escher and me"*) with `#a04a2a` surface cards, `#0b0b0b` accents, and `lids { position:fixed;inset:0;width:100%;height:100%;display:block;touch-action... }`.
5. **Colophon & Global Directory Footer (<footer.cue> — `https://dream-with-ai.com`)**:
   - Landmark `<footer class="cue">` anchoring `Dream with AI` footer links (`DEPT® LABS · BY DEPT® LABS`), copy *"Blink, and the dream moves on. Close your eyes and keep them"*, and `#e4e0d6` structural dividers.
