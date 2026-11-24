---
title: "UI & UX Architecture: theperformancelab-ca"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: theperformancelab-ca

## Overview & Design Identity
- **Target**: `theperformancelab-ca` (**The Performance Lab — Sports Science & Athletic Testing in Toronto**)
- **Production URL**: [https://theperformancelab.ca/](https://theperformancelab.ca/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#171717` canvas, `#f2f2f2` ink, `#ff0000` accent)
- **Summary**: The Performance Lab is a Toronto sports science centre offering 3D motion-capture testing, performance training, and sports therapy — tru...
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `display`
- **Body Font Stack**: `display`
- **Monospace / Technical Font Stack**: `mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 39px`, `line-height: 31.2px`, `font-weight: 500`, `letter-spacing: -1.56px`); CSS variables `--font-display: var(--font-display-family)`, `--font-display-family: "display","display Fallback"`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 135px`, `line-height: 108px`, `font-weight: 500`, `letter-spacing: -5.4px`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-mono-family)`, `--font-mono-family: "mono","mono Fallback"`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#171717` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f2f2f2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `20 { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#ff0000` | `:hover { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#bbbbbb` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#bbbbbb` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |
| **Variable Token (`--color-base-white-01`)** | `#e0e0e0` | `var(--color-base-white-01)` in `:root` |
| **Variable Token (`--color-neutral-grey`)** | `#979797` | `var(--color-neutral-grey)` in `:root` |
| **Variable Token (`--color-neutral-grey-01`)** | `#727272` | `var(--color-neutral-grey-01)` in `:root` |
| **Variable Token (`--color-neutral-grey-03`)** | `#292929` | `var(--color-neutral-grey-03)` in `:root` |
| **Variable Token (`--color-performance-red`)** | `#ff350d` | `var(--color-performance-red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-base-white` | `#f2f2f2` | Canvas / Surface Token |
| `--color-base-white-01` | `#e0e0e0` | Canvas / Surface Token |
| `--color-base-white-02` | `#bbb` | Canvas / Surface Token |
| `--color-neutral-grey` | `#979797` | Brand / Palette Token |
| `--color-neutral-grey-01` | `#727272` | Brand / Palette Token |
| `--color-neutral-grey-03` | `#292929` | Brand / Palette Token |
| `--color-core-black` | `#171717` | Canvas / Surface Token |
| `--color-performance-red` | `#ff350d` | Brand / Palette Token |
| `--font-display` | `var(--font-display-family)` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono-family)` | Typography / Scale Token |
| `--font-diatype` | `var(--font-diatype-family)` | Typography / Scale Token |
| `--ease-out-expo` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--ease-in-out-quart` | `cubic-bezier(.76,0,.24,1)` | Motion / Easing Token |
| `--background` | `var(--color-core-black)` | Canvas / Surface Token |
| `--foreground` | `var(--color-base-white)` | Typography Ink Token |
| `--font-display-family` | `"display","display Fallback"` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `theperformancelab-ca`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x62px`) hosting `The Performance Lab — Sports Science` navigation (`H O M E · W H O W E A R E · B L O G · C O N T A C T`), DOM attributes (`data-precedence="next"`, `data-theme="dark"`, `data-services-open="false"`, `data-scroll-state="false"`), and stylesheet rule `.__className_9dcdb7 { font-family:display,display Fallback }`.
2. **Hero Stage & Focal Lead (<section.mx-auto> — `UNLOCKNEXT LEVELPERFORMANCE`)**:
   - Landmark `<section class="mx-auto relative">` presenting display lead `UNLOCKNEXT LEVELPERFORMANCE` and copy excerpt *"EVERYTHING YOUR BODY NEEDS TO PERFORM, RECOVER, AND LAST."* over `#171717` canvas and `#f2f2f2` ink.
3. **Primary Showcase & Content Grid (<section.hidden> — `UNLOCK NEXT LEVEL PERFORMANCE`)**:
   - Landmark `<section class="hidden relative">` rendering section `UNLOCK NEXT LEVEL PERFORMANCE` with copy *"B O O K A C O N S U L T A T I O N"*, asset references (`desktop.jpg`, `i1.webp`, `i2.webp`, `i3.webp`), and grid rule `.__variable_9dcdb7 { --font-display-family:"display","display Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Helping you move better, recover s`)**:
   - Landmark `<section class="mx-auto relative">` framing `Helping you move better, recover smarter, and per...` and `Reach your goals. Whether you’re pursuing profess...` (*"Everything your body needs to perform, recover, and last."*) with `#000000` surface cards, `#ff0000` accents, and `.__className_ac1fe6 { font-family:mono,mono Fallback;font-weight:400;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.mx-auto> — `https://theperformancelab.ca/`)**:
   - Landmark `<footer class="mx-auto flex">` anchoring `The Performance Lab — Sports Sci` footer links (`H O M E · W H O W E A R E · B L O G · C O N T A C T`), copy *"The Performance Lab specializes in elite diagnostics, person"*, and `#bbbbbb` structural dividers.
