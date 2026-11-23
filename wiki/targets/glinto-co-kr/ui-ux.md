---
title: "UI & UX Architecture: glinto-co-kr"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: glinto-co-kr

## Overview & Design Identity
- **Target**: `glinto-co-kr` (**Glinto — Creative studio**)
- **Production URL**: [https://glinto.co.kr](https://glinto.co.kr)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff5c34`)
- **Summary**: Glinto is a creative studio where one team takes brand strategy and identity, film and photography, design, and web and app development f...
- **Total Clean CSS Variables Extracted**: `292` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Pretendard Variable`
- **Body Font Stack**: `Pretendard Variable`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--fs-xl: 1.25rem`, `--fs-h1: 1.625rem`, `--fs-display-sans: 2.125rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 60px`, `font-weight: 600`, `letter-spacing: -0.6px`); CSS variables `--fs-lg: 1.125rem`, `--fs-h2: 1.375rem`, `--tracking-h2: -.01em`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--fs-base: 1rem`, `--fs-body-s: .8125rem`, `--fs-body-m: .875rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--label-ink-start: var(--lime-cream-start)`, `--label-ink-end: var(--lime-cream-end)`, `--fs-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f131f` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fdeceb` | `var(--danger-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ff5c34` | `var(--accent-500)` in `:root` |
| **Secondary / Muted Copy** | `#626880` | `var(--mock-muted)` in `:root` |
| **Structural Hairline Border** | `#626880` | hairline divider derived from `var(--mock-muted)` in `:root` |
| **Variable Token (`--accent-50`)** | `#fff3ee` | `var(--accent-50)` in `:root` |
| **Variable Token (`--accent-100`)** | `#ffe4d9` | `var(--accent-100)` in `:root` |
| **Variable Token (`--accent-200`)** | `#ffc7b0` | `var(--accent-200)` in `:root` |
| **Variable Token (`--accent-300`)** | `#ffa47d` | `var(--accent-300)` in `:root` |
| **Variable Token (`--accent-400`)** | `#ff7f54` | `var(--accent-400)` in `:root` |
| **Variable Token (`--accent-600`)** | `#e8451f` | `var(--accent-600)` in `:root` |
| **Variable Token (`--accent-700`)** | `#c13215` | `var(--accent-700)` in `:root` |
| **Variable Token (`--accent-800`)** | `#922712` | `var(--accent-800)` in `:root` |
| **Variable Token (`--accent-900`)** | `#611a0c` | `var(--accent-900)` in `:root` |
| **Variable Token (`--neutral-50`)** | `#fbf9f7` | `var(--neutral-50)` in `:root` |
| **Variable Token (`--neutral-100`)** | `#f5f1ed` | `var(--neutral-100)` in `:root` |
| **Variable Token (`--neutral-200`)** | `#e8e1da` | `var(--neutral-200)` in `:root` |
| **Variable Token (`--neutral-300`)** | `#d6ccc2` | `var(--neutral-300)` in `:root` |
| **Variable Token (`--neutral-400`)** | `#b3a79c` | `var(--neutral-400)` in `:root` |
| **Variable Token (`--neutral-500`)** | `#8f8177` | `var(--neutral-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent-50` | `#fff3ee` | Brand / Palette Token |
| `--accent-100` | `#ffe4d9` | Brand / Palette Token |
| `--accent-200` | `#ffc7b0` | Brand / Palette Token |
| `--accent-300` | `#ffa47d` | Brand / Palette Token |
| `--accent-400` | `#ff7f54` | Brand / Palette Token |
| `--accent-500` | `#ff5c34` | Brand / Palette Token |
| `--accent-600` | `#e8451f` | Brand / Palette Token |
| `--accent-700` | `#c13215` | Brand / Palette Token |
| `--accent-800` | `#922712` | Brand / Palette Token |
| `--accent-900` | `#611a0c` | Brand / Palette Token |
| `--neutral-50` | `#fbf9f7` | Color / Atmospheric Token |
| `--neutral-100` | `#f5f1ed` | Color / Atmospheric Token |
| `--neutral-200` | `#e8e1da` | Color / Atmospheric Token |
| `--neutral-300` | `#d6ccc2` | Color / Atmospheric Token |
| `--neutral-400` | `#b3a79c` | Color / Atmospheric Token |
| `--neutral-500` | `#8f8177` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header-wrap> — `glinto-co-kr`)**:
   - Landmark `<header class="site-header-wrap top-0">` (`1440x64px`) hosting `Glinto — Creative studio` navigation (`About · Services · Glinto.dev · Works · Contact`), DOM attributes (`data-theme="light"`, `data-reveal-ready`, `data-progress-ready`, `data-precedence="next"`), and stylesheet rule `sans_efc253b3-module__w1i8Da__cla... { font-family:DM Sans,DM Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Everything your brand needs, from `)**:
   - Landmark `<section class="antialiased">` presenting display lead `Everything your brand needs, from one team` and copy excerpt *"Creative studio for identity, visuals, and code."* over `#ffffff` canvas and `#0f131f` ink.
3. **Primary Showcase & Content Grid (<section.pt-24> — `Solutions shaped by how your brand`)**:
   - Landmark `<section class="pt-24">` rendering section `Solutions shaped by how your brand runs` with copy *"Engineering Build it"*, asset references (`2f7d2945a32bc936-s.p.0q9pvfn3wr_3...`, `5c285b27cdda1fe8-s.p.0lsanbtneewq...`, `0k1f2nt08p6_n.css`, `3b84er6uv62xn.css`), and grid rule `sans_efc253b3-module__w1i8Da__var... { --font-dm-sans:"DM Sans", "DM Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.pt-24:nth(2)> — `Launch & care`)**:
   - Landmark `<section class="pt-24">` framing `Launch & care` and `Experience with brands across industries` (*"From brand strategy to design, media and development, specialists"*) with `#fdeceb` surface cards, `#ff5c34` accents, and `f_kr_611a1780-module__N7vmma__cla... { font-family:Noto Serif KR,Noto Serif KR Fallback;font-style:normal;font-... }`.
5. **Colophon & Global Directory Footer (<footer.mt-24> — `https://glinto.co.kr`)**:
   - Landmark `<footer class="mt-24">` anchoring `Glinto — Creative studio` footer links (`About · Services · Glinto.dev · Works · Contact`), copy *"Start small with the one service you need right now."*, and `#626880` structural dividers.
