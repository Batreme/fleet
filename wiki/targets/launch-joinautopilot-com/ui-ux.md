# UI & UX Architecture: launch-joinautopilot-com

## Overview & Design Identity
- **Target**: `launch-joinautopilot-com` (**Home**)
- **Production URL**: [https://launch.joinautopilot.com](https://launch.joinautopilot.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f1f2f3` / `#3cbe69`)
- **Summary**: Instant access to the world's capital. Become a Pilot and launch your first fund in minutes. Join top performers managing $1.2B+ in assets.
- **Total Clean CSS Variables Extracted**: `465` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Fkgrotesk`
- **Body Font Stack**: `clamp(.875rem`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_design-system---font-size--h1: clamp(5.75rem,4.98529rem + 3.13726vw,8.75rem)`, `--_design-system---line-height--h1: 1`, `--_design-system---font-weight--h1: 400`
- **Section Heading (`H2`)**: CSS variables `--_design-system---font-size--h2: clamp(3.5rem,3.11765rem + 1.56863vw,5rem)`, `--_design-system---line-height--h2: 1.02`, `--_design-system---font-weight--h2: 400`; rule `h2` (`font-size: var(--font-size-h3)`, `line-height: var(--line-height-h3-...`, `letter-spacing: var(--letter-spacing-...`)
- **Body Copy**: CSS variables `--_design-system---font-size--body: clamp(.875rem,.843137rem + .130719vw,1rem)`, `--_design-system---line-height--body: 1.3`, `--_design-system---font-weight--body: 400`; rule `,p` (`font-size: var(--font-size-body)`, `line-height: var(--line-height-body)`, `letter-spacing: var(--letter-spacing-...`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: CSS variables `--_design-system---letter-spacing--body: -.01em`, `--_design-system---letter-spacing--h1: -.06em`, `--_design-system---letter-spacing--h2: -.05em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1f2f3` | `var(--_design-system---color--primary-light)` in `:root` |
| **Primary Typography Ink** | `#0d0d0d` | `var(--_design-system---color--primary-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fcfcfc` | `var(--_design-system---color--surface-background)` in `:root` |
| **Interactive Accent / Highlight** | `#3cbe69` | `var(--_design-system---color--green)` in `:root` |
| **Secondary / Muted Copy** | `#141414` | `var(--_design-system---color--hover-on-light)` in `:root` |
| **Structural Hairline Border** | `#dcdde0` | `var(--_design-system---color--hover-on-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_design-system---role--bg` | `var(--_design-system---color--surface-background)` | Canvas / Surface Token |
| `--_design-system---font--primary` | `Fkgrotesk,Arial,sans-serif` | Brand / Palette Token |
| `--_design-system---role--fg` | `var(--_design-system---color--primary-dark)` | Typography Ink Token |
| `--_design-system---font-size--body` | `clamp(.875rem,.843137rem + .130719vw,1rem)` | Typography / Scale Token |
| `--_design-system---line-height--body` | `1.3` | Typography / Scale Token |
| `--_design-system---font-weight--body` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--body` | `-.01em` | Typography / Scale Token |
| `--_design-system---font-size--h1` | `clamp(5.75rem,4.98529rem + 3.13726vw,8.75rem)` | Typography / Scale Token |
| `--_design-system---line-height--h1` | `1` | Typography / Scale Token |
| `--_design-system---font-weight--h1` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--h1` | `-.06em` | Typography / Scale Token |
| `--_design-system---font-size--h2` | `clamp(3.5rem,3.11765rem + 1.56863vw,5rem)` | Typography / Scale Token |
| `--_design-system---line-height--h2` | `1.02` | Typography / Scale Token |
| `--_design-system---font-weight--h2` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--h2` | `-.05em` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header_wrap> — `launch-joinautopilot-com`)**:
   - Landmark `<header class="header_wrap">` hosting `Home` navigation (`N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`), DOM attributes (`data-wf-domain="launch.joinautopilot.com"`, `data-wf-page="6a2d51f45ce6148dcfffd71a"`, `data-wf-site="6a07168d6f6cfe1d38b6d627"`, `data-route="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.home_hero_wrap> — `A u t o p i l o t`)**:
   - Landmark `<section class="home_hero_wrap">` presenting display lead `A u t o p i l o t` and copy excerpt *"Access to main content"* over `#f1f2f3` canvas and `#0d0d0d` ink.
3. **Primary Showcase & Content Grid (<section.steps_wrap> — `T h i s i s w h e r e i t g e t s `)**:
   - Landmark `<section class="steps_wrap l-section">` rendering section `T h i s i s w h e r e i t g e t s f u n . This is...` with copy *"M e n u Menu C l o s e Close"*, asset references (`cdn.prod.website-files.com`, `ob-autopilot.shared.8ecce8ba9.min...`, `6a316c0692d4727f15940a67_favicon.png`, `6a316c0605a3b4d0e37557a7_favicon.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.billackman_wrap> — `P i c k y o u r s t o c k s . Pick`)**:
   - Landmark `<section class="billackman_wrap l-section">` framing `P i c k y o u r s t o c k s . Pick your stocks.` and `B i l l A c k m a n t o o k 1 0 y e a r s t o r a...` (*"H a l l o f F a m e Hall of Fame"*) with `#fcfcfc` surface cards, `#3cbe69` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.home_footer_wrap> — `https://launch.joinautopilot.com`)**:
   - Landmark `<footer class="home_footer_wrap l-section">` anchoring `Home` footer links (`N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`), copy *"M o n e t i z a t i o n Monetization"*, and `#dcdde0` structural dividers.
