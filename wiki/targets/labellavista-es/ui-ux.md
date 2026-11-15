# UI & UX Architecture: labellavista-es

## Overview & Design Identity
- **Target**: `labellavista-es` (**LABELLAVISTA — Creative production co.**)
- **Production URL**: [https://labellavista.es/](https://labellavista.es/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0a0a0a` canvas, `#fff` ink, `#fff` accent)
- **Summary**: LABELLAVISTA is a creative production co. based in Galicia and Madrid: music videos, commercials and films, shot wherever the story is.
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo Fallback`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: CSS variables `--display: clamp(64px, 9vw, 160px)`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--body)`, `var(--ui)`, `var(--display)`, `var(--section)`, `13px`)
- **Body Copy**: CSS variables `--body: clamp(15px, 1.1vw, 17px)`
- **Metadata & Labels**: CSS variables `--font-dm-mono: "DM Mono", "DM Mono Fallback"`, `--font-mono: var(--font-dm-mono), ui-monospace, "Courier New", monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#eee9de` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#111` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--white)` in `:root` |
| **Secondary / Muted Copy** | `#2f4a8a` | `var(--blue)` in `:root` |
| **Structural Hairline Border** | `#6e8fd6` | `var(--blue-lift)` in `:root` |
| **Variable Token (`--cream`)** | `#e2d6c0` | `var(--cream)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-archivo` | `"Archivo", "Archivo Fallback"` | Typography / Scale Token |
| `--font-dm-mono` | `"DM Mono", "DM Mono Fallback"` | Typography / Scale Token |
| `--font-slab` | `"Alfa Slab One", "Alfa Slab One Fallback"` | Typography / Scale Token |
| `--black` | `#0a0a0a` | Canvas / Surface Token |
| `--paper` | `#eee9de` | Canvas / Surface Token |
| `--ink` | `#111` | Typography Ink Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--blue` | `#2f4a8a` | Color / Atmospheric Token |
| `--blue-lift` | `#6e8fd6` | Color / Atmospheric Token |
| `--cream` | `#e2d6c0` | Color / Atmospheric Token |
| `--font-sans` | `var(--font-archivo), system-ui, -apple-system, "Segoe UI", sans-serif` | Typography / Scale Token |
| `--font-mono` | `var(--font-dm-mono), ui-monospace, "Courier New", monospace` | Typography / Scale Token |
| `--display` | `clamp(64px, 9vw, 160px)` | Dimension / Scale Token |
| `--section` | `clamp(32px, 2.8vw, 40px)` | Dimension / Scale Token |
| `--body` | `clamp(15px, 1.1vw, 17px)` | Dimension / Scale Token |
| `--ui` | `11px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bar> — `labellavista-es`)**:
   - Landmark `<header class="bar">` hosting `LABELLAVISTA — Creative production c` navigation (`MUSIC VIDEOS · COMMERCIALS · FILMS · STUDIO · CONTACT`), DOM attributes (`data-cover`, `data-precedence="next"`, `data-room="dark"`, `data-hidden="false"`), and stylesheet rule `hivo_8c2be2a3-module__iX1fDW__cla... { font-family:Archivo,Archivo Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.reel> — `LABELLAVISTA`)**:
   - Landmark `<section class="reel">` presenting display lead `LABELLAVISTA` and copy excerpt *"Creative production co."* over `#0a0a0a` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.reel> — `Creative production co.`)**:
   - Landmark `<section class="reel">` rendering section `Creative production co.` with copy *"GALICIA / MADRID 18:19:56 · UTC+01"*, asset references (`21ca8f3f56c22ca2-s.p.1cp9-4nby68j...`, `36363bfb06833f56-s.p.38hmww4cj4vm...`, `cabin-window.webp`, `cabin-shade.webp`), and grid rule `chivo_8c2be2a3-module__iX1fDW__va... { --font-archivo:"Archivo", "Archivo Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.reel> — `GALICIA / MADRID 18:19:56 · UTC+01`)**:
   - Landmark `<section class="reel">` framing `GALICIA / MADRID 18:19:56 · UTC+01` and `( 01 ) Music videos` (*"( 01 ) Music videos"*) with `#111` surface cards, `#fff` accents, and `mono_685a951c-module__v6oBuq__cla... { font-family:DM Mono,DM Mono Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://labellavista.es/`)**:
   - Landmark `<footer class="foot ui">` anchoring `LABELLAVISTA — Creative producti` footer links (`MUSIC VIDEOS · COMMERCIALS · FILMS · STUDIO · CONTACT`), copy *"( 02 ) Commercials"*, and `#6e8fd6` structural dividers.
