---
title: "UI & UX Architecture: explore-auravinyl-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: explore-auravinyl-com

## Overview & Design Identity
- **Target**: `explore-auravinyl-com` (**Aura Vinyl Color Explorer**)
- **Production URL**: [https://explore.auravinyl.com](https://explore.auravinyl.com)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#161616` / `#e3fc02`)
- **Summary**: Explore over 500 colors across matte, satin, and gloss finishes from Aura Premium Vinyl. Find vinyl wrap ideas and inspiration.
- **Total Clean CSS Variables Extracted**: `57` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 30px`, `line-height: 27px`, `font-weight: 900`, `letter-spacing: -0.6px`); rule `.title` (`font-size: 18px`, `line-height: 1.1`, `letter-spacing: -.02em`, `font-weight: 800`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 28px`, `line-height: 25.2px`, `font-weight: 900`, `letter-spacing: -0.56px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `.body` (`font-size: 13px`, `line-height: 1.5`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13px`, `line-height: normal`, `font-weight: 700`); CSS variables `--font-mono: "Geist Mono", ui-monospace, monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#161616` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a0a` | `var(--bg)` in `:root` |
| **Interactive Accent / Highlight** | `#e3fc02` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#808080` | `var(--text-3)` in `:root` |
| **Structural Hairline Border** | `#262626` | `var(--line)` in `:root` |
| **Variable Token (`--bg-sunken`)** | `#050505` | `var(--bg-sunken)` in `:root` |
| **Variable Token (`--raised`)** | `#1e1e1e` | `var(--raised)` in `:root` |
| **Variable Token (`--line-steel`)** | `#404040` | `var(--line-steel)` in `:root` |
| **Variable Token (`--line-strong`)** | `#6b6b6b` | `var(--line-strong)` in `:root` |
| **Variable Token (`--text`)** | `#f5f5f5` | `var(--text)` in `:root` |
| **Variable Token (`--text-2`)** | `#a3a3a3` | `var(--text-2)` in `:root` |
| **Variable Token (`--signal-hover`)** | `#efff5c` | `var(--signal-hover)` in `:root` |
| **Variable Token (`--danger`)** | `#ff5a4f` | `var(--danger)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0a0a0a` | Canvas / Surface Token |
| `--bg-raised` | `#161616` | Canvas / Surface Token |
| `--bg-sunken` | `#050505` | Canvas / Surface Token |
| `--raised` | `#1e1e1e` | Color / Atmospheric Token |
| `--line` | `#262626` | Color / Atmospheric Token |
| `--line-steel` | `#404040` | Color / Atmospheric Token |
| `--line-strong` | `#6b6b6b` | Color / Atmospheric Token |
| `--text` | `#f5f5f5` | Typography Ink Token |
| `--text-2` | `#a3a3a3` | Typography Ink Token |
| `--text-3` | `#808080` | Typography Ink Token |
| `--signal` | `#e3fc02` | Color / Atmospheric Token |
| `--signal-hover` | `#efff5c` | Color / Atmospheric Token |
| `--on-signal` | `#0a0a0a` | Color / Atmospheric Token |
| `--danger` | `#ff5a4f` | Color / Atmospheric Token |
| `--float-bg` | `rgb(22 22 22 / .9)` | Canvas / Surface Token |
| `--float-border` | `1px solid rgb(255 255 255 / .08)` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.head> — `explore-auravinyl-com`)**:
   - Landmark `<header class="head">` (`1440px`) hosting `Aura Vinyl Color Explorer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-target="explore-auravinyl-com"`), and stylesheet rule `.FormDialog.on { visibility:visible;opacity:1;pointer-events:auto;transition:opacity var(... }`.
2. **Hero Stage & Focal Lead (<section.mbar> — `Arctic Fire`)**:
   - Landmark `<section class="mbar">` presenting display lead `Arctic Fire` and copy excerpt *"No colors match. Clear the hue or collection, or try another word"* over `#161616` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.card> — `No colors match. Clear the hue or `)**:
   - Landmark `<section class="card">` rendering section `No colors match. Clear the hue or collection, or` with copy *"Please enable javascript"*, asset references (`favicon.svg`, `180.png`, `152.png`, `167.png`), and grid rule `.FormDialog { padding:10px }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Please enable javascript`)**:
   - Landmark `<section class="sec">` framing `Please enable javascript` and `Show more / 741 left` (*"Show more / 741 left"*) with `#0a0a0a` surface cards, `#e3fc02` accents, and `.FormDialog .backdrop { position:absolute;inset:0;background:rgba(5,5,5,.8) }`.
5. **Colophon & Global Directory Footer (<footer.shell> — `https://explore.auravinyl.com`)**:
   - Landmark `<footer class="shell">` anchoring `Aura Vinyl Color Explorer` footer links (`Overview · Index · Archive · About · Contact`), copy *"Ultra Gloss / Nebula"*, and `#262626` structural dividers.
