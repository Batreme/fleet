---
title: "UI & UX Architecture: aya-nl"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: aya-nl

## Overview & Design Identity
- **Target**: `aya-nl` (**Danstheater AYA - eigenzinnige voorstellingen voor jong publiek**)
- **Production URL**: [https://aya.nl](https://aya.nl)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#ff2f11` canvas, `#fffdfd` ink, `#0000ee` accent)
- **Summary**: AYA voorstellingen voor kinderen en jongeren spelen in theaters en op scholen. Met een spannende mix van dans, spel, zang en livemuziek u...
- **Total Clean CSS Variables Extracted**: `66` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Copal Std Solid`
- **Body Font Stack**: `Copal Std Solid Placeholder`
- **Monospace / Technical Font Stack**: `Fragment Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 104px`, `line-height: 93.6px`, `font-weight: 400`); rule `h1` (`font-size: 64px`, `line-height: 90%`, `letter-spacing: 0em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 82px`, `line-height: 73.8px`, `font-weight: 400`); rule `h2` (`font-size: 56px`, `line-height: 90%`, `letter-spacing: 0em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 18px`, `line-height: 140%`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ff2f11` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fffdfd` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#191717` | `-n7gQ8 .framer-styles-preset-zd... { background-color: #191717 }` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#000000` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f02c10` | `var(--border-color)` in `:root` (`rgba(0, 0, 0, 0.06)`) |
| **Variable Token (`--token-663e5150-46d2-40b1-95af-592c05b7fae4`)** | `#f1ead8` | `var(--token-663e5150-46d2-40b1-95af-592c05b7fae4)` in `:root` |
| **Variable Token (`--token-0af63665-dda9-44b8-ad7f-2dd784961186`)** | `#948a8a` | `var(--token-0af63665-dda9-44b8-ad7f-2dd784961186)` in `:root` |
| **Variable Token (`--token-52487f1d-1e6b-4aed-b3c9-9be3b54f4138`)** | `#c3b5f9` | `var(--token-52487f1d-1e6b-4aed-b3c9-9be3b54f4138)` in `:root` |
| **Variable Token (`--token-3bf58b77-e2f0-4be9-9dc5-677a4ffe590d`)** | `#b185dc` | `var(--token-3bf58b77-e2f0-4be9-9dc5-677a4ffe590d)` in `:root` |
| **Variable Token (`--token-d2bc2ea8-f8c3-4125-b01e-8ddfab04ae3e`)** | `#9759de` | `var(--token-d2bc2ea8-f8c3-4125-b01e-8ddfab04ae3e)` in `:root` |
| **Variable Token (`--token-cdc1cd47-38f4-40aa-a3b4-638453d43e33`)** | `#740180` | `var(--token-cdc1cd47-38f4-40aa-a3b4-638453d43e33)` in `:root` |
| **Variable Token (`--token-7164b3b8-4b85-4deb-9335-cef9eefdbce4`)** | `#e4fc51` | `var(--token-7164b3b8-4b85-4deb-9335-cef9eefdbce4)` in `:root` |
| **Variable Token (`--token-fea6ee1e-8ef0-442e-a2a0-c12d9de040df`)** | `#6dfe1f` | `var(--token-fea6ee1e-8ef0-442e-a2a0-c12d9de040df)` in `:root` |
| **Variable Token (`--token-8916fd57-bc64-4336-8d71-cd1b8ea49a35`)** | `#79b18d` | `var(--token-8916fd57-bc64-4336-8d71-cd1b8ea49a35)` in `:root` |
| **Variable Token (`--token-dbf88913-7943-413d-87e4-f9ef23a07d87`)** | `#5a5e25` | `var(--token-dbf88913-7943-413d-87e4-f9ef23a07d87)` in `:root` |
| **Variable Token (`--token-ec796718-9e9b-44e7-9bfe-925cd88b05d8`)** | `#01a127` | `var(--token-ec796718-9e9b-44e7-9bfe-925cd88b05d8)` in `:root` |
| **Variable Token (`--token-6cd2dfce-0dc1-457b-ad40-6aff16787638`)** | `#2e5745` | `var(--token-6cd2dfce-0dc1-457b-ad40-6aff16787638)` in `:root` |
| **Variable Token (`--token-bde3f413-9fb1-4992-8a57-31caf08869e1`)** | `#eac4c8` | `var(--token-bde3f413-9fb1-4992-8a57-31caf08869e1)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-721acf4f-d590-43e6-b5df-f984cd027c07` | `#191717` | Color / Atmospheric Token |
| `--token-62705c1f-74ca-4581-86e6-11f8a22c6ec9` | `#ff2f11` | Color / Atmospheric Token |
| `--token-663e5150-46d2-40b1-95af-592c05b7fae4` | `#f1ead8` | Color / Atmospheric Token |
| `--token-d7cd2efb-fc4c-4268-93d0-66c609851248` | `#fffdfd` | Color / Atmospheric Token |
| `--token-0af63665-dda9-44b8-ad7f-2dd784961186` | `#948a8a` | Color / Atmospheric Token |
| `--token-52487f1d-1e6b-4aed-b3c9-9be3b54f4138` | `#c3b5f9` | Color / Atmospheric Token |
| `--token-3bf58b77-e2f0-4be9-9dc5-677a4ffe590d` | `#b185dc` | Color / Atmospheric Token |
| `--token-d2bc2ea8-f8c3-4125-b01e-8ddfab04ae3e` | `#9759de` | Color / Atmospheric Token |
| `--token-cdc1cd47-38f4-40aa-a3b4-638453d43e33` | `#740180` | Color / Atmospheric Token |
| `--token-7164b3b8-4b85-4deb-9335-cef9eefdbce4` | `#e4fc51` | Color / Atmospheric Token |
| `--token-fea6ee1e-8ef0-442e-a2a0-c12d9de040df` | `#6dfe1f` | Color / Atmospheric Token |
| `--token-8916fd57-bc64-4336-8d71-cd1b8ea49a35` | `#79b18d` | Color / Atmospheric Token |
| `--token-dbf88913-7943-413d-87e4-f9ef23a07d87` | `#5a5e25` | Color / Atmospheric Token |
| `--token-ec796718-9e9b-44e7-9bfe-925cd88b05d8` | `#01a127` | Color / Atmospheric Token |
| `--token-6cd2dfce-0dc1-457b-ad40-6aff16787638` | `#2e5745` | Color / Atmospheric Token |
| `--token-bde3f413-9fb1-4992-8a57-31caf08869e1` | `#eac4c8` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.framer-pbvui3> — `aya-nl`)**:
   - Landmark `<header class="framer-pbvui3">` (`1440x54px`) hosting `Danstheater AYA - eigenzinnige voors` navigation (`Agenda · Voorstellingen · Educatie · Over Aya · Nieuws`), DOM attributes (`data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`), and stylesheet rule `font-face { font-family: "Copal Std Solid"; src: url("https://framerusercontent.com/... }`.
