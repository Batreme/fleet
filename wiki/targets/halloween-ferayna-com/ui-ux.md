# UI & UX Architecture: halloween-ferayna-com

## Overview & Design Identity
- **Target**: `halloween-ferayna-com` (**Every brief has a face · Ferayna**)
- **Production URL**: [https://halloween.ferayna.com/](https://halloween.ferayna.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0c0f0e` / `#5c6c63`)
- **Summary**: Nine projects you have met before, carved into lanterns on a rock spire. A Halloween scene by Ferayna. Scroll to climb.
- **Total Clean CSS Variables Extracted**: `35` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `reckless`
- **Body Font Stack**: `reckless Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--typography-font-display: var(--font-reckless), Georgia, serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `13px`, `6px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `13px`, `6px`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--typography-font-mono)`, `--typography-font-mono: ui-monospace, SFMono-Regular, Menlo`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0c0f0e` | `var(--colors-night)` in `:root` |
| **Primary Typography Ink** | `#151a18` | `var(--colors-plate)` in `:root` |
| **Elevated Surface / Card Substrate** | `#29322e` | `var(--colors-moss)` in `:root` |
| **Interactive Accent / Highlight** | `#5c6c63` | `var(--colors-sage)` in `:root` |
| **Secondary / Muted Copy** | `#9aa69f` | `var(--colors-dim)` in `:root` |
| **Structural Hairline Border** | `#ece7e1` | `var(--colors-ink)` in `:root` |
| **Variable Token (`--colors-green`)** | `#37d657` | `var(--colors-green)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-reckless` | `"reckless", "reckless Fallback"` | Typography / Scale Token |
| `--font-grotta` | `"grotta", "grotta Fallback"` | Typography / Scale Token |
| `--thread-at` | `0%` | Dimension / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--radius-3xl` | `1.5rem` | Elevation / Border Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--typography-font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--typography-font-mono)` | Typography / Scale Token |
| `--colors-night` | `#0c0f0e` | Brand / Palette Token |
| `--colors-plate` | `#151a18` | Brand / Palette Token |
| `--colors-moss` | `#29322e` | Brand / Palette Token |
| `--colors-sage` | `#5c6c63` | Brand / Palette Token |
| `--colors-dim` | `#9aa69f` | Brand / Palette Token |
| `--colors-ink` | `#ece7e1` | Typography Ink Token |
| `--colors-green` | `#37d657` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.scene-thread> — `halloween-ferayna-com`)**:
   - Landmark `<nav class="scene-thread pointer-events-none">` hosting `Every brief has a face · Ferayna` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-scene-stage="true"`, `data-shot="0"`, `data-scene-fade="true"`), and stylesheet rule `less_ee4802df-module__FYuYzW__cla... { font-family:reckless,reckless Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<main.text-foreground> — `Every brief has a face`)**:
   - Landmark `<main class="text-foreground">` presenting display lead `Every brief has a face` and copy excerpt *"The lanterns can't light in this browser."* over `#0c0f0e` canvas and `#ece7e1` ink.
3. **Primary Showcase & Content Grid (<main.antialiased> — `The simple one`)**:
   - Landmark `<main class="antialiased">` rendering section `The simple one` with copy *"Every brief has a face"*, asset references (`Grotta_Regular-s.p.0hpxf2bw567b9....`, `RecklessCondensedS_Book-s.p.2no44...`, `2qvmtax7tpqlc.css`, `3dxvrezqwk0-f.js`), and grid rule `kless_ee4802df-module__FYuYzW__va... { --font-reckless:"reckless", "reckless Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.sr-only> — `The serious one`)**:
   - Landmark `<main class="sr-only">` framing `The serious one` and `The secret one` (*"Nine projects you have met before. Scroll to meet them again."*) with `#29322e` surface cards, `#5c6c63` accents, and `otta_9a104af5-module__lGjW5a__cla... { font-family:grotta,grotta Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.scene-stage> — `https://halloween.ferayna.com/`)**:
   - Landmark `<footer class="scene-stage">` anchoring `Every brief has a face · Ferayna` footer links (`Overview · Index · Archive · About · Contact`), copy *"Turn the sound on Turn Turn the the sound sound on on"*, and `#ece7e1` structural dividers.
