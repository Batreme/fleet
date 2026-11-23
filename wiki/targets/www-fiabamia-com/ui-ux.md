---
title: "UI & UX Architecture: www-fiabamia-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-fiabamia-com

## Overview & Design Identity
- **Target**: `www-fiabamia-com` (**FiabaMia — Personalized bedtime stories for children**)
- **Production URL**: [https://www.fiabamia.com/](https://www.fiabamia.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#05040f` / `#f5c842`)
- **Summary**: Every night a brand-new bedtime story where your child is the hero: written in 30 seconds to fit their age, with music, interactive sound...
- **Total Clean CSS Variables Extracted**: `186` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Nunito`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 27.2px`, `line-height: 29.92px`, `font-weight: 300`, `letter-spacing: -0.544px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(1.45rem,2.6vw,1.85rem)`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 300`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: clamp(1.05rem,1.5vw,1.38rem)`, `line-height: 1.4`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10.56px`, `line-height: 15.84px`, `font-weight: 400`, `letter-spacing: 2.3232px`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .42em`, `letter-spacing: 0`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#05040f` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f8f4ff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#252550` | `var(--color-night-card)` in `:root` |
| **Interactive Accent / Highlight** | `#f5c842` | `var(--color-accent-gold)` in `:root` |
| **Secondary / Muted Copy** | `#6b5a3e` | `var(--color-ink-warm)` in `:root` |
| **Structural Hairline Border** | `#e8d9b5` | `var(--color-book-border)` in `:root` |
| **Variable Token (`--color-red-300`)** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Variable Token (`--color-red-400`)** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Variable Token (`--color-red-500`)** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Variable Token (`--color-amber-50`)** | `#fffbeb` | `var(--color-amber-50)` in `:root` |
| **Variable Token (`--color-amber-300`)** | `#ffd236` | `var(--color-amber-300)` in `:root` |
| **Variable Token (`--color-amber-400`)** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Variable Token (`--color-amber-500`)** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Variable Token (`--color-amber-600`)** | `#dd7400` | `var(--color-amber-600)` in `:root` |
| **Variable Token (`--color-amber-700`)** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Variable Token (`--color-yellow-400`)** | `#fac800` | `var(--color-yellow-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lightningcss-dark` | `initial` | Canvas / Surface Token |
| `--font-lora` | `"Lora", "Lora Fallback"` | Typography / Scale Token |
| `--font-cormorant-sc` | `"Cormorant SC", "Cormorant SC Fallback"` | Typography / Scale Token |
| `--font-nunito` | `"Nunito", "Nunito Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-nunito)` | Typography / Scale Token |
| `--font-serif` | `var(--font-lora)` | Typography / Scale Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-amber-50` | `#fffbeb` | Brand / Palette Token |
| `--color-amber-300` | `#ffd236` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-amber-600` | `#dd7400` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-yellow-400` | `#fac800` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.vg-testata> — `www-fiabamia-com`)**:
   - Landmark `<header class="vg-testata">` (`1425x84px`) hosting `FiabaMia — Personalized bedtime stor` navigation (`Create a story`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `lora_59c43264-module__4gbARq__cla... { font-family:Lora,Lora Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.vg-hero> — `Personalized bedtime stories for c`)**:
   - Landmark `<section class="vg-hero is-via">` presenting display lead `Personalized bedtime stories for children A fairy...` and copy excerpt *"FIABAMIA · A BEDTIME FAIRY TALE"* over `#05040f` canvas and `#f8f4ff` ink.
3. **Primary Showcase & Content Grid (<section.vg-lettura> — `A story made to measure: name, age`)**:
   - Landmark `<section class="vg-lettura">` rendering section `A story made to measure: name, age, value, place...` with copy *"FiabaMia · a bedtime fairy tale"*, asset references (`07454f8ad8aaac57-s.p.0tqkxa-w3pk~...`, `25e51d4a4d803f16-s.p.01lzzy~hm0v2...`, `4917c4fe274b6773-s.p.03o7i-1ioayt...`, `54fc36028e2bb174-s.p.0nkps02--w45...`), and grid rule `.lora_59c43264-module__4gbARq__va... { --font-lora:"Lora", "Lora Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.vg-tunnel> — `E v e r y s t o r y h a s i t s o `)**:
   - Landmark `<section class="vg-tunnel">` framing `E v e r y s t o r y h a s i t s o w n m u s i c` and `W o r d s t h a t c o m e t o l i f e` (*"No one has ever told it…"*) with `#252550` surface cards, `#f5c842` accents, and `t_sc_8e09fe47-module__uQmyda__cla... { font-family:Cormorant SC,Cormorant SC Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.vg-fondo> — `https://www.fiabamia.com/`)**:
   - Landmark `<footer class="vg-fondo site-footer">` anchoring `FiabaMia — Personalized bedtime ` footer links (`Create a story`), copy *"N o o n e h a s e v e r t o l d i t …"*, and `#e8d9b5` structural dividers.
