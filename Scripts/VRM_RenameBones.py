# Rename VRoid Bones to UE4 Compatible

import bpy
context = bpy.context
obj = context.object

# By default, you can't just import VRoid models into Unreal Engine without any modifications.
# This is due to the fact that VRoid armature has it's own naming convention for the bones,
# which does not match with UE4's standard bone naming conventions. However, VRoid shares
# the same bone hierarchy with UE4's, save for few auxillary twist and IK bones.
# Those bones aren't as important as other critical bones.

# This script is based from my script for MLTD bone renaming.

# USAGE:
#    1. Either save this script somewhere in your storage drive, or copy it directly to Blender's Text Editor
#    2. Load the script.
#    3. Make sure your VRoid armature is selected.
#    4. Execute the script, and voila!

bonenames = [
    ("Root",                    "root"),
    ("J_Bip_C_Hips",            "pelvis"),
    ("J_Bip_C_Spine",           "spine_01"),
    ("J_Bip_C_Chest",           "spine_02"),
    ("J_Bip_C_UpperChest",      "spine_03"),
    ("J_Bip_C_Neck",            "neck_01"),
    ("J_Bip_C_Head",            "head"),
    ("J_Adj_HairBase",          "hairbase"),
    ("J_Adj_L_FaceEye",         "eyes_l"),
    ("J_Adj_R_FaceEye",         "eyes_r"),
    ("J_Sec_L_Bust1",           "breasts_01_l"),
    ("J_Sec_L_Bust2",           "breasts_02_l"),
    ("J_Sec_R_Bust1",           "breasts_01_r"),
    ("J_Sec_R_Bust2",           "breasts_02_r"),
    ("J_Bip_L_Shoulder",        "clavicle_l"),
    ("J_Bip_L_UpperArm",        "upperarm_l"),
    ("J_Bip_L_LowerArm",        "lowerarm_l"),
    ("J_Bip_L_Hand",            "hand_l"),
    ("J_Bip_L_Thumb1",          "thumb_01_l"),
    ("J_Bip_L_Thumb2",          "thumb_02_l"),
    ("J_Bip_L_Thumb3",          "thumb_03_l"),
    ("J_Bip_L_Index1",          "index_01_l"),
    ("J_Bip_L_Index2",          "index_02_l"),
    ("J_Bip_L_Index3",          "index_03_l"),
    ("J_Bip_L_Middle1",         "middle_01_l"),
    ("J_Bip_L_Middle2",         "middle_02_l"),
    ("J_Bip_L_Middle3",         "middle_03_l"),
    ("J_Bip_L_Ring1",           "ring_01_l"),
    ("J_Bip_L_Ring2",           "ring_02_l"),
    ("J_Bip_L_Ring3",           "ring_03_l"),
    ("J_Bip_L_Little1",         "pinky_01_l"),
    ("J_Bip_L_Little2",         "pinky_02_l"),
    ("J_Bip_L_Little3",         "pinky_03_l"),
    ("J_Bip_R_Shoulder",        "clavicle_r"),
    ("J_Bip_R_UpperArm",        "upperarm_r"),
    ("J_Bip_R_LowerArm",        "lowerarm_r"),
    ("J_Bip_R_Hand",            "hand_r"),
    ("J_Bip_R_Thumb1",          "thumb_01_r"),
    ("J_Bip_R_Thumb2",          "thumb_02_r"),
    ("J_Bip_R_Thumb3",          "thumb_03_r"),
    ("J_Bip_R_Index1",          "index_01_r"),
    ("J_Bip_R_Index2",          "index_02_r"),
    ("J_Bip_R_Index3",          "index_03_r"),
    ("J_Bip_R_Middle1",         "middle_01_r"),
    ("J_Bip_R_Middle2",         "middle_02_r"),
    ("J_Bip_R_Middle3",         "middle_03_r"),
    ("J_Bip_R_Ring1",           "ring_01_r"),
    ("J_Bip_R_Ring2",           "ring_02_r"),
    ("J_Bip_R_Ring3",           "ring_03_r"),
    ("J_Bip_R_Little1",         "pinky_01_r"),
    ("J_Bip_R_Little2",         "pinky_02_r"),
    ("J_Bip_R_Little3",         "pinky_03_r"),
    ("J_Bip_L_UpperLeg",        "thigh_l"),
    ("J_Bip_L_LowerLeg",        "calf_l"),
    ("J_Bip_L_Foot",            "foot_l"),
    ("J_Bip_L_ToeBase",         "ball_l"),
    ("J_Bip_R_UpperLeg",        "thigh_r"),
    ("J_Bip_R_LowerLeg",        "calf_r"),
    ("J_Bip_R_Foot",            "foot_r"),
    ("J_Bip_R_ToeBase",         "ball_r")
]

for name, newname in bonenames:
    # Get the pose bone with name
    pb = obj.pose.bones.get(name)
    # Move on if no matching bone found
    if pb is None:
        continue
    # rename
    pb.name = newname