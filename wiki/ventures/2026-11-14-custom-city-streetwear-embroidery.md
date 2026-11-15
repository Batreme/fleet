---
title: "Venture: Custom-City Streetwear Embroidery Platform"
date: 2026-11-14
status: completed
tags:
  - venture
  - ecommerce
  - streetwear
  - nextjs
  - canvas
  - embroidery
outcome_summary: "Designed and built custom-city: a dark heavyweight industrial streetwear e-commerce platform featuring an interactive 2D live embroidery simulator, 3D puff relief preview, Tech Pack production sheet generator, city drops, BLIK checkout, and B2B volume pricing calculator."
---

# Venture: Custom-City Streetwear Embroidery Platform

## Context & Desired Outcome
- **Problem / Goal**: Build an authentic, dark industrial streetwear brand & shop ("custom-city") specialized in computer machine embroidery (logos, custom graphics, typography, 3D puff relief) on heavyweight garments (up to 480 GSM).
- **Target Outcome**: A production-ready Next.js application built strictly outside `/fleet` in `/root/projects/custom-city` with:
  1. Interactive 2D live embroidery customizer (garment selector, front/back perspectives, zone bounds, satin stitch texture pattern, 16 Madeira thread colors, 3D puff simulation).
  2. Tech Pack generator (exportable machine specification with dimensions in mm, needle types, stabilizer backing, and stitch counts).
  3. City Drops storefront showcasing 4 limited edition heavy pieces.
  4. Full checkout simulation featuring Polish BLIK 6-digit code validation, timer, and confetti celebration.
  5. Interactive B2B bulk tier calculator for clothing brands and crews.

## Approach Taken
- **Architecture & Isolation**: Created a standalone repository at `/root/projects/custom-city` adhering strictly to workspace boundaries, and deployed to `/app/custom-city` on the VPS.
- **Anti-AI-Slop Overhaul (Fleet Playbooks)**:
  - Applied blueprints from `[[agency-and-ecommerce-patterns]]` and `[[tech-and-experimental-patterns]]`.
  - Replaced generic SaaS card grids with an Asymmetric Split-Screen Hero (`twohalves-co` pattern) and a Floating Bottom Dock (`FloatingPillNav` from `romainavalle-dev`).
  - **Real-Time 3D WebGL Hero Garment Rack (`tech-and-experimental-patterns`)**: Upgraded the Hero right-hand obsidian viewport from CSS-perspective 2D SVGs to a full Three.js WebGL spatial substrate (`z-0`) with procedural PBR French Terry & ribbed knit textures (`bumpMap`, `roughnessMap`, `sheen`), sculpted 3D garment meshes (`hoodie`, `tshirt`, `crewneck`, `beanie`), 3D raised puff embroidery patches, `pointer-events-none` Telemetry HUD (`z-10` with corner reticles, live azimuth/FPS), and `pointer-events-auto` CAD `X-RAY` wireframe & `ORBIT` controls (`z-20`).
  - Implemented the Optical Macro Loupe (20x magnifying lens) with thread filament inspection.
  - Added Tajima 15-needle slot rack (`#01-#15`), real stitch density controls (`0.30 - 0.55 mm`), wireframe X-Ray CAD mode, and dynamic runtime/meter telemetry.
  - Applied strict 3:4 portrait aspect ratio discipline (`--aspect-ratio: .75`) on product cards with physical weight in grams, model stats, and batch remaining counters.
  - Synchronized cart state across tabs via `BroadcastChannel('custom_city_cart_sync')` (Shopify Shop JS v2 pattern).

## Challenges & Obstacles
- **ESLint no-unused-vars during Next.js production build**: Catch clauses and unused variables flagged by Next.js 15 strict linting were resolved by cleaning unused parameters and integrating state variables directly into interactive controls.
- **Realistic Embroidery Simulation**: Rendering thread sheen without heavy external 3D WebGL assets was solved using an SVG filter + patterned diagonal satin stitch lines with anisotropic lighting and ambient occlusion shadows for 3D Puff relief.
- **Image Upload Rendering & SVG Blending**: In SVG, overlaying `<rect fill="url(#patternId)" style={{ mixBlendMode: 'overlay' }}>` directly over an `<image>` tag caused dark/transparent graphics to blackout in modern rendering engines. Resolved by rendering the `<image>` with dedicated cross-browser attributes (`href` and `xlinkHref`), adding drop-shadow underlays for 3D puff relief, and providing an SVG `feColorMatrix` pipeline for dynamic Madeira thread tinting or full-color display.
- **Playwright Visual Verification & UI Collision**: Using headless Chromium via Playwright revealed that internal zone coordinate badges (`Lewa Pierś`, `100x100MM`, `3D PUFF`) were positioned directly inside the embroidery bounding box with opaque black backgrounds (`bg-[#050608]/90`), which physically obscured up to 80% of uploaded logos and images. Resolved by re-architecting the embroidery frame so that technical telemetry badges sit strictly *outside* the frame (above and below), leaving the interior 100% clean and transparent. Default zone was also updated to prominent `center_chest` (and `large_back`), giving instant large-scale visibility for custom artwork.

## Final Outcome & Artifacts
- **Repository**: Located at `/root/projects/custom-city` with clean git history (`feat: initial release of custom-city streetwear embroidery platform`).
- **Production Server**: Deployed directly on the user's VPS (`31.70.120.216`, alongside `ozaklad`) in `/app/custom-city`, managed by systemd (`custom-city.service`) on port 3000 and reverse-proxied by Nginx on port 80.
- **GitHub Repository**: Pushed and synced to `https://github.com/Batreme/custom-city`.
- **Deliverables**:
  - Live Customizer with Realtime Pricing & Canvas Embroidery Simulation.
  - Printable / Downloadable Production Tech Pack Spec Sheet.
  - City Drops #01-#04 limited catalogue.
  - Cart Slide-over & BLIK 6-digit Checkout flow.
  - Interactive B2B Volume Pricing Calculator.

## Reusable Lessons
- **Stitch Texture Simulation**: Combining SVG angled satin lines (`patternTransform="rotate(45)"`) with dual `feDropShadow` filters creates a remarkably convincing thread and 3D puff embroidery effect in pure CSS/SVG without WebGL overhead.
- **Web Audio Haptics**: Generating synthetic oscillator clicks and chimes eliminates the need for external MP3 audio asset dependencies.
- **Links to relevant playbooks**: [[agency-and-ecommerce-patterns]], [[tech-and-experimental-patterns]]
