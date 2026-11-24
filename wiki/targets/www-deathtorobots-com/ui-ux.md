---
title: "UI & UX Architecture: www-deathtorobots-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-deathtorobots-com

## Overview & Design Identity
- **Target**: `www-deathtorobots-com` (**Death to Robots**)
- **Production URL**: [https://www.deathtorobots.com/](https://www.deathtorobots.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#18181c` canvas, `#facfd7` ink, `#0000ee` accent)
- **Summary**: Death To Robots is a multi disciplinary creative agency working with brands to bring their stories to life.
- **Total Clean CSS Variables Extracted**: `31` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Display`
- **Body Font Stack**: `Libre Caslon Text`
- **Monospace / Technical Font Stack**: `Fragment Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 72px`, `font-weight: 500`, `letter-spacing: -2.16px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 62px`, `line-height: 68.2px`, `font-weight: 400`, `letter-spacing: -2.48px`); rule `h2` (`font-size: 62px`, `line-height: 110%`, `letter-spacing: -.04em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 15px`, `line-height: 120%`, `letter-spacing: -.04em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#18181c` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#facfd7` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffd4e7` | `var(--border-color)` in `:root` (`var(--token-908df3da-acb6-4887-9b...`) |
| **Variable Token (`--token-dacee660-a67c-4051-becf-4db07353f7b4`)** | `#c99a99` | `var(--token-dacee660-a67c-4051-becf-4db07353f7b4)` in `:root` |
| **Variable Token (`--token-95cae479-a51e-4b73-bdc7-90fa75ba5517`)** | `#e6f3f7` | `var(--token-95cae479-a51e-4b73-bdc7-90fa75ba5517)` in `:root` |
| **Variable Token (`--token-35498dc0-e879-4403-885a-88dac352d8b5`)** | `#f4f0f1` | `var(--token-35498dc0-e879-4403-885a-88dac352d8b5)` in `:root` |
| **Variable Token (`--token-fc6d5ea3-c283-4bf2-b7f4-8555ae2b42a3`)** | `#09090a` | `var(--token-fc6d5ea3-c283-4bf2-b7f4-8555ae2b42a3)` in `:root` |
| **Variable Token (`--token-16de7c3c-1de6-4c69-bb44-67f15599c539`)** | `#ffffff` | `var(--token-16de7c3c-1de6-4c69-bb44-67f15599c539)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-908df3da-acb6-4887-9bd8-cb0ea958bbbc` | `#facfd7` | Color / Atmospheric Token |
| `--token-dacee660-a67c-4051-becf-4db07353f7b4` | `#c99a99` | Color / Atmospheric Token |
| `--token-95cae479-a51e-4b73-bdc7-90fa75ba5517` | `#e6f3f7` | Color / Atmospheric Token |
| `--token-35498dc0-e879-4403-885a-88dac352d8b5` | `#f4f0f1` | Color / Atmospheric Token |
| `--token-6194d64f-9929-472b-87b8-3361a2342d68` | `#18181c` | Color / Atmospheric Token |
| `--token-fc6d5ea3-c283-4bf2-b7f4-8555ae2b42a3` | `#09090a` | Color / Atmospheric Token |
| `--token-16de7c3c-1de6-4c69-bb44-67f15599c539` | `#fff` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.framer-cZUYc> — `www-deathtorobots-com`)**:
   - Landmark `<header class="framer-cZUYc">` (`1440px`) hosting `Death to Robots` navigation (`View project · Privacy Policy`), DOM attributes (`data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`, `data-fid="6850ab2d3e85af3c59772..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.framer-40HKB> — `CREATIVITY WITH THE HUMAN TOUCH`)**:
   - Landmark `<section class="framer-40HKB">` presenting display lead `CREATIVITY WITH THE HUMAN TOUCH` and copy excerpt *"Said the human to the robot. And the robot was sad. For it knew t"* over `#18181c` canvas and `#facfd7` ink.
3. **Primary Showcase & Content Grid (<section.framer-MvPmZ> — `Said the human to the robot. And t`)**:
   - Landmark `<section class="framer-MvPmZ">` rendering section `Said the human to the robot. And the robot was s` with copy *"We are seasoned individuals. Marketing aficionados driven by our "*, asset references (`C3gIWFd95Sm9nRAlHsGFIAHc.png`, `9ElfLHgpoirQvFUBxVdBZSXBbY.png`, `fonts.gstatic.com`, `script`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<section.framer-JsaAU> — `We are seasoned individuals. Marke`)**:
   - Landmark `<section class="framer-JsaAU">` framing `We are seasoned individuals. Marketing aficionad` and `Each cohort operates under the direction of a se` (*"Each cohort operates under the direction of a senior partner. Our"*) with `#000000` surface cards, `#0000ee` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-owpXO> — `https://www.deathtorobots.com/`)**:
   - Landmark `<footer class="framer-owpXO">` anchoring `Death to Robots` footer links (`View project · Privacy Policy`), copy *"Relationship + Insight + Creativity = Results with Purpose"*, and `#ffd4e7` structural dividers.
