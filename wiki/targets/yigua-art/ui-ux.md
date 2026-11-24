---
title: "UI & UX Architecture: yigua-art"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: yigua-art

## Overview & Design Identity
- **Target**: `yigua-art` (**一卦**)
- **Production URL**: [https://yigua.art/?lang=en](https://yigua.art/?lang=en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3f0e8` canvas, `#171815` ink, `#65645e` accent)
- **Summary**: 讓卦回到卦。一次起卦，只呈現卦象與原典；解讀留給你。
- **Total Clean CSS Variables Extracted**: `60` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Georgia`
- **Body Font Stack**: `PingFang TC`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56.8px`, `line-height: 63.616px`, `font-weight: 500`, `letter-spacing: 0.6816px`); rule `h1` (`line-height: 1.12`, `letter-spacing: .025em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.65rem,3vw,2.2rem)`, `letter-spacing: .12em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`letter-spacing: .02em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .68rem`, `letter-spacing: .08em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f0e8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171815` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e8e3d7` | `var(--paper-deep)` in `:root` |
| **Interactive Accent / Highlight** | `#65645e` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#65645e` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d6d0c4` | `var(--line)` in `:root` |
| **Variable Token (`--paper-light`)** | `#f8f6ef` | `var(--paper-light)` in `:root` |
| **Variable Token (`--cinnabar`)** | `#963e32` | `var(--cinnabar)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#f3f0e8` | Canvas / Surface Token |
| `--paper-deep` | `#e8e3d7` | Canvas / Surface Token |
| `--paper-light` | `#f8f6ef` | Canvas / Surface Token |
| `--ink` | `#171815` | Typography Ink Token |
| `--ink-soft` | `#65645e` | Typography Ink Token |
| `--line` | `#d6d0c4` | Color / Atmospheric Token |
| `--cinnabar` | `#963e32` | Color / Atmospheric Token |
| `--background` | `var(--paper)` | Canvas / Surface Token |
| `--foreground` | `var(--ink)` | Typography Ink Token |
| `--card` | `var(--paper-light)` | Design System Custom Token |
| `--card-foreground` | `var(--ink)` | Typography Ink Token |
| `--popover` | `var(--paper-light)` | Design System Custom Token |
| `--popover-foreground` | `var(--ink)` | Typography Ink Token |
| `--primary` | `var(--ink)` | Brand / Palette Token |
| `--primary-foreground` | `var(--paper)` | Typography Ink Token |
| `--secondary` | `var(--paper-deep)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `yigua-art`)**:
   - Landmark `<header class="site-header">` (`1296x80px`) hosting `一卦` navigation (`64 Hexagrams · About Yi Gua · Privacy · Developer · Researchers`), DOM attributes (`data-locale="en"`, `data-startup-lifecycle-bound="true"`, `data-startup-booted="true"`, `data-text-size="medium"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.casting-experience> — `Let the hexagram remain itself.`)**:
   - Landmark `<section class="casting-experience">` presenting display lead `Let the hexagram remain itself.` and copy excerpt *"One casting. Only the figure and original text; the interpretatio"* over `#f3f0e8` canvas and `#171815` ink.
3. **Primary Showcase & Content Grid (<section.casting-experience:nth(2)> — `One casting. Only the figure and o`)**:
   - Landmark `<section class="casting-experience">` rendering section `One casting. Only the figure and original text; ` with copy *"One casting. Only the figure and original text;"*, asset references (`index.B1O6CZI_.css`, `index-BdTq9GkK.js`, `rolldown-runtime-C60lm6uB.js`, `framework-D_rUT4EX.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.casting-experience:nth(3)> — `One casting. Only the figure and o`)**:
   - Landmark `<section class="casting-experience">` framing `One casting. Only the figure and original text;` and `the interpretation is yours.` (*"the interpretation is yours."*) with `#e8e3d7` surface cards, `#65645e` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yigua.art/?lang=en`)**:
   - Landmark `<footer class="site-footer">` anchoring `一卦` footer links (`64 Hexagrams · About Yi Gua · Privacy · Developer · Researchers`), copy *"Version 1.4.31 · Updated 2026-11-04 CC BY 4.0 · Original pre"*, and `#d6d0c4` structural dividers.
