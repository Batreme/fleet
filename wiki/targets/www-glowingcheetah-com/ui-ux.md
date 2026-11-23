---
title: "UI & UX Architecture: www-glowingcheetah-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-glowingcheetah-com

## Overview & Design Identity
- **Target**: `www-glowingcheetah-com` (**Glowing Cheetah Studios · Father & Son Indie Game Studio**)
- **Production URL**: [https://www.glowingcheetah.com/](https://www.glowingcheetah.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#131313` canvas, `#ffffff` ink, `#ffff00` accent)
- **Summary**: Glowing Cheetah is a father and son indie studio making games, books and animation. Creators of Pigeon’s Mission, a pixel platformer on S...
- **Total Clean CSS Variables Extracted**: `84` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Ojuju`
- **Body Font Stack**: `Circular Std`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 153px`, `line-height: 137.7px`, `font-weight: 800`, `letter-spacing: 3.06px`); CSS variables `--font-display: "Thanks",Impact,"Arial Narrow",sans-serif`, `--text-display: clamp(56px,6.5vw,96px)`, `--text-h1: 56px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 136.8px`, `line-height: 123.12px`, `font-weight: 800`, `letter-spacing: 1.368px`); CSS variables `--text-h2: 40px`
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--text-body: var(--fg-2)`, `--font-body: "Circular Std",system-ui,sans-serif`, `--leading-body: 1.5`; rule `body` (`font-size: var(--text-body)`, `line-height: var(--leading-body)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--font-mono: "SF Mono",Menlo,Consolas,monospace`, `--text-small: 14px`, `--text-caption: 12px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#131313` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#b00020` | `.sc-logic-error { background: #b00020 }` |
| **Interactive Accent / Highlight** | `#ffff00` | `a:hover { color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#1f1f1f` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2f2f2f` | `var(--line-1)` in `:root` (`rgba(255,255,255,.12)`) |
| **Variable Token (`--night-2`)** | `#2a2a2a` | `var(--night-2)` in `:root` |
| **Variable Token (`--yellow`)** | `#fffdb8` | `var(--yellow)` in `:root` |
| **Variable Token (`--yellow-glow`)** | `#d5b123` | `var(--yellow-glow)` in `:root` |
| **Variable Token (`--yellow-deep`)** | `#b8981c` | `var(--yellow-deep)` in `:root` |
| **Variable Token (`--ember`)** | `#df7042` | `var(--ember)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--night-deep` | `#131313` | Color / Atmospheric Token |
| `--night` | `#1F1F1F` | Color / Atmospheric Token |
| `--night-2` | `#2A2A2A` | Color / Atmospheric Token |
| `--yellow` | `#FFFDB8` | Color / Atmospheric Token |
| `--yellow-glow` | `#D5B123` | Color / Atmospheric Token |
| `--yellow-deep` | `#B8981C` | Color / Atmospheric Token |
| `--ember` | `#DF7042` | Color / Atmospheric Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--ink` | `#1F1F1F` | Typography Ink Token |
| `--fg-1` | `#FFFFFF` | Typography Ink Token |
| `--fg-2` | `rgba(255,255,255,.72)` | Typography Ink Token |
| `--fg-3` | `rgba(255,255,255,.48)` | Typography Ink Token |
| `--line-1` | `rgba(255,255,255,.12)` | Color / Atmospheric Token |
| `--line-2` | `rgba(255,255,255,.24)` | Color / Atmospheric Token |
| `--ink-1` | `#1F1F1F` | Typography Ink Token |
| `--ink-2` | `rgba(31,31,31,.72)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.gc-rv> — `www-glowingcheetah-com`)**:
   - Landmark `<nav class="gc-rv">` (`1440x144px`) hosting `Glowing Cheetah Studios · Father & S` navigation (`Projects · Team · Contact`), DOM attributes (`data-dc-tpl="1"`, `data-sc-name="Root"`, `data-dc-tpl="2"`, `data-dc-tpl="3"`), and stylesheet rule `l.sc-dc-streaming .sc-interp.sc-m... { position:relative; background:color-mix(in srgb,currentColor 5%,transpar... }`.
2. **Hero Stage & Focal Lead (<section.sc-host> — `WE CRAFT STORIES`)**:
   - Landmark `<section class="sc-host">` presenting display lead `WE CRAFT STORIES` and copy excerpt *"We're a father and son creative studio bringing stories to life t"* over `#131313` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.gc-skip> — `We craft stories`)**:
   - Landmark `<section class="gc-skip">` rendering section `We craft stories` with copy *"We're a father and son creative studio bringing stories to life t"*, asset references (`clarity.js`, `ylwyja15eg`, `icon.svg`, `favicon-32.png`), and grid rule `before { animation:none; background:color-mix(in srgb,currentColor 8%,transparent) }`.
4. **Interactive Detail & Feature Matrix (<section.gc-intro__panel> — `An indie studio`)**:
   - Landmark `<section class="gc-intro__panel">` framing `An indie studio` and `Pigeon's Mission` (*"Fly into a world of excitement as Archie embarks on a mission to "*) with `#b00020` surface cards, `#ffff00` accents, and `.sc-host.sc-has-error { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.gc-sr> — `https://www.glowingcheetah.com/`)**:
   - Landmark `<footer class="gc-sr">` anchoring `Glowing Cheetah Studios · Father` footer links (`Projects · Team · Contact`), copy *"A sci-fi epic rooted in Afrofuturism about three interconnec"*, and `#2f2f2f` structural dividers.
