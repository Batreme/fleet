---
title: "UI & UX Architecture: senawastudio-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: senawastudio-com

## Overview & Design Identity
- **Target**: `senawastudio-com` (**Senawa · Architecture & Interior Design Studio in Jakarta**)
- **Production URL**: [https://senawastudio.com](https://senawastudio.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f2eb` canvas, `#302620` ink, `#8a5a2b` accent)
- **Summary**: Architecture made for how people actually live. An architecture, interior, and furniture design studio in the Greater Jakarta area.
- **Total Clean CSS Variables Extracted**: `58` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sora`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 31.5px`, `line-height: 37.8px`, `font-weight: 300`, `letter-spacing: -0.315px`); CSS variables `--font-display: var(--font-sora), "Sora", var(--font-sans), "Helvetica Neue", sans-serif`
- **Section Heading (`H2`)**: observed font-size ladder: `31.5px`, `14px`, `12px`, `13.3333px`, `10px`
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 24.5px`, `font-weight: 300`); CSS variables `--font-body: var(--font-sans), "Inter", "Helvetica Neue", sans-serif`, `--leading-body: 1.75`; rule `p` (`font-size: clamp(.9375rem,1vw,1.0625rem)`, `line-height: var(--leading-body)`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 24.5px`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f2eb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#302620` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#302620` | live computed `main` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#8a5a2b` | `var(--umber)` in `:root` |
| **Secondary / Muted Copy** | `#302620` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dcd2bf` | `var(--rule-light)` in `:root` |
| **Variable Token (`--linen`)** | `#ede6d8` | `var(--linen)` in `:root` |
| **Variable Token (`--sand`)** | `#d4c9b4` | `var(--sand)` in `:root` |
| **Variable Token (`--oak`)** | `#a8967e` | `var(--oak)` in `:root` |
| **Variable Token (`--walnut`)** | `#6b5a48` | `var(--walnut)` in `:root` |
| **Variable Token (`--lichen`)** | `#4a5247` | `var(--lichen)` in `:root` |
| **Variable Token (`--flax`)** | `#8c7b5c` | `var(--flax)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wool` | `#f6f2eb` | Color / Atmospheric Token |
| `--linen` | `#ede6d8` | Color / Atmospheric Token |
| `--sand` | `#d4c9b4` | Color / Atmospheric Token |
| `--oak` | `#a8967e` | Color / Atmospheric Token |
| `--walnut` | `#6b5a48` | Color / Atmospheric Token |
| `--slate` | `#302620` | Color / Atmospheric Token |
| `--lichen` | `#4a5247` | Color / Atmospheric Token |
| `--flax` | `#8c7b5c` | Color / Atmospheric Token |
| `--color-bg` | `var(--wool)` | Canvas / Surface Token |
| `--color-text` | `var(--slate)` | Typography Ink Token |
| `--color-text-sub` | `var(--slate)` | Typography Ink Token |
| `--color-text-caption` | `var(--slate)` | Typography Ink Token |
| `--color-border` | `var(--sand)` | Brand / Palette Token |
| `--font-body` | `var(--font-sans), "Inter", "Helvetica Neue", sans-serif` | Typography / Scale Token |
| `--font-display` | `var(--font-sora), "Sora", var(--font-sans), "Helvetica Neue", sans-serif` | Typography / Scale Token |
| `--font-accent` | `var(--font-sora), "Sora", var(--font-sans), "Helvetica Neue", sans-serif` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.Nav-module__bLoQaq__nav> — `senawastudio-com`)**:
   - Landmark `<nav class="Nav-module__bLoQaq__nav Nav-module__bLoQaq__navHome">` (`1440x88px`) hosting `Senawa · Architecture & Interior Des` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-active`, `data-hero`), and stylesheet rule `nter_c21b1aaa-module__0pqmKW__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Senawa, Architecture & Interior De`)**:
   - Landmark `<section class="antialiased">` presenting display lead `Senawa, Architecture & Interior Design Studio in...` and copy excerpt *"AA House, Residential, 2025 (1 of 8)"* over `#f6f2eb` canvas and `#302620` ink.
3. **Primary Showcase & Content Grid (<section.skip-link> — `AA House, Residential, 2025 (1 of `)**:
   - Landmark `<section class="skip-link">` rendering section `AA House, Residential, 2025 (1 of 8)` with copy *"BSD, Tangerang Selatan"*, asset references (`clarity.js`, `xmr8ny30a5`, `0ha4m18glnjqn.js`, `3r7r9eemmq-97.js`), and grid rule `inter_c21b1aaa-module__0pqmKW__va... { --font-sans:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.Nav-module__bLoQaq__nav> — `BSD, Tangerang Selatan`)**:
   - Landmark `<section class="Nav-module__bLoQaq__nav">` framing `BSD, Tangerang Selatan` and `Residential · 2025` (*"Residential · 2025"*) with `#302620` surface cards, `#8a5a2b` accents, and `sora_2a023f4c-module__BGqKYq__cla... { font-family:Sora,Sora Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.Nav-module__bLoQaq__navHome> — `https://senawastudio.com`)**:
   - Landmark `<footer class="Nav-module__bLoQaq__navHome">` anchoring `Senawa · Architecture & Interior` footer links (`Overview · Index · Archive · About · Contact`), copy *"Louver House Giriloka"*, and `#dcd2bf` structural dividers.
