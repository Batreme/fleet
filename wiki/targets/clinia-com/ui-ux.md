---
title: "UI & Design System: clinia-com"
date: 2026-11-14
target: "[[overview|clinia-com]]"
---

# UI Architecture & Design Tokens: clinia-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--color-transparent` | `transparent` |
| `--color-current` | `currentColor` |
| `--color-black` | `#000` |
| `--color-white` | `#fff` |
| `--color-primary` | `#1a1a1e` |
| `--color-secondary` | `#ff5c00` |
| `--color-body` | `light-dark(color-mix(in srgb,currentColor,transparent 50%),c` |
| `--color-vital` | `#ff5c00` |
| `--color-noble` | `#cca44f` |
| `--color-trust` | `#95795c` |
| `--color-trust-dark` | `#53402c` |
| `--color-remedy` | `#fcf8ef` |
| `--color-remedy-dark` | `#ecd9b9` |
| `--color-remedy-medium` | `#f2eee5` |
| `--color-remedy-light` | `#f9f7f2` |
| `--color-aura` | `#f7f1ff` |
| `--color-aura-dark` | `#cabbdb` |
| `--color-mend` | `#ffccaf` |
| `--color-mend-light` | `#ffe4d3` |
| `--color-thistle` | `#e3daed` |
| `--color-peach` | `#f1e0cb` |
| `--gray-50` | `rgba(0,0,0,.051)` |
| `--gray-100` | `rgba(0,0,0,.102)` |
| `--gray-500` | `rgba(0,0,0,.502)` |
| `--gray-700` | `#2f2f34` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `nav-main` | `site-header__nav position-relative d-none d-xl-block pointer-events-all justify-self-center` |
| `<nav>` | `-` | `site-header__rightNav d-flex align-items-center grid-gap-8 justify-self-end` |
| `<nav>` | `nav-main` | `site-nav__nav d-flex flex-column row-gap-30 pt-40 pb-40` |
| `<nav>` | `-` | `links-nav d-flex pb-row-hero__buttons justify-content-center justify-content-md-center justify-conte` |
| `<nav>` | `-` | `pb-row-text-medias-tabs__tabList d-none d-md-flex position-relative blossom-carousel` |
| `<nav>` | `-` | `links-nav d-flex pb-row-text-medias-tabs__buttons mt-8 mt-xl-auto --layout-mobile-horizontal --layou` |
| `<nav>` | `-` | `links-nav d-flex pb-row-text-medias-tabs__buttons mt-8 mt-xl-auto --layout-mobile-horizontal --layou` |
| `<nav>` | `-` | `links-nav d-flex pb-row-text-medias-tabs__buttons mt-8 mt-xl-auto --layout-mobile-horizontal --layou` |
| `<nav>` | `-` | `links-nav d-flex pb-row-rich-scrolling-content__buttons --layout-mobile-horizontal --layout-tablet-h` |
| `<nav>` | `-` | `links-nav d-flex pb-row-rich-scrolling-content__buttons --layout-mobile-horizontal --layout-tablet-h` |
| `<nav>` | `-` | `links-nav d-flex pb-row-certifications__buttons col-span-xl-6 col-start-md-2 col-start-xl-7 --layout` |
| `<nav>` | `-` | `links-nav d-flex pb-row-promo__buttons justify-items-center --layout-mobile-horizontal --layout-tabl` |
| `<nav>` | `-` | `social-links site-footer__socialLinks` |
| `<nav>` | `-` | `site-footer__nav col-span-md-5 col-start-md-4 col-span-xl-6 col-start-xl-7 mb-10 mb-md-0 mb-xl-60 ml` |
| `<nav>` | `-` | `site-footer__bottomNav fz-12 lh-140 col-start-xl-7 col-span-md-5 col-span-xl-4 align-self-md-center ` |
