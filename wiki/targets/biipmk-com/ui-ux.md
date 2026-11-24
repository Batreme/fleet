---
title: "UI & UX Architecture: biipmk-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: biipmk-com

## Overview & Design Identity
- **Target**: `biipmk-com` (**biipmk**)
- **Production URL**: [https://biipmk.com/](https://biipmk.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f0f0f1` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: French art director and keycap designer with 10+ years experience. Specializing in mechanical keyboard design, custom keycap sets, and vi...
- **Total Clean CSS Variables Extracted**: `45` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Satoshi Placeholder`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 89.6px`, `font-weight: 400`); rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 140%`, `letter-spacing: 0em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 89.6px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 120%`, `letter-spacing: 0em`, `font-weight: 700`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0f1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#2e2e2f` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2e2e2f` | `var(--border-color)` in `:root` |
| **Variable Token (`--token-1ef64e56-8935-4468-b341-7e1dc51bb63d`)** | `#fff9` | `var(--token-1ef64e56-8935-4468-b341-7e1dc51bb63d)` in `:root` |
| **Variable Token (`--token-f56b1214-00aa-4536-9ffd-154101bb6be0`)** | `#d2d2d2` | `var(--token-f56b1214-00aa-4536-9ffd-154101bb6be0)` in `:root` |
| **Variable Token (`--token-63ff77c2-576f-40e9-b4c2-5caf21c4f1e9`)** | `#bcbcbd` | `var(--token-63ff77c2-576f-40e9-b4c2-5caf21c4f1e9)` in `:root` |
| **Variable Token (`--token-d752c2e3-4387-4d99-8931-9ec888af3ba1`)** | `#9d9d9f` | `var(--token-d752c2e3-4387-4d99-8931-9ec888af3ba1)` in `:root` |
| **Variable Token (`--token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe`)** | `#8a8a8c` | `var(--token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe)` in `:root` |
| **Variable Token (`--token-8a478efd-d44a-4177-9d88-c7291b9d6b8f`)** | `#6d6d6f` | `var(--token-8a478efd-d44a-4177-9d88-c7291b9d6b8f)` in `:root` |
| **Variable Token (`--token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f`)** | `#636365` | `var(--token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f)` in `:root` |
| **Variable Token (`--token-a4711fc1-f7ea-49d6-acf3-e384c36b6979`)** | `#4d4d4f` | `var(--token-a4711fc1-f7ea-49d6-acf3-e384c36b6979)` in `:root` |
| **Variable Token (`--token-ead8cd39-f167-4cb4-a750-94b1094ca9b4`)** | `#3c3c3d` | `var(--token-ead8cd39-f167-4cb4-a750-94b1094ca9b4)` in `:root` |
| **Variable Token (`--token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d`)** | `#252526` | `var(--token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-a58b3a81-59cc-45f7-ae05-091785ff903e` | `#fff` | Color / Atmospheric Token |
| `--token-9a61cb06-3a3a-4375-8be8-66b9dda45d4e` | `#2e2e2f` | Color / Atmospheric Token |
| `--token-1ef64e56-8935-4468-b341-7e1dc51bb63d` | `#fff9` | Color / Atmospheric Token |
| `--token-b3a4db72-7cd5-441a-86c3-f810b7cadc92` | `#f0f0f1` | Color / Atmospheric Token |
| `--token-f56b1214-00aa-4536-9ffd-154101bb6be0` | `#d2d2d2` | Color / Atmospheric Token |
| `--token-63ff77c2-576f-40e9-b4c2-5caf21c4f1e9` | `#bcbcbd` | Color / Atmospheric Token |
| `--token-d752c2e3-4387-4d99-8931-9ec888af3ba1` | `#9d9d9f` | Color / Atmospheric Token |
| `--token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe` | `#8a8a8c` | Color / Atmospheric Token |
| `--token-8a478efd-d44a-4177-9d88-c7291b9d6b8f` | `#6d6d6f` | Color / Atmospheric Token |
| `--token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f` | `#636365` | Color / Atmospheric Token |
| `--token-a4711fc1-f7ea-49d6-acf3-e384c36b6979` | `#4d4d4f` | Color / Atmospheric Token |
| `--token-ead8cd39-f167-4cb4-a750-94b1094ca9b4` | `#3c3c3d` | Color / Atmospheric Token |
| `--token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d` | `#252526` | Color / Atmospheric Token |
| `--token-2ef8ddb3-0f66-468d-abb6-13d65e017e32` | `#d2d2d280` | Color / Atmospheric Token |
| `--token-d5e104ff-e396-4ea1-8a79-0d0dbbc87b4d` | `#fff` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.framer-yfoBI> — `biipmk-com`)**:
   - Landmark `<nav class="framer-yfoBI framer-1rw6cnj">` (`1440x50px`) hosting `biipmk` navigation (`Home · Works · About · Contact`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `.hidden-1qegrwl { display:none!important }`.
2. **Hero Stage & Focal Lead (<article.framer-sbufwg> — `Mechanical keyboards & keycaps des`)**:
   - Landmark `<article class="framer-sbufwg">` presenting display lead `Mechanical keyboards & keycaps design` and copy excerpt *"M e c h a n i c a l"* over `#f0f0f1` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.framer-sbufwg:nth(2)> — `M e c h a n i c a l k e y b o a r `)**:
   - Landmark `<article class="framer-sbufwg">` rendering section `M e c h a n i c a l k e y b o a r d s & k e y c a...` with copy *"Strasbourg, France."*, asset references (`pmry2NqhXUH8l6AL2sqCWz37mfA.png`, `KonkIH5joVcpFDiWUIosk62WxE8.png`, `02sP8aoNizSrkiNxivI6fvFyU.png`, `framerusercontent.com`), and grid rule `.hidden-72rtr7 { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<article.framer-sbufwg:nth(3)> — `S e l e c t e d w o r k s`)**:
   - Landmark `<article class="framer-sbufwg">` framing `S e l e c t e d w o r k s` and `PBTfans No Signal` (*"M e c h a n i c a l k e y b o a r d s & k e y c a..."*) with `#ffffff` surface cards, `#0000ee` accents, and `.hidden-6reknn { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-geIks> — `https://biipmk.com/`)**:
   - Landmark `<footer class="framer-geIks framer-VygiK">` anchoring `biipmk` footer links (`Home · Works · About · Contact`), copy *"S e l e c t e d w o r k s"*, and `#2e2e2f` structural dividers.
