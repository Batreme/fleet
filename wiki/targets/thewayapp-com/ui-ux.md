---
title: "UI & UX Architecture: thewayapp-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: thewayapp-com

## Overview & Design Identity
- **Target**: `thewayapp-com` (**The Way App - Meditation that lasts a lifetime — The Way**)
- **Production URL**: [https://thewayapp.com](https://thewayapp.com)
- **Final Redirected URL**: [https://www.thewayapp.com/](https://www.thewayapp.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#267768`)
- **Summary**: A long-term path of deep meditation training, guided by Zen Master Henry Shukman
- **Total Clean CSS Variables Extracted**: `228` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `nunito`
- **Body Font Stack**: `nunito Fallback`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: observed font-size ladder: `100%`, `9.0909090909vw`, `60px`, `120px`, `6.0606060606vw`
- **Section Heading (`H2`)**: observed font-size ladder: `100%`, `9.0909090909vw`, `60px`, `120px`, `6.0606060606vw`
- **Body Copy**: rule `p` (`font-size: 18px`)
- **Metadata & Labels**: observed font-size ladder: `100%`, `9.0909090909vw`, `60px`, `120px`, `6.0606060606vw`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `canvas-modal-luma` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | `.form_consentLabel__oKm0C { color: black }` (`#000000`) |
| **Elevated Surface / Card Substrate** | `#f7ede8` | `.scholarship_amountBadge__jyNhN { background: #f7ede8 }` |
| **Interactive Accent / Highlight** | `#267768` | `.Preloader_cta___rMP3 { color: #267768 }` |
| **Secondary / Muted Copy** | `#7d9792` | `.EndCard_offerPrice__4IHKn { color: #7d9792 }` |
| **Structural Hairline Border** | `#e5e5e5` | `.Accordion_item__siU0V { border-bottom: #e5e5e5 }` |
| **Variable Token (`--color-evergreen-light`)** | `#e8f2f0` | `var(--color-evergreen-light)` in `:root` |
| **Variable Token (`--color-evergreen-default`)** | `#1c5349` | `var(--color-evergreen-default)` in `:root` |
| **Variable Token (`--color-evergreen-dark`)** | `#122e28` | `var(--color-evergreen-dark)` in `:root` |
| **Variable Token (`--color-deepsea-light`)** | `#e6f2f0` | `var(--color-deepsea-light)` in `:root` |
| **Variable Token (`--color-deepsea-dark`)** | `#1a5249` | `var(--color-deepsea-dark)` in `:root` |
| **Variable Token (`--color-terracotta-default`)** | `#c1775b` | `var(--color-terracotta-default)` in `:root` |
| **Variable Token (`--color-terracotta-dark`)** | `#8f5440` | `var(--color-terracotta-dark)` in `:root` |
| **Variable Token (`--color-cloudberry-light`)** | `#fff7f6` | `var(--color-cloudberry-light)` in `:root` |
| **Variable Token (`--color-cloudberry-default`)** | `#ffe9e7` | `var(--color-cloudberry-default)` in `:root` |
| **Variable Token (`--color-cloudberry-dark`)** | `#f5c4bf` | `var(--color-cloudberry-dark)` in `:root` |
| **Variable Token (`--color-sky-light`)** | `#e7f8ff` | `var(--color-sky-light)` in `:root` |
| **Variable Token (`--color-sky-default`)** | `#e8f8ff` | `var(--color-sky-default)` in `:root` |
| **Variable Token (`--color-desert-light`)** | `#f8e1d9` | `var(--color-desert-light)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--blur-background` | `blur(12px)` | Canvas / Surface Token |
| `--color-evergreen-light` | `#e8f2f0` | Canvas / Surface Token |
| `--color-evergreen-default` | `#1c5349` | Brand / Palette Token |
| `--color-evergreen-dark` | `#122e28` | Canvas / Surface Token |
| `--color-deepsea-light` | `#e6f2f0` | Canvas / Surface Token |
| `--color-deepsea-default` | `#267768` | Brand / Palette Token |
| `--color-deepsea-dark` | `#1a5249` | Canvas / Surface Token |
| `--color-terracotta-light` | `#f7ede8` | Canvas / Surface Token |
| `--color-terracotta-default` | `#c1775b` | Brand / Palette Token |
| `--color-terracotta-dark` | `#8f5440` | Canvas / Surface Token |
| `--color-cloudberry-light` | `#fff7f6` | Canvas / Surface Token |
| `--color-cloudberry-default` | `#ffe9e7` | Brand / Palette Token |
| `--color-cloudberry-dark` | `#f5c4bf` | Canvas / Surface Token |
| `--color-sky-light` | `#e7f8ff` | Canvas / Surface Token |
| `--color-sky-default` | `#e8f8ff` | Brand / Palette Token |
| `--color-desert-light` | `#f8e1d9` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Header_header__gtmFw> — `thewayapp-com`)**:
   - Landmark `<header class="Header_header__gtmFw theme-light">` (`1440px`) hosting `The Way App - Meditation that lasts ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `root { font-synthesis:none;text-rendering:optimizeLegibility;-webkit-text-size-... }`.
2. **Hero Stage & Focal Lead (<article.StaticNarrative_root__V_9OR> — `The end of your search. The start `)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` presenting display lead `The end of your search. The start of your journey.` and copy excerpt *"The end of your search."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.StaticNarrative_root__V_9OR:nth(2)> — `One way forward`)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` rendering section `One way forward` with copy *"The start of your journey."*, asset references (`75aacf3429424351-s.p.woff2`, `df8e05a132a73a9c-s.p.woff2`, `95817d087ee99a00.css`, `6fc6cebf31cdec86.css`), and grid rule `html { overflow-x:hidden;scrollbar-width:thin;scroll-behavior:smooth }`.
4. **Interactive Detail & Feature Matrix (<article.StaticNarrative_root__V_9OR:nth(3)> — `Meet your teacher: Henry Shukman`)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` framing `Meet your teacher: Henry Shukman` and `A path that deepens with every step` (*"Most meditation apps give you countless options. The Way offers o"*) with `#f7ede8` surface cards, `#267768` accents, and `video { width:100%;height:auto;-webkit-user-select:none;-moz-user-select:none;us... }`.
5. **Colophon & Global Directory Footer (<footer.type-ui-micro> — `https://thewayapp.com`)**:
   - Landmark `<footer class="type-ui-micro StaticNarrative_attribution__25nmb">` anchoring `The Way App - Meditation that la` footer links (`Overview · Index · Archive · About · Contact`), copy *"I've finally been able to commit to daily meditation after y"*, and `#e5e5e5` structural dividers.
