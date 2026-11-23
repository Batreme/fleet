---
title: "UI & UX Architecture: www-velaaprivateisland-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-velaaprivateisland-com

## Overview & Design Identity
- **Target**: `www-velaaprivateisland-com` (**Velaa Private Island Maldives**)
- **Production URL**: [https://www.velaaprivateisland.com/](https://www.velaaprivateisland.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#e8e6df` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: The World's Best Kept Secret
- **Total Clean CSS Variables Extracted**: `48` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Canela Text LC Web Thin`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 80px`, `font-weight: 100`, `letter-spacing: -1.6px`); CSS variables `--text-truncation-display-inline-for-safari-16: inline`, `--text-truncation-display-none-for-safari-16: none`; rule `h1` (`font-size: 60px`, `line-height: 100%`, `letter-spacing: -.02em`, `font-weight: 100`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 60px`, `font-weight: 100`, `letter-spacing: -1.2px`); rule `h2` (`font-size: 48px`, `line-height: 100%`, `letter-spacing: -.02em`, `font-weight: 100`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 150%`, `letter-spacing: 0em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e8e6df` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `2lq7sn.rich-text-wrapper blockq... { background-color: #dddddd }` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#4b4335` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#8a8479` | `var(--border-color)` in `:root` (`var(--token-b2023aa5-98b5-447b-bf...`) |
| **Variable Token (`--token-df8a0dff-7898-4597-93d1-7c8c4165687e`)** | `#ffffff` | `var(--token-df8a0dff-7898-4597-93d1-7c8c4165687e)` in `:root` |
| **Variable Token (`--token-64804b58-d0c9-408c-8ef8-18e7c8c4fa42`)** | `#fffc` | `var(--token-64804b58-d0c9-408c-8ef8-18e7c8c4fa42)` in `:root` |
| **Variable Token (`--token-c9cc39ca-b83c-4612-97b2-3b045f31b8b2`)** | `#fff9` | `var(--token-c9cc39ca-b83c-4612-97b2-3b045f31b8b2)` in `:root` |
| **Variable Token (`--token-04acd034-cd76-4966-889c-0be31a7f0cd7`)** | `#010101` | `var(--token-04acd034-cd76-4966-889c-0be31a7f0cd7)` in `:root` |
| **Variable Token (`--token-63ce1974-4123-43fe-af3f-45583d0362a1`)** | `#040326` | `var(--token-63ce1974-4123-43fe-af3f-45583d0362a1)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-df8a0dff-7898-4597-93d1-7c8c4165687e` | `#fff` | Color / Atmospheric Token |
| `--token-64804b58-d0c9-408c-8ef8-18e7c8c4fa42` | `#fffc` | Color / Atmospheric Token |
| `--token-c9cc39ca-b83c-4612-97b2-3b045f31b8b2` | `#fff9` | Color / Atmospheric Token |
| `--token-04acd034-cd76-4966-889c-0be31a7f0cd7` | `#010101` | Color / Atmospheric Token |
| `--token-59d5d661-5e78-4b72-9e79-cd47aff41722` | `#e8e6df` | Color / Atmospheric Token |
| `--token-0a872567-8429-4796-9d1f-16128f686cfc` | `#4b4335` | Color / Atmospheric Token |
| `--token-a75c5af9-0c80-4a37-bd5a-30e8355d8a08` | `#010101cc` | Color / Atmospheric Token |
| `--token-b2023aa5-98b5-447b-bfed-ac60292ed2aa` | `#4b433599` | Color / Atmospheric Token |
| `--token-c05169e4-f21b-4021-88d5-c3405b44ef9c` | `#01010199` | Color / Atmospheric Token |
| `--token-3c8552f2-f351-49db-acd1-4cf7d791ba30` | `#4b433533` | Color / Atmospheric Token |
| `--token-63ce1974-4123-43fe-af3f-45583d0362a1` | `#040326` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-velaaprivateisland-com`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Velaa Private Island Maldives` navigation (`Find your home · Step into adventure · Explore all dining · See what awaits · Villas Villas`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<div.lenis-autoToggle> — `A symphony of flavours & shared mo`)**:
   - Landmark `<div class="lenis-autoToggle">` presenting display lead `A symphony of flavours & shared moments` and copy excerpt *"From the moment you arrive, the world outside fades. The air is l"* over `#e8e6df` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.framer-Olafn> — `Velaa is a world of its own.`)**:
   - Landmark `<div class="framer-Olafn">` rendering section `Velaa is a world of its own.` with copy *"Discover Story of Velaa"*, asset references (`SeYxW6iTSKyLSDpsNhJ7cT1OhI.png`, `GXFdcLw3RCaSfwQY7YSTLdzO0Vk.png`, `fonts.gstatic.com`, `script`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<div.framer-h13ff> — `T h e a r t o f c o m i n g h o m `)**:
   - Landmark `<div class="framer-h13ff">` framing `T h e a r t o f c o m i n g h o m e , w h e r e e...` and `More than paradise, it's the feeling of being exa...` (*"Your personal butler is the guardian of your peace. It’s beyond s"*) with `#dddddd` surface cards, `#0000ee` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.framer-sg5GW> — `https://www.velaaprivateisland.com/`)**:
   - Landmark `<footer class="framer-sg5GW">` anchoring `Velaa Private Island Maldives` footer links (`Find your home · Step into adventure · Explore all dining · See what awaits · Villas Villas`), copy *"Everything at Velaa begins with majaa — the spirit of joy an"*, and `#8a8479` structural dividers.
