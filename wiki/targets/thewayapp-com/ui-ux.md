---
title: "UI & UX Architecture: thewayapp-com"
date: 2026-11-24
captured_at: 2026-11-24
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
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#267768`)
- **Summary**: A long-term path of deep meditation training, guided by Zen Master Henry Shukman
- **Total Clean CSS Variables Extracted**: `228` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `nunito`
- **Body Font Stack**: `nunito Fallback`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 92px`, `font-weight: 500`, `letter-spacing: -1.6px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 58px`, `font-weight: 500`, `letter-spacing: -0.96px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 18px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7ede8` | `.scholarship_amountBadge__jyNhN { background: #f7ede8 }` |
| **Interactive Accent / Highlight** | `#267768` | `.Preloader_cta___rMP3 { color: #267768 }` |
| **Secondary / Muted Copy** | `#1c5349` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5e5e5` | `.Accordion_item__siU0V { border-bottom: #e5e5e5 }` |
| **Variable Token (`--color-evergreen-light`)** | `#e8f2f0` | `var(--color-evergreen-light)` in `:root` |
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
   - Landmark `<header class="Header_header__gtmFw theme-light">` (`1440x60px`) hosting `The Way App - Meditation that lasts ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `root { font-synthesis:none;text-rendering:optimizeLegibility;-webkit-text-size-... }`.
2. **Hero Stage & Focal Lead (<article.StaticNarrative_root__V_9OR> — `The end of your search. The start `)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` presenting display lead `The end of your search. The start of your journey.` and copy excerpt *"Your first guided moment is about to begin..."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.StaticNarrative_root__V_9OR:nth(2)> — `One way forward`)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` rendering section `One way forward` with copy *"The end of your search."*, asset references (`75aacf3429424351-s.p.woff2`, `df8e05a132a73a9c-s.p.woff2`, `95817d087ee99a00.css`, `6fc6cebf31cdec86.css`), and grid rule `html { overflow-x:hidden;scrollbar-width:thin;scroll-behavior:smooth }`.
4. **Interactive Detail & Feature Matrix (<article.StaticNarrative_root__V_9OR:nth(3)> — `Meet your teacher: Henry Shukman`)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` framing `Meet your teacher: Henry Shukman` and `A path that deepens with every step` (*"The start of your journey."*) with `#f7ede8` surface cards, `#267768` accents, and `video { width:100%;height:auto;-webkit-user-select:none;-moz-user-select:none;us... }`.
5. **Colophon & Global Directory Footer (<footer.type-ui-micro> — `https://thewayapp.com`)**:
   - Landmark `<footer class="type-ui-micro StaticNarrative_attribution__25nmb">` anchoring `The Way App - Meditation that la` footer links (`Overview · Index · Archive · About · Contact`), copy *"Most meditation apps give you countless options. The Way off"*, and `#e5e5e5` structural dividers.
