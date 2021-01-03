# Rename VRoid shape keys with better naming convention!

import bpy
context = bpy.context
obj = context.object

# This script will rename VRoid shape keys with PAST FUTURE's naming convention.
# Unreal Engine doesn't care about the naming of the shape keys, however, for the sake of simplicity,
# and to ease scripting of shape keys in BP, it's a good practice to use easy to understand naming
# conventions.

# If you're a modder, you can refer to this script to implement facial animations.

# This array is the template used for the batch rename script.
# The format for the array element goes like this:
#           ("old name","new name")
# Quote mark is not omitted. Add comma if there's a new shape key you want to rename.
sknames = [
        ("Face.M_F00_000_00_Fcl_ALL_Angry",    "Face - Angry"),
        ("Face.M_F00_000_00_Fcl_ALL_Fun",      "Face - Grin"),
        ("Face.M_F00_000_00_Fcl_ALL_Joy",      "Face - Happy"),
        ("Face.M_F00_000_00_Fcl_ALL_Sorrow",   "Face - Frown"),
        ("Face.M_F00_000_00_Fcl_ALL_Surprised","Face - Surprised"),
        ("Face.M_F00_000_00_Fcl_BRW_Angry",    "Brows - Angry"),
        ("Face.M_F00_000_00_Fcl_BRW_Fun",      "Brows - Grin"),
        ("Face.M_F00_000_00_Fcl_BRW_Joy",      "Brows - Happy"),
        ("Face.M_F00_000_00_Fcl_BRW_Sorrow",   "Brows - Frown"),
        ("Face.M_F00_000_00_Fcl_BRW_Surprised","Brows - Surprise"),
        ("Face.M_F00_000_00_Fcl_EYE_Natural",  "Eyes - Natural"),      # doesn't seem to do anything
        ("Face.M_F00_000_00_Fcl_EYE_Fun",      "Eyes - Angry"),
        ("Face.M_F00_000_00_Fcl_EYE_Close",    "Eyes - Close Down Both"),
        ("Face.M_F00_000_00_Fcl_EYE_Close_R",  "Eyes - Close Down L"),
        ("Face.M_F00_000_00_Fcl_EYE_Close_L",  "Eyes - Close Down R"),
        ("Face.M_F00_000_00_Fcl_EYE_Joy",      "Eyes - Close Up Both"),
        ("Face.M_F00_000_00_Fcl_EYE_Joy_R",    "Eyes - Close Up R"),
        ("Face.M_F00_000_00_Fcl_EYE_Joy_L",    "Eyes - Close Up L"),
        ("Face.M_F00_000_00_Fcl_EYE_Sorrow",   "Eyes - Frown"),
        ("Face.M_F00_000_00_Fcl_EYE_Sorrow",   "Eyes - Frown"),
        ("Face.M_F00_000_00_Fcl_EYE_Surprised","Eyes - Surprised"),
        ("Face.M_F00_000_00_Fcl_EYE_Extra",    "Eyes - Extra"),
        ("Face.M_F00_000_00_Fcl_MTH_Up",       "Mouth - Shift Up"),
        ("Face.M_F00_000_00_Fcl_MTH_Down",     "Mouth - Shift Down"),
        ("Face.M_F00_000_00_Fcl_MTH_Angry",    "Mouth - Frown"),
        ("Face.M_F00_000_00_Fcl_MTH_Neutral",  "Mouth - Neutral"),
        ("Face.M_F00_000_00_Fcl_MTH_Fun",      "Mouth - Grin"),
        ("Face.M_F00_000_00_Fcl_MTH_Joy",      "Mouth - Happy"),
        ("Face.M_F00_000_00_Fcl_MTH_Sorrow",   "Mouth - Sad"),
        ("Face.M_F00_000_00_Fcl_MTH_Surprised","Mouth - Surprised"),
        ("Face.M_F00_000_00_Fcl_MTH_A",        "Mouth - A"),
        ("Face.M_F00_000_00_Fcl_MTH_I",        "Mouth - I"),
        ("Face.M_F00_000_00_Fcl_MTH_U",        "Mouth - U"),
        ("Face.M_F00_000_00_Fcl_MTH_E",        "Mouth - E"),
        ("Face.M_F00_000_00_Fcl_MTH_O",        "Mouth - O"),
        ("Face.M_F00_000_00_Fcl_HA_Fung1",     "Fangs - Vampire Both"),
        ("Face.M_F00_000_00_Fcl_HA_Fung1_Low", "Fangs - Vampire Lower"),
        ("Face.M_F00_000_00_Fcl_HA_Fung1_Up",  "Fangs - Vampire Upper"),
        ("Face.M_F00_000_00_Fcl_HA_Fung2",     "Fangs - Shark Both"),
        ("Face.M_F00_000_00_Fcl_HA_Fung2_Low", "Fangs - Shark Lower"),
        ("Face.M_F00_000_00_Fcl_HA_Fung2_Up",  "Fangs - Shark Upper"),
        ("Face.M_F00_000_00_Fcl_HA_Fung1",     "Fangs - Vampire Both"),
        ("Face.M_F00_000_00_Fcl_HA_Fung1_Low", "Fangs - Vampire Lower"),
        ("Face.M_F00_000_00_Fcl_HA_Fung1_Up",  "Fangs - Vampire Upper"),
        ("EyeExtra_01Face.M_F00_000_00_EyeExtra_On","Eye Extras - Toggle")
]

for name, newname in sknames:
    # Get shape keys in the mesh
    keys = obj.data.shape_keys.key_blocks
    for key in keys:
        # Validate key name before renaming it
        if key.name == name:
            key.name = key.name.replace(name, newname)
        else:
            continue
