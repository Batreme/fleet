# UI & UX Architecture: glinto-co-kr

## Overview & Design Identity
- **Target**: `glinto-co-kr` (**Glinto — Creative studio**)
- **Production URL**: [https://glinto.co.kr](https://glinto.co.kr)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ffc7b0`)
- **Summary**: Glinto is a creative studio where one team takes brand strategy and identity, film and photography, design, and web and app development f...
- **Total Clean CSS Variables Extracted**: `293` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `DM Sans Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--text-h1: var(--fs-h1)`, `--text-h1--line-height: var(--lh-figma)`, `--text-display-sans: var(--fs-display-sans)`
- **Section Heading (`H2`)**: CSS variables `--text-h2: var(--fs-h2)`, `--text-h2--line-height: var(--lh-figma)`, `--subtitle-color: var(--gray-200)`
- **Body Copy**: CSS variables `--text-body-s: var(--fs-body-s)`, `--text-body-s--line-height: var(--lh-figma)`, `--text-body-m: var(--fs-body-m)`
- **Metadata & Labels**: CSS variables `--text-sm: var(--fs-sm)`, `--text-sm--line-height: var(--lh-sm)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#fff3ee` | `var(--accent-50)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffe4d9` | `var(--accent-100)` in `:root` |
| **Interactive Accent / Highlight** | `#ffc7b0` | `var(--accent-200)` in `:root` |
| **Secondary / Muted Copy** | `#ffa47d` | `var(--accent-300)` in `:root` |
| **Structural Hairline Border** | `#ff7f54` | `var(--accent-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-dm-sans` | `"DM Sans", "DM Sans Fallback"` | Typography / Scale Token |
| `--header-fill` | `0` | Layout / Spatial Grid Token |
| `--px-x` | `80%` | Dimension / Scale Token |
| `--px-y` | `0%` | Dimension / Scale Token |
| `--wm-x` | `20%` | Dimension / Scale Token |
| `--wm-y` | `30%` | Dimension / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-sm` | `var(--fs-sm)` | Typography Ink Token |
| `--text-sm--line-height` | `var(--lh-sm)` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--ease-in` | `cubic-bezier(.4, 0, 1, 1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header-wrap> — `glinto-co-kr`)**:
   - Landmark `<header class="site-header-wrap sticky">` hosting `Glinto — Creative studio` navigation (`About · Services · Glinto.dev · Works · Contact`), DOM attributes (`data-theme="light"`, `data-reveal-ready`, `data-progress-ready`, `data-precedence="next"`), and stylesheet rule `sans_efc253b3-module__w1i8Da__cla... { font-family:DM Sans,DM Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Everything your brand needs, from `)**:
   - Landmark `<section class="antialiased">` presenting display lead `Everything your brand needs, from one team` and copy excerpt *"Services Glinto.dev"* over `#fff` canvas and `#ff7f54` ink.
3. **Primary Showcase & Content Grid (<section.pt-24> — `Media`)**:
   - Landmark `<section class="pt-24">` rendering section `Media` with copy *"Creative studio for identity, visuals, and code."*, asset references (`2f7d2945a32bc936-s.p.0q9pvfn3wr_3...`, `5c285b27cdda1fe8-s.p.0lsanbtneewq...`, `0k1f2nt08p6_n.css`, `0twwmijs60d6j.css`), and grid rule `sans_efc253b3-module__w1i8Da__var... { --font-dm-sans:"DM Sans", "DM Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.pt-24> — `Design`)**:
   - Landmark `<section class="pt-24">` framing `Design` and `Engineering` (*"BX Plan it BX Plan it"*) with `#ffe4d9` surface cards, `#ffc7b0` accents, and `host { --header-fill:0;--px-x:80%;--px-y:0% }`.
5. **Colophon & Global Directory Footer (<footer.mt-24> — `https://glinto.co.kr`)**:
   - Landmark `<footer class="mt-24">` anchoring `Glinto — Creative studio` footer links (`About · Services · Glinto.dev · Works · Contact`), copy *"Media Capture it Media Capture it"*, and `#ff7f54` structural dividers.
