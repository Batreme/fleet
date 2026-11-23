---
title: "UI & UX Architecture: www-danielebuser-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-danielebuser-com

## Overview & Design Identity
- **Target**: `www-danielebuser-com` (**Daniele Buser · Creative Developer**)
- **Production URL**: [https://www.danielebuser.com/](https://www.danielebuser.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0a0a0a` canvas, `#f6f6f6` ink, `#ff4500` accent)
- **Summary**: Explore Daniele Buser's creative development projects: interactive 3D web experiences, WebGL experiments, and high-performance front-end...
- **Total Clean CSS Variables Extracted**: `72` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `neueHaasGrotesk`
- **Body Font Stack**: `neueHaasGrotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 208.8px`, `line-height: 177.48px`, `font-weight: 400`, `letter-spacing: -5.22px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 30.56px`, `line-height: 30.56px`, `font-weight: 400`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--text-body-lg: 1.125rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f6f6f6` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1e1e1e` | `var(--color-card-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#ff4500` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#6b6b6b` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#1a1a1a` | `var(--color-grid-line-dark)` in `:root` |
| **Variable Token (`--color-rose-400`)** | `#ff667f` | `var(--color-rose-400)` in `:root` |
| **Variable Token (`--color-neutral-200`)** | `#e5e5e5` | `var(--color-neutral-200)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-neue-haas), sans-serif` | Typography / Scale Token |
| `--color-rose-400` | `#ff667f` | Brand / Palette Token |
| `--color-neutral-200` | `#e5e5e5` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75 / 1.125)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `www-danielebuser-com`)**:
   - Landmark `<header class="pointer-events-none top-0">` (`1440x69px`) hosting `Daniele Buser · Creative Developer` navigation (`PROJECTS · ABOUT · CONTACTS`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `host { --color-rose-400:lab(64.4125% 63.0291 19.2068);--color-neutral-200:lab(9... }`.
2. **Hero Stage & Focal Lead (<section.pt-16> — `Projects '26`)**:
   - Landmark `<section class="pt-16 flex">` presenting display lead `Projects '26` and copy excerpt *"Creative Developer"* over `#0a0a0a` canvas and `#f6f6f6` ink.
3. **Primary Showcase & Content Grid (<section.pb-64> — `Projects ' 26`)**:
   - Landmark `<section class="pb-64 relative">` rendering section `Projects ' 26` with copy *"If you have a project in mind, feel free to reach out - I'd be gl"*, asset references (`NeueHaasGroteskDisplay_Bold-s.p.0...`, `NeueHaasGroteskDisplay_Light-s.p....`, `NeueHaasGroteskDisplay_Reg-s.p.2r...`, `0g5culx7t__ba.css`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.bg-background> — `SELECTED WORKS`)**:
   - Landmark `<section class="bg-background text-foreground">` framing `SELECTED WORKS` and `Leonardo Berselli's Portfolio` (*"LinkedIn (opens in new tab)"*) with `#1e1e1e` surface cards, `#ff4500` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.pointer-events-none> — `https://www.danielebuser.com/`)**:
   - Landmark `<footer class="pointer-events-none bottom-0">` anchoring `Daniele Buser · Creative Develop` footer links (`PROJECTS · ABOUT · CONTACTS`), copy *"(opens in new tab)"*, and `#1a1a1a` structural dividers.
