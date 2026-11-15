# UI & UX Architecture: thesovietflip-com

## Overview & Design Identity
- **Target**: `thesovietflip-com` (**The Soviet Flip**)
- **Production URL**: [https://thesovietflip.com/](https://thesovietflip.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0f0f0c` canvas, `#fff0d3` ink, `#fff0d3` accent)
- **Summary**: A visual historical research project about the Cold War, Israel, the USSR, and the rise of modern Palestinian identity, with archival sou...
- **Total Clean CSS Variables Extracted**: `33` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Stalinist One`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`)
- **Body Copy**: CSS variables `--map-body-font: "Jost",sans-serif`; rule `p` (`line-height: 1.2!important`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `25px`, `11px`, `13px`, `10px`, `19px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0f0f0c` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#ebe5d6` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#903c32` | `var(--red)` in `:root` |
| **Interactive Accent / Highlight** | `#fff0d3` | `:hover { color: #fff0d3 }` |
| **Secondary / Muted Copy** | `#dba181` | `:first-child { color: #dba181 }` |
| **Structural Hairline Border** | `#b5634f` | `::-webkit-slider-runnable-track { background: #b5634f }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0f0f0c` | Typography Ink Token |
| `--paper` | `#ebe5d6` | Canvas / Surface Token |
| `--red` | `#903c32` | Color / Atmospheric Token |
| `--site-cursor` | `url(/cursors/arrow.png),auto` | Design System Custom Token |
| `--link-cursor` | `url(/cursors/magnifier.png),pointer` | Typography Ink Token |
| `--map-heading-font` | `"Russo One",sans-serif` | Typography Ink Token |
| `--map-heading-weight` | `400` | Typography Ink Token |
| `--map-body-font` | `"Jost",sans-serif` | Typography / Scale Token |
| `--drawer-side` | `1` | Design System Custom Token |
| `--drawer-progress` | `0` | Design System Custom Token |
| `--peek` | `0px` | Dimension / Scale Token |
| `--ribbon-tail` | `24px` | Dimension / Scale Token |
| `--bookmark-width` | `88px!important` | Layout / Spatial Grid Token |
| `--listener-shift` | `18px` | Dimension / Scale Token |
| `--progress` | `0%` | Dimension / Scale Token |
| `--initial-transform` | `none` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.motion-enabled> — `thesovietflip-com`)**:
   - Landmark `<header class="motion-enabled">` hosting `The Soviet Flip` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-astro-transition-scope="astro-yztbsuuz-1"`, `data-astro-cid-ju4pidww`, `data-astro-rerun`, `data-astro-exec`), and stylesheet rule `root { color-scheme:dark;--ink:0f0f0c;--paper:ebe5d6;--red:903c32 }`.
2. **Hero Stage & Focal Lead (<section.reading-view> — `The Soviet Flip`)**:
   - Landmark `<section class="reading-view">` presenting display lead `The Soviet Flip` and copy excerpt *"For source corrections, archival material, licensing questions, o"* over `#0f0f0c` canvas and `#fff0d3` ink.
3. **Primary Showcase & Content Grid (<section.reading-block> — `האזנה רציפה`)**:
   - Landmark `<section class="reading-block">` rendering section `האזנה רציפה` with copy *"info@thesovietflip.com"*, asset references (`ae304b70d9495a89f84a.woff2`, `cca183354fd3fefb84fd.woff2`, `2b5199f9f43249f2ad78.webp`, `3118562a4483c1224195.webp`), and grid rule `html { scroll-behavior:smooth;background:var(--ink);-webkit-text-size-adjust:10... }`.
4. **Interactive Detail & Feature Matrix (<section.reading-block> — `info@thesovietflip.com`)**:
   - Landmark `<section class="reading-block">` framing `info@thesovietflip.com` and `© 2026 The Soviet Flip. All rights reserved. All` (*"© 2026 The Soviet Flip. All rights reserved. All content, researc"*) with `#903c32` surface cards, `#fff0d3` accents, and `body { color:var(--paper);background:var(--ink);margin:0;font-family:Assistant,... }`.
5. **Colophon & Global Directory Footer (<footer.book-turning-page> — `https://thesovietflip.com/`)**:
   - Landmark `<footer class="book-turning-page">` anchoring `The Soviet Flip` footer links (`Overview · Index · Archive · About · Contact`), copy *"S o v i e t F l i p"*, and `#b5634f` structural dividers.
