---
title: "UI & UX Architecture: thesovietflip-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: thesovietflip-com

## Overview & Design Identity
- **Target**: `thesovietflip-com` (**The Soviet Flip**)
- **Production URL**: [https://thesovietflip.com/](https://thesovietflip.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×968px`, Mobile `390×908px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0f0f0c` canvas, `#ffffff` ink, `#903c32` accent)
- **Summary**: A visual historical research project about the Cold War, Israel, the USSR, and the rise of modern Palestinian identity, with archival sou...
- **Total Clean CSS Variables Extracted**: `40` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Assistant`
- **Body Font Stack**: `Assistant`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 36px`, `line-height: 45px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20px`, `line-height: 22px`, `font-weight: 800`); rule `h2` (`font-size: 27px`, `line-height: 1.08`, `font-weight: 800`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--map-body-font: "Jost",sans-serif`; rule `p` (`line-height: 1.2`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`); rule `small` (`font-size: 12px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0f0f0c` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#71362d` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#903c32` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ebe5d6` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#903c32` | `:checked { border-color: #903c32 }` |

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
| `--bookmark-width` | `88px` | Layout / Spatial Grid Token |
| `--listener-shift` | `18px` | Dimension / Scale Token |
| `--button-size` | `62px` | Layout / Spatial Grid Token |
| `--ring-size` | `55px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.motion-enabled> — `thesovietflip-com`)**:
   - Landmark `<header class="motion-enabled">` (`1440px`) hosting `The Soviet Flip` navigation (`עברית · English · Русский`), DOM attributes (`data-astro-transition-scope="astro-yztbsuuz-1"`, `data-astro-cid-ju4pidww`, `data-a11y-contrast="default"`, `data-a11y-saturation="default"`), and stylesheet rule `root { color-scheme:dark;--ink:0f0f0c;--paper:ebe5d6;--red:903c32 }`.
2. **Hero Stage & Focal Lead (<section.reading-view> — `The Soviet Flip`)**:
   - Landmark `<section class="reading-view">` presenting display lead `The Soviet Flip` and copy excerpt *"For source corrections, archival material, licensing questions, o"* over `#0f0f0c` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.reading-block> — `For source corrections, archival m`)**:
   - Landmark `<section class="reading-block">` rendering section `For source corrections, archival material, licen` with copy *"info@thesovietflip.com"*, asset references (`ae304b70d9495a89f84a.woff2`, `cca183354fd3fefb84fd.woff2`, `2b5199f9f43249f2ad78.webp`, `3118562a4483c1224195.webp`), and grid rule `html { scroll-behavior:smooth;background:var(--ink);-webkit-text-size-adjust:10... }`.
4. **Interactive Detail & Feature Matrix (<section.reading-block:nth(2)> — `info@thesovietflip.com`)**:
   - Landmark `<section class="reading-block">` framing `info@thesovietflip.com` and `© 2026 The Soviet Flip. All rights reserved. All` (*"© 2026 The Soviet Flip. All rights reserved. All content, researc"*) with `#71362d` surface cards, `#903c32` accents, and `body { color:var(--paper);background:var(--ink);margin:0;font-family:Assistant,... }`.
5. **Colophon & Global Directory Footer (<footer.sf-loader-digits> — `https://thesovietflip.com/`)**:
   - Landmark `<footer class="sf-loader-digits">` anchoring `The Soviet Flip` footer links (`עברית · English · Русский`), copy *"S o v i e t F l i p"*, and `#903c32` structural dividers.
