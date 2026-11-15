# UI & UX Architecture: findra-art

## Overview & Design Identity
- **Target**: `findra-art` (**Findra: the AI character feed**)
- **Production URL**: [https://findra.art/](https://findra.art/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f7` accent)
- **Summary**: Who is rising among AI characters on TikTok, Instagram, X and YouTube: what they look like, their legends and where to follow them.
- **Total Clean CSS Variables Extracted**: `59` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-anton), Impact, "Arial Narrow", sans-serif`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#09090b` | `var(--background)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f5f7` | `var(--foreground)` in `:root` |
| **Secondary / Muted Copy** | `#a1a1aa` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#141417` | `var(--surface)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--font-anton` | `"Anton", "Anton Fallback"` | Typography / Scale Token |
| `--font-permanent-marker` | `"Permanent Marker", "Permanent Marker Fallback"` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `findra-art`)**:
   - Landmark `<header class="sticky top-0">` hosting `Findra: the AI character feed` navigation (`Feed · Magazine · Wire · Leaderboard · 40 Under 40`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="1.6.1"`, `data-test="skip-to-content"`), and stylesheet rule `.u8MhCG_className { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.border-foreground> — `Breaking`)**:
   - Landmark `<section class="border-foreground flex">` presenting display lead `Breaking` and copy excerpt *"Don Nuger’s Instagram account is unavailable"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.group> — `Who’s rising`)**:
   - Landmark `<article class="group relative">` rendering section `Who’s rising` with copy *"The account could not be read on November 13 or this morning. It "*, asset references (`60143a72b8d6b7a7338339c64f9bcd8bb...`, `3f38907974d4f61e778b2b56d301ade05...`, `3qago8bg0x8_-.css`, `30qn3skk62nz8.js`), and grid rule `.u8MhCG_variable { --font-geist:"Geist", "Geist Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.border-border> — `The week on Findra`)**:
   - Landmark `<section class="border-border flex">` framing `The week on Findra` and `Latest story` (*"AI characters and the audiences they are building on TikTok, Inst"*) with `#09090b` surface cards, `#f5f5f7` accents, and `.mJqafq_className { font-family:Anton,Anton Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.text-muted> — `https://findra.art/`)**:
   - Landmark `<footer class="text-muted mx-auto">` anchoring `Findra: the AI character feed` footer links (`Feed · Magazine · Wire · Leaderboard · 40 Under 40`), copy *"adventurous ai cat character"*, and `#141417` structural dividers.
