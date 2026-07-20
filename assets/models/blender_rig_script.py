"""
JoyAI-Sim Robotic Arm Auto-Rigging Script for Blender
=====================================================
Usage:
1. Open Blender
2. File → Import → glTF 2.0 → select '主页桌子3d拆分.glb'
3. Switch to Scripting workspace tab
4. Click "New" to create a new text block
5. Paste this entire script
6. Click "Run Script"
7. File → Export → glTF 2.0 → save as '主页桌子3d_rigged.glb'
   Check: Armatures ✓, Skinning ✓
"""

import bpy
from mathutils import Vector

# ============================================================
# PART MAPPING
# ============================================================
BONE_PARTS = {
    'L_Base':      [47],
    'L_Disc':      [25, 62],
    'L_Joint1':    [6],
    'L_Arm1':      [22],
    'L_Joint2':    [7],
    'L_Arm2':      [24, 55],
    'L_Joint3':    [12],
    'L_Arm3':      [42, 10, 58, 49],
    'L_GripBase':  [46],
    'L_GripL':     [8],
    'L_GripR':     [31],
    'R_Base':      [19],
    'R_Disc':      [4, 48, 60],
    'R_Joint1':    [51, 39, 40, 37, 61],
    'R_Arm1':      [36, 54, 53],
    'R_Joint2':    [2, 1],
    'R_Arm2':      [34],
    'R_Joint3':    [26],
    'R_Arm3':      [30],
    'R_Joint4':    [32],
    'R_Arm4':      [3, 13],
    'R_GripBase':  [44],
    'R_GripL':     [9],
    'R_GripR':     [33],
    'Table':       [21],
    'PenHolder':   [16],
    'Box1':        [14],
    'Box2':        [41],
    'Cup':         [18],
    'Pencils_holder': [28, 29, 0, 27],
    'Pencils_table':  [35, 11, 5],
}

BONE_HIERARCHY = {
    'L_Disc': 'L_Base', 'L_Joint1': 'L_Disc', 'L_Arm1': 'L_Joint1',
    'L_Joint2': 'L_Arm1', 'L_Arm2': 'L_Joint2', 'L_Joint3': 'L_Arm2',
    'L_Arm3': 'L_Joint3', 'L_GripBase': 'L_Arm3',
    'L_GripL': 'L_GripBase', 'L_GripR': 'L_GripBase',
    'R_Disc': 'R_Base', 'R_Joint1': 'R_Disc', 'R_Arm1': 'R_Joint1',
    'R_Joint2': 'R_Arm1', 'R_Arm2': 'R_Joint2', 'R_Joint3': 'R_Arm2',
    'R_Arm3': 'R_Joint3', 'R_Joint4': 'R_Arm3', 'R_Arm4': 'R_Joint4',
    'R_GripBase': 'R_Arm4', 'R_GripL': 'R_GripBase', 'R_GripR': 'R_GripBase',
    'PenHolder': 'Table', 'Box1': 'Table', 'Box2': 'Table',
    'Cup': 'Table', 'Pencils_holder': 'PenHolder', 'Pencils_table': 'Table',
}

# ============================================================
# HELPERS
# ============================================================
def find_mesh(part_id):
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and f'tripo_part_{part_id}' in obj.name:
            return obj
    return None

def get_center(part_ids):
    centers = []
    for pid in part_ids:
        obj = find_mesh(pid)
        if obj:
            bbox = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
            centers.append(sum(bbox, Vector()) / 8)
    if not centers:
        return Vector((0, 0, 0))
    return sum(centers, Vector()) / len(centers)

# ============================================================
# MAIN — no bpy.ops, pure data API
# ============================================================
print("\n" + "=" * 60)
print("JoyAI-Sim Auto-Rigging Script")
print("=" * 60)

# Step 1: Check meshes
print("\nStep 1: Checking meshes...")
all_ids = set()
for parts in BONE_PARTS.values():
    all_ids.update(parts)
found = sum(1 for pid in all_ids if find_mesh(pid))
print(f"  Found {found}/{len(all_ids)} meshes")

# Step 2: Create armature (pure data API, no operators)
print("\nStep 2: Creating armature...")
armature_data = bpy.data.armatures.new('RobotArmature')
armature_obj = bpy.data.objects.new('RobotArmature', armature_data)
bpy.context.scene.collection.objects.link(armature_obj)

# Step 3: Add bones — must be in edit mode
# Use override context to avoid poll failures
print("\nStep 3: Creating bones...")
bpy.context.view_layer.objects.active = armature_obj
armature_obj.select_set(True)

# Force object mode first if needed
if bpy.context.object and bpy.context.object.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')

bpy.ops.object.mode_set(mode='EDIT')

BONE_LENGTH = 0.02
for bone_name, part_ids in BONE_PARTS.items():
    center = get_center(part_ids)
    bone = armature_data.edit_bones.new(bone_name)
    bone.head = center
    bone.tail = center + Vector((0, BONE_LENGTH, 0))
    print(f"  Bone '{bone_name}' at ({center.x:.3f}, {center.y:.3f}, {center.z:.3f})")

# Step 4: Hierarchy
print("\nStep 4: Setting hierarchy...")
for child_name, parent_name in BONE_HIERARCHY.items():
    child = armature_data.edit_bones.get(child_name)
    parent = armature_data.edit_bones.get(parent_name)
    if child and parent:
        child.parent = parent
        child.use_connect = False

bpy.ops.object.mode_set(mode='OBJECT')

# Step 5: Bind meshes to bones
print("\nStep 5: Binding meshes...")
for bone_name, part_ids in BONE_PARTS.items():
    for pid in part_ids:
        obj = find_mesh(pid)
        if not obj:
            continue

        # Add armature modifier
        for m in [m for m in obj.modifiers if m.type == 'ARMATURE']:
            obj.modifiers.remove(m)
        mod = obj.modifiers.new('Armature', 'ARMATURE')
        mod.object = armature_obj

        # Create vertex group (all verts, weight 1.0)
        if bone_name in obj.vertex_groups:
            obj.vertex_groups.remove(obj.vertex_groups[bone_name])
        vg = obj.vertex_groups.new(name=bone_name)
        vg.add(list(range(len(obj.data.vertices))), 1.0, 'REPLACE')

        # Parent to armature
        obj.parent = armature_obj
        obj.parent_type = 'ARMATURE'

        print(f"  Part {pid} → '{bone_name}'")

# Step 6: Set rotation mode
print("\nStep 6: Setting rotation mode...")
bpy.context.view_layer.objects.active = armature_obj
bpy.ops.object.mode_set(mode='POSE')
for pbone in armature_obj.pose.bones:
    pbone.rotation_mode = 'XYZ'
bpy.ops.object.mode_set(mode='OBJECT')

print("\n" + "=" * 60)
print(f"DONE! Created {len(BONE_PARTS)} bones")
print("=" * 60)
print("\nExport: File → Export → glTF 2.0")
print("  Format: GLB")
print("  Check: Armatures ✓, Skinning ✓")
print("  Save as: 主页桌子3d_rigged.glb")
