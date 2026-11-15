# UI & UX Architecture: deathbyscroll-com

## Overview & Design Identity
- **Target**: `deathbyscroll-com` (**Death by Scroll**)
- **Production URL**: [https://deathbyscroll.com](https://deathbyscroll.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#111` / `#777`)
- **Summary**: Killer scroll animation. Perfect for product launches, microsites, and explainers. Create a cult-like devotion to your brand.
- **Total Clean CSS Variables Extracted**: `83` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aesteric`
- **Body Font Stack**: `Girthy`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-size--h1: 2.3125rem`, `--line-height--h1: 2.375rem`
- **Section Heading (`H2`)**: CSS variables `--font-size--h2: 2.5rem`, `--line-height--h2: 3rem`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.2`, `letter-spacing: 2px`, `font-weight: 600`)
- **Body Copy**: CSS variables `--typeface-body: "Setanz",serif`, `--typeface-body-bold: "Satoshi Black",sans-serif`, `--line-height--body: 1.375rem`; rule `p` (`font-size: 1rem`, `line-height: 1.25rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `1em`, `80%`, `75%`, `100%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111` | `var(--color-off-black)` in `:root` |
| **Primary Typography Ink** | `#282828` | `var(--color-medium-grey)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1e1e1e` | `var(--color-dark-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#777` | `var(--color-light-grey)` in `:root` |
| **Secondary / Muted Copy** | `#f4efed` | `var(--color-off-white)` in `:root` |
| **Structural Hairline Border** | `#e8e8e8` | `var(--color-highlight)` in `:root` |
| **Variable Token (`--color-red`)** | `#d52127` | `var(--color-red)` in `:root` |
| **Variable Token (`--color-purple`)** | `#ae5eff` | `var(--color-purple)` in `:root` |
| **Variable Token (`--color-red-muted`)** | `#ff5e5e` | `var(--color-red-muted)` in `:root` |
| **Variable Token (`--color-red-white`)** | `#fad2d2` | `var(--color-red-white)` in `:root` |
| **Variable Token (`--color-green`)** | `#4cc44c` | `var(--color-green)` in `:root` |
| **Variable Token (`--color-shadow-2`)** | `#212121` | `var(--color-shadow-2)` in `:root` |
| **Variable Token (`--color-shadow-3`)** | `#222` | `var(--color-shadow-3)` in `:root` |
| **Variable Token (`--color-brass`)** | `#f9de95` | `var(--color-brass)` in `:root` |
| **Variable Token (`--color-brass-dark`)** | `#e7b882` | `var(--color-brass-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-off-black` | `#111` | Canvas / Surface Token |
| `--color-medium-grey` | `#282828` | Brand / Palette Token |
| `--color-dark-grey` | `#1e1e1e` | Canvas / Surface Token |
| `--color-light-grey` | `#777` | Canvas / Surface Token |
| `--color-off-white` | `#f4efed` | Canvas / Surface Token |
| `--color-highlight` | `#e8e8e8` | Canvas / Surface Token |
| `--color-red` | `#d52127` | Brand / Palette Token |
| `--color-purple` | `#ae5eff` | Brand / Palette Token |
| `--color-red-rgb` | `213,33,39` | Brand / Palette Token |
| `--color-red-muted` | `#ff5e5e` | Brand / Palette Token |
| `--color-red-white` | `#fad2d2` | Canvas / Surface Token |
| `--color-green` | `#4cc44c` | Brand / Palette Token |
| `--color-shadow-2` | `#212121` | Brand / Palette Token |
| `--color-shadow-3` | `#222` | Brand / Palette Token |
| `--color-brass` | `#f9de95` | Brand / Palette Token |
| `--color-brass-dark` | `#e7b882` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.dxs-header> — `deathbyscroll-com`)**:
   - Landmark `<header class="dxs-header">` hosting `Death by Scroll` navigation (`Summon us Summon us`), DOM attributes (`data-open-accessibility="accessibility-toggle-..."`, `data-end-announce="Summon Us. The page n..."`, `data-guided="prev"`, `data-guided="playpause"`), and stylesheet rule `root { --font-size--h1:5.375rem;--font-size--h2:4rem;--line-height--h1:5.375rem... }`.
2. **Hero Stage & Focal Lead (<section.guided-player> — `Death by Scroll. Killer scroll ani`)**:
   - Landmark `<section class="guided-player">` presenting display lead `Death by Scroll. Killer scroll animation` and copy excerpt *"Accessibility options"* over `#111` canvas and `#f4efed` ink.
3. **Primary Showcase & Content Grid (<section.temple-scene> — `Scene player`)**:
   - Landmark `<section class="temple-scene">` rendering section `Scene player` with copy *"The Offering The Offering"*, asset references (`tg-girthyultra-webfont.woff2`, `Satoshi-Bold.woff2`, `styles.min.css`, `favicon.png`), and grid rule `html { -webkit-text-size-adjust:100%;line-height:1.15 }`.
4. **Interactive Detail & Feature Matrix (<section.heads-scene> — `Don't just get people's attention,`)**:
   - Landmark `<section class="heads-scene">` framing `Don't just get people's attention, get inside the...` and `Don't Don't just just get get people's people's a...` (*"Death Scrolls Death Scrolls"*) with `#1e1e1e` surface cards, `#777` accents, and `main { display:block }`.
5. **Colophon & Global Directory Footer (<footer.dxs-footer> — `https://deathbyscroll.com`)**:
   - Landmark `<footer class="dxs-footer">` anchoring `Death by Scroll` footer links (`Summon us Summon us`), copy *"Summon us Summon us"*, and `#e8e8e8` structural dividers.
