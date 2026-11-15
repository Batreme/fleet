# UI & UX Architecture: www-theboringblog-ai

## Overview & Design Identity
- **Target**: `www-theboringblog-ai` (**The Boring Blog — art, engineering and AI**)
- **Production URL**: [http://www.theboringblog.ai/](http://www.theboringblog.ai/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#f5f4ee`)
- **Summary**: Boring stuff about art, engineering, AI, and the little things that rarely make noise.
- **Total Clean CSS Variables Extracted**: `427` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Fraunces`
- **Body Font Stack**: `Fraunces Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-display-sm: 1.75rem`, `--text-display-sm--line-height: 1.15`, `--text-display-sm--letter-spacing: -.025em`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: clamp(1.7rem,5vw,2.7rem)`, `line-height: 1.06`, `letter-spacing: -.024em`, `font-weight: 400`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: 1.6`)
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-geist-mono), ui-monospace, "SF Mono", "Cascadia Code", monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`; rule `small` (`font-size: inherit`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-ink-0)` in `:root` |
| **Primary Typography Ink** | `#fcfbf6` | `var(--color-ink-25)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fafaf6` | `var(--color-ink-50)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f4ee` | `var(--color-ink-100)` in `:root` |
| **Secondary / Muted Copy** | `#eeede6` | `var(--color-ink-200)` in `:root` |
| **Structural Hairline Border** | `#e4e3db` | `var(--color-ink-300)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rail` | `calc(2px + var(--reach,0) * 2px)` | Dimension / Scale Token |
| `--walk` | `0` | Design System Custom Token |
| `--clip-to` | `inset(-.5rem round var(--radius-control))` | Dimension / Scale Token |
| `--omnibar-bar` | `0px` | Dimension / Scale Token |
| `--night` | `0` | Design System Custom Token |
| `--gold` | `0` | Design System Custom Token |
| `--font-mono` | `var(--font-geist-mono), ui-monospace, "SF Mono", "Cascadia Code", monospace` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xs` | `20rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mast> — `www-theboringblog-ai`)**:
   - Landmark `<header class="mast">` hosting `The Boring Blog — art, engineering a` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.number-demo .demo__stage { padding:calc(var(--spacing) * 6);overflow:visible }`.
2. **Hero Stage & Focal Lead (<section.hero> — `T h e n o t B o r i n g B l o g ?`)**:
   - Landmark `<section class="hero">` presenting display lead `T h e n o t B o r i n g B l o g ?` and copy excerpt *"T h e n o t B o r i n g B l o g ?"* over `#fff` canvas and `#e4e3db` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `T h e n o t B o r i n g B l o g ?`)**:
   - Landmark `<section class="hero">` rendering section `T h e n o t B o r i n g B l o g ?` with copy *"B o r i n g s t u f f a b o u t a r t , e n g i n e e r i n g , A"*, asset references (`3u9ew09158abr.css`, `331x1juguzcku.css`, `1g5rc0qzmf3ta.css`, `1l3760h_x0b06.css`), and grid rule `.number-demo .demo__frame { overflow:visible }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `B o r i n g s t u f f a b o u t a `)**:
   - Landmark `<section class="hero">` framing `B o r i n g s t u f f a b o u t a r t , e n g i ` and `e n g i n e e r i n g ,` (*"e n g i n e e r i n g ,"*) with `#fafaf6` surface cards, `#f5f4ee` accents, and `.number-demo__states { gap:calc(var(--spacing) * 6);grid-template-columns:repeat(2,minmax(0,1fr... }`.
5. **Colophon & Global Directory Footer (<footer.hero__word> — `http://www.theboringblog.ai/`)**:
   - Landmark `<footer class="hero__word">` anchoring `The Boring Blog — art, engineeri` footer links (`Overview · Index · Archive · About · Contact`), copy *"B o r i n g s t u f f a b o u t a r t , e n g i "*, and `#e4e3db` structural dividers.
