# UI & UX Architecture: www-rikoutaku-work

## Overview & Design Identity
- **Target**: `www-rikoutaku-work` (**Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio**)
- **Production URL**: [https://www.rikoutaku.work/](https://www.rikoutaku.work/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#2e3bff` / `#e9e4d8`)
- **Summary**: Rikoutaku（リコウタク）のポートフォリオサイト「RI.Studio」。東京を拠点とするインタラクション／UI・UXデザイナー。3Dスクロール体験、アプリUI、Web、AR、モーションの作品集。Interaction & UI/UX Designer based in...
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(29px,2.5vw,40px)`, `line-height: 1.36`, `letter-spacing: -.055em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(94px,10.2vw,164px)`, `line-height: .94`)
- **Body Copy**: rule `p` (`font-size: 12px`, `line-height: 1.65`, `letter-spacing: -.01em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `22px`, `clamp(64px,11.5vw,210px)`, `20px`, `clamp(54px,16vw,110px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#2e3bff` | `var(--ri-curtain-bg)` in `:root` |
| **Primary Typography Ink** | `#f0f0f7` | `var(--ri-curtain-ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0b0b0c` | `var(--bg)` in `:root` |
| **Interactive Accent / Highlight** | `#e9e4d8` | `var(--text)` in `:root` |
| **Secondary / Muted Copy** | `#2a2926` | `var(--faint)` in `:root` |
| **Structural Hairline Border** | `#ff3b24` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-2`)** | `#d92c18` | `var(--accent-2)` in `:root` |
| **Variable Token (`--circle-outline`)** | `#505050` | `var(--circle-outline)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ri-ease` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ri-ease-io` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Easing Token |
| `--ri-ease-in` | `cubic-bezier(.7, 0, .84, 0)` | Motion / Easing Token |
| `--ri-curtain-bg` | `#2e3bff` | Canvas / Surface Token |
| `--ri-curtain-ink` | `#f0f0f7` | Typography Ink Token |
| `--ri-curtain-z` | `2147483000` | Design System Custom Token |
| `--bg` | `#0b0b0c` | Canvas / Surface Token |
| `--text` | `#e9e4d8` | Typography Ink Token |
| `--dim` | `#e9e4d8` | Color / Atmospheric Token |
| `--faint` | `#2a2926` | Color / Atmospheric Token |
| `--accent` | `#ff3b24` | Brand / Palette Token |
| `--accent-2` | `#d92c18` | Brand / Palette Token |
| `--circle-outline` | `#505050` | Elevation / Border Token |
| `--ease` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ease-soft` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--pad` | `clamp(1.4rem, 2.4vw, 2.8rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c2n-header> — `www-rikoutaku-work`)**:
   - Landmark `<header class="c2n-header c2n-navigation-simple">` hosting `Rikoutaku（リコウタク）— RI.Studio · Intera` navigation (`01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`), DOM attributes (`data-composition="two"`, `data-c2n-room="hero"`, `data-engine="three.js r165"`, `data-motion-system="studio"`), and stylesheet rule `.ri-curtain { position:fixed;top:0;right:0;bottom:0;left:0;z-index:var(--ri-curtain-z)... }`.
2. **Hero Stage & Focal Lead (<section.composition-two> — `Rikoutaku（リコウタク）— RI.Studio · Inte`)**:
   - Landmark `<section class="composition-two">` presenting display lead `Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX...` and copy excerpt *"seq 001 — est.2026"* over `#2e3bff` canvas and `#f0f0f7` ink.
3. **Primary Showcase & Content Grid (<section.c2n-hero> — `技術と感性で、 記憶に残る体験を。`)**:
   - Landmark `<section class="c2n-hero">` rendering section `技術と感性で、 記憶に残る体験を。` with copy *"INDEPENDENT DESIGNERTOKYO, JAPAN I N D E P E N D E N T D E S I G "*, asset references (`favicon.svg`, `theme-boot.js`, `2026-8-10-white.glb`, `fonts.googleapis.com`), and grid rule `.ri-curtain.is-on { visibility:visible;pointer-events:auto }`.
4. **Interactive Detail & Feature Matrix (<section.c2n-thinking> — `A SPACE FOR IDEAS. A S P A C E F O`)**:
   - Landmark `<section class="c2n-thinking c2n-paper">` framing `A SPACE FOR IDEAS. A S P A C E F O R I D E A S .` and `Beyond the frame. B e y o n d t h e f r a m e . I...` (*"INDEPENDENT DESIGNERTOKYO, JAPAN"*) with `#0b0b0c` surface cards, `#e9e4d8` accents, and `.ri-curtain-shade { position:absolute;top:0;right:0;bottom:0;left:0;background:111219;transf... }`.
5. **Colophon & Global Directory Footer (<footer.c2n-contact> — `https://www.rikoutaku.work/`)**:
   - Landmark `<footer class="c2n-contact c2n-paper">` anchoring `Rikoutaku（リコウタク）— RI.Studio · In` footer links (`01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`), copy *"I N D E P E N D E N T D E S I G N E R T O K Y O , J A P A N"*, and `#ff3b24` structural dividers.
