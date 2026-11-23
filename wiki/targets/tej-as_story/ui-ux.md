---
title: "UI & UX Architecture: tej-as_story"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: tej-as_story

## Overview & Design Identity
- **Target**: `tej-as_story` (**The testimony and autobiography of Tejas Kumar**)
- **Production URL**: [https://tej.as/story](https://tej.as/story)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f1ea` / `#1ed760`)
- **Summary**: Tejas Kumar died at 4 and was revived, got about 19 days of school a year, and is now an AI engineer at IBM. His full testimony, in 39 ch...
- **Total Clean CSS Variables Extracted**: `148` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Switzer`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 180px`, `line-height: 144px`, `font-weight: 900`, `letter-spacing: -7.2px`); CSS variables `--font-display: "Jost", "Futura", "Century Gothic", "Trebuchet MS", system-ui, sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 109.44px`, `line-height: 94.1184px`, `font-weight: 900`, `letter-spacing: -3.50208px`)
- **Body Copy**: live computed `body` (`font-size: 18.72px`, `line-height: 30.3264px`, `font-weight: 400`); CSS variables `--font-body: "Switzer", "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif`, `--t-body: clamp(1.125rem, 1.3vw, 1.3125rem)`, `--lh-body: 1.62`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18.72px`, `line-height: 30.3264px`, `font-weight: 400`); CSS variables `--fg-label: color-mix(in srgb, var(--fg-2) 72%, var(--fg))`, `--font-mono: "Geist Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--t-small: clamp(.9375rem, 1vw, 1rem)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f1ea` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a0708` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e8e4da` | `var(--paper-2)` in `:root` |
| **Interactive Accent / Highlight** | `#1ed760` | `var(--brand-spotify)` in `:root` |
| **Secondary / Muted Copy** | `#4a4441` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d8d3c7` | `var(--paper-rule)` in `:root` |
| **Variable Token (`--ink`)** | `#161012` | `var(--ink)` in `:root` |
| **Variable Token (`--rule-dark`)** | `#2a2426` | `var(--rule-dark)` in `:root` |
| **Variable Token (`--bone`)** | `#f2efe9` | `var(--bone)` in `:root` |
| **Variable Token (`--ash`)** | `#a39b98` | `var(--ash)` in `:root` |
| **Variable Token (`--ash-dim`)** | `#8c8481` | `var(--ash-dim)` in `:root` |
| **Variable Token (`--paper-dim`)** | `#6b6460` | `var(--paper-dim)` in `:root` |
| **Variable Token (`--paper-rule-lit`)** | `#b3aa99` | `var(--paper-rule-lit)` in `:root` |
| **Variable Token (`--red`)** | `#ef3340` | `var(--red)` in `:root` |
| **Variable Token (`--red-paper`)** | `#96101c` | `var(--red-paper)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--void` | `#0a0708` | Color / Atmospheric Token |
| `--ink` | `#161012` | Typography Ink Token |
| `--rule-dark` | `#2a2426` | Canvas / Surface Token |
| `--rule-dark-lit` | `#4a4441` | Canvas / Surface Token |
| `--bone` | `#f2efe9` | Color / Atmospheric Token |
| `--ash` | `#a39b98` | Color / Atmospheric Token |
| `--ash-dim` | `#8c8481` | Color / Atmospheric Token |
| `--paper` | `#f4f1ea` | Canvas / Surface Token |
| `--paper-2` | `#e8e4da` | Canvas / Surface Token |
| `--paper-ink` | `#0a0708` | Canvas / Surface Token |
| `--paper-mid` | `#4a4441` | Canvas / Surface Token |
| `--paper-dim` | `#6b6460` | Canvas / Surface Token |
| `--paper-rule` | `#d8d3c7` | Canvas / Surface Token |
| `--paper-rule-lit` | `#b3aa99` | Canvas / Surface Token |
| `--red` | `#ef3340` | Color / Atmospheric Token |
| `--red-paper` | `#96101c` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `tej-as_story`)**:
   - Landmark `<header class="topbar">` (`1440x62px`) hosting `The testimony and autobiography of T` navigation (`Speaking · Story · Podcast · Blog · Book Fluent React`), DOM attributes (`data-theme="light"`, `data-track="Nav Click"`, `data-track-label="Wordmark"`, `data-track-href="/"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.px-gutter> — `The thread.`)**:
   - Landmark `<section class="px-gutter pb-l">` presenting display lead `The thread.` and copy excerpt *"I was supposed to be an abortion, then I was supposed to be dead,"* over `#f4f1ea` canvas and `#0a0708` ink.
3. **Primary Showcase & Content Grid (<section.summary> — `The thread .`)**:
   - Landmark `<section class="summary">` rendering section `The thread .` with copy *"19 February 1993 Born"*, asset references (`favicon.svg`, `story`, `array.js`, `jost-var.woff2`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.border-hairline> — `The short version.`)**:
   - Landmark `<section class="border-hairline px-gutter">` framing `The short version.` and `A job out of nowhere` (*"May 1993 The mirror"*) with `#e8e4da` surface cards, `#1ed760` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-hairline> — `https://tej.as/story`)**:
   - Landmark `<footer class="border-hairline px-gutter">` anchoring `The testimony and autobiography ` footer links (`Speaking · Story · Podcast · Blog · Book Fluent React`), copy *"1997 A job out of nowhere"*, and `#d8d3c7` structural dividers.
