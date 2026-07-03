# JoyAI-Sim Landing Page

## Goal

Build a premium interactive landing page inspired by Loot's particle interaction style.

The entire hero section should feel like a futuristic embodied AI sandbox.

Everything visible is made from millions of glowing particles.

NOT a galaxy.

NOT random particles.

Instead, particles reconstruct an interactive desktop environment.

------------------------------------------------------------

# Overall Style

Keywords

Embodied Intelligence
Physical Simulation
Minimalism
Dark Sci-fi
Premium
Apple-like
Calm
Elegant
Interactive
Not flashy

Mood

Quiet.

Precise.

Alive.

Every particle should feel like it has weight.

------------------------------------------------------------

# Background

Pure black

Color

#050505

No gradients.

No textures.

No stars.

Background should disappear completely.

------------------------------------------------------------

# Camera

Perspective Camera

FOV:
40°

Camera Position

X = 0

Y = 1.8

Z = 8

Slight downward angle (around -12°)

The user should feel like standing in front of a workbench.

------------------------------------------------------------

# Main Scene

Everything is constructed entirely from particles.

Scene contains

Workbench

Two robotic grippers

Coffee mug

Pencil holder

Three pencils

Notebook

Small cube

Small sphere

Everything remains static unless interacted with.

------------------------------------------------------------

# Particle Count

Entire Scene

400,000 particles

Workbench

120,000

Each robotic gripper

70,000 ×2

Coffee mug

20,000

Pencil holder

18,000

Each pencil

4,000

Notebook

18,000

Cube

8,000

Sphere

10,000

Floating ambient particles

50,000

------------------------------------------------------------

# Particle Size

Random

0.8px

↓

2.2px

Average

1.3px

Soft circular particles.

No square pixels.

------------------------------------------------------------

# Color Palette

Only four colors.

Background

#050505

White

#F5F7FA

Blue

#6EC9FF

Deep Blue

#3D6DFF

Accent

#9D7CFF

Distribution

70% White

20% Light Blue

8% Deep Blue

2% Purple

Never use saturated colors.

------------------------------------------------------------

# Material

Particles should emit light.

Very soft bloom.

No metallic material.

No glossy surface.

The particles themselves ARE the material.

------------------------------------------------------------

# Object Construction

Every object should look recognizable.

Not voxel.

Not point cloud scanning.

Particles should perfectly reconstruct smooth geometry.

Particles should be denser on edges.

Less dense on flat surfaces.

------------------------------------------------------------

# Idle Animation

Nothing is perfectly static.

Every particle slowly breathes.

Amplitude

1~3 mm

Noise

Curl Noise

Speed

Extremely slow.

Almost imperceptible.

Objects should feel alive.

------------------------------------------------------------

# Mouse Interaction

Mouse never pushes objects.

Instead:

Mouse generates a local flow field.

Particles within

12 cm

slowly swirl around cursor.

Movement amplitude

3~6 mm

When cursor leaves

Particles slowly return.

No snapping.

------------------------------------------------------------

# Keyboard Interaction

Keyboard controls two robotic grippers.

A / D

Move left/right

W / S

Move forward/backward

Q / E

Move up/down

SPACE

Open / Close gripper

Movement

Smooth interpolation.

Never instant.

------------------------------------------------------------

# Gripper Interaction

The gripper can grab

Cube

Notebook

Coffee mug

Pencil

Sphere

When grabbing

Particles stay attached.

Very small vibration.

When released

Object settles naturally.

------------------------------------------------------------

# Ambient Particles

Around every object

Random floating particles.

Very sparse.

Slow movement.

Like microscopic dust.

------------------------------------------------------------

# Lighting

Single Area Light

Top Left

Soft White

Intensity

1.8

One Rim Light

Right Rear

Blue

Intensity

0.5

Very subtle.

------------------------------------------------------------

# Post Processing

Bloom

Very soft

Threshold

0.92

Intensity

0.4

Radius

0.6

Vignette

Very subtle

Chromatic Aberration

OFF

Film Grain

OFF

Motion Blur

OFF

------------------------------------------------------------

# Performance

Target FPS

60 FPS

Desktop

GPU Particle Simulation

Use Instanced Buffer Geometry

Use GLSL shaders

Avoid CPU animation.

All particle movement should happen on GPU.

------------------------------------------------------------

# User Feeling

The first impression should be

"I am looking into an AI physical simulation world."

Not a game.

Not a website.

Not a particle demo.

It should feel like an interactive robotics sandbox built from light.
