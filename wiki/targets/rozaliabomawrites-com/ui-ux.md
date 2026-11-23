---
title: "UI & UX Architecture: rozaliabomawrites-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: rozaliabomawrites-com

## Overview & Design Identity
- **Target**: `rozaliabomawrites-com` (**Rozalia Boma — Multicultural Romance Author**)
- **Production URL**: [https://rozaliabomawrites.com/](https://rozaliabomawrites.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5dafb` / `#ffcc00`)
- **Summary**: Official site of Rozalia Boma, author of multicultural YA romance. Books, diary entries, guestbook and newsletter.
- **Total Clean CSS Variables Extracted**: `270` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Knewave`
- **Body Font Stack**: `Plus Jakarta Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 96px`, `line-height: 96px`, `font-weight: 400`, `letter-spacing: -1.92px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 93.9404px`, `line-height: 89.2434px`, `font-weight: 400`, `letter-spacing: 0.939404px`); rule `h2` (`letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`line-height: 1.65`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5dafb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#491237` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--normal-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ffcc00` | `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }` |
| **Secondary / Muted Copy** | `#fa3899` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5e7eb` | `:after { border-color: #e5e7eb }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `290 80% 92%` | Canvas / Surface Token |
| `--foreground` | `320 60% 18%` | Typography Ink Token |
| `--card` | `0 0% 100%` | Dimension / Scale Token |
| `--card-foreground` | `320 60% 18%` | Typography Ink Token |
| `--popover` | `0 0% 100%` | Dimension / Scale Token |
| `--popover-foreground` | `320 60% 18%` | Typography Ink Token |
| `--primary` | `330 95% 60%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |
| `--secondary` | `280 85% 78%` | Brand / Palette Token |
| `--secondary-foreground` | `320 60% 18%` | Typography Ink Token |
| `--muted` | `320 60% 95%` | Dimension / Scale Token |
| `--muted-foreground` | `320 25% 45%` | Typography Ink Token |
| `--accent` | `195 90% 75%` | Brand / Palette Token |
| `--accent-foreground` | `320 60% 18%` | Typography Ink Token |
| `--destructive` | `0 84% 60%` | Dimension / Scale Token |
| `--destructive-foreground` | `0 0% 100%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.top-0> — `rozaliabomawrites-com`)**:
   - Landmark `<nav class="top-0 left-0">` (`1440x68px`) hosting `Rozalia Boma — Multicultural Romance` navigation (`Home · Author · Books · Blog · Guestbook`), DOM attributes (`data-artifact-kind="dwl_content_hash"`, `data-artifact-id="db5c4db312500dfaed9e3..."`, `data-commit-sha="37366776bd44c18a989e4..."`, `data-context-token="v1.eyJwcm9qZWN0X2lkIj..."`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Rozalia Boma — writing multicultur`)**:
   - Landmark `<section class="fixed">` presenting display lead `Rozalia Boma — writing multicultural romances` and copy excerpt *"I'm Polish Nigerian, soon moving out of Hong Kong to go back to L"* over `#f5dafb` canvas and `#491237` ink.
3. **Primary Showcase & Content Grid (<section.overflow-x-clip> — `I'm Polish Nigerian, soon moving o`)**:
   - Landmark `<section class="overflow-x-clip overflow-y-visible">` rendering section `I'm Polish Nigerian, soon moving out of Hong Kon` with copy *"Beware! Black Eastern European baddies on the rise!"*, asset references (`holo-sky-bg-C4iYYOxV.webp`, `fonts.googleapis.com`, `fonts.gstatic.com`, `sykz-yx0lLcxQaSIhS23-w.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-24> — `Beware! Black Eastern European bad`)**:
   - Landmark `<section class="py-24 relative">` framing `Beware! Black Eastern European baddies on the ri` and `w r i t i n g m u l t i c u l t u r a l` (*"w r i t i n g m u l t i c u l t u r a l"*) with `#ffffff` surface cards, `#ffcc00` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mt-8> — `https://rozaliabomawrites.com/`)**:
   - Landmark `<footer class="mt-8 relative">` anchoring `Rozalia Boma — Multicultural Rom` footer links (`Home · Author · Books · Blog · Guestbook`), copy *"m u l t i c u l t u r a l"*, and `#e5e7eb` structural dividers.
