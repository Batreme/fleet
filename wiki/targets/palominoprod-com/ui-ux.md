# UI & UX Architecture: palominoprod-com

## Overview & Design Identity
- **Target**: `palominoprod-com` (**Palomino — Cinematic Sports & Brand Films**)
- **Production URL**: [https://palominoprod.com/](https://palominoprod.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ff6568` / `#05df72`)
- **Summary**: Cinematic sports and branded films—from global campaigns to athlete documentaries and live events—with strategy, premium production & edi...
- **Total Clean CSS Variables Extracted**: `68` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `HostGrotesk`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `,h1` (`font-size: clamp(38px,5vw,101px)`, `line-height: 1.2`, `font-weight: 600`)
- **Section Heading (`H2`)**: CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `,h2` (`font-size: clamp(26px,3vw,50px)`, `line-height: 1.2`, `font-weight: 600`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(38px,5vw,101px)`, `clamp(26px,3vw,50px)`, `clamp(20px,2vw,30px)`, `30px`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Primary Typography Ink** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff8b1a` | `var(--color-orange-400)` in `:root` |
| **Interactive Accent / Highlight** | `#05df72` | `var(--color-green-400)` in `:root` |
| **Secondary / Muted Copy** | `#00c758` | `var(--color-green-500)` in `:root` |
| **Structural Hairline Border** | `#e2e8f0` | `var(--color-slate-200)` in `:root` |
| **Variable Token (`--color-slate-300`)** | `#cad5e2` | `var(--color-slate-300)` in `:root` |
| **Variable Token (`--color-slate-400`)** | `#90a1b9` | `var(--color-slate-400)` in `:root` |
| **Variable Token (`--color-slate-600`)** | `#45556c` | `var(--color-slate-600)` in `:root` |
| **Variable Token (`--color-slate-700`)** | `#314158` | `var(--color-slate-700)` in `:root` |
| **Variable Token (`--color-slate-900`)** | `#0f172b` | `var(--color-slate-900)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--screen-loader-burst` | `0px` | Dimension / Scale Token |
| `--media-control-background` | `transparent!important` | Canvas / Surface Token |
| `--media-control-hover-background` | `transparent!important` | Canvas / Surface Token |
| `--media-button-icon-width` | `100%!important` | Layout / Spatial Grid Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-orange-400` | `#ff8b1a` | Brand / Palette Token |
| `--color-green-400` | `#05df72` | Brand / Palette Token |
| `--color-green-500` | `#00c758` | Brand / Palette Token |
| `--color-slate-200` | `#e2e8f0` | Brand / Palette Token |
| `--color-slate-300` | `#cad5e2` | Brand / Palette Token |
| `--color-slate-400` | `#90a1b9` | Brand / Palette Token |
| `--color-slate-600` | `#45556c` | Brand / Palette Token |
| `--color-slate-700` | `#314158` | Brand / Palette Token |
| `--color-slate-900` | `#0f172b` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.px-x-default> — `palominoprod-com`)**:
   - Landmark `<header class="px-x-default fixed">` hosting `Palomino — Cinematic Sports & Brand ` navigation (`W O R K W O R K · A B O U T A B O U T`), DOM attributes (`data-next-head`, `data-n-g`, `data-n-css`, `data-nimg="1"`), and stylesheet rule `.animation-sample { will-change:transform;animation:6s ease-in-out infinite sample }`.
2. **Hero Stage & Focal Lead (<section.relative> — `SPORTS INTO STORIES`)**:
   - Landmark `<section class="relative top-0">` presenting display lead `SPORTS INTO STORIES` and copy excerpt *"A B O U T A B O U T"* over `#ff6568` canvas and `#e2e8f0` ink.
3. **Primary Showcase & Content Grid (<section.pt-y-default> — `OUR CLIENTS`)**:
   - Landmark `<section class="pt-y-default noise-overlay">` rendering section `OUR CLIENTS` with copy *"C O N T A C T C O N T A C T"*, asset references (`favicon.ico`, `HostGrotesk-Variable.woff2`, `0d_rtsbnnnoar.css`, `0eydbtu3qzciz.js`), and grid rule `html { scrollbar-width:none;-ms-overflow-style:none }`.
4. **Interactive Detail & Feature Matrix (<section.px-x-default> — `SELECTED PROJECTS`)**:
   - Landmark `<section class="px-x-default pt-y-default">` framing `SELECTED PROJECTS` and `Running FW26 × Decathlon` (*"Sports film and photography studio. We turn brand campaigns and a"*) with `#ff8b1a` surface cards, `#05df72` accents, and `html ::selection { background:var(--color-black);color:var(--color-white) }`.
5. **Colophon & Global Directory Footer (<footer.w-screen> — `https://palominoprod.com/`)**:
   - Landmark `<footer class="w-screen bg-white">` anchoring `Palomino — Cinematic Sports & Br` footer links (`W O R K W O R K · A B O U T A B O U T`), copy *"Where effort meets the light. A glimpse of the stories we've"*, and `#e2e8f0` structural dividers.
