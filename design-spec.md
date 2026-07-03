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

### Primary (Brand Blue)

| Role | Value | Usage |
|------|-------|-------|
| Primary | `#2563EB` | Buttons, links, active states, brand accent |
| Primary Hover | `#1D4ED8` | Button hover, link hover |
| Primary Light BG | `#EFF6FF` | Active sidebar item bg, selected state bg |
| Primary Light Border | `#BFDBFE` / `#DBEAFE` | Highlighted tag border, blue card bg |

### Neutrals (Slate)

| Role | Value | Usage |
|------|-------|-------|
| Heading / Title | `#0F172A` | H1, H2, brand name, primary headings |
| Body Dark | `#1E293B` | Body text on light bg |
| Body Medium | `#334155` | Key labels, hint-key text |
| Body Default | `#475569` | Subtitle, hint text, secondary content |
| Body Light | `#64748B` | Paragraph text, sidebar items, muted labels |
| Muted | `#94A3B8` | Placeholder, section labels, skip note |
| Border | `#E2E8F0` | Card borders, dividers, input borders |
| Border Light | `#CBD5E1` | Hover borders, arm illustration |
| Hover BG | `#F1F5F9` | Sidebar hover, light button bg |
| Page BG | `#FAFBFD` / `#F8FAFC` | Page background |
| Card BG | `#FFFFFF` | Cards, modals, scene preview |

### Semantic

| Role | Value | Usage |
|------|-------|-------|
| Success | `#22C55E` / `#16A34A` | Success state, positive indicator |
| Success Light | `#86EFAC` / `#4ADE80` | Success bg, illustration objects |
| Warning | `#F59E0B` / `#FBBF24` | Warning badges, hook stat icon |
| Warning Dark | `#92400E` / `#B45309` | Warning text on light bg |
| Warning Light BG | `#FFF7ED` / `#FFFBEB` | Warning card bg |
| Warning Light Border | `#FED7AA` / `#FDE68A` | Warning card border |
| Error | `#DC2626` / `#EF4444` | Error state, failure indicator |
| Error Light | `#F87171` / `#FCA5A5` | Error bg, soft error |

### Decorative (Game UI)

| Role | Value | Usage |
|------|-------|-------|
| Object Blue | `#93C5FD` | Illustration object (cup) |
| Object Yellow | `#FCD34D` | Illustration object (book) |
| Object Green | `#86EFAC` | Illustration object (pen) |
| Purple Accent | `#818CF8` / `#A78BFA` | Decorative accent, chart |
| Pink Accent | `#F472B6` | Decorative accent |
| Cyan Accent | `#67E8F9` | Decorative accent |

### Usage Rules

- No saturated gradients
- If gradients used: White → Blue, opacity < 8%
- Border prefer `rgba(15,23,42,0.06)` for subtle dividers

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
