---
title: "UI & UX Architecture: www-nereo-io"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-nereo-io

## Overview & Design Identity
- **Target**: `www-nereo-io` (**Nereo — AI Video Generator for Creators & Marketers**)
- **Production URL**: [https://www.nereo.io/](https://www.nereo.io/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#15191f` canvas, `#ffffff` ink, `#ffd23f` accent)
- **Summary**: Generate stunning 4K videos with AI. Create professional videos from text prompts with realistic physics and native audio. Start free today.
- **Total Clean CSS Variables Extracted**: `137` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `__Unbounded_73c992`
- **Body Font Stack**: `__Outfit_a80a2d`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 68px`, `font-weight: 700`, `letter-spacing: -0.9px`); CSS variables `--font-display: var(--font-sans)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 26px`, `line-height: 32px`, `font-weight: 700`, `letter-spacing: 0.52px`); rule `h2` (`font-size: 1.875rem`, `line-height: 2.25rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--removed-body-scroll-bar-size: 0px`; rule `p` (`line-height: 1.625`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: 60px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#15191f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `nav` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#171717` | `var(--sd-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#ffd23f` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#2b8fea` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#262626` | `var(--sd-line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sidebar-background` | `var(--background)` | Canvas / Surface Token |
| `--sidebar-foreground` | `var(--foreground)` | Typography Ink Token |
| `--sidebar-primary` | `var(--primary)` | Brand / Palette Token |
| `--sidebar-primary-foreground` | `var(--primary-foreground)` | Typography Ink Token |
| `--sidebar-accent` | `var(--background)` | Brand / Palette Token |
| `--sidebar-accent-foreground` | `var(--primary)` | Typography Ink Token |
| `--sidebar-border` | `var(--border)` | Elevation / Border Token |
| `--sidebar-ring` | `var(--ring)` | Elevation / Border Token |
| `--font-heading` | `var(--font-sans)` | Typography Ink Token |
| `--background` | `262 76% 95%` | Canvas / Surface Token |
| `--foreground` | `262 5% 10%` | Typography Ink Token |
| `--card` | `262 50% 90%` | Dimension / Scale Token |
| `--card-foreground` | `262 5% 10%` | Typography Ink Token |
| `--popover` | `262 76% 95%` | Dimension / Scale Token |
| `--popover-foreground` | `262 95% 10%` | Typography Ink Token |
| `--primary` | `210 75% 50%` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.gap-6> — `www-nereo-io`)**:
   - Landmark `<nav class="gap-6 hidden">` (`1248x40px`) hosting `Nereo — AI Video Generator for Creat` navigation (`Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `AI Video Generator for Creators & `)**:
   - Landmark `<section class="relative overflow-hidden">` presenting display lead `AI Video Generator for Creators & Marketers` and copy excerpt *"Turn a prompt, a photo or a reference into a finished video. Veo "* over `#15191f` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.gap-4> — `Nereo Agent Describe the video. Th`)**:
   - Landmark `<section class="gap-4 border-nl-rule">` rendering section `Nereo Agent Describe the video. The agent writes...` with copy *"Start creating free"*, asset references (`e4af272ccee01ff0-s.p.woff2`, `logo.png`, `322e14d06135256b.css`, `a7f88efd924ba4d6.css`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.border-nl-rule> — `Seedance 2.5 One continuous 30-sec`)**:
   - Landmark `<section class="gap-4 border-nl-rule">` framing `Seedance 2.5 One continuous 30-second take, nativ...` and `Seedance 2.0 Audio and video generated together,...` (*"Describe the video. The agent writes the shots, generates them an"*) with `#171717` surface cards, `#ffd23f` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.antialiased> — `https://www.nereo.io/`)**:
   - Landmark `<footer class="antialiased">` anchoring `Nereo — AI Video Generator for C` footer links (`Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`), copy *"LUMA NOOK — A Daily Tea Ritual"*, and `#262626` structural dividers.
