---
title: "UI & Design System: kohenavocats-com_avocats-droit-famille-paris"
date: 2026-11-14
target: "[[overview|kohenavocats-com_avocats-droit-famille-paris]]"
---

# UI Architecture & Design Tokens: kohenavocats-com_avocats-droit-famille-paris

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--e-contact-buttons-size-small` | `48px` |
| `--e-contact-buttons-size-medium` | `56px` |
| `--e-contact-buttons-size-large` | `64px` |
| `--e-contact-buttons-svg-size-small` | `24px` |
| `--e-contact-buttons-svg-size-medium` | `28px` |
| `--e-contact-buttons-svg-size-large` | `32px` |
| `--e-contact-buttons-transition-duration` | `.3s` |
| `--e-contact-buttons-transition` | `all var(--e-contact-buttons-transition-duration)` |
| `--e-contact-buttons-overlap-margin` | `-10px` |
| `--e-contact-buttons-chat-button-padding-block-end` | `8px` |
| `--e-contact-buttons-chat-button-padding-block-start` | `8px` |
| `--e-contact-buttons-chat-button-padding-inline-end` | `16px` |
| `--e-contact-buttons-chat-button-padding-inline-start` | `16px` |
| `--display` | `flex` |
| `--flex-direction` | `column` |
| `--container-widget-width` | `100%` |
| `--container-widget-height` | `initial` |
| `--container-widget-flex-grow` | `0` |
| `--container-widget-align-self` | `initial` |
| `--flex-wrap-mobile` | `wrap` |
| `--display` | `flex` |
| `--flex-direction` | `column` |
| `--container-widget-width` | `100%` |
| `--container-widget-height` | `initial` |
| `--container-widget-flex-grow` | `0` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--poin` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<nav>` | `-` | `elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--poin` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<nav>` | `-` | `hk-footer-seo-scroll` |
| `<nav>` | `-` | `km-grid` |
| `<header>` | `-` | `elementor elementor-25177 elementor-location-header` |
| `<header>` | `-` | `elementor-element elementor-element-3572e1c4 e-con-full navo e-flex e-con e-parent e-lazyloaded elem` |
| `<header>` | `-` | `elementor-element elementor-element-3572e1c4 e-con-full navo e-flex e-con e-parent e-lazyloaded elem` |
| `<header>` | `-` | `kohen-avis-panel-header` |
| `<header>` | `-` | `kfh-form-heading` |
| `<header>` | `kohen12-header` | `` |
| `<main>` | `content` | `site-main post-31901 page type-page status-publish has-post-thumbnail hentry` |
| `<footer>` | `-` | `kohen-avis-panel-footer` |
