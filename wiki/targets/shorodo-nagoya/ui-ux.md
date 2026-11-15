# UI & UX Architecture: shorodo-nagoya

## Overview & Design Identity
- **Target**: `shorodo-nagoya` (**松露堂 — 手の中の温度 · 明治十年創業・名古屋 円頓寺の和菓子処**)
- **Production URL**: [https://shorodo.nagoya/](https://shorodo.nagoya/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#c8834a`)
- **Summary**: 明治十年（1877年）創業、名古屋・円頓寺本町商店街の御菓子処 松露堂。季節であんこの硬さを変え、すり蜜の熱を炭火と手で計る——看板の松露糖と、一枚ずつ手焼きする金鯱きんつば。
- **Total Clean CSS Variables Extracted**: `21` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Shorodo Mincho`
- **Body Font Stack**: `Shorodo Cormorant`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.8rem`, `1rem`, `.58rem`, `.66rem`, `1.65rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: .72rem`, `letter-spacing: .4em`, `font-weight: 500`)
- **Body Copy**: rule `body` (`line-height: 2.1`, `letter-spacing: .05em`)
- **Metadata & Labels**: rule `small` (`font-size: .58rem`, `letter-spacing: .34em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0d0d` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#16100b` | `var(--koge)` in `:root` |
| **Elevated Surface / Card Substrate** | `#8b5a2b` | `var(--copper)` in `:root` |
| **Interactive Accent / Highlight** | `#c8834a` | `var(--copper-hi)` in `:root` |
| **Secondary / Muted Copy** | `#fcfbf7` | `var(--ivory)` in `:root` |
| **Structural Hairline Border** | `#f3efe6` | `var(--washi)` in `:root` |
| **Variable Token (`--sumi`)** | `#231f1c` | `var(--sumi)` in `:root` |
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
   - Landmark `<nav class="chrome__nav">` hosting `松露堂 — 手の中の温度 · 明治十年創業・名古屋 円頓寺の和菓子処` navigation (`品書き · 御案内 · EN`), DOM attributes (`data-dur="9.5"`, `data-amp="18"`, `data-delay="0"`, `data-dur="8.0"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `手の中の温度 手 の 中 の 温 度`)**:
   - Landmark `<section class="hero">` presenting display lead `手の中の温度 手 の 中 の 温 度` and copy excerpt *"松露堂 SHORODO — SINCE 1877 / 名古屋 円頓寺本町 （頁の初めへ）"* over `#0d0d0d` canvas and `#fcfbf7` ink.
3. **Primary Showcase & Content Grid (<section.chapter> — `帳場 HISTORY`)**:
   - Landmark `<section class="chapter history">` rendering section `帳場 HISTORY` with copy *"このページは「手の中の温度」を主題に、炭火・銅板・すり蜜・手のひらと、章が進むごとに温度が下がっていく構成でお店を紹介します。"*, asset references (`en.html`, `tw.html`, `cn.html`, `logo_shouten.png`), and grid rule `html.lenis { height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.news> — `お知らせ NEWS`)**:
   - Landmark `<section class="news">` framing `お知らせ NEWS` and `町 ENDOJI` (*"銅鍋のすり蜜に、あん玉をくぐらせる手元"*) with `#8b5a2b` surface cards, `#c8834a` accents, and `.lenis.lenis-smooth { scroll-behavior:auto }`.
5. **Colophon & Global Directory Footer (<footer.matsuba> — `https://shorodo.nagoya/`)**:
   - Landmark `<footer class="matsuba">` anchoring `松露堂 — 手の中の温度 · 明治十年創業・名古屋 円頓寺の和菓` footer links (`品書き · 御案内 · EN`), copy *"THE TEMPERATURE IN THE HAND"*, and `#f3efe6` structural dividers.
