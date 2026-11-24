---
title: "UI & UX Architecture: palominoprod-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: palominoprod-com

## Overview & Design Identity
- **Target**: `palominoprod-com` (**Palomino — Cinematic Sports & Brand Films**)
- **Production URL**: [https://palominoprod.com/](https://palominoprod.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×2484px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0000`)
- **Summary**: Cinematic sports and branded films—from global campaigns to athlete documentaries and live events—with strategy, premium production & edi...
- **Total Clean CSS Variables Extracted**: `68` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `HostGrotesk`
- **Body Font Stack**: `HostGrotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 172.8px`, `line-height: 172.8px`, `font-weight: 600`); rule `,h1` (`font-size: clamp(38px,5vw,101px)`, `line-height: 1.2`, `font-weight: 600`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 43.2px`, `line-height: 51.84px`, `font-weight: 600`); CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `,h2` (`font-size: clamp(26px,3vw,50px)`, `line-height: 1.2`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#008000` | `.bg-green-500 { background-color: green }` (`#008000`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.bg-red-500 { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#008000` | `.text-green-400 { color: green }` (`#008000`) |
| **Structural Hairline Border** | `#080748` | `30 { border-color: #080748 }` |
| **Variable Token (`--color-red-400`)** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Variable Token (`--color-red-500`)** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Variable Token (`--color-orange-400`)** | `#ff8b1a` | `var(--color-orange-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--x-double-default` | `calc(var(--x-default) * 2)` | Design System Custom Token |
| `--y-double-default` | `calc(var(--y-default) * 2)` | Design System Custom Token |
| `--x-default` | `20px` | Dimension / Scale Token |
| `--y-default` | `clamp(20px, 8svh, 100px)` | Dimension / Scale Token |
| `--x-half-default` | `calc(var(--x-default) / 2)` | Design System Custom Token |
| `--y-half-default` | `calc(var(--y-default) / 2)` | Design System Custom Token |
| `--font-host-grotesk` | `"HostGrotesk", sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--screen-loader-burst` | `0px` | Dimension / Scale Token |
| `--media-control-background` | `transparent` | Canvas / Surface Token |
| `--media-control-hover-background` | `transparent` | Canvas / Surface Token |
| `--media-button-icon-width` | `100%` | Layout / Spatial Grid Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-orange-400` | `#ff8b1a` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.px-x-default> — `palominoprod-com`)**:
   - Landmark `<header class="px-x-default top-0">` (`1440x75px`) hosting `Palomino — Cinematic Sports & Brand ` navigation (`W O R K W O R K · A B O U T A B O U T`), DOM attributes (`data-next-head`, `data-n-g`, `data-n-css`, `data-nimg="1"`), and stylesheet rule `.animation-sample { will-change:transform;animation:6s ease-in-out infinite sample }`.
2. **Hero Stage & Focal Lead (<section.top-0> — `SPORTS INTO STORIES`)**:
   - Landmark `<section class="top-0 min-h-fit">` presenting display lead `SPORTS INTO STORIES` and copy excerpt *"Sports film and photography studio. We turn brand campaigns and a"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.pt-y-default> — `SELECTED PROJECTS`)**:
   - Landmark `<section class="pt-y-default noise-overlay">` rendering section `SELECTED PROJECTS` with copy *"Where effort meets the light. A glimpse of the stories we've brou"*, asset references (`favicon.ico`, `HostGrotesk-Variable.woff2`, `0d_rtsbnnnoar.css`, `0eydbtu3qzciz.js`), and grid rule `html { scrollbar-width:none;-ms-overflow-style:none }`.
4. **Interactive Detail & Feature Matrix (<section.px-x-default> — `Running FW26 × Decathlon`)**:
   - Landmark `<section class="px-x-default pt-y-default">` framing `Running FW26 × Decathlon` and `Mennen TV Spot` (*"S E E A L L W O R K S E E A L L W O R K"*) with `#008000` surface cards, `#ff0000` accents, and `html ::selection { background:var(--color-black);color:var(--color-white) }`.
5. **Colophon & Global Directory Footer (<footer.select-none> — `https://palominoprod.com/`)**:
   - Landmark `<footer class="select-none bottom-0">` anchoring `Palomino — Cinematic Sports & Br` footer links (`W O R K W O R K · A B O U T A B O U T`), copy *"S E E A L L W O R K"*, and `#080748` structural dividers.
