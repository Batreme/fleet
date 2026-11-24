---
title: "UI & UX Architecture: shorodo-nagoya"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: shorodo-nagoya

## Overview & Design Identity
- **Target**: `shorodo-nagoya` (**松露堂 — 手の中の温度 · 明治十年創業・名古屋 円頓寺の和菓子処**)
- **Production URL**: [https://shorodo.nagoya/](https://shorodo.nagoya/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#231f1c`)
- **Summary**: 明治十年（1877年）創業、名古屋・円頓寺本町商店街の御菓子処 松露堂。季節であんこの硬さを変え、すり蜜の熱を炭火と手で計る——看板の松露糖と、一枚ずつ手焼きする金鯱きんつば。
- **Total Clean CSS Variables Extracted**: `21` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Shorodo Mincho`
- **Body Font Stack**: `Shorodo Mincho`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 72px`, `font-weight: 500`, `letter-spacing: 15.84px`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 43.2px`, `line-height: 69.12px`, `font-weight: 500`, `letter-spacing: 8.64px`); rule `h2` (`font-size: .72rem`, `letter-spacing: .4em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 33.6px`, `font-weight: 400`, `letter-spacing: 0.8px`); rule `body` (`line-height: 2.1`, `letter-spacing: .05em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11.2px`, `line-height: 23.52px`, `font-weight: 400`, `letter-spacing: 3.808px`); rule `small` (`font-size: .58rem`, `letter-spacing: .34em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0d0d` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fcfbf7` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `#loader { background: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#231f1c` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#c8834a` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#333332` | `.rl-minor line { stroke: #333332 }` |
| **Variable Token (`--koge`)** | `#16100b` | `var(--koge)` in `:root` |
| **Variable Token (`--copper`)** | `#8b5a2b` | `var(--copper)` in `:root` |
| **Variable Token (`--washi`)** | `#f3efe6` | `var(--washi)` in `:root` |
| **Variable Token (`--enji`)** | `#7e2a2e` | `var(--enji)` in `:root` |
| **Variable Token (`--enji-hi`)** | `#a03a3c` | `var(--enji-hi)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#0d0d0d` | Canvas / Surface Token |
| `--koge` | `#16100b` | Color / Atmospheric Token |
| `--copper` | `#8b5a2b` | Color / Atmospheric Token |
| `--copper-hi` | `#c8834a` | Color / Atmospheric Token |
| `--copper-dim` | `rgba(139,90,43,.35)` | Color / Atmospheric Token |
| `--ivory` | `#fcfbf7` | Color / Atmospheric Token |
| `--ivory-70` | `rgba(252,251,247,.70)` | Color / Atmospheric Token |
| `--ivory-40` | `rgba(252,251,247,.48)` | Color / Atmospheric Token |
| `--ivory-14` | `rgba(252,251,247,.14)` | Color / Atmospheric Token |
| `--washi` | `#f3efe6` | Color / Atmospheric Token |
| `--sumi` | `#231f1c` | Color / Atmospheric Token |
| `--sumi-60` | `rgba(35,31,28,.66)` | Color / Atmospheric Token |
| `--sumi-30` | `rgba(35,31,28,.45)` | Color / Atmospheric Token |
| `--sumi-ink` | `rgba(35,31,28,.64)` | Typography Ink Token |
| `--enji` | `#7e2a2e` | Color / Atmospheric Token |
| `--enji-hi` | `#a03a3c` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.chrome__nav> — `shorodo-nagoya`)**:
   - Landmark `<nav class="chrome__nav">` (`247x24px`) hosting `松露堂 — 手の中の温度 · 明治十年創業・名古屋 円頓寺の和菓子処` navigation (`品書き · 御案内 · EN`), DOM attributes (`data-src="assets/hero_surimitsu..."`, `data-fade`, `data-cursor="計"`, `data-cursor="観"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `手の中の温度 手の中の温度`)**:
   - Landmark `<section class="hero">` presenting display lead `手の中の温度 手の中の温度` and copy excerpt *"このページは「手の中の温度」を主題に、炭火・銅板・すり蜜・手のひらと、章が進むごとに温度が下がっていく構成でお店を紹介します。"* over `#0d0d0d` canvas and `#fcfbf7` ink.
3. **Primary Showcase & Content Grid (<section.chapter> — `手の中の温度 手 の 中 の 温 度`)**:
   - Landmark `<section class="chapter history">` rendering section `手の中の温度 手 の 中 の 温 度` with copy *"銅鍋のすり蜜に、あん玉をくぐらせる手元"*, asset references (`en.html`, `tw.html`, `cn.html`, `logo_shouten.png`), and grid rule `html.lenis { height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.news> — `手仕事 PHILOSOPHY`)**:
   - Landmark `<section class="news late-in">` framing `手仕事 PHILOSOPHY` and `銘 SIGNATURE — 看板の二菓` (*"THE TEMPERATURE IN THE HAND"*) with `#000000` surface cards, `#231f1c` accents, and `.lenis.lenis-smooth { scroll-behavior:auto }`.
5. **Colophon & Global Directory Footer (<footer.hide-cursor> — `https://shorodo.nagoya/`)**:
   - Landmark `<footer class="hide-cursor">` anchoring `松露堂 — 手の中の温度 · 明治十年創業・名古屋 円頓寺の和菓` footer links (`品書き · 御案内 · EN`), copy *"明治十年、甘味処として創業。 屋号は藤鎌、 名古屋・伊勢町に暖簾を掲げました。 戦火に焼かれて円頓寺本町へ —— 砂糖の"*, and `#333332` structural dividers.
