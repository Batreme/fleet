# UI & UX Architecture: jimo-ai_product-ai

## Overview & Design Identity
- **Target**: `jimo-ai_product-ai` (**AI Agent for User Onboarding in SaaS · Jimo**)
- **Production URL**: [https://jimo.ai/product/ai](https://jimo.ai/product/ai)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#7ab1fe` / `#171717`)
- **Summary**: Jimo's Adoption Agent lives inside your SaaS. It guides users step by step, answers questions from your docs, and takes actions for them....
- **Total Clean CSS Variables Extracted**: `317` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--code)`, `11px`, `13px`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--code)`, `11px`, `13px`, `14px`)
- **Body Copy**: rule `p` (`font-size: 32px`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 12px`, `line-height: 16px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7ab1fe` | `var(--acc)` in `:root` |
| **Primary Typography Ink** | `#9cc0ff` | `var(--acc-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2b7fff` | `var(--blue)` in `:root` |
| **Interactive Accent / Highlight** | `#171717` | `var(--color-neutral-900)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--color-black)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--color-white)` in `:root` |
| **Variable Token (`--hair`)** | `#ffffff14` | `var(--hair)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--draw` | `cubic-bezier(.65, 0, .35, 1)` | Motion / Timing Token |
| `--glide` | `cubic-bezier(.32, .72, 0, 1)` | Motion / Timing Token |
| `--acc` | `#7ab1fe` | Color / Atmospheric Token |
| `--acc-text` | `#9cc0ff` | Typography Ink Token |
| `--blue` | `#2b7fff` | Color / Atmospheric Token |
| `--hair` | `#ffffff14` | Color / Atmospheric Token |
| `--pad` | `40px` | Layout / Spatial Grid Token |
| `--card-w` | `480px` | Dimension / Scale Token |
| `--code` | `13px` | Dimension / Scale Token |
| `--peek` | `45px` | Dimension / Scale Token |
| `--lift` | `0px` | Dimension / Scale Token |
| `--sc` | `.93` | Design System Custom Token |
| `--nd` | `.12s` | Motion / Timing Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-jlp` | `"DM Sans", "DM Sans Fallback"` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.jlp-fnav> — `jimo-ai_product-ai`)**:
   - Landmark `<header class="jlp-fnav jlp-btn-dark">` hosting `AI Agent for User Onboarding in SaaS` navigation (`Products · Use Case · Pricing · Customers · Resources`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `ento-sdk-module__RcAs1W__root.is-... { opacity:1;pointer-events:auto }`.
2. **Hero Stage & Focal Lead (<section.relative> — `An agent in your SaaS that makes a`)**:
   - Landmark `<section class="relative z-20">` presenting display lead `An agent in your SaaS that makes adoption skyrock...` and copy excerpt *"Adoption Agent New Guides, answers and acts in your product"* over `#7ab1fe` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `One agent. Three modes .`)**:
   - Landmark `<section class="relative">` rendering section `One agent. Three modes .` with copy *"Adoption Agent New"*, asset references (`5c285b27cdda1fe8-s.p.0yo6-5yoeeud...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `gt-walsheim-medium.ttf`, `gt-walsheim-regular.ttf`), and grid rule `.bento-sdk-module__RcAs1W__scene { transform-origin:0 0;width:100%;height:100%;position:absolute;top:0;left... }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Guides users on the fly`)**:
   - Landmark `<section class="relative">` framing `Guides users on the fly` and `Answers contextual questions` (*"Guides, answers and acts in your product"*) with `#2b7fff` surface cards, `#171717` accents, and `.bento-sdk-module__RcAs1W__frame { --pad:24px;--card-w:440px;--code:12px;--w:330px }`.
5. **Colophon & Global Directory Footer (<footer.footer-module__d_pQKq__root> — `https://jimo.ai/product/ai`)**:
   - Landmark `<footer class="footer-module__d_pQKq__root">` anchoring `AI Agent for User Onboarding in ` footer links (`Products · Use Case · Pricing · Customers · Resources`), copy *"Interface knowledge"*, and `#fff` structural dividers.
