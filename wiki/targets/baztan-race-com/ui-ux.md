# UI & UX Architecture: baztan-race-com

## Overview & Design Identity
- **Target**: `baztan-race-com` (**Baztan Race**)
- **Production URL**: [https://baztan-race.com](https://baztan-race.com)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#FFFFFF` ink, `#DDF240` accent)
- **Summary**: Venez affronter la route mythique de la vallée du Baztan entre Bayonne et Pampelune. Entre cols somptueux et forêts mystérieuses, vivez l...
- **Total Clean CSS Variables Extracted**: `126` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Outfit Bold`
- **Body Font Stack**: `Outfit Light`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 3.5rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 4rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 2.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 3rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 14px!important`, `font-weight: 300!important`)
- **Metadata & Labels**: CSS variables `--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",`, `--text-xs: 0.875rem`, `--text-xs--line-height: calc(1 / 0.75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#FFFFFF` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0D0D0D` | `var(--color-primary)` in `:root` |
| **Interactive Accent / Highlight** | `#DDF240` | `var(--color-green-flash)` in `:root` |
| **Secondary / Muted Copy** | `#C7A882` | `var(--color-brown)` in `:root` |
| **Structural Hairline Border** | `#6B654B` | `var(--color-green-deep)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--menu-ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Motion / Easing Token |
| `--menu-ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Motion / Easing Token |
| `--menu-ease-in` | `cubic-bezier(0.5, 0, 0.75, 0)` | Motion / Easing Token |
| `--menu-btn-r` | `calc(var(--menu-btn-h, 44px) / 2)` | Dimension / Scale Token |
| `--gradient-progress` | `0%` | Dimension / Scale Token |
| `--hero-ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Motion / Easing Token |
| `--hero-ease-in-out` | `cubic-bezier(0.87, 0, 0.13, 1)` | Motion / Easing Token |
| `--hero-ease-back` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Motion / Easing Token |
| `--m2ccb-gap` | `1rem` | Layout / Spatial Grid Token |
| `--font-sans` | `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji",` | Typography / Scale Token |
| `--font-mono` | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",` | Typography / Scale Token |
| `--color-red-500` | `oklch(63.7% 0.237 25.331)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% 0.006 264.531)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% 0.01 258.338)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% 0.022 261.325)` | Brand / Palette Token |
| `--color-gray-500` | `oklch(55.1% 0.027 264.364)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.main-header> — `baztan-race-com`)**:
   - Landmark `<header class="main-header fixed">` hosting `Baztan Race` navigation (`L’épreuve · Les parcours · Galerie · Infos pratiques · Français`), DOM attributes (`data-rocket-prefetch`, `data-rocket-preload`, `data-nowprocket`, `data-cfasync="false"`), and stylesheet rule `html { overflow-x:hidden;max-width:100vw }`.
2. **Hero Stage & Focal Lead (<section.hero-full> — `suivez-nous`)**:
   - Landmark `<section class="hero-full relative">` presenting display lead `suivez-nous` and copy excerpt *"Cartes et Profils GPX"* over `#000000` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.text-intro> — `Sur les traces du B a s a j a u n`)**:
   - Landmark `<section class="text-intro relative">` rendering section `Sur les traces du B a s a j a u n` with copy *"Français English Español Euskara"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `connect.facebook.net`, `matomo.mak2com.fr`), and grid rule `body { max-width:100vw;position:relative }`.
4. **Interactive Detail & Feature Matrix (<section.title-section> — `Choisis ta course`)**:
   - Landmark `<section class="title-section relative">` framing `Choisis ta course` and `BAZTAN REAL #1` (*"MERCI POUR CETTE 1ÈRE ÉDITION !"*) with `#0D0D0D` surface cards, `#DDF240` accents, and `header { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.bg-dark-1> — `https://baztan-race.com`)**:
   - Landmark `<footer class="bg-dark-1 pb-16">` anchoring `Baztan Race` footer links (`L’épreuve · Les parcours · Galerie · Infos pratiques · Français`), copy *"Revivez la 1ère édition Voir l'aftermovie"*, and `#6B654B` structural dividers.
