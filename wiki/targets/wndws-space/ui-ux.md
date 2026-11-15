# UI & UX Architecture: wndws-space

## Overview & Design Identity
- **Target**: `wndws-space` (**windows · place is temporary. you are not.**)
- **Production URL**: [https://wndws.space/](https://wndws.space/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#dcdcdc` / `#000`)
- **Summary**: Upload your window — tell what chapter of life you're living through.
- **Total Clean CSS Variables Extracted**: `13` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Times New Roman`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#dcdcdc` | `html::-webkit-scrollbar-thumb { background: #dcdcdc }` |
| **Primary Typography Ink** | `#cacaca` | `html::-webkit-scrollbar-thumb { border: #cacaca }` |
| **Elevated Surface / Card Substrate** | `#fff` | `tml.prelude-route::-webkit-scro... { border-color: #fff }` |
| **Interactive Accent / Highlight** | `#000` | `::-moz-selection { color: #000 }` |
| **Secondary / Muted Copy** | `#d9d9d9` | `::-webkit-scrollbar-thumb { background: #d9d9d9 }` |
| **Structural Hairline Border** | `#c9c9c9` | `::-webkit-scrollbar-thumb:hover { background: #c9c9c9 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-reveal-duration` | `.92s` | Typography Ink Token |
| `--text-reveal-ease` | `cubic-bezier(.22,1,.36,1)` | Typography Ink Token |
| `--frame` | `10px` | Dimension / Scale Token |
| `--frame-radius` | `6px` | Elevation / Border Token |
| `--nav-drop` | `8px` | Layout / Spatial Grid Token |
| `--fr` | `var(--frame-radius)` | Dimension / Scale Token |
| `--edge` | `linear-gradient(#000,#000)` | Color / Atmospheric Token |
| `--band` | `10px` | Dimension / Scale Token |
| `--logo-h` | `25px` | Dimension / Scale Token |
| `--lift` | `0px` | Dimension / Scale Token |
| `--slide` | `-7px` | Dimension / Scale Token |
| `--tilt` | `-2.5deg` | Design System Custom Token |
| `--teaser-i` | `0` | Motion / Easing Token |
| `--wndws-space-bg` | `#dcdcdc` | Canvas Substrate (from `html::-webkit-scrollbar-thumb { background: #dcdcdc }`) |
| `--wndws-space-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--wndws-space-surface` | `#fff` | Surface Substrate (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `wndws-space`)**:
   - Landmark `<nav class="nav">` hosting `windows · place is temporary. you ar` navigation (`prelude prelude`), DOM attributes (`data-v-20a15833`, `data-v-e0841100`, `data-v-feaf1087`, `data-v-217c40e4`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<div.custom-cursor-enabled> — `windows · place is temporary. you `)**:
   - Landmark `<div class="custom-cursor-enabled">` presenting display lead `windows · place is temporary. you are not.` and copy excerpt *"windows · place is temporary. you are not."* over `#dcdcdc` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<div.nuxt-route-announcer> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="nuxt-route-announcer">` rendering section `Featured Work & Interactive Showcase` with copy *"𝕲𝖊𝖔𝖗𝖌𝖎𝖔 𝕲𝖔𝖌𝖆𝖓𝖓𝖎 — Tbilisi, Georgia"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `entry.DtyUHzly.css`), and grid rule `html::-webkit-scrollbar { width:10px }`.
4. **Interactive Detail & Feature Matrix (<div.route-stage> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="route-stage">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Rita — Moscow, Russia"*) with `#fff` surface cards, `#000` accents, and `html::-webkit-scrollbar-track { background:transparent }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://wndws.space/`)**:
   - Landmark `<footer class="site-footer">` anchoring `windows · place is temporary. yo` footer links (`prelude prelude`), copy *"Andrey — Marseille, France"*, and `#c9c9c9` structural dividers.
