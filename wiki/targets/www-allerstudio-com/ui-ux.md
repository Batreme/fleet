---
title: "UI & UX Architecture: www-allerstudio-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-allerstudio-com

## Overview & Design Identity
- **Target**: `www-allerstudio-com` (**ALLER Studio — Product design and development studio**)
- **Production URL**: [https://www.allerstudio.com/](https://www.allerstudio.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f9fafb` / `#0000ff`)
- **Summary**: Product design and development studio for Web3, AI, fintech, and gaming.
- **Total Clean CSS Variables Extracted**: `475` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Rajdhani`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 56px`, `font-weight: 600`); CSS variables `--text-5xl: 3rem`, `--text-5xl--line-height: 1`, `--font-display: var(--font-rajdhani), "Arial Narrow", sans-serif`; rule `h1` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`)
- **Section Heading (`H2`)**: live computed `h2 (largest visible desktop heading)` (`font-size: 64px`, `line-height: 1.2`, `font-weight: 600`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9fafb` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#121212` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f7f8` | `var(--color-surface-bg-2)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `:text-blue-600 a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#787878` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dadee2` | `var(--color-border)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--duration-quick` | `.15s` | Motion / Easing Token |
| `--duration-fast` | `.25s` | Motion / Easing Token |
| `--duration-medium` | `.35s` | Motion / Easing Token |
| `--duration-very-slow` | `.5s` | Motion / Easing Token |
| `--ease-smooth-out` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--ease-bounce` | `cubic-bezier(.34, 1.35, .64, 1)` | Motion / Easing Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-rajdhani` | `"Rajdhani", "Rajdhani Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-inter), "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header-in> — `www-allerstudio-com`)**:
   - Landmark `<header class="header-in top-4">` (`954x64px`) hosting `ALLER Studio — Product design and de` navigation (`Services · Case Studies · Studio · Insights · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.jjo8ZG_className { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.pt-40> — `Product design and development stu`)**:
   - Landmark `<section class="pt-40 relative">` presenting display lead `Product design and development studio for Web3, A...` and copy excerpt *"Lima · 12:17 PM UTC-5"* over `#f9fafb` canvas and `#121212` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Technology can be complex. The exp`)**:
   - Landmark `<section class="relative px-4">` rendering section `Technology can be complex. The experience should...` with copy *"Not made for the moment."*, asset references (`3206eb66b875a5b3-s.p.3gjg6tthudz5...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `a079e02bba5bf7ab-s.p.2yv0x3fl1lx-...`, `a10c617c9026098c-s.p.1a-q6cj6za4e...`), and grid rule `.jjo8ZG_variable { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.pt-20> — `Complex flows`)**:
   - Landmark `<section class="pt-20 pb-4">` framing `Complex flows` and `Low user trust` (*"Built for what follows."*) with `#f6f7f8` surface cards, `#0000ff` accents, and `.U4jUma_className { font-family:Rajdhani,Rajdhani Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.z-42> — `https://www.allerstudio.com/`)**:
   - Landmark `<footer class="z-42 bg-dark-950">` anchoring `ALLER Studio — Product design an` footer links (`Services · Case Studies · Studio · Insights · Contact`), copy *"Product strategy · UX/UI · Branding · Development"*, and `#dadee2` structural dividers.
