# UI & UX Architecture: layersoftime-studio

## Overview & Design Identity
- **Target**: `layersoftime-studio` (**LAYERS OF TIME — The show runs on our clock.**)
- **Production URL**: [https://layersoftime.studio/](https://layersoftime.studio/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#08090b` / `#e9ecef`)
- **Summary**: LAYERS OF TIME is a show studio in Singapore. We design light, video and sound for live rooms, and we build the engine that keeps all of...
- **Total Clean CSS Variables Extracted**: `35` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Söhne`
- **Body Font Stack**: `Söhne Mono`
- **Monospace / Technical Font Stack**: `Söhne Mono`
- **Hero Display (`H1`)**: CSS variables `--fs-h1: clamp(2.25rem, 5.5vw, 5.5rem)`
- **Section Heading (`H2`)**: CSS variables `--fs-h2: clamp(1.75rem, 3.6vw, 3.5rem)`; rule `h2` (`font-size: var(--fs-h3)`, `letter-spacing: -.015em`, `font-weight: 500`)
- **Body Copy**: CSS variables `--fs-body: 1.0625rem`
- **Metadata & Labels**: CSS variables `--fs-small: .9375rem`, `--fs-label: .75rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#08090b` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#0e1013` | `var(--panel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#14171b` | `var(--panel-2)` in `:root` |
| **Interactive Accent / Highlight** | `#e9ecef` | `var(--fg)` in `:root` |
| **Secondary / Muted Copy** | `#8a9099` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#767c85` | `var(--faint)` in `:root` |
| **Variable Token (`--line`)** | `#e9ecef1f` | `var(--line)` in `:root` |
| **Variable Token (`--line-strong`)** | `#e9ecef47` | `var(--line-strong)` in `:root` |
| **Variable Token (`--signal`)** | `#d4178f` | `var(--signal)` in `:root` |
| **Variable Token (`--signal-live`)** | `#ff29c4` | `var(--signal-live)` in `:root` |
| **Variable Token (`--signal-fill`)** | `#8f0e66` | `var(--signal-fill)` in `:root` |
| **Variable Token (`--parallax`)** | `#22d3ee` | `var(--parallax)` in `:root` |
| **Variable Token (`--parsec`)** | `#a3e635` | `var(--parsec)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#08090b` | Canvas / Surface Token |
| `--panel` | `#0e1013` | Color / Atmospheric Token |
| `--panel-2` | `#14171b` | Color / Atmospheric Token |
| `--fg` | `#e9ecef` | Typography Ink Token |
| `--muted` | `#8a9099` | Color / Atmospheric Token |
| `--faint` | `#767c85` | Color / Atmospheric Token |
| `--line` | `#e9ecef1f` | Color / Atmospheric Token |
| `--line-strong` | `#e9ecef47` | Color / Atmospheric Token |
| `--signal` | `#d4178f` | Color / Atmospheric Token |
| `--signal-live` | `#ff29c4` | Color / Atmospheric Token |
| `--signal-fill` | `#8f0e66` | Color / Atmospheric Token |
| `--parallax` | `#22d3ee` | Color / Atmospheric Token |
| `--parsec` | `#a3e635` | Color / Atmospheric Token |
| `--ease` | `cubic-bezier(.22, .61, .36, 1)` | Motion / Easing Token |
| `--d-fast` | `.16s` | Motion / Timing Token |
| `--d-base` | `.32s` | Motion / Timing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `layersoftime-studio`)**:
   - Landmark `<header class="header">` hosting `LAYERS OF TIME — The show runs on ou` navigation (`Work · Studio · Software · Log · Contact`), DOM attributes (`data-theme="dark"`, `data-astro-exec`, `data-header`, `data-astro-cid-nen7h5rs`), and stylesheet rule `.brand__mark { flex:none;width:17px;height:20px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `The show runs on our clock.`)**:
   - Landmark `<section class="hero">` presenting display lead `The show runs on our clock.` and copy excerpt *"18:21:18:27 UTC · SINGULARITY 0.9.13"* over `#08090b` canvas and `#e9ecef` ink.
3. **Primary Showcase & Content Grid (<section.chapter> — `A show studio in Singapore that bu`)**:
   - Landmark `<section class="chapter chapter--light">` rendering section `A show studio in Singapore that builds the softwa...` with copy *"SINGULARITY 0.9.13"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `soehne-kraftig.woff2`, `soehne-buch.woff2`), and grid rule `hover { color:var(--fg) }`.
4. **Interactive Detail & Feature Matrix (<section.section-tight> — `Rooms we have run.`)**:
   - Landmark `<section class="section-tight">` framing `Rooms we have run.` and `Built on tour, between soundcheck and doors.` (*"hello@layersoftime.studio"*) with `#14171b` surface cards, `#e9ecef` accents, and `.footer__mark { flex:none;width:44px;height:52px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://layersoftime.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `LAYERS OF TIME — The show runs o` footer links (`Work · Studio · Software · Log · Contact`), copy *"Zervex · 8 Ubi Road 2, #08-03 · Singapore 408538"*, and `#767c85` structural dividers.
