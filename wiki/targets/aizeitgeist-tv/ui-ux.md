# UI & UX Architecture: aizeitgeist-tv

## Overview & Design Identity
- **Target**: `aizeitgeist-tv` (**AI Zeitgeist · What the world says about AI**)
- **Production URL**: [https://aizeitgeist.tv](https://aizeitgeist.tv)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#007a33`)
- **Summary**: What the world says about AI, one quote at a time. A running wall of the global conversation about artificial intelligence, updated daily.
- **Total Clean CSS Variables Extracted**: `71` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Schibsted Grotesk`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(1.9rem,4vw,2.6rem)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2.4rem,8vw,7rem)`, `line-height: 1`, `letter-spacing: -.03em`, `font-weight: 800`)
- **Body Copy**: rule `p` (`font-size: 1rem`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--av3-meta-gap: 16px`, `--av3-label-fs: clamp(1.3rem, 2.5vw, 1.7rem)`; rule `small` (`font-size: .78rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#f5f5f7` | `var(--fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#00ff66` | `var(--accent)` in `:root` |
| **Interactive Accent / Highlight** | `#007a33` | `.award:hover { color: #007a33 }` |
| **Secondary / Muted Copy** | `#101010` | `.intro-actions { background: #101010 }` |
| **Structural Hairline Border** | `#00c853` | `:hover { color: #00c853 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#000` | Canvas / Surface Token |
| `--fg` | `#f5f5f7` | Typography Ink Token |
| `--fg-2` | `rgb(245 245 247 / .62)` | Typography Ink Token |
| `--fg-3` | `rgb(245 245 247 / .5)` | Typography Ink Token |
| `--fg-4` | `rgb(245 245 247 / .36)` | Typography Ink Token |
| `--line` | `rgb(245 245 247 / .14)` | Color / Atmospheric Token |
| `--pill-line` | `rgb(245 245 247 / .3)` | Color / Atmospheric Token |
| `--sheen` | `rgb(245 245 247 / .32)` | Color / Atmospheric Token |
| `--pill-bg` | `rgb(20 20 20 / .72)` | Canvas / Surface Token |
| `--pop-bg` | `rgb(16 16 16 / .92)` | Canvas / Surface Token |
| `--kbd-line` | `rgb(245 245 247 / .28)` | Color / Atmospheric Token |
| `--kbd-bg` | `rgb(245 245 247 / .08)` | Canvas / Surface Token |
| `--accent` | `#00ff66` | Brand / Palette Token |
| `--grid-alpha` | `.075` | Layout / Spatial Grid Token |
| `--font` | `"Schibsted Grotesk", "Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--pill-h` | `60px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.brand> — `aizeitgeist-tv`)**:
   - Landmark `<header class="brand">` hosting `AI Zeitgeist · What the world says a` navigation (`The Wall live · What's hot · Archive · Speakers · Topics`), DOM attributes (`data-theme="dark"`, `data-themes="off"`, `data-consent-state="ask"`, `data-archive="v3"`), and stylesheet rule `html { scroll-padding-top:var(--jump, 100px) }`.
2. **Hero Stage & Focal Lead (<section.hero> — `AI Zeitgeist: what the world says `)**:
   - Landmark `<section class="hero">` presenting display lead `AI Zeitgeist: what the world says about AI, one q...` and copy excerpt *"What the world says about artificial intelligence. No commentary,"* over `#000` canvas and `#f5f5f7` ink.
3. **Primary Showcase & Content Grid (<article.hero-noscript> — `Can machines think?`)**:
   - Landmark `<article class="hero-noscript">` rendering section `Can machines think?` with copy *"May we count your visit with Google Analytics?"*, asset references (`@AIZeitgeist`, `feed.xml`, `live.json`, `sitemap.xml`), and grid rule `body { margin:0;background:var(--bg);color:var(--fg);font-family:var(--font);fo... }`.
4. **Interactive Detail & Feature Matrix (<section.menu-it> — `Daily by mail`)**:
   - Landmark `<section class="menu-it">` framing `Daily by mail` and `Archive` (*"No ads, no profiles. Privacy"*) with `#00ff66` surface cards, `#007a33` accents, and `.archive-count { font-variant-numeric:tabular-nums }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://aizeitgeist.tv`)**:
   - Landmark `<footer class="foot">` anchoring `AI Zeitgeist · What the world sa` footer links (`The Wall live · What's hot · Archive · Speakers · Topics`), copy *"Alan Turing, 1950. Source and context . The moving wall need"*, and `#00c853` structural dividers.
