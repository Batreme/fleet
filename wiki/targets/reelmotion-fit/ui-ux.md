---
title: "UI & UX Architecture: reelmotion-fit"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: reelmotion-fit

## Overview & Design Identity
- **Target**: `reelmotion-fit` (**Reel Motion: Turn Workout Videos Into Exercise Routines**)
- **Production URL**: [https://reelmotion.fit/](https://reelmotion.fit/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f7fb` canvas, `#0e1116` ink, `#0d95e8` accent)
- **Summary**: Paste a link from YouTube, Instagram, or TikTok and Reel Motion creates an illustrated, step-by-step workout you can follow on iPhone and...
- **Total Clean CSS Variables Extracted**: `249` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 66px`, `line-height: 68.64px`, `font-weight: 700`, `letter-spacing: -1.65px`); CSS variables `--page-title-display: block`, `--Display: Inter Tight`, `--TextDisplay: clamp(32px, 5.4vw, 66px)`; rule `h1` (`font-size: 35px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 50.88px`, `font-weight: 700`, `letter-spacing: -1.2px`); CSS variables `--TextH2: clamp(30px, 3.9vw, 48px)`; rule `h2` (`font-size: var( --e-global-typography-se...`, `line-height: var( --e-global-typog...`, `letter-spacing: var( --e-global-typog...`, `font-weight: var( --e-glob...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--Body: Inter`, `--TextBody: 16px`; rule `p` (`font-size: 16px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--TextSmall: 15px`, `--e-global-typography-primary-letter-spacing: -0.025em`, `--e-global-typography-secondary-letter-spacing: -0.025em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f7fb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0e1116` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0d95e8` | `.fancybox-share__button--tw:hover { background: #0d95e8 }` |
| **Secondary / Muted Copy** | `#8a93a3` | `var(--Muted)` in `:root` |
| **Structural Hairline Border** | `#cccccc` | `pre { border: #cccccc }` |
| **Variable Token (`--e-gv-d8119ec`)** | `#934cff` | `var(--e-gv-d8119ec)` in `:root` |
| **Variable Token (`--e-gv-22831a4`)** | `#7a32f0` | `var(--e-gv-22831a4)` in `:root` |
| **Variable Token (`--e-gv-c75aa4e`)** | `#2f7cf8` | `var(--e-gv-c75aa4e)` in `:root` |
| **Variable Token (`--e-gv-ac48b9b`)** | `#78aafa` | `var(--e-gv-ac48b9b)` in `:root` |
| **Variable Token (`--e-gv-399bfaa`)** | `#975af4` | `var(--e-gv-399bfaa)` in `:root` |
| **Variable Token (`--e-gv-cd3db67`)** | `#f5f4fb` | `var(--e-gv-cd3db67)` in `:root` |
| **Variable Token (`--e-gv-0105447`)** | `#161a20` | `var(--e-gv-0105447)` in `:root` |
| **Variable Token (`--e-gv-80cc8b6`)** | `#6b6f7b` | `var(--e-gv-80cc8b6)` in `:root` |
| **Variable Token (`--e-gv-d4944d5`)** | `#e6e4f0` | `var(--e-gv-d4944d5)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp--style--global--content-size` | `800px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1200px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--e-gv-d8119ec` | `#934cff` | Color / Atmospheric Token |
| `--e-gv-22831a4` | `#7a32f0` | Color / Atmospheric Token |
| `--e-gv-c75aa4e` | `#2f7cf8` | Color / Atmospheric Token |
| `--e-gv-ac48b9b` | `#78aafa` | Color / Atmospheric Token |
| `--e-gv-399bfaa` | `#975af4` | Color / Atmospheric Token |
| `--e-gv-1036c6e` | `#ffffff` | Color / Atmospheric Token |
| `--e-gv-cd3db67` | `#f5f4fb` | Color / Atmospheric Token |
| `--e-gv-0105447` | `#161a20` | Color / Atmospheric Token |
| `--e-gv-9d9c176` | `#161a20` | Color / Atmospheric Token |
| `--e-gv-80cc8b6` | `#6b6f7b` | Color / Atmospheric Token |
| `--e-gv-d4944d5` | `#e6e4f0` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.elementor> — `reelmotion-fit`)**:
   - Landmark `<nav class="elementor elementor-15">` (`1440x0px`) hosting `Reel Motion: Turn Workout Videos Int` navigation (`Reel Motion · Home · Features · How it works · Pricing`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-elementor-device-mode="desktop"`), and stylesheet rule `html { line-height:1.15;-webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.elementor-element> — `Any workout video becomes a routin`)**:
   - Landmark `<section class="elementor-element elementor-element-rmfeatsec">` presenting display lead `Any workout video becomes a routine you can` and copy excerpt *"Paste a link from YouTube, Instagram, or TikTok. Get illustrated "* over `#f5f7fb` canvas and `#0e1116` ink.
3. **Primary Showcase & Content Grid (<section.elementor-element-rmhowsec> — `Read once, run hands-free`)**:
   - Landmark `<section class="elementor-element elementor-element-rmhowsec">` rendering section `Read once, run hands-free` with copy *"Reel Motion reads the video for you, then hands back a workout yo"*, asset references (`fonts.googleapis.com`, `embed`, `reset.css`, `theme.css`), and grid rule `before { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.elementor-element-rmpricesec> — `Illustrated exercises`)**:
   - Landmark `<section class="elementor-element elementor-element-rmpricesec">` framing `Illustrated exercises` and `Hands-free control` (*"Start and finish positions, drawn for every move."*) with `#ffffff` surface cards, `#0d95e8` accents, and `pre { font-family:monospace;font-size:1em;white-space:pre-wrap }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://reelmotion.fit/`)**:
   - Landmark `<footer class="elementor elementor-68">` anchoring `Reel Motion: Turn Workout Videos` footer links (`Reel Motion · Home · Features · How it works · Pricing`), copy *"Say start, next, or done. Your phone stays on the floor."*, and `#cccccc` structural dividers.
