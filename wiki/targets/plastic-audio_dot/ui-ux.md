# UI & UX Architecture: plastic-audio_dot

## Overview & Design Identity
- **Target**: `plastic-audio_dot` (**Record internal audio on Mac, with key and BPM · DOT**)
- **Production URL**: [https://plastic.audio/dot/](https://plastic.audio/dot/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#F2F0EA` canvas, `#0A0908` ink, `#5A5853` accent)
- **Summary**: Record internal audio on Mac with no BlackHole or Soundflower to set up. DOT gives every clip its key, BPM and chords. Drag it into your...
- **Total Clean CSS Variables Extracted**: `33` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Uncut Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.78em`, `12px`, `15px`, `11px`, `18px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.78em`, `12px`, `15px`, `11px`, `18px`)
- **Body Copy**: rule `p` (`font-size: calc(var(--u)*16/18)`, `line-height: calc(var(--u)*24/18)`)
- **Metadata & Labels**: rule `.label` (`font-size: calc(var(--u)*12/18)`, `line-height: calc(var(--u)*20/18)`, `letter-spacing: .1em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#F2F0EA` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#0A0908` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#86847E` | `var(--grey)` in `:root` |
| **Interactive Accent / Highlight** | `#5A5853` | `var(--faint)` in `:root` |
| **Secondary / Muted Copy** | `#3A3834` | `var(--hair)` in `:root` |
| **Structural Hairline Border** | `#DA291C` | `var(--red)` in `:root` |

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
   - Landmark `<header class="pn">` hosting `Record internal audio on Mac, with k` navigation (`How it works · Pricing`), DOM attributes (`data-cfasync="false"`, `data-state="open"`, `data-loaded="1"`, `data-src="media/demo-av1.mp4?v=..."`), and stylesheet rule `a:hover { color:F2F0EA }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Catch any sound your Mac plays.`)**:
   - Landmark `<section class="hero">` presenting display lead `Catch any sound your Mac plays.` and copy excerpt *"DOT Audio Recorder DOT"* over `#F2F0EA` canvas and `#0A0908` ink.
3. **Primary Showcase & Content Grid (<section.intro> — `From “what was that?” to a clip in`)**:
   - Landmark `<section class="intro">` rendering section `From “what was that?” to a clip in your session` with copy *"DOT Audio Recorder"*, asset references (`s.js`, `favicon.ico`, `icon.svg`, `apple-touch-icon.png`), and grid rule `.sr { position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0) }`.
4. **Interactive Detail & Feature Matrix (<section.statement> — `Know the key and BPM before you us`)**:
   - Landmark `<section class="statement">` framing `Know the key and BPM before you use it.` and `Record without leaving your DAW.` (*"DOT Audio Recorder Catch any sound your Mac plays."*) with `#86847E` surface cards, `#5A5853` accents, and `.rdot.s { width:8px;height:8px;margin:0 10px 0 0;transform:none;vertical-align:1px }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://plastic.audio/dot/`)**:
   - Landmark `<footer class="foot pfoot">` anchoring `Record internal audio on Mac, wi` footer links (`How it works · Pricing`), copy *"Catch any sound your Mac plays."*, and `#DA291C` structural dividers.
