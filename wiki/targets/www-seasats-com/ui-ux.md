---
title: "UI & UX Architecture: www-seasats-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-seasats-com

## Overview & Design Identity
- **Target**: `www-seasats-com` (**Seasats · Ocean Autonomy That Works**)
- **Production URL**: [https://www.seasats.com/](https://www.seasats.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fffdfd` / `#4e9a85`)
- **Summary**: Missions completed for defense, science, and commercial customers around the world.
- **Total Clean CSS Variables Extracted**: `138` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `seasonMix`
- **Body Font Stack**: `seasonSans`
- **Monospace / Technical Font Stack**: `supplyMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 124px`, `line-height: 111.6px`, `font-weight: 400`, `letter-spacing: -1.24px`); rule `h1` (`font-size: 4.8rem`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 80px`, `font-weight: 400`, `letter-spacing: -0.8px`); rule `h2` (`font-size: 2.4rem`, `line-height: 1.2`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--body-adjustOffset: calc(59.8rem / -2)`, `--body-adjustScale: 0.66`, `--body-adjustScalePrecise: 0.585`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 24px`, `line-height: 28.8px`, `font-weight: 500`); CSS variables `--fontSupplyMono: "supplyMono","supplyMono Fallback",monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fffdfd` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#232323` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e3ede4` | `var(--modal-contentBackgroundColor)` in `:root` |
| **Interactive Accent / Highlight** | `#4e9a85` | `var(--gradient)` in `:root` |
| **Secondary / Muted Copy** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dcdada` | `.ContentStats_item__LxyN9 { border-top: #dcdada }` |
| **Variable Token (`--gradient`)** | `#183f34` | `var(--gradient)` in `:root` |
| **Variable Token (`--gradient`)** | `#2b3922` | `var(--gradient)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wrapperWidth` | `144rem` | Layout / Spatial Grid Token |
| `--headerHeight` | `7.2rem` | Layout / Spatial Grid Token |
| `--columns` | `24` | Layout / Spatial Grid Token |
| `--gutter` | `1.2rem` | Layout / Spatial Grid Token |
| `--margin` | `3.2rem` | Layout / Spatial Grid Token |
| `--radius` | `0.8rem` | Elevation / Border Token |
| `--colorText` | `#232323` | Typography Ink Token |
| `--colorAccent` | `#e3ede4` | Brand / Palette Token |
| `--gradient` | `linear-gradient(180deg,#4e9a85,#183f34 52.82%,#2b3922 75.83%)` | Color / Atmospheric Token |
| `--body-adjustOffset` | `calc(59.8rem / -2)` | Dimension / Scale Token |
| `--body-adjustScale` | `0.66` | Design System Custom Token |
| `--body-adjustScalePrecise` | `0.585` | Design System Custom Token |
| `--fontSeasonMix` | `"seasonMix","seasonMix Fallback",serif` | Typography / Scale Token |
| `--fontSeasonSans` | `"seasonSans","seasonSans Fallback",sans-serif` | Typography / Scale Token |
| `--fontSupplyMono` | `"supplyMono","supplyMono Fallback",monospace` | Typography / Scale Token |
| `--uiOffset` | `48px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Header_container__U6gzw> — `www-seasats-com`)**:
   - Landmark `<header class="Header_container__U6gzw">` (`1376x72px`) hosting `Seasats · Ocean Autonomy That Works` navigation (`Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `video { margin:0;padding:0;font:inherit;font-size:100%;vertical-align:baseline;b... }`.
2. **Hero Stage & Focal Lead (<main.browser-ui-overlay> — `Ocean Autonomy That Works`)**:
   - Landmark `<main class="browser-ui-overlay">` presenting display lead `Ocean Autonomy That Works` and copy excerpt *"Ocean Autonomy That Works"* over `#fffdfd` canvas and `#232323` ink.
3. **Primary Showcase & Content Grid (<main.browser-ui-overlay--top> — `Deploy in minutes.`)**:
   - Landmark `<main class="browser-ui-overlay--top">` rendering section `Deploy in minutes.` with copy *"E x p l o r e p r o d u c t s E x p l o r e p r o d u c t s"*, asset references (`d11d81b0342c0709.css`, `a14bc365605f91b3.css`, `110e11ba57841c1c.css`, `5ef63a433e26978c.css`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<main.ThemeBackground_background__xCT8k> — `Detect from miles.`)**:
   - Landmark `<main class="ThemeBackground_background__xCT8k">` framing `Detect from miles.` and `React at once.` (*"E x p l o r e p r o d u c t s"*) with `#e3ede4` surface cards, `#4e9a85` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.seasats.com/`)**:
   - Landmark `<footer class="footer Footer_container__kRlyj">` anchoring `Seasats · Ocean Autonomy That Wo` footer links (`Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`), copy *"The coordinates of the ghost fleet."*, and `#dcdada` structural dividers.
