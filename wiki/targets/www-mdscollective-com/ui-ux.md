# UI & UX Architecture: www-mdscollective-com

## Overview & Design Identity
- **Target**: `www-mdscollective-com` (**MDS Collective · China Marketing Agency for Hotels & Tourism**)
- **Production URL**: [https://www.mdscollective.com](https://www.mdscollective.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#101010` ink, `#5f5f5b` accent)
- **Summary**: Award-winning China marketing agency for luxury hotels and tourism brands. RedNote, WeChat, Douyin, KOLs and AI search. Formerly Metric D...
- **Total Clean CSS Variables Extracted**: `15` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(54px,9.8vw,156px)`, `line-height: 1.02`, `letter-spacing: -.025em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(38px,5.6vw,88px)`, `line-height: 1.02`, `letter-spacing: -.025em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 15px`)
- **Metadata & Labels**: rule `small` (`font-size: .5em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#f3f3f1` | `var(--bg2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#101010` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#5f5f5b` | `var(--ink2)` in `:root` |
| **Secondary / Muted Copy** | `#767671` | `var(--ink3)` in `:root` |
| **Structural Hairline Border** | `#8e8e89` | `var(--ink3-lg)` in `:root` |
| **Variable Token (`--rule`)** | `#a3a39e` | `var(--rule)` in `:root` |
| **Variable Token (`--line`)** | `#e3e3df` | `var(--line)` in `:root` |
| **Variable Token (`--gold`)** | `#1c486d` | `var(--gold)` in `:root` |
| **Variable Token (`--orange`)** | `#e6872d` | `var(--orange)` in `:root` |
| **Variable Token (`--hl`)** | `#e6872d52` | `var(--hl)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#fff` | Canvas / Surface Token |
| `--bg2` | `#f3f3f1` | Canvas / Surface Token |
| `--ink` | `#101010` | Typography Ink Token |
| `--ink2` | `#5f5f5b` | Typography Ink Token |
| `--ink3` | `#767671` | Typography Ink Token |
| `--ink3-lg` | `#8e8e89` | Typography Ink Token |
| `--rule` | `#a3a39e` | Color / Atmospheric Token |
| `--line` | `#e3e3df` | Color / Atmospheric Token |
| `--gold` | `#1c486d` | Color / Atmospheric Token |
| `--navy` | `#1c486d` | Layout / Spatial Grid Token |
| `--orange` | `#e6872d` | Color / Atmospheric Token |
| `--serif` | `"Instrument Serif","PS Times","Times New Roman",Georgia,serif` | Typography / Scale Token |
| `--sans` | `"Helvetica Neue",Helvetica,Arial,system-ui,sans-serif` | Typography / Scale Token |
| `--r-lg` | `24px` | Dimension / Scale Token |
| `--hl` | `#e6872d52` | Color / Atmospheric Token |
| `--www-mdscollectiv-bg` | `#fff` | Canvas Substrate (from `var(--bg)` in `:root`) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-mdscollective-com`)**:
   - Landmark `<nav class="lenis">` hosting `MDS Collective · China Marketing Age` navigation (`About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`), DOM attributes (`data-u="hello"`, `data-d="mdscollective.com"`, `data-src-sm="/video/hero-720.mp4"`, `data-src-lg="/video/hero-1080.mp4"`), and stylesheet rule `selection { color:fff;background:e6872d }`.
2. **Hero Stage & Focal Lead (<section.brand-hero> — `Luxury Marketing targeting Chinese`)**:
   - Landmark `<section class="brand-hero">` presenting display lead `Luxury Marketing targeting Chinese & East Asian T...` and copy excerpt *"Hotels & Hospitality"* over `#fff` canvas and `#101010` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `FIT travelers have evolved. AI is `)**:
   - Landmark `<section class="hero wrap">` rendering section `FIT travelers have evolved. AI is now where their...` with copy *"Airlines & Cruises"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `hero-1080.mp4`), and grid rule `body { background:var(--bg);color:var(--ink);font-family:var(--sans);margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.hero-media> — `We are your long-term East Asia ma`)**:
   - Landmark `<section class="hero-media wrap">` framing `We are your long-term East Asia marketing partner.` and `Visit Qatar` (*"Theme Parks & Entertainment"*) with `#101010` surface cards, `#5f5f5b` accents, and `html.lenis { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://www.mdscollective.com`)**:
   - Landmark `<footer class="wrap">` anchoring `MDS Collective · China Marketing` footer links (`About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`), copy *"Safaris & Tour Operators"*, and `#8e8e89` structural dividers.
