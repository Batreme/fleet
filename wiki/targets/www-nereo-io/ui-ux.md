# UI & UX Architecture: www-nereo-io

## Overview & Design Identity
- **Target**: `www-nereo-io` (**Nereo — AI Video Generator for Creators & Marketers**)
- **Production URL**: [https://www.nereo.io/](https://www.nereo.io/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#404040` canvas, `#fff` ink, `#b1b1b7` accent)
- **Summary**: Generate stunning 4K videos with AI. Create professional videos from text prompts with realistic physics and native audio. Start free today.
- **Total Clean CSS Variables Extracted**: `127` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `__Outfit_a80a2d`
- **Body Font Stack**: `__Outfit_Fallback_a80a2d`
- **Monospace / Technical Font Stack**: `__IBM_Plex_Sans_Arabic_559684`
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-sans)`
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.875rem`, `line-height: 2.25rem`)
- **Body Copy**: rule `p` (`line-height: 1.625`)
- **Metadata & Labels**: CSS variables `--xy-edge-label-background-color-default: #fff`, `--xy-edge-label-color-default: inherit`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#404040` | `var(--sd-line2)` in `:root` |
| **Primary Typography Ink** | `#262626` | `var(--sd-line)` in `:root` |
| **Elevated Surface / Card Substrate** | `#171717` | `var(--sd-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#b1b1b7` | `var(--xy-edge-stroke-default)` in `:root` |
| **Secondary / Muted Copy** | `#555` | `var(--xy-edge-stroke-selected-default)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--xy-minimap-background-color-default)` in `:root` |

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
| `--ai-ad-step-angle` | `0deg` | Design System Custom Token |
| `--duration` | `38s` | Motion / Easing Token |
| `--font-display` | `var(--font-sans)` | Typography / Scale Token |
| `--gap` | `12px` | Layout / Spatial Grid Token |
| `--sd-line2` | `#404040!important` | Color / Atmospheric Token |
| `--sd-line` | `#262626!important` | Color / Atmospheric Token |
| `--sd-paper` | `#171717!important` | Canvas / Surface Token |
| `--sd-raise` | `#262626!important` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.hidden> — `www-nereo-io`)**:
   - Landmark `<nav class="hidden items-center">` hosting `Nereo — AI Video Generator for Creat` navigation (`Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.sticky> — `AI Video Generator for Creators & `)**:
   - Landmark `<section class="sticky top-0">` presenting display lead `AI Video Generator for Creators & Marketers` and copy excerpt *"Video Tools AI Anime Shorts Text to Video Flow AI Video Generator"* over `#404040` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Nereo Agent Describe the video. Th`)**:
   - Landmark `<section class="relative overflow-hidden">` rendering section `Nereo Agent Describe the video. The agent writes...` with copy *"Flow AI Video Generator"*, asset references (`logo.png`, `322e14d06135256b.css`, `1957d3acd0c31940.css`, `935ae15180c0d693.css`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Seedance 2.5 One continuous 30-sec`)**:
   - Landmark `<section class="flex flex-col">` framing `Seedance 2.5 One continuous 30-second take, nativ...` and `Seedance 2.0 Audio and video generated together,...` (*"Reference to Video"*) with `#171717` surface cards, `#b1b1b7` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.antialiased> — `https://www.nereo.io/`)**:
   - Landmark `<footer class="antialiased">` anchoring `Nereo — AI Video Generator for C` footer links (`Nereo · Home · AI Anime Shorts · Text to Video · Image to Video`), copy *"ElevenLabs Alternative"*, and `#fff` structural dividers.
