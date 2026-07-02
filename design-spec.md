# JoyAI-Sim Landing Page Design Spec

> Visual standard reference: Apple Product Page, Linear.app, OpenAI, Google

---

## Overall Style

- Modern minimalism
- Lots of whitespace, breathing room
- Large typography
- Soft shadows, very subtle gradients
- No heavy borders
- No enterprise dashboard / cloud platform aesthetics
- No dense layouts, no AI-generated generic cards

---

## Canvas

| Property | Value |
|----------|-------|
| Background | `#FAFBFD` |
| Max content width | 1440px |
| Grid | 12-column |
| Section spacing | 140px |
| Content padding | 120px desktop / 32px tablet / 20px mobile |

---

## Typography

Font: **Inter** or **SF Pro Display**

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Hero Title | 72px | 800 | Line Height 1.05 |
| Subtitle | 22px | 400 | Color #475569, Max Width 620px |
| Section Title | 52px | 700 | |
| Body | 18px | - | Line Height 1.7, Color #64748B |
| Metric Numbers | 42px | 700 | |

- Never use long paragraphs
- Every paragraph < 3 lines

---

## Color System

| Role | Value |
|------|-------|
| Primary | `#2563EB` |
| Hover | `#1D4ED8` |
| Dark | `#0F172A` |
| Secondary Text | `#64748B` |
| Background | `#F8FAFC` |
| Card Background | `#FFFFFF` |
| Border | `rgba(15,23,42,0.06)` |

- No saturated gradients
- If gradients used: White → Blue, opacity < 8%

---

## Shadows

| Element | Shadow |
|---------|--------|
| Cards | `0 12px 40px rgba(15,23,42,0.06)` |
| Hover | `0 20px 60px rgba(15,23,42,0.12)` |

No dark shadows.

---

## Border Radius

| Element | Radius |
|---------|--------|
| Hero Image | 32px |
| Cards | 24px |
| Buttons | 16px |
| Metric Cards | 20px |

---

## Motion Design

- Hero robot: slow breathing animation
- Cards: hover lift 4px
- Buttons: glow on hover
- Metric numbers: count-up animation
- Video: parallax
- Mouse: smooth scrolling
- Nothing should feel static

---

## Design Principles

1. Every section answers one question
2. Hero: "Can I beat AI?" → Why is it fun? → How does it work? → How good is the tech? → Start playing
3. Always design for **curiosity before explanation**
4. Prioritize emotion, visual storytelling, and gameplay over feature explanation
5. The page should make users want to click "Start Challenge" within 5 seconds

---

## Anti-patterns

- No traditional company homepage feel
- No documentation website feel
- No Alibaba Cloud / Huawei Cloud aesthetics
- No dense feature grids
- No corporate CTA banners
