---
title: "UI & UX Architecture: b3xgraphics-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: b3xgraphics-com

## Overview & Design Identity
- **Target**: `b3xgraphics-com` (**B3X Graphics · Freelance Sports Art Director & Designer**)
- **Production URL**: [https://b3xgraphics.com/](https://b3xgraphics.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#02132c` canvas, `#ffffff` ink, `#0073ff` accent)
- **Summary**: B3X Graphics: freelance art direction and design specialising in sport. Branding, campaign design and socials content for some of the big...
- **Total Clean CSS Variables Extracted**: `192` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Palma Heavy`
- **Body Font Stack**: `Aileron`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 110.88px`, `line-height: 110.88px`, `font-weight: 600`); CSS variables `--cc-font-display: 'Palma Heavy' , sans-serif`, `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: clamp(44px,7vw,96px)`, `line-height: 1.08`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 27.36px`, `line-height: 27.36px`, `font-weight: 600`); rule `h2` (`font-size: 2rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--cc-font-body: 'Aileron' , sans-serif`; rule `p` (`font-size: 15.5px`, `line-height: 1.62`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#02132c` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#061a3a` | `var(--proj-bg-2)` in `:root` |
| **Interactive Accent / Highlight** | `#0073ff` | `var(--e-global-color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#767676` | `var(--wc-subtext)` in `:root` |
| **Structural Hairline Border** | `#25344a` | `var(--line)` in `:root` (`rgba(255,255,255,.14)`) |
| **Variable Token (`--cc-ink`)** | `#031b3d` | `var(--cc-ink)` in `:root` |
| **Variable Token (`--cc-bone`)** | `#eaf2ff` | `var(--cc-bone)` in `:root` |
| **Variable Token (`--cc-steel`)** | `#606060` | `var(--cc-steel)` in `:root` |
| **Variable Token (`--cc-red`)** | `#0474ff` | `var(--cc-red)` in `:root` |
| **Variable Token (`--cc-gold`)** | `#04b5ff` | `var(--cc-gold)` in `:root` |
| **Variable Token (`--cc-ui-raised`)** | `#0a2347` | `var(--cc-ui-raised)` in `:root` |
| **Variable Token (`--cc-ui-raised-2`)** | `#0d2b57` | `var(--cc-ui-raised-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-ink` | `#031b3d` | Typography Ink Token |
| `--cc-bone` | `#eaf2ff` | Color / Atmospheric Token |
| `--cc-steel` | `#606060` | Color / Atmospheric Token |
| `--cc-red` | `#0474ff` | Color / Atmospheric Token |
| `--cc-gold` | `#04b5ff` | Color / Atmospheric Token |
| `--cc-navy` | `#031b3d` | Layout / Spatial Grid Token |
| `--cc-sky` | `#04b5ff` | Color / Atmospheric Token |
| `--cc-deep` | `#02132c` | Color / Atmospheric Token |
| `--cc-ui-bg` | `#02132c` | Canvas / Surface Token |
| `--cc-ui-raised` | `#0a2347` | Color / Atmospheric Token |
| `--cc-ui-raised-2` | `#0d2b57` | Color / Atmospheric Token |
| `--cc-ui-on-accent` | `#fff` | Brand / Palette Token |
| `--cc-font-display` | `'Palma Heavy' , sans-serif` | Typography / Scale Token |
| `--cc-font-body` | `'Aileron' , sans-serif` | Typography / Scale Token |
| `--navy` | `#031b3d` | Layout / Spatial Grid Token |
| `--sky` | `#04b5ff` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.b3xh-bar> — `b3xgraphics-com`)**:
   - Landmark `<header class="b3xh-bar">` (`1377x88px`) hosting `B3X Graphics · Freelance Sports Art ` navigation (`Home · Projects · The Lab · About · Shop`), DOM attributes (`data-b3xh-page="home"`, `data-b3xh-bound="1"`, `data-elementor-type="wp-page"`, `data-elementor-id="1301"`), and stylesheet rule `html.b3x-blueprint body { background-color:02132c!important;background-image:none!important }`.
2. **Hero Stage & Focal Lead (<section.b3xr-feat> — `B3X GRAPHICS STUDIO`)**:
   - Landmark `<section class="b3xr-feat">` presenting display lead `B3X GRAPHICS STUDIO` and copy excerpt *"I WORK WITH SOME OF THE BIGGEST BRANDS IN SPORT"* over `#02132c` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.b3xt> — `B3X Graphics Studio`)**:
   - Landmark `<section class="b3xt b3xt-armed">` rendering section `B3X Graphics Studio` with copy *"I work with some of the biggest brands in sport"*, asset references (`favicon.svg`, `A.chrome.css,qv=1791897283.pagesp...`, `A.fonts.css,,qv==1791378108+style...`, `home.css`), and grid rule `.b3xbp-lines { filter:drop-shadow(0 0 .6px rgba(2,14,38,.55)) }`.
4. **Interactive Detail & Feature Matrix (<section.b3xt-armed> — `Freelance Art Director & Designer`)**:
   - Landmark `<section class="b3xt b3xt-armed">` framing `Freelance Art Director & Designer` and `Featured projects` (*"2025/26 WSL Champions Social Media"*) with `#061a3a` surface cards, `#0073ff` accents, and `.b3xbp-line { fill:none;stroke:88b0dd;stroke-width:1.1;vector-effect:non-scaling-strok... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://b3xgraphics.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `B3X Graphics · Freelance Sports ` footer links (`Home · Projects · The Lab · About · Shop`), copy *"Spurs 1901 Anniversary Social Media"*, and `#25344a` structural dividers.
