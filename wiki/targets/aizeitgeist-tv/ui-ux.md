---
title: "UI & UX Architecture: aizeitgeist-tv"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: aizeitgeist-tv

## Overview & Design Identity
- **Target**: `aizeitgeist-tv` (**AI Zeitgeist: AI quotes from the people shaping it**)
- **Production URL**: [https://aizeitgeist.tv](https://aizeitgeist.tv)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#00ff66`)
- **Summary**: AI quotes from the people shaping it: what researchers, founders, politicians and critics say about artificial intelligence, one quote at...
- **Total Clean CSS Variables Extracted**: `75` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Schibsted Grotesk`
- **Body Font Stack**: `Schibsted Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 46.4px`, `font-weight: 700`); rule `h1` (`font-size: clamp(1.9rem,4vw,2.6rem)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 80px`, `font-weight: 800`, `letter-spacing: -2.4px`); rule `h2` (`font-size: clamp(2.4rem,8vw,7rem)`, `line-height: 1`, `letter-spacing: -.03em`, `font-weight: 800`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`); rule `p` (`font-size: 1rem`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`); CSS variables `--av3-meta-gap: 16px`, `--av3-label-fs: clamp(1.3rem, 2.5vw, 1.7rem)`; rule `small` (`font-size: .78rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f7` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141414` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00ff66` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#00c853` | `:hover { color: #00c853 }` |
| **Structural Hairline Border** | `#222223` | `var(--line)` in `:root` (`rgb(245 245 247 / .14)`) |

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
   - Landmark `<header class="brand">` (`407x44px`) hosting `AI Zeitgeist: AI quotes from the peo` navigation (`The Wall live · What's hot 59 · Archive 2,670 · Speakers 283 · Topics 10`), DOM attributes (`data-theme="dark"`, `data-themes="off"`, `data-consent-state="ask"`, `data-archive="v3"`), and stylesheet rule `html { scroll-padding-top:var(--jump, 100px) }`.
2. **Hero Stage & Focal Lead (<section.archive> — `AI Zeitgeist: what the world says `)**:
   - Landmark `<section class="archive reveal">` presenting display lead `AI Zeitgeist: what the world says about AI, one q...` and copy excerpt *"What the world says about artificial intelligence. No commentary,"* over `#000000` canvas and `#f5f5f7` ink.
3. **Primary Showcase & Content Grid (<section.hot-home> — `The people on the wall`)**:
   - Landmark `<section class="hot-home">` rendering section `The people on the wall` with copy *"What everyone said about AI over the years containing"*, asset references (`@AIZeitgeist`, `feed.xml`, `live.json`, `sitemap.xml`), and grid rule `body { margin:0;background:var(--bg);color:var(--fg);font-family:var(--font);fo... }`.
4. **Interactive Detail & Feature Matrix (<section.people> — `Share the wall`)**:
   - Landmark `<section class="people rv-on">` framing `Share the wall` and `Follow the wall` (*"2,670 quotes Newest · Most often quoted people Clear all Play on "*) with `#141414` surface cards, `#00ff66` accents, and `.archive-count { font-variant-numeric:tabular-nums }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://aizeitgeist.tv`)**:
   - Landmark `<footer class="foot">` anchoring `AI Zeitgeist: AI quotes from the` footer links (`The Wall live · What's hot 59 · Archive 2,670 · Speakers 283 · Topics 10`), copy *"2,670 quotes Newest · Most often quoted people"*, and `#222223` structural dividers.
