---
title: "UI & Design System: microdose-studio"
date: 2026-11-14
target: "[[overview|microdose-studio]]"
---

# UI Architecture & Design Tokens: microdose-studio

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--color-black` | `#19171b` |
| `--color-dark` | `#0c152a` |
| `--color-muted` | `#6b6c71` |
| `--color-white` | `#ffffff` |
| `--color-bg-dark` | `#121113` |
| `--color-card-bg` | `#e8e8ec` |
| `--color-blue-start` | `#1935d9` |
| `--color-blue-end` | `#2f2be2` |
| `--color-blue-border` | `#1f34c9` |
| `--color-footer-border` | `rgba(116, 84, 84, 0.15)` |
| `--color-white-50` | `rgba(255, 255, 255, 0.5)` |
| `--color-grey-cool` | `#818a94` |
| `--font-primary` | `'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans` |
| `--font-accent` | `'Metal', serif` |
| `--radius-lg` | `16px` |
| `--radius-xl` | `24px` |
| `--radius-pill` | `100px` |
| `--shadow-color-near` | `rgba(14, 15, 43, 0.08)` |
| `--shadow-color-far` | `rgba(66, 39, 92, 0.02)` |
| `--shadow-card` | `0px 1px 2px var(--shadow-color-near), 0px 43px 80px var(--sh` |
| `--shadow-blue-inset` | `inset 0px 1px 4px #2a3edc, inset 0px 4px 16px rgba(255, 255,` |
| `--shadow-dark-pill-inset` | `inset 0px 1px 0px 1px #2d2a2d` |
| `--shadow-photo-card` | `0 70px 109px -10px rgba(88, 92, 95, 0.08),
0 0 0 1px rgba(51` |
| `--color-pill-bg` | `rgba(62, 44, 62, 0.10)` |
| `--color-dark-border` | `rgba(255, 255, 255, 0.06)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav blur-fade-in nav--logo-blend` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `footer` |
