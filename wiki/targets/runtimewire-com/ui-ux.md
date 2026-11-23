---
title: "UI & UX Architecture: runtimewire-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: runtimewire-com

## Overview & Design Identity
- **Target**: `runtimewire-com` (**RuntimeWire: Breaking tech news. Before everyone else.**)
- **Production URL**: [https://runtimewire.com](https://runtimewire.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f9fafb` canvas, `#171a26` ink, `#cb3610` accent)
- **Summary**: Breaking tech news. Before everyone else. Independent investigations, original reporting and a continuous news feed covering startups and...
- **Total Clean CSS Variables Extracted**: `209` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Newsreader`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44.64px`, `line-height: 46.4256px`, `font-weight: 600`, `letter-spacing: -0.53568px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.028em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 43.2px`, `line-height: 45.792px`, `font-weight: 600`, `letter-spacing: -0.5184px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`letter-spacing: .09em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 15.6px`, `font-weight: 600`, `letter-spacing: 0.12px`); CSS variables `--app-font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace`, `--font-mono: var(--app-font-mono)`, `--text-xs: .75rem`; rule `small` (`font-size: 12px`, `line-height: 1.45`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9fafb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171a26` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffa500` | `.bg-orange-500 { background-color: orange }` (`#ffa500`) |
| **Interactive Accent / Highlight** | `#cb3610` | `.a11y-signup .bg-primary { background-color: #cb3610 }` |
| **Secondary / Muted Copy** | `#8a93a6` | `.rw-nojs-footer { color: #8a93a6 }` |
| **Structural Hairline Border** | `#7fe0a8` | `50 { border-color: #7fe0a8 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rw-static-asset-revision` | `20260900` | Design System Custom Token |
| `--background` | `230 18% 6%` | Canvas / Surface Token |
| `--foreground` | `210 20% 96%` | Typography Ink Token |
| `--border` | `230 14% 14%` | Elevation / Border Token |
| `--input` | `230 14% 14%` | Dimension / Scale Token |
| `--ring` | `13 100% 56%` | Elevation / Border Token |
| `--card` | `230 18% 8%` | Dimension / Scale Token |
| `--card-foreground` | `210 20% 96%` | Typography Ink Token |
| `--card-border` | `230 14% 14%` | Elevation / Border Token |
| `--popover` | `230 18% 8%` | Dimension / Scale Token |
| `--popover-foreground` | `210 20% 96%` | Typography Ink Token |
| `--popover-border` | `230 14% 14%` | Elevation / Border Token |
| `--primary` | `13 100% 56%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |
| `--primary-readable` | `13 100% 56%` | Brand / Palette Token |
| `--secondary` | `230 14% 12%` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.public-site-header> — `runtimewire-com`)**:
   - Landmark `<header class="public-site-header backdrop-blur-md">` (`1440x114px`) hosting `RuntimeWire: Breaking tech news. Bef` navigation (`Investigations · Stories · AI · Startups · Venture`), DOM attributes (`data-testid="skip-to-content"`, `data-anim="static"`, `data-testid="header-search-button"`, `data-testid="theme-switch"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.border-border> — `Amazon Prime Air drone crashes on `)**:
   - Landmark `<section class="border-border relative">` presenting display lead `Amazon Prime Air drone crashes on Detroit home af...` and copy excerpt *"Residents say the MK30 rose into a fiber-optic line on November 2"* over `#f9fafb` canvas and `#171a26` ink.
3. **Primary Showcase & Content Grid (<article.gap-4> — `Microsoft backs OpenAI's proposal `)**:
   - Landmark `<article class="gap-4 flex">` rendering section `Microsoft backs OpenAI's proposal to pause fronti...` with copy *"The Daily Briefing"*, asset references (`investigations.xml`, `stories.xml`, `featured`, `favicon.ico`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.border-border> — `Editor’s picks`)**:
   - Landmark `<article class="gap-4 border-border">` framing `Editor’s picks` and `Win an NVIDIA DGX Spark` (*"Published 1 hour ago"*) with `#ffa500` surface cards, `#cb3610` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-border> — `https://runtimewire.com`)**:
   - Landmark `<footer class="border-border mt-20">` anchoring `RuntimeWire: Breaking tech news.` footer links (`Investigations · Stories · AI · Startups · Venture`), copy *"Microsoft AI chief Mustafa Suleyman endorsed OpenAI's plan f"*, and `#7fe0a8` structural dividers.
