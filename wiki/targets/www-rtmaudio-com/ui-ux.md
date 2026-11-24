---
title: "UI & UX Architecture: www-rtmaudio-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-rtmaudio-com

## Overview & Design Identity
- **Target**: `www-rtmaudio-com` (**RTM Audio · Audio plug-ins for mixing and mastering**)
- **Production URL**: [https://www.rtmaudio.com](https://www.rtmaudio.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0e0f10` / `#d6c5a3`)
- **Summary**: Mixing and mastering plug-ins, built by working engineers. Judge the change. Not the volume.
- **Total Clean CSS Variables Extracted**: `73` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Söhne Breit`
- **Body Font Stack**: `Söhne Breit`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 76.2899px`, `line-height: 71.7125px`, `font-weight: 500`, `letter-spacing: -1.90725px`); CSS variables `--display-weight: 500`, `--t-display: clamp(3.0518rem,2.3212rem + 2.7188vw,4.7684rem)`, `--lh-display: .94`; rule `h1` (`letter-spacing: -.02em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48.8288px`, `line-height: 48.8288px`, `font-weight: 500`, `letter-spacing: -0.976576px`); rule `h2` (`font-size: clamp(2.8rem,8vw,8rem)`, `line-height: .84`, `letter-spacing: -.045em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: 0.288px`); CSS variables `--t-body: 1rem`, `--lh-body: 24px`, `--tr-body: 0`; rule `body` (`letter-spacing: .018em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12.8px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: 1.792px`); CSS variables `--mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace`, `--t-label: .8rem`, `--m-label: .8rem`; rule `small` (`font-size: .65rem`, `letter-spacing: .13em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0e0f10` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f0e9dc` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#121315` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#d6c5a3` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b08b5c` | `var(--ink-dim)` in `:root` |
| **Structural Hairline Border** | `#252524` | `var(--line)` in `:root` (`rgba(240,233,220,.10)`) |
| **Variable Token (`--green`)** | `#57c279` | `var(--green)` in `:root` |
| **Variable Token (`--well`)** | `#07080a` | `var(--well)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--display-weight` | `500` | Design System Custom Token |
| `--void` | `#0e0f10` | Color / Atmospheric Token |
| `--ink` | `#f0e9dc` | Typography Ink Token |
| `--ink-2` | `#d6c5a3` | Typography Ink Token |
| `--ink-dim` | `#b08b5c` | Typography Ink Token |
| `--green` | `#57c279` | Color / Atmospheric Token |
| `--line` | `rgba(240,233,220,.10)` | Color / Atmospheric Token |
| `--line-2` | `rgba(240,233,220,.22)` | Color / Atmospheric Token |
| `--wash` | `rgba(240,233,220,.05)` | Color / Atmospheric Token |
| `--well` | `#07080a` | Color / Atmospheric Token |
| `--raise` | `#121315` | Color / Atmospheric Token |
| `--glass` | `rgba(14,15,16,.72)` | Color / Atmospheric Token |
| `--acc` | `#b08b5c` | Color / Atmospheric Token |
| `--edge` | `inset 0 1px 0 rgba(240,233,220,.07)` | Color / Atmospheric Token |
| `--e1` | `var(--edge),0 1px 0 rgba(0,0,0,.5),0 34px 68px -34px rgba(0,0,0,.7)` | Color / Atmospheric Token |
| `--vignette` | `inset 0 0 34px 6px rgba(0,0,0,.55),inset 0 0 96px 20px rgba(8,6,4,.34)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.campaigns-head> — `www-rtmaudio-com`)**:
   - Landmark `<header class="campaigns-head">` (`1296x194px`) hosting `RTM Audio · Audio plug-ins for mixin` navigation (`Plugins Plugins · Store Store · About About · Account Account`), DOM attributes (`data-consent="granted"`, `data-i18n-key="RTM Audio · Audio plu..."`, `data-i18n-content="Mixing and mastering..."`, `data-i18n-content="Mixing and mastering..."`), and stylesheet rule `root { --display-weight:500; }`.
2. **Hero Stage & Focal Lead (<section.take> — `Judge the change. Not the volume.`)**:
   - Landmark `<section class="take">` presenting display lead `Judge the change. Not the volume.` and copy excerpt *"Mixing and mastering plug-ins, built by working engineers."* over `#0e0f10` canvas and `#f0e9dc` ink.
3. **Primary Showcase & Content Grid (<section.campaigns> — `Nine in the rack.`)**:
   - Landmark `<section class="campaigns">` rendering section `Nine in the rack.` with copy *"EQ, vocals, dynamics and loudness."*, asset references (`clarity.js`, `soehne-breit-kraftig.woff2`, `fonts.css`, `site.css`), and grid rule `body { letter-spacing:.018em }`.
4. **Interactive Detail & Feature Matrix (<article.campaign-panel> — `Your whole rack, in one app.`)**:
   - Landmark `<article class="campaign-panel material-light">` framing `Your whole rack, in one app.` and `One-time licences. No subscription.` (*"Download, install and activate every plug-in you own. Free for Ma"*) with `#121315` surface cards, `#d6c5a3` accents, and `.hero h1 { letter-spacing:-.02em }`.
5. **Colophon & Global Directory Footer (<footer.cn-ground> — `https://www.rtmaudio.com`)**:
   - Landmark `<footer class="cn-ground">` anchoring `RTM Audio · Audio plug-ins for m` footer links (`Plugins Plugins · Store Store · About About · Account Account`), copy *"Try any plug-in in the store first."*, and `#252524` structural dividers.
