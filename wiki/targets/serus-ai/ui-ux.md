---
title: "UI & UX Architecture: serus-ai"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: serus-ai

## Overview & Design Identity
- **Target**: `serus-ai` (**Serus — Agentic Privacy & Intelligence**)
- **Production URL**: [https://serus.ai/](https://serus.ai/)
- **Final Redirected URL**: [https://www.serus.ai/](https://www.serus.ai/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#800080`)
- **Summary**: Your own privacy agent: finds what's exposed, removes it, watches for more and lets you check who you're dealing with. Protection and int...
- **Total Clean CSS Variables Extracted**: `177` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Reckless`
- **Body Font Stack**: `Geist Variable`
- **Monospace / Technical Font Stack**: `Geist Mono Variable`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 46px`, `font-weight: 400`, `letter-spacing: -0.7px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`, `letter-spacing: -0.96px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: 30px`, `line-height: 40px`, `letter-spacing: -.6px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`line-height: 1.625`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--chart-label: oklch(45% .01 260)`, `--font-mono: "Geist Mono Variable", ui-monospace, monospace`, `--text-xs: .75rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0d0d` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f5` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#800080` | `.bt-pill-page { background-color: purple }` (`#800080`) |
| **Interactive Accent / Highlight** | `#800080` | `.prose-serus a:hover { color: purple }` (`#800080`) |
| **Secondary / Muted Copy** | `#808080` | `.eyebrow { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#808080` | `.border-gray-200 { border-color: #808080 }` |
| **Variable Token (`--dither-fill`)** | `#ebebeb` | `var(--dither-fill)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dither-fill` | `#ebebeb` | Color / Atmospheric Token |
| `--chart-1` | `oklch(32% 0 none)` | Color / Atmospheric Token |
| `--chart-2` | `oklch(41% 0 none)` | Color / Atmospheric Token |
| `--chart-3` | `oklch(54% 0 none)` | Color / Atmospheric Token |
| `--chart-4` | `oklch(71% 0 none)` | Color / Atmospheric Token |
| `--chart-5` | `oklch(89% 0 none)` | Color / Atmospheric Token |
| `--chart-background` | `oklch(100% 0 0)` | Canvas / Surface Token |
| `--chart-foreground` | `oklch(14.5% .004 285)` | Typography Ink Token |
| `--chart-foreground-muted` | `oklch(55% .014 260)` | Typography Ink Token |
| `--chart-line-primary` | `var(--chart-1)` | Brand / Palette Token |
| `--chart-line-secondary` | `var(--chart-2)` | Brand / Palette Token |
| `--chart-crosshair` | `oklch(40% .1828 274.34)` | Color / Atmospheric Token |
| `--chart-grid` | `oklch(90% 0 0)` | Layout / Spatial Grid Token |
| `--chart-brush-border` | `var(--chart-grid)` | Elevation / Border Token |
| `--chart-tooltip-background` | `oklch(100% 0 0/.92)` | Canvas / Surface Token |
| `--chart-tooltip-foreground` | `oklch(21% 0 0)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `serus-ai`)**:
   - Landmark `<header class="top-0 bg-background-canvas">` (`1440x56px`) hosting `Serus — Agentic Privacy & Intelligen` navigation (`People Meet the team · Blog News & guides`), DOM attributes (`data-id="D6EM0HRC77UCIF8JNLS0"`, `data-id="D6EM0HRC77UCIF8JNLS0"`, `data-astro-cid-nen7h5rs`, `data-nav-menu`), and stylesheet rule `hover { transform:translateY(calc(var(--lift) - 6px)) rotate(0deg) }`.
2. **Hero Stage & Focal Lead (<section.bg-background-canvas> — `Meet your personal security assist`)**:
   - Landmark `<section class="bg-background-canvas text-sds-text-default">` presenting display lead `Meet your personal security assistant` and copy excerpt *"Proactive protection against threats and scams, and removal of yo"* over `#0d0d0d` canvas and `#f5f5f5` ink.
3. **Primary Showcase & Content Grid (<section.px-4> — `Other AI waits to be asked. Serus `)**:
   - Landmark `<section class="px-4 py-20">` rendering section `Other AI waits to be asked. Serus texts you first.` with copy *"Serus announces fundraising"*, asset references (`clientParamBuilder.bundle.js`, `identify_f7846436.js`, `main.MTUyMzg1YjAxMQ.js`, `events.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.py-20> — `It notices when your data comes ba`)**:
   - Landmark `<section class="px-4 py-20">` framing `It notices when your data comes back` and `It watches the world around you` (*"Used by people at leading companies"*) with `#800080` surface cards, `#800080` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.pb-6> — `https://serus.ai/`)**:
   - Landmark `<footer class="pb-6 pt-16">` anchoring `Serus — Agentic Privacy & Intell` footer links (`People Meet the team · Blog News & guides`), copy *"A contact is hacked"*, and `#808080` structural dividers.
