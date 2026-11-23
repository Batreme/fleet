---
title: "UI & UX Architecture: untitledfilm-framer-website"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: untitledfilm-framer-website

## Overview & Design Identity
- **Target**: `untitledfilm-framer-website` (**“Untitled.”**)
- **Production URL**: [https://untitledfilm.framer.website/](https://untitledfilm.framer.website/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#0000ee` accent)
- **Summary**: Discover our premium Framer template built for filmmakers and filmmaking agencies specializing in narrative and commercial production. Ci...
- **Total Clean CSS Variables Extracted**: `38` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Display`
- **Body Font Stack**: `Inter Display Placeholder`
- **Monospace / Technical Font Stack**: `Spline Sans Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 46px`, `font-weight: 500`, `letter-spacing: -1.6px`); rule `h1` (`font-size: 32px`, `line-height: 115%`, `letter-spacing: -.04em`, `font-weight: 500`)
- **Section Heading (`H2`)**: observed font-size ladder: `40px`, `12px`, `16px`, `var(--font-size)`, `var(--framer-font-size)`
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 1.2em`, `letter-spacing: -.01em`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `::selection { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#0000ee` | hairline divider derived from live computed `a` `color` (`computed_styles.json`) |
| **Variable Token (`--token-728d667e-192a-43c3-9c63-5896e9b6b9a2`)** | `#aeaca8` | `var(--token-728d667e-192a-43c3-9c63-5896e9b6b9a2)` in `:root` |
| **Variable Token (`--token-e53dc5d9-c7b0-4885-9cc3-75b0357dc9f7`)** | `#0a0a0a` | `var(--token-e53dc5d9-c7b0-4885-9cc3-75b0357dc9f7)` in `:root` |
| **Variable Token (`--token-caf9a657-a30e-4472-b3ca-0fba92ef6291`)** | `#363636` | `var(--token-caf9a657-a30e-4472-b3ca-0fba92ef6291)` in `:root` |
| **Variable Token (`--token-00d06dfa-06ca-485d-b1a0-c62c60933780`)** | `#c4c4c2` | `var(--token-00d06dfa-06ca-485d-b1a0-c62c60933780)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-9130abfd-2b2e-4652-8967-849c63d0f658` | `#fff` | Color / Atmospheric Token |
| `--token-50ec6c5c-a89d-4939-ab4e-f53ebea8cf63` | `#000` | Color / Atmospheric Token |
| `--token-728d667e-192a-43c3-9c63-5896e9b6b9a2` | `#aeaca8` | Color / Atmospheric Token |
| `--token-e53dc5d9-c7b0-4885-9cc3-75b0357dc9f7` | `#0a0a0a` | Color / Atmospheric Token |
| `--token-1000dd73-bde8-4ac7-9fb1-7ba3d170cea9` | `gray` | Design System Custom Token |
| `--token-d794ee9b-e334-4cd0-a7c7-9ca9d4ce2167` | `#fff` | Color / Atmospheric Token |
| `--token-caf9a657-a30e-4472-b3ca-0fba92ef6291` | `#363636` | Color / Atmospheric Token |
| `--token-00d06dfa-06ca-485d-b1a0-c62c60933780` | `#c4c4c2` | Color / Atmospheric Token |
| `--token-2fafc004-c4d0-4774-b2d3-bca8581a8919` | `#fff` | Color / Atmospheric Token |
| `--token-a78d294f-f3c7-4a88-b97e-670acf5e369f` | `#000` | Color / Atmospheric Token |
| `--token-df0587c7-0e65-43e2-ae9e-b0d3bc25eb50` | `#000` | Color / Atmospheric Token |
| `--token-9daa5760-deab-45ca-8dbb-ce92ef3fc8c3` | `#aeaca8` | Color / Atmospheric Token |
| `--token-3003b0e1-8475-4880-85ef-e6c8af07bd77` | `#000` | Color / Atmospheric Token |
| `--token-1d9a6d9c-dbe2-415a-b7b4-8369c22dbbed` | `#fff` | Color / Atmospheric Token |
| `--infinity` | `infinity` | Design System Custom Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.framer-yk3ex1> — `untitledfilm-framer-website`)**:
   - Landmark `<nav class="framer-yk3ex1">` (`1440x59px`) hosting `“Untitled.”` navigation (`“Untitled.” · [view work]`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.framer-1czbuyf> — `Golden Static`)**:
   - Landmark `<section class="framer-1czbuyf">` presenting display lead `Golden Static` and copy excerpt *"New York, Brooklyn"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.framer-qdz5y> — `Aurelia Studios`)**:
   - Landmark `<section class="framer-qdz5y framer-qt7BG">` rendering section `Aurelia Studios` with copy *"California, Big Sur"*, asset references (`fvHWptZ6qmlvCKfCMpUD3xRGR0.png`, `e3TdWqBmA0UQeUI4Q2TUBUkHWw.png`, `fonts.gstatic.com`, `hls.min.js`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<section.framer-qt7BG> — `Ultraviolet Bloom`)**:
   - Landmark `<section class="framer-qdz5y framer-qt7BG">` framing `Ultraviolet Bloom` and `Lumora Lab` (*"hello@untitled.com"*) with `#ffffff` surface cards, `#0000ee` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-yk3ex1> — `https://untitledfilm.framer.website/`)**:
   - Landmark `<footer class="framer-yk3ex1">` anchoring `“Untitled.”` footer links (`“Untitled.” · [view work]`), copy *"®2026 All Rights Reserved · “Untitled.”"*, and `#0000ee` structural dividers.
