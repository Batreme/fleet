# UI & UX Architecture: tibdigital-com

## Overview & Design Identity
- **Target**: `tibdigital-com` (**TIB Digital · Built by humans. Powered by AI.**)
- **Production URL**: [https://tibdigital.com](https://tibdigital.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0c10` / `#0a0c10`)
- **Summary**: TIB Digital is an Austin and Hong Kong studio building AI-powered web, mobile and platform software for founders and agencies. Built by h...
- **Total Clean CSS Variables Extracted**: `72` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: 2.5rem`, `line-height: calc(var(--spacing) *...`, `letter-spacing: -.06em`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `,.h2` (`font-size: 2rem`, `line-height: calc(var(--spacing) * 9)`, `letter-spacing: -.06em`, `font-weight: var(--font-we...`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `,.paragraph` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: -.04em`)
- **Metadata & Labels**: CSS variables `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`, `--font-mono: var(--font-geist-mono)`, `--text-xs: .75rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0c10` | `var(--pl-dark)` in `:root` |
| **Primary Typography Ink** | `#00ff85` | `var(--pl-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e9eceb` | `var(--pl-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#0a0c10` | `var(--color-black)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--color-white)` in `:root` |
| **Structural Hairline Border** | `#141b23` | `var(--color-rich-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pl-dark` | `#0b0c10` | Canvas / Surface Token |
| `--pl-green` | `#00ff85` | Color / Atmospheric Token |
| `--pl-ink` | `#e9eceb` | Typography Ink Token |
| `--font-geist-sans` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--font-geist-mono` | `"Geist Mono", "Geist Mono Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-geist-sans)` | Typography / Scale Token |
| `--font-mono` | `var(--font-geist-mono)` | Typography / Scale Token |
| `--color-black` | `#0a0c10` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-5xl` | `64rem` | Layout / Spatial Grid Token |
| `--container-7xl` | `80rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.text-light> — `tibdigital-com`)**:
   - Landmark `<header class="text-light fixed">` hosting `TIB Digital · Built by humans. Power` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-perf-tier="full"`, `data-page-transition-ready="true"`, `data-page-loader-done="true"`, `data-precedence="next"`), and stylesheet rule `root { --pl-dark:0b0c10;--pl-green:00ff85;--pl-ink:e9eceb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Built by Humans. Powered by AI. Ma`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Built by Humans. Powered by AI. Made for what's n...` and copy excerpt *"Work ] ) W & % o % & r # # k"* over `#0b0c10` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.bg-grey-light> — `First prototype <24 hrs`)**:
   - Landmark `<section class="bg-grey-light relative">` rendering section `First prototype <24 hrs` with copy *"] ) W & % o % & r # # k"*, asset references (`07a39a8a4660cc7c-s.p.0r6juujl39pe...`, `605ce01b664af129-s.p.0wgildi0cnwt...`, `24e2077-fs8_m.css`, `235q64u4xcxu9.css`), and grid rule `.pl-glow-mount { pointer-events:none;position:absolute;inset:0 }`.
4. **Interactive Detail & Feature Matrix (<section.bg-grey-light> — `Design systems that ship`)**:
   - Landmark `<section class="bg-grey-light text-rich-black">` framing `Design systems that ship` and `AI agents in production` (*"About · $ A & % b # # o ) ( u € · t"*) with `#e9eceb` surface cards, `#0a0c10` accents, and `.pl-glow { pointer-events:none;width:100%;height:100%;display:block;position:absolu... }`.
5. **Colophon & Global Directory Footer (<footer.text-light> — `https://tibdigital.com`)**:
   - Landmark `<footer class="text-light relative">` anchoring `TIB Digital · Built by humans. P` footer links (`Overview · Index · Archive · About · Contact`), copy *"· $ A & % b # # o ) ( u € · t"*, and `#141b23` structural dividers.
