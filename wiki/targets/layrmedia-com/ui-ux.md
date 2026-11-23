---
title: "UI & UX Architecture: layrmedia-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: layrmedia-com

## Overview & Design Identity
- **Target**: `layrmedia-com` (**LAYR Media · Creative Photography & Videography Studio**)
- **Production URL**: [https://layrmedia.com/](https://layrmedia.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f8f7f6` / `#ff0033`)
- **Summary**: A Toronto-based photography and video production studio creating high-quality commercial, brand, corporate and social content from concep...
- **Total Clean CSS Variables Extracted**: `37` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Koulen`
- **Body Font Stack**: `Koulen`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 172.8px`, `line-height: 138.24px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 115.2px`, `line-height: 86.4px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f7f6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171717` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.bg-background { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#ff0033` | `var(--color-red)` in `:root` |
| **Secondary / Muted Copy** | `#008000` | `.text-green-500 { color: green }` (`#008000`) |
| **Structural Hairline Border** | `#ffffff` | `20 { border-color: #ffffff }` |
| **Variable Token (`--color-red-500`)** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Variable Token (`--color-red-600`)** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Variable Token (`--color-amber-950`)** | `#461901` | `var(--color-amber-950)` in `:root` |
| **Variable Token (`--color-green-500`)** | `#00c758` | `var(--color-green-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#171717` | Canvas / Surface Token |
| `--color-white` | `#f8f7f6` | Canvas / Surface Token |
| `--color-red` | `#f03` | Brand / Palette Token |
| `--font-koulen` | `"Koulen", "Koulen Fallback"` | Typography / Scale Token |
| `--font-work-sans` | `"Work Sans", "Work Sans Fallback"` | Typography / Scale Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-amber-950` | `#461901` | Brand / Palette Token |
| `--color-green-500` | `#00c758` | Brand / Palette Token |
| `--color-neutral-900` | `#171717` | Brand / Palette Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.relative> — `layrmedia-com`)**:
   - Landmark `<header class="relative w-full">` (`1440x1800px`) hosting `LAYR Media · Creative Photography & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r184"`, `data-original-fill="F8F7F6"`, `data-original-fill="F8F7F6"`), and stylesheet rule `ulen_aaaf4d07-module__jwNIZW__cla... { font-family:Koulen,Koulen Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `LAYR. MEDIA`)**:
   - Landmark `<section class="relative">` presenting display lead `LAYR. MEDIA` and copy excerpt *"[ ENTER WITHOUT SOUND ]"* over `#f8f7f6` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<section.h-fit> — `[ ENTER WITHOUT SOUND ]`)**:
   - Landmark `<section class="h-fit relative">` rendering section `[ ENTER WITHOUT SOUND ]` with copy *"START A PROJECT START A PROJECT"*, asset references (`6c6a3def8289aaff-s.p.42fhi38wiwr8...`, `7ddd198311ba7843-s.p.3kq6k02b2ysv...`, `1.jpg`, `2.jpg`), and grid rule `oulen_aaaf4d07-module__jwNIZW__va... { --font-koulen:"Koulen", "Koulen Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.group> — `START A PROJECT START A PROJECT`)**:
   - Landmark `<section class="group bg-red">` framing `START A PROJECT START A PROJECT` and `© 2026 LAYR — Toronto, CA` (*"© 2026 LAYR — Toronto, CA"*) with `#ffffff` surface cards, `#ff0033` accents, and `sans_6c6a0eaa-module__Tqlsvq__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.overflow-x-clip> — `https://layrmedia.com/`)**:
   - Landmark `<footer class="overflow-x-clip w-full">` anchoring `LAYR Media · Creative Photograph` footer links (`Overview · Index · Archive · About · Contact`), copy *"Creative Production Studio"*, and `#ffffff` structural dividers.
