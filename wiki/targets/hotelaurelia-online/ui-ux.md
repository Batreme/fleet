# UI & UX Architecture: hotelaurelia-online

## Overview & Design Identity
- **Target**: `hotelaurelia-online` (**Villa Aurelia — Butik Lüks Otel & Rezervasyon**)
- **Production URL**: [https://hotelaurelia.online/](https://hotelaurelia.online/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6efe5` canvas, `#1f1a15` ink, `#8a7d6c` accent)
- **Summary**: Villa Aurelia; sakin, sinematik bir kaçamak olarak tasarlanmış butik lüks otel. Odalar, gastronomi, deneyimler, düğünler ve doğrudan reze...
- **Total Clean CSS Variables Extracted**: `86` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Berlingske Serif`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Body Copy**: rule `,body` (`font-weight: 300`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f6efe5` | `var(--lume-bone)` in `:root` |
| **Primary Typography Ink** | `#ede4d3` | `var(--lume-cream)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1f1a15` | `var(--lume-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#8a7d6c` | `var(--lume-mute)` in `:root` |
| **Secondary / Muted Copy** | `#b78a6b` | `var(--lume-rose)` in `:root` |
| **Structural Hairline Border** | `#f5f0e4` | `var(--au-cream)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `36 30% 96%` | Canvas / Surface Token |
| `--foreground` | `210 20% 18%` | Typography Ink Token |
| `--card` | `36 30% 98%` | Dimension / Scale Token |
| `--card-foreground` | `210 20% 18%` | Typography Ink Token |
| `--popover` | `36 30% 96%` | Dimension / Scale Token |
| `--popover-foreground` | `210 20% 18%` | Typography Ink Token |
| `--primary` | `200 55% 48%` | Brand / Palette Token |
| `--primary-foreground` | `36 30% 98%` | Typography Ink Token |
| `--secondary` | `36 22% 90%` | Brand / Palette Token |
| `--secondary-foreground` | `210 20% 18%` | Typography Ink Token |
| `--muted` | `36 18% 92%` | Dimension / Scale Token |
| `--muted-foreground` | `210 12% 42%` | Typography Ink Token |
| `--accent` | `38 55% 58%` | Brand / Palette Token |
| `--accent-foreground` | `210 20% 18%` | Typography Ink Token |
| `--destructive` | `0 60% 50%` | Dimension / Scale Token |
| `--destructive-foreground` | `36 30% 98%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `hotelaurelia-online`)**:
   - Landmark `<header class="fixed top-0">` hosting `Villa Aurelia — Butik Lüks Otel & Re` navigation (`ODALAR · GASTRONOMİ · DENEYİMLER · JOURNAL`), DOM attributes (`data-artifact-kind="dwl_content_hash"`, `data-artifact-id="b530ed7030d66d8b94f08..."`, `data-commit-sha="8f86fc78813222994402b..."`, `data-context-token="v1.eyJwcm9qZWN0X2lkIj..."`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.rune-revealed> — `L a d o l c e v i t a`)**:
   - Landmark `<section class="rune-revealed rune-reveal-up">` presenting display lead `L a d o l c e v i t a` and copy excerpt *"Yaz Sezonu Yaz Nisan – Ekim"* over `#f6efe5` canvas and `#1f1a15` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Özenle işlenmiş, titizlikle tasarl`)**:
   - Landmark `<section class="relative h-screen">` rendering section `Özenle işlenmiş, titizlikle tasarlanmış.` with copy *"Kış Sezonu Kış Kasım – Mart"*, asset references (`favicon.png`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.au-about-reveal> — `Dinlenmek ve huzur bulmak için ide`)**:
   - Landmark `<section class="au-about-reveal relative">` framing `Dinlenmek ve huzur bulmak için ideal yer` and `Süit` (*"titizlikle tasarlanmış."*) with `#1f1a15` surface cards, `#8a7d6c` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://hotelaurelia.online/`)**:
   - Landmark `<footer class="relative overflow-hidden">` anchoring `Villa Aurelia — Butik Lüks Otel ` footer links (`ODALAR · GASTRONOMİ · DENEYİMLER · JOURNAL`), copy *"Villa Aurelia; mimariye, ışığa ve orada yaşanan hayata duyul"*, and `#f5f0e4` structural dividers.
