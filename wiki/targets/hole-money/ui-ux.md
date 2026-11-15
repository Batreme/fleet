# UI & UX Architecture: hole-money

## Overview & Design Identity
- **Target**: `hole-money` (**Money Hole**)
- **Production URL**: [https://hole.money](https://hole.money)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e4e4e7` / `#afafb6`)
- **Summary**: Money Hole is a free personal finance manager for tracking income, expenses, accounts and budgets. Analytics, multi-currency support and...
- **Total Clean CSS Variables Extracted**: `63` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IBM Plex Sans`
- **Body Font Stack**: `IBM Plex Serif`
- **Monospace / Technical Font Stack**: `IBM Plex Sans`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `24px`, `22px`, `9px`, `8px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `24px`, `22px`, `9px`, `8px`)
- **Body Copy**: rule `body` (`letter-spacing: -.1px`)
- **Metadata & Labels**: rule `small` (`font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e4e4e7` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--card)` in `:root` |
| **Elevated Surface / Card Substrate** | `#18181b` | `var(--primary)` in `:root` |
| **Interactive Accent / Highlight** | `#afafb6` | `var(--grab)` in `:root` |
| **Secondary / Muted Copy** | `#d7d7db` | `var(--divider)` in `:root` |
| **Structural Hairline Border** | `#797986` | `var(--ink2)` in `:root` |
| **Variable Token (`--module`)** | `#ffffff80` | `var(--module)` in `:root` |
| **Variable Token (`--glass`)** | `#ffffff73` | `var(--glass)` in `:root` |
| **Variable Token (`--bsm`)** | `#ffffff4d` | `var(--bsm)` in `:root` |
| **Variable Token (`--shadow-btn`)** | `#0000000a` | `var(--shadow-btn)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ios` | `cubic-bezier(.32,.72,0,1)` | Motion / Timing Token |
| `--bg` | `#e4e4e7` | Canvas / Surface Token |
| `--module` | `#ffffff80` | Color / Atmospheric Token |
| `--card` | `#ffffff` | Color / Atmospheric Token |
| `--glass` | `#ffffff73` | Color / Atmospheric Token |
| `--bsm` | `#ffffff4d` | Color / Atmospheric Token |
| `--primary` | `#18181b` | Brand / Palette Token |
| `--grab` | `#afafb6` | Color / Atmospheric Token |
| `--divider` | `#d7d7db` | Color / Atmospheric Token |
| `--gstroke` | `#ffffff73` | Elevation / Border Token |
| `--shadow-btn` | `#0000000a` | Elevation / Border Token |
| `--icon-shadow` | `#0000000a` | Elevation / Border Token |
| `--ink` | `#18181b` | Typography Ink Token |
| `--ink2` | `#797986` | Typography Ink Token |
| `--inv` | `#ffffff` | Color / Atmospheric Token |
| `--ph` | `#afafb6` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.paused> — `hole-money`)**:
   - Landmark `<header class="paused">` hosting `Money Hole` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-c="0"`, `data-m="0"`, `data-s="1"`, `data-v="incT"`), and stylesheet rule `.stage { position:relative;width:432px;height:871px }`.
2. **Hero Stage & Focal Lead (<section.sl> — `Income sources`)**:
   - Landmark `<section class="sl show">` presenting display lead `Income sources` and copy excerpt *"Spending by Category"* over `#e4e4e7` canvas and `#18181b` ink.
3. **Primary Showcase & Content Grid (<section.sl> — `Accounts`)**:
   - Landmark `<section class="sl">` rendering section `Accounts` with copy *"For example, Salary to Cash, ten thousand dollars"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon.ico`), and grid rule `.device { position:absolute;left:0;top:0;width:432px;height:871px;transform-origin... }`.
4. **Interactive Detail & Feature Matrix (<section.sl> — `Expenses`)**:
   - Landmark `<section class="sl">` framing `Expenses` and `Expense category` (*"Manage Your Finance"*) with `#18181b` surface cards, `#afafb6` accents, and `.dcut { position:absolute;background:linear-gradient(817e73,c3beac);border-radiu... }`.
5. **Colophon & Global Directory Footer (<footer.dframe> — `https://hole.money`)**:
   - Landmark `<footer class="dframe">` anchoring `Money Hole` footer links (`Overview · Index · Archive · About · Contact`), copy *"– no intrusive ads or subscriptions"*, and `#797986` structural dividers.
