# UI & UX Architecture: www-kaviengcreative-com

## Overview & Design Identity
- **Target**: `www-kaviengcreative-com` (**Kavieng Cheng · Art Director and Creative**)
- **Production URL**: [https://www.kaviengcreative.com/](https://www.kaviengcreative.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#050505` canvas, `#f0efe9` ink, `#0a0a09` accent)
- **Summary**: Kavieng Cheng is a Hong Kong-based art director and creative working across advertising, product, fine art and photography.
- **Total Clean CSS Variables Extracted**: `10` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Heros`
- **Body Font Stack**: `Junicode`
- **Monospace / Technical Font Stack**: `Junicode`
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: -.055em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `18px`, `13px`, `11px`, `15px`)
- **Body Copy**: rule `p` (`letter-spacing: -.006em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `18px`, `13px`, `11px`, `15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#050505` | `var(--archive-black)` in `:root` |
| **Primary Typography Ink** | `#f0efe9` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c9c8c3` | `var(--page-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#0a0a09` | `var(--hard-ink)` in `:root` |
| **Secondary / Muted Copy** | `#8a8a84` | `var(--graphite)` in `:root` |
| **Structural Hairline Border** | `#aaa9a2` | `var(--silver)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--archive-black` | `#050505` | Canvas / Surface Token |
| `--paper` | `#f0efe9` | Canvas / Surface Token |
| `--page-grey` | `#c9c8c3` | Color / Atmospheric Token |
| `--hard-ink` | `#0a0a09` | Typography Ink Token |
| `--graphite` | `#8a8a84` | Color / Atmospheric Token |
| `--silver` | `#aaa9a2` | Color / Atmospheric Token |
| `--rule-dark` | `rgba(10, 10, 9, .19)` | Canvas / Surface Token |
| `--rule-light` | `rgba(240, 239, 233, .19)` | Canvas / Surface Token |
| `--gutter` | `40px` | Layout / Spatial Grid Token |
| `--perspective-blur` | `0px` | Elevation / Border Token |
| `--www-kaviengcreat-bg` | `#050505` | Canvas Substrate (from `var(--archive-black)` in `:root`) |
| `--www-kaviengcreat-ink` | `#f0efe9` | Primary Typography Ink (stylesheet-derived) |
| `--www-kaviengcreat-surface` | `#c9c8c3` | Surface Substrate (stylesheet-derived) |
| `--www-kaviengcreat-accent` | `#0a0a09` | Interactive Accent (stylesheet-derived) |
| `--www-kaviengcreat-muted` | `#8a8a84` | Secondary Ink (stylesheet-derived) |
| `--www-kaviengcreat-border` | `#aaa9a2` | Structural Border (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.archive-header> — `www-kaviengcreative-com`)**:
   - Landmark `<header class="archive-header">` hosting `Kavieng Cheng · Art Director and Cre` navigation (`Archive · About · Awards · Press · Private`), DOM attributes (`data-route="archive"`, `data-route="archive"`, `data-route="about"`, `data-route="awards"`), and stylesheet rule `app { width:100%;height:100%;margin:0;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.view-shell> — `Kavieng Cheng`)**:
   - Landmark `<section class="view-shell">` presenting display lead `Kavieng Cheng` and copy excerpt *"Art director + creative"* over `#050505` canvas and `#f0efe9` ink.
3. **Primary Showcase & Content Grid (<section.view-shell> — `Art director + creative`)**:
   - Landmark `<section class="view-shell">` rendering section `Art director + creative` with copy *"Kavieng Cheng Art director + creative"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `main-C5DSeFRy.js`), and grid rule `html { background:var(--archive-black) }`.
4. **Interactive Detail & Feature Matrix (<section.view-shell> — `Kavieng Cheng Art director + creat`)**:
   - Landmark `<section class="view-shell">` framing `Kavieng Cheng Art director + creative` and `The UN-billed Space` (*"The UN-billed Space"*) with `#c9c8c3` surface cards, `#0a0a09` accents, and `body { background:var(--archive-black);color:var(--paper);font-family:Heros,Ari... }`.
5. **Colophon & Global Directory Footer (<footer.loader__hint> — `https://www.kaviengcreative.com/`)**:
   - Landmark `<footer class="loader__hint">` anchoring `Kavieng Cheng · Art Director and` footer links (`Archive · About · Awards · Press · Private`), copy *"The Touch Annual Report"*, and `#aaa9a2` structural dividers.
