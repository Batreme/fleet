---
title: "UI & UX Architecture: plastic-audio_dot"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: plastic-audio_dot

## Overview & Design Identity
- **Target**: `plastic-audio_dot` (**Record internal audio on Mac, with key and BPM · DOT**)
- **Production URL**: [https://plastic.audio/dot/](https://plastic.audio/dot/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0a0908` canvas, `#f2f0ea` ink, `#088ef9` accent)
- **Summary**: Record internal audio on Mac with no BlackHole or Soundflower to set up. DOT gives every clip its key, BPM and chords. Drag it into your...
- **Total Clean CSS Variables Extracted**: `757` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Uncut Sans`
- **Body Font Stack**: `Uncut Sans`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 88px`, `line-height: 89.76px`, `font-weight: 400`, `letter-spacing: -1.76px`); CSS variables `--listItemCheckMobileDisplay: none`, `--listItemCheckDesktopDisplay: block`; rule `h1` (`font-size: 36px`, `line-height: 48px`, `letter-spacing: -.025em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 73.44px`, `font-weight: 400`, `letter-spacing: -1.44px`); rule `h2` (`font-size: 30px`, `line-height: 39px`, `letter-spacing: -.025em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--linkBrandedRoot-fontSizeBodyLg: clamp(14px,1.143em,20px)`, `--linkBrandedRoot-fontLineHeightBodyLg: clamp(17px,1.43em,25px)`, `--linkBrandedRoot-fontSizeBodyMd: clamp(12px,1em,20px)`; rule `p` (`font-size: calc(var(--u)*16/18)`, `line-height: calc(var(--u)*24/18)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 19px`, `font-weight: 400`); CSS variables `--linkUi-fontSizeLabelLg: var(--linkUi-fontSizeBodyLg)`, `--linkUi-fontSizeLabelMd: var(--linkUi-fontSizeBodyMd)`, `--linkUi-fontSizeLabelSm: var(--linkUi-fontSizeBodySm)`; rule `.label` (`font-size: calc(var(--u)*12/18)`, `line-height: calc(var(--u)*20/18)`, `letter-spacing: .1em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0908` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f2f0ea` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141414` | `var(--lemon-background)` in `:root` |
| **Interactive Accent / Highlight** | `#088ef9` | `var(--linkUi-colorInfo400)` in `:root` |
| **Secondary / Muted Copy** | `#808080` | `var(--lemon-secondary-text)` in `:root` |
| **Structural Hairline Border** | `#ff0000` | `.dragmock .slot { border: #ff0000 }` |
| **Variable Token (`--grey`)** | `#86847e` | `var(--grey)` in `:root` |
| **Variable Token (`--faint`)** | `#5a5853` | `var(--faint)` in `:root` |
| **Variable Token (`--hair`)** | `#3a3834` | `var(--hair)` in `:root` |
| **Variable Token (`--red`)** | `#da291c` | `var(--red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#F2F0EA` | Canvas / Surface Token |
| `--ink` | `#0A0908` | Typography Ink Token |
| `--grey` | `#86847E` | Color / Atmospheric Token |
| `--faint` | `#5A5853` | Color / Atmospheric Token |
| `--hair` | `#3A3834` | Color / Atmospheric Token |
| `--red` | `#DA291C` | Color / Atmospheric Token |
| `--serif` | `"Uncut Sans","Helvetica Neue",Helvetica,sans-serif` | Typography / Scale Token |
| `--in` | `92px` | Dimension / Scale Token |
| `--tie` | `9px` | Dimension / Scale Token |
| `--pair` | `18px` | Dimension / Scale Token |
| `--gs` | `27px` | Dimension / Scale Token |
| `--row` | `36px` | Dimension / Scale Token |
| `--group` | `54px` | Dimension / Scale Token |
| `--section` | `72px` | Dimension / Scale Token |
| `--s96` | `108px` | Dimension / Scale Token |
| `--s128` | `144px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pn> — `plastic-audio_dot`)**:
   - Landmark `<header class="pn">` (`621x56px`) hosting `Record internal audio on Mac, with k` navigation (`How it works · Pricing`), DOM attributes (`data-cfasync="false"`, `data-state="open"`, `data-loaded="1"`, `data-src="media/demo-av1.mp4?v=..."`), and stylesheet rule `a:hover { color:F2F0EA }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Catch any sound your Mac plays.`)**:
   - Landmark `<section class="hero">` presenting display lead `Catch any sound your Mac plays.` and copy excerpt *"Press Record in your menu bar, from any app, even your DAW. DOT k"* over `#0a0908` canvas and `#f2f0ea` ink.
3. **Primary Showcase & Content Grid (<section.intro> — `Press Record in your menu bar, fro`)**:
   - Landmark `<section class="intro">` rendering section `Press Record in your menu bar, from any app, eve` with copy *"DOT Audio Recorder"*, asset references (`s.js`, `favicon.ico`, `icon.svg`, `apple-touch-icon.png`), and grid rule `.sr { position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0) }`.
4. **Interactive Detail & Feature Matrix (<section.statement> — `DOT Audio Recorder`)**:
   - Landmark `<section class="statement">` framing `DOT Audio Recorder` and `DOT Audio Recorder Catch any sound your Mac play` (*"DOT Audio Recorder Catch any sound your Mac plays."*) with `#141414` surface cards, `#088ef9` accents, and `.rdot.s { width:8px;height:8px;margin:0 10px 0 0;transform:none;vertical-align:1px }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://plastic.audio/dot/`)**:
   - Landmark `<footer class="foot pfoot">` anchoring `Record internal audio on Mac, wi` footer links (`How it works · Pricing`), copy *"Catch any sound your Mac plays."*, and `#ff0000` structural dividers.
