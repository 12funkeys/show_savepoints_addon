import bpy
from bpy.app.handlers import persistent

bl_info = {
    "name" : "Save Point Addon",
    "author" : "12funkeys",
    "version" : (0,1),
    "blender" : (2, 81, 0),
    "description" : "Show savepoints in undo history",
    "wiki_url" : "https://github.com/12funkeys/show_savepoints_addon/wiki",
    "category" : "Tools"
}

class bpy_OT_savepoint(bpy.types.Operator):

    bl_idname = "view3d.savepoint"
    bl_label = "Save Point"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        print("Save Point")
        bpy.ops.ed.undo_push(message="Save Point")
        return {'FINISHED'}  
	
@persistent
def load_handler(dummy):
	bpy.app.handlers.save_post.append(bpy_OT_savepoint.execute)

def register():
	bpy.utils.register_class(bpy_OT_savepoint)
	bpy.app.handlers.load_post.append(load_handler)

def unregister():
	bpy.utils.unregister_class(bpy_OT_savepoint)
	bpy.app.handlers.load_post.remove(load_handler)

if __name__ == "__main__":
    register()

