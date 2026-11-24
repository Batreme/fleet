---
title: "UI & UX Architecture: jimo-ai_product-ai"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: jimo-ai_product-ai

## Overview & Design Identity
- **Target**: `jimo-ai_product-ai` (**AI Agent for User Onboarding in SaaS · Jimo**)
- **Production URL**: [https://jimo.ai/product/ai](https://jimo.ai/product/ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#2b7fff`)
- **Summary**: Jimo's Adoption Agent lives inside your SaaS. It guides users step by step, answers questions from your docs, and takes actions for them....
- **Total Clean CSS Variables Extracted**: `317` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 86.4px`, `line-height: 89.856px`, `font-weight: 300`, `letter-spacing: -3.024px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.8px`, `line-height: 65.664px`, `font-weight: 300`, `letter-spacing: -1.824px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 32px`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 11.5px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0f0f0f` | `var(--pbg)` in `:root` |
| **Interactive Accent / Highlight** | `#2b7fff` | `.jlp-root .jlp-launcher-btn--start { background: #2b7fff }` |
| **Secondary / Muted Copy** | `#9aa3b5` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#141414` | `var(--line)` in `:root` (`ffffff14`) |
| **Variable Token (`--pm-fg`)** | `#071331` | `var(--pm-fg)` in `:root` |
| **Variable Token (`--pm-2`)** | `#7c8a99` | `var(--pm-2)` in `:root` |
| **Variable Token (`--pm-2-on`)** | `#4d637b` | `var(--pm-2-on)` in `:root` |
| **Variable Token (`--pm-hl`)** | `#f2f4f6` | `var(--pm-hl)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--card-w` | `344px` | Dimension / Scale Token |
| `--card-h` | `300px` | Dimension / Scale Token |
| `--pad` | `22px` | Layout / Spatial Grid Token |
| `--book-w` | `176px` | Dimension / Scale Token |
| `--mx` | `50%` | Dimension / Scale Token |
| `--my` | `50%` | Dimension / Scale Token |
| `--open` | `0` | Design System Custom Token |
| `--jlp-fnav-lift` | `10px` | Layout / Spatial Grid Token |
| `--jlp-fnav-fade` | `36px` | Layout / Spatial Grid Token |
| `--jlp-fnav-veil` | `1` | Layout / Spatial Grid Token |
| `--jlp-fnav-ease` | `cubic-bezier(.22, 1, .36, 1)` | Layout / Spatial Grid Token |
| `--pm-fg` | `#071331` | Typography Ink Token |
| `--pm-soft` | `#071331cc` | Color / Atmospheric Token |
| `--pm-2` | `#7c8a99` | Color / Atmospheric Token |
| `--pm-2-on` | `#4d637b` | Color / Atmospheric Token |
| `--pm-hl` | `#f2f4f6` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.jlp-fnav> — `jimo-ai_product-ai`)**:
   - Landmark `<header class="jlp-fnav jlp-btn-dark">` (`1440x88px`) hosting `AI Agent for User Onboarding in SaaS` navigation (`Products · Use Case · Pricing · Customers · Resources`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `module__rJ0bIq__row::-webkit-scro... { display:none }`.
2. **Hero Stage & Focal Lead (<section.text-center> — `An agent in your SaaS that makes a`)**:
   - Landmark `<section class="text-center relative">` presenting display lead `An agent in your SaaS that makes adoption skyrock...` and copy excerpt *"Jimo Agent sees your interface, and becomes a tutor for your user"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `One agent. Three modes .`)**:
   - Landmark `<section class="relative">` rendering section `One agent. Three modes .` with copy *"Every user gets a guide"*, asset references (`5c285b27cdda1fe8-s.p.0yo6-5yoeeud...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `gt-walsheim-medium.ttf`, `gt-walsheim-regular.ttf`), and grid rule `.customer-stories-module__rJ0bIq_... { --card-w:344px;--card-h:300px;--pad:22px;--book-w:176px;flex:0 0 var(--c... }`.
4. **Interactive Detail & Feature Matrix (<section.relative:nth(2)> — `Guides users on the fly`)**:
   - Landmark `<section class="relative">` framing `Guides users on the fly` and `Answers contextual questions` (*"Help your users convert with a personal guide."*) with `#0f0f0f` surface cards, `#2b7fff` accents, and `ries-module__rJ0bIq__card:focus-v... { transform:translateY(-4px);box-shadow:inset 0 0 0 1px fff3,0 24px 60px 0... }`.
5. **Colophon & Global Directory Footer (<footer.footer-module__d_pQKq__root> — `https://jimo.ai/product/ai`)**:
   - Landmark `<footer class="footer-module__d_pQKq__root">` anchoring `AI Agent for User Onboarding in ` footer links (`Products · Use Case · Pricing · Customers · Resources`), copy *"Help your users convert"*, and `#141414` structural dividers.
