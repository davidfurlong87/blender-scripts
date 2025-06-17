import os
import bpy

# put the location to the folder where the objs are located here in this fashion
# this line will only work on windows ie C:\objects
path_to_obj_dir = os.path('D://Warhammer Models/bs export/Necrons')

file_ending = ".glb"

 
# get list of all files in directory
file_list = sorted(os.listdir(path_to_obj_dir))

# get a list of files ending in 'obj'
object_list = [item for item in file_list if item.endswith(file_ending)]
# 
## loop through the strings in list and add the files to the scene
for object in object_list:
    print(object)
#    path_to_file = os.path.join(path_to_obj_dir, item)
#    bpy.ops.import_scene.obj(filepath = path_to_file, use_split_objects=False, use_split_groups=False)