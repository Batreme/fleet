---
title: "UI & UX Architecture: baboonbutts-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: baboonbutts-com

## Overview & Design Identity
- **Target**: `baboonbutts-com` (**Baboon Butts - The redder the better!**)
- **Production URL**: [https://baboonbutts.com/](https://baboonbutts.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#00c2ff` accent)
- **Summary**: This Cheeky ad campaign to show how effective a little strategy – and a lot of raunchy visuals and messaging – can be.
- **Total Clean CSS Variables Extracted**: `769` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `mono45-headline`
- **Body Font Stack**: `mono45-headline`
- **Monospace / Technical Font Stack**: `mono45-headline`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 120px`, `line-height: 96px`, `font-weight: 400`); CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `h1` (`font-size: clamp(3rem, -3.3099rem + 13.1...`, `line-height: 0.8`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 33.6842px`, `font-weight: 400`); rule `h2` (`font-size: clamp(2.1875rem, 1.7493rem +...`, `line-height: 0.8421052632`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `body` (`line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 32px`, `line-height: 26.88px`, `font-weight: 400`); CSS variables `--gf-ctrl-label-font-size-primary: var(--wp--preset--font-size--32-px)`, `--gf-ctrl-label-font-size-req: var(--wp--preset--font-size--32-px)`, `--gf-ctrl-label-font-weight-req: 700`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#204ce5` | `var(--gf-field-pg-prog-bar-bg-color-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#00c2ff` | `var(--gf-field-pg-prog-bar-bg-gradient-blues)` in `:root` |
| **Secondary / Muted Copy** | `#112337` | `var(--gf-color-secondary-contrast)` in `:root` |
| **Structural Hairline Border** | `#204ce5` | `gform-datepicker-calendar td.se... { border: #204ce5 }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--wp--style--global--content-size` | `82.125rem` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `82.125rem` | Layout / Spatial Grid Token |
| `--header-height` | `90px` | Layout / Spatial Grid Token |
| `--gf-form-gap-x` | `32px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wp-block-thirtysixblocks-header> — `baboonbutts-com`)**:
   - Landmark `<header class="wp-block-thirtysixblocks-header">` (`1440x90px`) hosting `Baboon Butts - The redder the better` navigation (`Get a Hold of Us`), DOM attributes (`data-magnet`, `data-magnet-movement="80"`, `data-magnet-rotation="15"`, `data-magnet-smooth="0.5"`), and stylesheet rule `.gform-theme--framework ::before { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.wp-block-thirtysixblocks-slide> — `Before billboards, branding, and b`)**:
   - Landmark `<section class="wp-block-thirtysixblocks-slide slide-intro">` presenting display lead `Before billboards, branding, and billion-dollar a...` and copy excerpt *"“*” indicates required fields"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.wp-block-thirtysixblocks-image> — `Meet one of nature’s most eye-catc`)**:
   - Landmark `<section class="wp-block-thirtysixblocks-image">` rendering section `Meet one of nature’s most eye-catching advertisin...` with copy *"A cheeky look at one of nature’s most successful forms of adverti"*, asset references (`insight.min.js`, `use.typekit.net`, `style-index.css`, `bmx2okd.css`), and grid rule `.gform-theme--framework button { cursor:revert }`.
4. **Interactive Detail & Feature Matrix (<section.wp-block-thirtysixblocks-slide:nth(2)> — `The baboon’s brilliantly bold back`)**:
   - Landmark `<section class="wp-block-thirtysixblocks-slide">` framing `The baboon’s brilliantly bold backside. T h e b a...` and `For female baboons, a bright, swollen backside is...` (*"Before billboards, branding, and billion-dollar ad campaigns, nat"*) with `#204ce5` surface cards, `#00c2ff` accents, and `.gform-theme--framework img { max-inline-size:100%;max-block-size:100% }`.
5. **Colophon & Global Directory Footer (<footer.wp-block-thirtysixblocks-footer> — `https://baboonbutts.com/`)**:
   - Landmark `<footer class="wp-block-thirtysixblocks-footer">` anchoring `Baboon Butts - The redder the be` footer links (`Get a Hold of Us`), copy *"B e f o r e b i l l b o a r d s , b r a n d i n g , a n d b "*, and `#204ce5` structural dividers.
