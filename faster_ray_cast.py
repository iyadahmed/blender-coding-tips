import bpy
from mathutils.bvhtree import BVHTree

C = bpy.context

# setup for faster way
bvh = BVHTree.FromObject(C.object, C.evaluated_depsgraph_get())

for i in range(999999):
    # Slower
    # C.object.ray_cast((0, 0, 0), (0, 0, -1))

    # Faster
    bvh.ray_cast((0, 0, 0), (0, 0, -1))
