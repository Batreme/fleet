# UI & UX Architecture: labs-griflan-com

## Overview & Design Identity
- **Target**: `labs-griflan-com` (**Griflan Labs**)
- **Production URL**: [https://labs.griflan.com/](https://labs.griflan.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fffddb` / `#181616`)
- **Summary**: A strategy-led design studio specializing in laying down the awesome sauce.
- **Total Clean CSS Variables Extracted**: `7` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roboto Mono`
- **Body Font Stack**: `sans`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.1rem`, `1.2rem`, `1.6rem`, `1.8rem`, `2.5rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.1rem`, `1.2rem`, `1.6rem`, `1.8rem`, `2.5rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.1rem`, `1.2rem`, `1.6rem`, `1.8rem`, `2.5rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.1rem`, `1.2rem`, `1.6rem`, `1.8rem`, `2.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fffddb` | `.caret-ink { color: #fffddb }` |
| **Primary Typography Ink** | `#181616` | `body { background: #181616 }` |
| **Elevated Surface / Card Substrate** | `#fff` | `body { color: #fff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--floor` | `min(8px,.75vw)` | Dimension / Scale Token |
| `--glass-fill` | `rgba(0,0,0,.4)` | Color / Atmospheric Token |
| `--size` | `390` | Layout / Spatial Grid Token |
| `--dim` | `rgb(64 63 55)` | Color / Atmospheric Token |
| `--calm` | `rgb(93 91 81)` | Color / Atmospheric Token |
| `--pill-w` | `400px` | Dimension / Scale Token |
| `--gap` | `8px` | Layout / Spatial Grid Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--tw-skew-x` | `0` | Design System Custom Token |
| `--tw-skew-y` | `0` | Design System Custom Token |
| `--labs-griflan-com-bg` | `#fffddb` | Canvas Substrate (from `.caret-ink { color: #fffddb }`) |
| `--labs-griflan-com-ink` | `#181616` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `labs-griflan-com`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `Griflan Labs` navigation (`Griflan Labs · About · Start A Project · Stax.ai · Mailerbot`), DOM attributes (`data-gpu="yes"`, `data-hid="gpu"`, `data-hid="faces"`, `data-hid="boot"`), and stylesheet rule `.type-display { font-size:max(5rem,min(calc(var(--floor, 8px)*5),8vh)) }`.
2. **Hero Stage & Focal Lead (<main.fixed> — `We are Griflan`)**:
   - Landmark `<main class="fixed inset-0">` presenting display lead `We are Griflan` and copy excerpt *"This site needs WebGPU. Open it in an up-to-date Chrome, Edge or "* over `#fffddb` canvas and `#181616` ink.
3. **Primary Showcase & Content Grid (<main.fixed> — `Big idea? You know where to find u`)**:
   - Landmark `<main class="fixed inset-0">` rendering section `Big idea? You know where to find us.` with copy *"This site needs WebGPU."*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `sans-400.UP_hgoQ5.json`, `sans-400.bin.B1ole0wm.gz`), and grid rule `.type-body { font-size:max(1.8rem,calc(var(--floor, 8px)*1.8));line-height:1.4 }`.
4. **Interactive Detail & Feature Matrix (<main.fixed> — `Griflan Labs`)**:
   - Landmark `<main class="fixed inset-0">` framing `Griflan Labs` and `Projects` (*"Open it in an up-to-date Chrome, Edge or Safari."*) with `#fff` surface cards, `#181616` accents, and `.type-list { font-size:max(1.5rem,calc(var(--floor, 8px)*1.5));line-height:1.5 }`.
5. **Colophon & Global Directory Footer (<footer.grid> — `https://labs.griflan.com/`)**:
   - Landmark `<footer class="grid">` anchoring `Griflan Labs` footer links (`Griflan Labs · About · Start A Project · Stax.ai · Mailerbot`), copy *"Griflan Labs is an experimental, bird’s-eye view of our work"*, and `#181616` structural dividers.
