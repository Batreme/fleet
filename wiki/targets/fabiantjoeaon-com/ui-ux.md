---
title: "UI & Design System: fabiantjoeaon-com"
date: 2026-11-14
target: "[[overview|fabiantjoeaon-com]]"
---

# UI Architecture & Design Tokens: fabiantjoeaon-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--digit-height` | `1.1em` |
| `--size` | `18px` |
| `--size` | `16px` |
| `--font-family` | `Arial, sans-serif` |
| `--font-mono` | `ui-monospace, monospace` |
| `--w-light` | `400` |
| `--w-regular` | `400` |
| `--w-book` | `400` |
| `--w-medium` | `500` |
| `--segment-reveal` | `0` |
| `--aside` | `calc(var(--project-left) - var(--page-gutter))` |
| `--main` | `var(--project-mediaWidth)` |
| `--rest` | `minmax(0, 1fr)` |
| `--next-gap` | `48px` |
| `--line-reveal` | `0` |
| `--corner` | `calc(14px * var(--line-reveal))` |
| `--page-gutter` | `clamp(20px, 3vw, 64px)` |
| `--nav-inset` | `clamp(20px, 2.1vw, 44px)` |
| `--text` | `#f3f3ef` |
| `--muted` | `#a3a6a7` |
| `--rule` | `rgba(220, 237, 239, 0.24)` |
| `--type-scale` | `0.86` |
| `--nav-font-size` | `calc(clamp(16px, 1.15vw, 24px) * var(--type-scale))` |
| `--meta-font-size` | `clamp(9.5px, 0.64vw, 12px)` |
| `--nav-line-scale` | `0` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `` |
| `<header>` | `-` | `no-webgpu-header` |
| `<main>` | `-` | `no-webgpu` |
| `<footer>` | `-` | `no-webgpu-footer` |