2. **Hero Stage & Focal Lead (<section.framer-Z9U3S> — `BRRROTHERS 6+`)**:
   - Landmark `<section class="framer-Z9U3S framer-cwJq3">` presenting display lead `BRRROTHERS 6+` and copy excerpt *"Overload 12+ Ontdek"* over `#ff2f11` canvas and `#fffdfd` ink.
3. **Primary Showcase & Content Grid (<section.framer-NxIXs> — `Eigenzinnig danstheater voor een j`)**:
   - Landmark `<section class="framer-NxIXs framer-X0WqL">` rendering section `Eigenzinnig danstheater voor een jong publiek.` with copy *"Spreken zonder woorden 12+ Ontdek"*, asset references (`Or12pwiuyAgiMvRWdQLIcZMcr0.svg`, `LLqEU4Zu3OKa98ycxXoQ6T8bHQ.png`, `476311956316258`, `fbevents.js`), and grid rule `.hidden-72rtr7 { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-T1bJL> — `Spreken zonder woorden 12+ Ontdek`)**:
   - Landmark `<section class="framer-T1bJL framer-X0WqL">` framing `Spreken zonder woorden 12+ Ontdek` and `Kokolampu 10+ Ontdek` (*"Kokolampu 10+ Ontdek"*) with `#191717` surface cards, `#0000ee` accents, and `.hidden-rjvtpu { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-Ysu5g> — `https://aya.nl`)**:
   - Landmark `<footer class="framer-Ysu5g framer-QSpah">` anchoring `Danstheater AYA - eigenzinnige v` footer links (`Agenda · Voorstellingen · Educatie · Over Aya · Nieuws`), copy *"UP NEXT: Stilzitten is voor stoelen 7+ Ontdek"*, and `#f02c10` structural dividers.
