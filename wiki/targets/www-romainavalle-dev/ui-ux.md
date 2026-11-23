---
title: "UI & UX Architecture: www-romainavalle-dev"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-romainavalle-dev

## Overview & Design Identity
- **Target**: `www-romainavalle-dev` (**Romain Avalle - Interactive developper**)
- **Production URL**: [https://www.romainavalle.dev/](https://www.romainavalle.dev/)
- **Final Redirected URL**: [https://romainavalle.dev/](https://romainavalle.dev/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#f3f2f1`)
- **Summary**: Romain Avalle, interactive developer since 2006. Team Lead & Tech Lead at REF Digital in Montréal. Awwwards jury member, 40+ Awwwards and...
- **Total Clean CSS Variables Extracted**: `11` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `RemusVariableVF`
- **Body Font Stack**: `RemusVariableVF`
- **Monospace / Technical Font Stack**: `andale-mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`)
- **Body Copy**: live computed `body` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`); rule `,body` (`font-size: 1.6rem`, `line-height: 1.2`, `letter-spacing: -.03rem`, `font-weight: 600`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12.3429px`, `line-height: 14.8114px`, `font-weight: 600`, `letter-spacing: -0.308571px`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f3f2f1` | `<meta name="theme-color" content="#f3f2f1">` in `dom.html` |
| **Secondary / Muted Copy** | `#000000` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000000` | hairline divider derived from secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `375` | Layout / Spatial Grid Token |
| `--lvh` | `1lvh` | Layout / Spatial Grid Token |
| `--dvh` | `1dvh` | Layout / Spatial Grid Token |
| `--svh` | `1svh` | Layout / Spatial Grid Token |
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.23, 1, .32, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-translate-z` | `0` | Design System Custom Token |
| `--www-romainavalle-bg` | `#ffffff` | Canvas Substrate (from live computed `browser-default` `background-color` (`computed_styles.json`)) |
| `--www-romainavalle-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.gap-8> — `www-romainavalle-dev`)**:
   - Landmark `<header class="gap-8 bottom-30">` (`337x31px`) hosting `Romain Avalle - Interactive developp` navigation (`Let's talk`), DOM attributes (`data-v-54411a74`, `data-char="R"`, `data-char="o"`, `data-char="m"`), and stylesheet rule `.common-scene { height:100lvh }`.
2. **Hero Stage & Focal Lead (<section.white> — `Romain Avalle`)**:
   - Landmark `<section class="white">` presenting display lead `Romain Avalle` and copy excerpt *"I'm Romain Avalle, an interactive developer with 20 years of dedi"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-black> — `R o m a i n A v a l l e`)**:
   - Landmark `<section class="bg-black">` rendering section `R o m a i n A v a l l e` with copy *"Interactive Developer"*, asset references (`gtm.js`, `_payload.json`, `BC66KIH3.js`, `B3W-aES6.js`), and grid rule `before { transform:scaleX(1) }`.
4. **Interactive Detail & Feature Matrix (<section.text-white> — `I n t e r a c t i v e D e v e l o `)**:
   - Landmark `<section class="text-white">` framing `I n t e r a c t i v e D e v e l o p e r` and `█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ` (*"█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░"*) with `#000000` surface cards, `#f3f2f1` accents, and `html.lenis body { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.z-1> — `https://www.romainavalle.dev/`)**:
   - Landmark `<footer class="z-1 h-screen">` anchoring `Romain Avalle - Interactive deve` footer links (`Let's talk`), copy *"R o m a i n A v a l l e"*, and `#000000` structural dividers.
