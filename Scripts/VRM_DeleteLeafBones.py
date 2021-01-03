# Obliterate unused leaf bones in VRoid models!

import bpy
context = bpy.context
obj = context.object

# By default, VRM Importer includes leaf bones automatically.
# It's cool and stuff, but it's not necessary for Blender, and will spew out
# scary long warning when imported to UE4.
# Use this script to obliterate those leaf bones in one click.

if obj.type == 'ARMATURE':
    armature = obj.data

bpy.ops.object.mode_set(mode='EDIT')

for bone in armature.edit_bones:
    if bone.name.endswith("_end") :
        armature.edit_bones.remove(bone)
    else:
        continue

bpy.ops.object.mode_set(mode='OBJECT')