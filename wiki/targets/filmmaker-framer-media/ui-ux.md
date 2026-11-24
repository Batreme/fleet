---
title: "UI & UX Architecture: filmmaker-framer-media"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: filmmaker-framer-media

## Overview & Design Identity
- **Target**: `filmmaker-framer-media` (**Filmmaker — Portfolio for Directors & Studios**)
- **Production URL**: [https://filmmaker.framer.media/](https://filmmaker.framer.media/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0000ee`)
- **Summary**: An independent film studio directing, shooting and finishing commercials, music videos, documentaries and short films, from the first ide...
- **Total Clean CSS Variables Extracted**: `29` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Switzer`
- **Body Font Stack**: `Switzer Placeholder`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`, `letter-spacing: -0.96px`); rule `h1` (`font-size: 48px`, `line-height: 1em`, `letter-spacing: -.02em`, `font-weight: 700`)
- **Section Heading (`H2`)**: observed font-size ladder: `48px`, `12px`, `14px`, `var(--font-size)`, `var(--framer-font-size)`
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 24px`, `line-height: 1.25em`, `letter-spacing: -.01em`, `font-weight: 600`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--selection-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#0000ee` | hairline divider derived from live computed `a` `color` (`computed_styles.json`) |
| **Variable Token (`--token-1ff0dbc2-5727-4025-9011-ab5e4843a4bf`)** | `#8e929e` | `var(--token-1ff0dbc2-5727-4025-9011-ab5e4843a4bf)` in `:root` |
| **Variable Token (`--token-0a4f7205-8d7c-4457-b654-54014e40dc6b`)** | `#494b52` | `var(--token-0a4f7205-8d7c-4457-b654-54014e40dc6b)` in `:root` |
| **Variable Token (`--token-1be011e0-feca-4140-878b-b3b075f07f18`)** | `#222224` | `var(--token-1be011e0-feca-4140-878b-b3b075f07f18)` in `:root` |
| **Variable Token (`--token-107047f9-7a86-4585-a089-f7c6945f5b94`)** | `#ff4444` | `var(--token-107047f9-7a86-4585-a089-f7c6945f5b94)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-f411dcae-2c7e-4242-8a06-6993e5583d49` | `#fff` | Color / Atmospheric Token |
| `--token-f454398d-5d46-4a7c-87d9-57e6a7bcdcf8` | `#000` | Color / Atmospheric Token |
| `--token-1ff0dbc2-5727-4025-9011-ab5e4843a4bf` | `#8e929e` | Color / Atmospheric Token |
| `--token-0a4f7205-8d7c-4457-b654-54014e40dc6b` | `#494b52` | Color / Atmospheric Token |
| `--token-1be011e0-feca-4140-878b-b3b075f07f18` | `#222224` | Color / Atmospheric Token |
| `--token-107047f9-7a86-4585-a089-f7c6945f5b94` | `#f44` | Color / Atmospheric Token |
| `--infinity` | `infinity` | Design System Custom Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `filmmaker-framer-media`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Filmmaker — Portfolio for Directors ` navigation (`Home · Works · About · Press · Contact`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<div.lenis-autoToggle> — `Filmmaker: a film studio for comme`)**:
   - Landmark `<div class="lenis-autoToggle">` presenting display lead `Filmmaker: a film studio for commercials, music v...` and copy excerpt *"(Scroll to explore)"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.lenis-stopped> — `Bloom`)**:
   - Landmark `<div class="lenis-stopped">` rendering section `Bloom` with copy *"Create a free website with Framer, the website builder loved by s"*, asset references (`VBRLrBkFJJ3iKvr3ee0PscUivO0.png`, `gOHbZD6M7GPcLWoAJjxuSCzbM4.png`, `script`, `gyMkyphEohfoNDaOxqDjcfioUEg.jpg`), and grid rule `.hidden-kh3wqm { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<div.framer-v2pXD> — `Red Lens`)**:
   - Landmark `<div class="framer-v2pXD">` framing `Red Lens` and `Second Skin` (*"Bloom"*) with `#ffffff` surface cards, `#0000ee` accents, and `.hidden-s381sx { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-nvb9y9> — `https://filmmaker.framer.media/`)**:
   - Landmark `<footer class="framer-nvb9y9">` anchoring `Filmmaker — Portfolio for Direct` footer links (`Home · Works · About · Press · Contact`), copy *"Red Lens"*, and `#0000ee` structural dividers.
