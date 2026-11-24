---
title: "UI & UX Architecture: tibdigital-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: tibdigital-com

## Overview & Design Identity
- **Target**: `tibdigital-com` (**TIB Digital · Built by humans. Powered by AI.**)
- **Production URL**: [https://tibdigital.com](https://tibdigital.com)
- **Final Redirected URL**: [https://www.tibdigital.com/](https://www.tibdigital.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×1744px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0c10` / `#00ff84`)
- **Summary**: TIB Digital is an Austin and Hong Kong studio building AI-powered web, mobile and platform software for founders and agencies. Built by h...
- **Total Clean CSS Variables Extracted**: `72` (curated live-grounded set below)

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

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0c10` | live computed `meta-theme-color` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | `var(--text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#00ff84` | `var(--color-gradient-green)` in `:root` |
| **Secondary / Muted Copy** | `#e9eceb` | `var(--pl-ink)` in `:root` |
| **Structural Hairline Border** | `#008000` | `.border-green { border-color: #008000 }` |
| **Variable Token (`--pl-dark`)** | `#0b0c10` | `var(--pl-dark)` in `:root` |
| **Variable Token (`--pl-green`)** | `#00ff85` | `var(--pl-green)` in `:root` |

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
   - Landmark `<header class="text-light top-0">` (`1440px`) hosting `TIB Digital · Built by humans. Power` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-lg="sheen-grad"`), and stylesheet rule `root { --pl-dark:0b0c10;--pl-green:00ff85;--pl-ink:e9eceb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Built by Humans. Powered by AI. Ma`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Built by Humans. Powered by AI. Made for what's n...` and copy excerpt *"IRONING OUT DIGITAL PRODUCTS"* over `#0a0c10` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.bg-grey-light> — `First prototype <24 hrs`)**:
   - Landmark `<section class="bg-grey-light relative">` rendering section `First prototype <24 hrs` with copy *"Built by Humans. Powered by AI. Made for what's next."*, asset references (`07a39a8a4660cc7c-s.p.0r6juujl39pe...`, `605ce01b664af129-s.p.0wgildi0cnwt...`, `24e2077-fs8_m.css`, `235q64u4xcxu9.css`), and grid rule `.pl-glow-mount { pointer-events:none;position:absolute;inset:0 }`.
4. **Interactive Detail & Feature Matrix (<section.text-rich-black> — `Design systems that ship`)**:
   - Landmark `<section class="bg-grey-light text-rich-black">` framing `Design systems that ship` and `AI agents in production` (*"NO WRINKLES. NO SHORTCUTS."*) with `#000000` surface cards, `#00ff84` accents, and `.pl-glow { pointer-events:none;width:100%;height:100%;display:block;position:absolu... }`.
5. **Colophon & Global Directory Footer (<footer.text-light> — `https://tibdigital.com`)**:
   - Landmark `<footer class="text-light relative">` anchoring `TIB Digital · Built by humans. P` footer links (`Overview · Index · Archive · About · Contact`), copy *"TIB Digital combines human creativity and advanced AI to bui"*, and `#008000` structural dividers.
