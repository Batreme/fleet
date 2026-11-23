---
title: "UI & UX Architecture: jimo-ai_product-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: jimo-ai_product-ai

## Overview & Design Identity
- **Target**: `jimo-ai_product-ai` (**AI Agent for User Onboarding in SaaS · Jimo**)
- **Production URL**: [https://jimo.ai/product/ai](https://jimo.ai/product/ai)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#2b7fff`)
- **Summary**: Jimo's Adoption Agent lives inside your SaaS. It guides users step by step, answers questions from your docs, and takes actions for them....
- **Total Clean CSS Variables Extracted**: `315` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `GT Walsheim Pro Regular`
- **Body Font Stack**: `GT Walsheim Pro Bold`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `10px`, `var(--jlp-btn-size)`, `12px`, `var(--code)`, `11px`
- **Section Heading (`H2`)**: observed font-size ladder: `10px`, `var(--jlp-btn-size)`, `12px`, `var(--code)`, `11px`
- **Body Copy**: rule `p` (`font-size: 32px`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 12px`, `line-height: 16px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `meta-theme-color` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | `var(--jlp-btn-fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#16254f` | `var(--jlp-btn-bg-hover)` in `:root` |
| **Interactive Accent / Highlight** | `#2b7fff` | `.jlp-root .jlp-launcher-btn--start { background: #2b7fff }` |
| **Secondary / Muted Copy** | `#9aa3b5` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#141414` | `var(--line)` in `:root` (`ffffff14`) |
| **Variable Token (`--token-c5f3a181-ce4f-4420-a296-873f4d681873`)** | `#fff0` | `var(--token-c5f3a181-ce4f-4420-a296-873f4d681873)` in `:root` |
| **Variable Token (`--token-f50d19c8-b71c-4ab6-8ff6-6267c86824d4`)** | `#071331` | `var(--token-f50d19c8-b71c-4ab6-8ff6-6267c86824d4)` in `:root` |
| **Variable Token (`--token-f4cc4358-9285-4b73-95d1-a84a305a5e4c`)** | `#2c2c2c` | `var(--token-f4cc4358-9285-4b73-95d1-a84a305a5e4c)` in `:root` |
| **Variable Token (`--token-019ac301-73c6-46eb-9851-3eb602913d3e`)** | `#9aa0b0` | `var(--token-019ac301-73c6-46eb-9851-3eb602913d3e)` in `:root` |
| **Variable Token (`--token-88c94126-8d08-4d70-ad93-089fe72c39c1`)** | `#1261eb` | `var(--token-88c94126-8d08-4d70-ad93-089fe72c39c1)` in `:root` |
| **Variable Token (`--token-6051c877-d0ec-4b68-8d57-1bfdb02b909c`)** | `#ffe6b8` | `var(--token-6051c877-d0ec-4b68-8d57-1bfdb02b909c)` in `:root` |
| **Variable Token (`--token-9eb2db68-5dd1-49a4-b3f4-b9acc27e81e7`)** | `#bdffea` | `var(--token-9eb2db68-5dd1-49a4-b3f4-b9acc27e81e7)` in `:root` |
| **Variable Token (`--token-b6e57dc6-83ba-4f1b-bdf7-3940ef910fb9`)** | `#deffad` | `var(--token-b6e57dc6-83ba-4f1b-bdf7-3940ef910fb9)` in `:root` |
| **Variable Token (`--token-da636760-7871-4b98-bdd9-6abbce729e64`)** | `#f0e3fc` | `var(--token-da636760-7871-4b98-bdd9-6abbce729e64)` in `:root` |
| **Variable Token (`--token-9711da88-e2ac-4365-a65b-ef48675c3f3b`)** | `#c7dbff` | `var(--token-9711da88-e2ac-4365-a65b-ef48675c3f3b)` in `:root` |
| **Variable Token (`--token-1f3054c2-a968-4818-ae15-ed9f1e78b6d9`)** | `#e1f5fa` | `var(--token-1f3054c2-a968-4818-ae15-ed9f1e78b6d9)` in `:root` |
| **Variable Token (`--token-ec921a20-8685-4652-8a21-8eb46519c519`)** | `#f7f7f7` | `var(--token-ec921a20-8685-4652-8a21-8eb46519c519)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-c5f3a181-ce4f-4420-a296-873f4d681873` | `#fff0` | Color / Atmospheric Token |
| `--token-f50d19c8-b71c-4ab6-8ff6-6267c86824d4` | `#071331` | Color / Atmospheric Token |
| `--token-f4cc4358-9285-4b73-95d1-a84a305a5e4c` | `#2c2c2c` | Color / Atmospheric Token |
| `--token-019ac301-73c6-46eb-9851-3eb602913d3e` | `#9aa0b0` | Color / Atmospheric Token |
| `--token-88c94126-8d08-4d70-ad93-089fe72c39c1` | `#1261eb` | Color / Atmospheric Token |
| `--token-7188acac-d059-4734-8660-0335540563b7` | `#000` | Color / Atmospheric Token |
| `--token-dcec509e-a65c-4559-bb8f-57a34c587571` | `#fff` | Color / Atmospheric Token |
| `--token-44c50bb1-0df2-493f-9bd1-8c00c0158dcb` | `#071331` | Color / Atmospheric Token |
| `--token-6051c877-d0ec-4b68-8d57-1bfdb02b909c` | `#ffe6b8` | Color / Atmospheric Token |
| `--token-9eb2db68-5dd1-49a4-b3f4-b9acc27e81e7` | `#bdffea` | Color / Atmospheric Token |
| `--token-b6e57dc6-83ba-4f1b-bdf7-3940ef910fb9` | `#deffad` | Color / Atmospheric Token |
| `--token-da636760-7871-4b98-bdd9-6abbce729e64` | `#f0e3fc` | Color / Atmospheric Token |
| `--token-9711da88-e2ac-4365-a65b-ef48675c3f3b` | `#c7dbff` | Color / Atmospheric Token |
| `--token-9474cd41-b035-4b11-aa31-8dd01bab53fe` | `#141414` | Color / Atmospheric Token |
| `--token-1f3054c2-a968-4818-ae15-ed9f1e78b6d9` | `#e1f5fa` | Color / Atmospheric Token |
| `--token-ec921a20-8685-4652-8a21-8eb46519c519` | `#f7f7f7` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.jlp-fnav> — `jimo-ai_product-ai`)**:
   - Landmark `<header class="jlp-fnav jlp-btn-dark">` (`1440px`) hosting `AI Agent for User Onboarding in SaaS` navigation (`Products · Use Case · Pricing · Customers · Resources`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.is-open { background-color:ffffff1c!important }`.
2. **Hero Stage & Focal Lead (<section.text-center> — `An agent in your SaaS that makes a`)**:
   - Landmark `<section class="text-center relative">` presenting display lead `An agent in your SaaS that makes adoption skyrock...` and copy excerpt *"Jimo Agent sees your interface, and becomes a tutor for your user"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `One agent. Three modes .`)**:
   - Landmark `<section class="relative">` rendering section `One agent. Three modes .` with copy *"Every user gets a guide"*, asset references (`5c285b27cdda1fe8-s.p.0yo6-5yoeeud...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `gt-walsheim-medium.ttf`, `gt-walsheim-regular.ttf`), and grid rule `hover { transform:scale(1.05);background-color:99eefe!important }`.
4. **Interactive Detail & Feature Matrix (<section.relative:nth(2)> — `Guides users on the fly`)**:
   - Landmark `<section class="relative">` framing `Guides users on the fly` and `Answers contextual questions` (*"Help your users convert with a personal guide."*) with `#16254f` surface cards, `#2b7fff` accents, and `active { transform:scale(.98) }`.
5. **Colophon & Global Directory Footer (<footer.footer-module__d_pQKq__root> — `https://jimo.ai/product/ai`)**:
   - Landmark `<footer class="footer-module__d_pQKq__root">` anchoring `AI Agent for User Onboarding in ` footer links (`Products · Use Case · Pricing · Customers · Resources`), copy *"Help your users convert"*, and `#141414` structural dividers.
