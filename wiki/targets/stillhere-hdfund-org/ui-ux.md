---
title: "UI & Design System: stillhere-hdfund-org"
date: 2026-11-14
target: "[[overview|stillhere-hdfund-org]]"
---

# UI Architecture & Design Tokens: stillhere-hdfund-org

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ink` | `#101210` |
| `--paper` | `#eeeee8` |
| `--muted` | `#a8aaa1` |
| `--gold` | `#FED545` |
| `--blue` | `#2564AA` |
| `--display` | `Barlow,'Arial Narrow',Impact,sans-serif` |
| `--body` | `Inter,Arial,sans-serif` |
| `--gutter` | `7.2vw}
*{box-sizing:border-box}html{scroll-padding-top:100px` |
| `--gutter` | `10vw}.chapter-copy{width:42%}.intro-caption{top:32%}}
@media` |
| `--gutter` | `7vw}.site-header{height:84px` |
| `--n-ink` | `#111111` |
| `--n-paper` | `#F7F5F0` |
| `--n-blue` | `#2564AA` |
| `--n-yellow` | `#FED545` |
| `--n-gutter` | `clamp(26px,6.25vw,120px)}
html{scroll-padding-top:65px}body{` |
| `--n-gutter` | `7vw}
 .site-header.is-compact{height:52px` |
| `--chapter-gutter` | `var(--n-gutter)` |
| `--campaign-red` | `#BB0305}
.punctuation{color:var(--campaign-red)}
:is(#openin` |
| `--doc-paper` | `#F7F5F0}
.timeline-intro{min-height:100svh` |
| `--mobile-gutter` | `clamp(20px,6vw,48px)` |
| `--n-gutter` | `var(--mobile-gutter)` |
| `--chapter-gutter` | `var(--mobile-gutter)}
 #site-header{padding:calc(10px + env(` |
| `--archive-camera` | `1` |
| `--archive-arrival` | `1` |
| `--archive-exit` | `0` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `site-header` | `site-header` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `campaign-footer` |
