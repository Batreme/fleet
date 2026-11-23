---
title: "UI & UX Architecture: findra-art"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: findra-art

## Overview & Design Identity
- **Target**: `findra-art` (**Findra: the AI character feed**)
- **Production URL**: [https://findra.art/](https://findra.art/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#09090b` canvas, `#ffffff` ink, `#e14bff` accent)
- **Summary**: Who is rising among AI characters on TikTok, Instagram, X and YouTube: what they look like, their legends and where to follow them.
- **Total Clean CSS Variables Extracted**: `59` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 176px`, `line-height: 158.4px`, `font-weight: 400`, `letter-spacing: 0.88px`); CSS variables `--font-display: var(--font-anton), Impact, "Arial Narrow", sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 112px`, `line-height: 100.8px`, `font-weight: 400`, `letter-spacing: 0.56px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#09090b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141417` | `var(--surface)` in `:root` |
| **Interactive Accent / Highlight** | `#e14bff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#a1a1aa` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#27272c` | `var(--border)` in `:root` |
| **Variable Token (`--foreground`)** | `#f5f5f7` | `var(--foreground)` in `:root` |
| **Variable Token (`--surface-hover`)** | `#1d1d21` | `var(--surface-hover)` in `:root` |
| **Variable Token (`--accent-foreground`)** | `#0a0a0b` | `var(--accent-foreground)` in `:root` |
| **Variable Token (`--paper`)** | `#f1ece1` | `var(--paper)` in `:root` |
| **Variable Token (`--ink`)** | `#1b1a17` | `var(--ink)` in `:root` |
| **Variable Token (`--ink-muted`)** | `#57524a` | `var(--ink-muted)` in `:root` |
| **Variable Token (`--ink-accent`)** | `#8a1ca6` | `var(--ink-accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#09090b` | Canvas / Surface Token |
| `--foreground` | `#f5f5f7` | Typography Ink Token |
| `--muted` | `#a1a1aa` | Color / Atmospheric Token |
| `--surface` | `#141417` | Canvas / Surface Token |
| `--surface-hover` | `#1d1d21` | Canvas / Surface Token |
| `--border` | `#27272c` | Elevation / Border Token |
| `--accent` | `#e14bff` | Brand / Palette Token |
| `--accent-foreground` | `#0a0a0b` | Typography Ink Token |
| `--paper` | `#f1ece1` | Canvas / Surface Token |
| `--ink` | `#1b1a17` | Typography Ink Token |
| `--ink-muted` | `#57524a` | Typography Ink Token |
| `--ink-accent` | `#8a1ca6` | Typography Ink Token |
| `--lightningcss-dark` | `initial` | Canvas / Surface Token |
| `--font-geist` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--font-anton` | `"Anton", "Anton Fallback"` | Typography / Scale Token |
| `--font-permanent-marker` | `"Permanent Marker", "Permanent Marker Fallback"` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `findra-art`)**:
   - Landmark `<header class="top-0 backdrop-blur-xl">` (`1440x64px`) hosting `Findra: the AI character feed` navigation (`Feed · Magazine · Wire · Leaderboard · 40 Under 40`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="1.6.1"`, `data-test="skip-to-content"`), and stylesheet rule `.u8MhCG_className { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<article.group> — `WHO’S RISING`)**:
   - Landmark `<article class="group justify-end">` presenting display lead `WHO’S RISING` and copy excerpt *"AI characters and the audiences they are building on TikTok, Inst"* over `#09090b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.border-border> — `Who’s rising`)**:
   - Landmark `<section class="border-border gap-3">` rendering section `Who’s rising` with copy *"adventurous ai cat character"*, asset references (`d25bf568acb89df91e84732c0a9d9da02...`, `3f38907974d4f61e778b2b56d301ade05...`, `d4d0f0a272f823cf8d0558137c9b10adc...`, `3qago8bg0x8_-.css`), and grid rule `.u8MhCG_variable { --font-geist:"Geist", "Geist Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.max-w-3xl> — `Claudia, the pop star anyone can m`)**:
   - Landmark `<section class="max-w-3xl gap-2">` framing `Claudia, the pop star anyone can make` and `Latest story` (*"ai animal influencer"*) with `#141417` surface cards, `#e14bff` accents, and `.mJqafq_className { font-family:Anton,Anton Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.text-muted> — `https://findra.art/`)**:
   - Landmark `<footer class="text-muted gap-4">` anchoring `Findra: the AI character feed` footer links (`Feed · Magazine · Wire · Leaderboard · 40 Under 40`), copy *"anime fighter brought to life"*, and `#27272c` structural dividers.
