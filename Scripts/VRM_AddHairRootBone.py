# Add hair root bone in your VRoid model!

import bpy
context = bpy.context
obj = context.object

# This script will add a new bone for parenting hair bones that was parented to head bone.
# Useful for reducing AnimDynamics node count in your AnimBP.

# Use this script first before renaming bones to UE4 compatible!

if obj.type == 'ARMATURE':
    armature = obj.data
else:
    def invalidobj(self, context):
        self.report({'ERROR'}, "Selected object is not an armature! Please select the armature from your VRoid model!")

bpy.ops.object.mode_set(mode='EDIT')

if  armature.edit_bones["J_Adj_HairBase"] == None:
    hairbone = armature.edit_bones.new("J_Adj_HairBase")
    hairbone.head = (0,1,1)
    hairbone.tail = (0,1,2)
    armature.edit_bones["J_Adj_HairBase"].parent = armature.edit_bones["J_Bip_C_Head"]

for bone in armature.edit_bones:
    if bone.name.startswith("HairJoint") and bone.parent == armature.edit_bones["J_Bip_C_Head"] :
        bone.parent = armature.edit_bones["J_Adj_HairBase"]
    else:
        continue

bpy.ops.object.mode_set(mode='OBJECT')