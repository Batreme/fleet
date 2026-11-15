# UI & UX Architecture: anokhee-dev_albatross

## Overview & Design Identity
- **Target**: `anokhee-dev_albatross` (**The Albatross**)
- **Production URL**: [https://anokhee.dev/albatross](https://anokhee.dev/albatross)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#c9cfdd` canvas, `#7d879e` ink, `#e7dfc9` accent)
- **Summary**: A lone albatross makes first contact with a strange place.
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: 0.01em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `10.5px`, `13px`, `11px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `10.5px`, `13px`, `11px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `10.5px`, `13px`, `11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c9cfdd` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#7d879e` | `var(--mute)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e6dfcc` | `var(--fill)` in `:root` |
| **Interactive Accent / Highlight** | `#e7dfc9` | `var(--lab-bg)` in `:root` |
| **Secondary / Muted Copy** | `#f1ead8` | `var(--lab-bg-2)` in `:root` |
| **Structural Hairline Border** | `#cdc2a5` | `var(--lab-line)` in `:root` |
| **Variable Token (`--lab-ink`)** | `#2a2721` | `var(--lab-ink)` in `:root` |
| **Variable Token (`--lab-mute`)** | `#76705f` | `var(--lab-mute)` in `:root` |
| **Variable Token (`--lab-faint`)** | `#a69e88` | `var(--lab-faint)` in `:root` |
| **Variable Token (`--lab-moss`)** | `#6f8a52` | `var(--lab-moss)` in `:root` |
| **Variable Token (`--lab-clay`)** | `#c0693a` | `var(--lab-clay)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#c9cfdd` | Typography Ink Token |
| `--mute` | `#7d879e` | Color / Atmospheric Token |
| `--fill` | `#e6dfcc` | Color / Atmospheric Token |
| `--track` | `rgba(230, 223, 204, 0.1)` | Color / Atmospheric Token |
| `--tile` | `300px` | Dimension / Scale Token |
| `--lab-bg` | `#e7dfc9` | Canvas / Surface Token |
| `--lab-bg-2` | `#f1ead8` | Canvas / Surface Token |
| `--lab-line` | `#cdc2a5` | Color / Atmospheric Token |
| `--lab-ink` | `#2a2721` | Typography Ink Token |
| `--lab-mute` | `#76705f` | Color / Atmospheric Token |
| `--lab-faint` | `#a69e88` | Color / Atmospheric Token |
| `--lab-moss` | `#6f8a52` | Color / Atmospheric Token |
| `--lab-clay` | `#c0693a` | Color / Atmospheric Token |
| `--lab-glass` | `rgba(231, 223, 201, 0.86)` | Color / Atmospheric Token |
| `--anokhee-dev-alba-bg` | `#c9cfdd` | Canvas Substrate (from `var(--ink)` in `:root`) |
| `--anokhee-dev-alba-ink` | `#7d879e` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.stars> — `anokhee-dev_albatross`)**:
   - Landmark `<nav class="stars">` hosting `The Albatross` navigation (`Field · Heads · Pillars · Obelisks · Trees`), DOM attributes (`data-woke`), and stylesheet rule `root { --ui: "Space Grotesk", "Inter", "IBM Plex Sans", "Helvetica Neue", syste... }`.
2. **Hero Stage & Focal Lead (<section.credits-col> — `The Albatross`)**:
   - Landmark `<section class="credits-col">` presenting display lead `The Albatross` and copy excerpt *"or WASD to fly • M to mute"* over `#c9cfdd` canvas and `#7d879e` ink.
3. **Primary Showcase & Content Grid (<section.credits-col> — `Forecast`)**:
   - Landmark `<section class="credits-col">` rendering section `Forecast` with copy *"Made by Anokhee Jandhyala"*, asset references (`favicon.svg`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `body { margin: 0; height: 100%; overflow: hidden; background: 0e1118; }`.
4. **Interactive Detail & Feature Matrix (<section.credits-col> — `Made by`)**:
   - Landmark `<section class="credits-col">` framing `Made by` and `Music` (*"Music For Dictionary Apps by Ichiro Nakagawa, CC BY"*) with `#e6dfcc` surface cards, `#e7dfc9` accents, and `canvas { display: block; cursor: grab; }`.
5. **Colophon & Global Directory Footer (<footer.near> — `https://anokhee.dev/albatross`)**:
   - Landmark `<footer class="near">` anchoring `The Albatross` footer links (`Field · Heads · Pillars · Obelisks · Trees`), copy *"freesound_community"*, and `#cdc2a5` structural dividers.
