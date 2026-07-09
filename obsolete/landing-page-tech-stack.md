# JoyAI-Sim Landing Page Tech Stack

> Visual standard reference: Apple Product Page, Linear.app, OpenAI, Google

---

## Core Framework

### 1. Next.js + React

**Purpose:**
- Website framework
- Routing
- Layout
- SEO
- Fonts
- UI Components
- Responsive design

**Why:**
Acts as the foundation of the entire website. Everything except the 3D scene lives here.

---

## 3D Rendering

### 2. React Three Fiber (R3F)

**Purpose:**
- Render the entire 3D scene
- Particle system
- Camera
- Mouse interaction
- Animation loop
- Scene management

**Why:**
React wrapper around Three.js, making complex WebGL development much easier.

---

### 3. Three.js

**Purpose:**
- WebGL rendering engine
- Camera
- Geometry
- Materials
- Lighting
- Raycasting
- GPU rendering

**Why:**
Underlying graphics engine used by React Three Fiber.

---

## GPU Particle System

### 4. GLSL Shaders (Vertex + Fragment Shader)

**Purpose:**
- Particle movement
- Particle color
- Glow
- Transparency
- Noise
- Flow field
- Mouse interaction
- Velocity simulation

**Why:**
This is what gives the particles their premium visual quality.
Almost every modern AI landing page relies on custom shaders.

---

### 5. GPGPU Particle Simulation (Framebuffer Objects / FBO)

**Purpose:**
- Simulate hundreds of thousands of particles
- GPU-based position updates
- GPU-based velocity updates
- Maintain smooth 60 FPS performance

**Why:**
Without GPGPU, the CPU becomes the bottleneck and particle counts must remain low.

---

## Visual Effects

### 6. @react-three/postprocessing

**Purpose:**
- Bloom
- Depth of Field
- Vignette
- Noise
- Ambient glow
- High-end cinematic rendering

**Why:**
Provides the polished, premium look seen on modern AI product websites.

---

## UI Animation

### 7. Framer Motion

**Purpose:**
- Logo animation
- Title fade-in
- Button transitions
- Loading animations
- UI micro-interactions

**Why:**
Used only for interface animations, not particle simulation.

---

## Development Tools

### 8. Leva

**Purpose:**
- Live parameter tuning
- Adjust particle count
- Mouse force
- Bloom intensity
- Colors
- Noise strength
- Camera speed

**Why:**
Makes visual iteration much faster during development.

---

### 9. Cursor

**Purpose:**
- AI-powered IDE
- Code generation
- Refactoring
- Rapid iteration

**Why:**
Primary development environment for vibecoding.

---

### 10. Claude Code

**Purpose:**
- Generate React Three Fiber code
- Generate GLSL shaders
- Optimize GPU particle systems
- Build interactive behaviors
- Refactor architecture

**Why:**
Excellent at engineering complex WebGL and graphics logic.

---

### 11. Gemini 2.5 Pro

**Purpose:**
- Creative coding
- Shader generation
- Experimental interactions
- Visual exploration
- Artistic effects

**Why:**
Particularly strong for creative visual programming and interaction design.

---

# Landing Page Interaction Design

## Background
- Fullscreen black canvas
- Blue-white particle nebula
- Continuous slow motion
- Breathing-like flow

---

## Mouse Hover
- Cursor transforms into a robotic gripper
- Nearby particles enter an influence field
- Particles swirl naturally instead of snapping

---

## Mouse Click
- Gripper closes
- Nearby particles gather into a compact energy cluster

---

## Drag
- Cluster follows cursor
- Leaves a smooth particle trail
- Maintains fluid motion

---

## Release
- No explosion
- No bounce-back
- Particles slowly disperse
- Randomized flow driven by procedural noise
- Gradually merge back into the nebula

---

# Visual Style

**Theme:**
- Minimal
- Sci-fi
- Embodied Intelligence
- Deep Space
- Premium AI

**Color Palette:**
- Pure Black (`#000000`)
- White
- Cyan
- Electric Blue

**Mood:**
- Calm
- Mysterious
- Immersive
- High-tech
- Elegant

**Keywords:**
GPU Particles, Nebula, Flow Field, Curl Noise, Procedural Animation, Interactive Simulation, Robotic Gripper, Embodied AI, Premium Landing Page
