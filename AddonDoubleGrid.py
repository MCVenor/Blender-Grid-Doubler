bl_info = {
    "name": "Grid DoubleHalf",
    "author": "Mc Venor",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolshelf > Double Grid Panel",
    "description": "Doubles or Halfs the gridsize",
    "warning": "",
    "doc_url": "",
    "category": "Grid Manipulation",
}

import bpy


class DoubleGridPanel(bpy.types.Panel):
    """Creates a Panel in the Tool Shelf"""
    bl_label = "Double Grid Panel"
    bl_idname = "OBJECT_PT_doublegridpanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("so.doublegrid")

        row = layout.row()
        row.operator("so.halfgrid")



class So_DoubleGrid(bpy.types.Operator):
    """Doubles the 3D view grid size"""
    bl_idname = "so.doublegrid"
    bl_label = "SimpleOperator DoubleGridSize"


    def execute(self, context):
        main_Double(context)
        return {'FINISHED'}
    
def main_Double(context):
    AREA = 'VIEW_3D'

    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if not area.type == AREA:
                continue

            for s in area.spaces:
                if s.type == AREA:
                    s.overlay.grid_scale = s.overlay.grid_scale * 2
                    break

def main_Half(context):
    AREA = 'VIEW_3D'

    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if not area.type == AREA:
                continue

            for s in area.spaces:
                if s.type == AREA:
                    s.overlay.grid_scale = s.overlay.grid_scale * 0.5
                    break

class So_HalfGrid(bpy.types.Operator):
    """Halves the 3D view grid size"""
    bl_idname = "so.halfgrid"
    bl_label = "SimpleOperator HalfGridSize"


    def execute(self, context):
        main_Half(context)
        return {'FINISHED'}
    


addon_keymaps = []


def menu_func(self, context):
    self.layout.operator(So_DoubleGrid.bl_idname, text=So_DoubleGrid.bl_label)
    self.layout.operator(So_HalfGrid.bl_idname, text=So_HalfGrid.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(DoubleGridPanel)
    bpy.utils.register_class(So_DoubleGrid)
    bpy.utils.register_class(So_HalfGrid)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
    # Add the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('so.doublegrid', type='PAGE_UP', value='PRESS')
        addon_keymaps.append((km, kmi))
    
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('so.halfgrid', type='PAGE_DOWN', value='PRESS')
        addon_keymaps.append((km, kmi))


def unregister():
    
        # Remove the hotkey 
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    bpy.utils.unregister_class(DoubleGridPanel)
    bpy.utils.unregister_class(So_DoubleGrid)
    bpy.utils.unregister_class(So_HalfGrid)
    bpy.types.VIEW3D_MT_object.remove(menu_func)




if __name__ == "__main__":
    register()

    # test call
    # bpy.ops.so.doublegrid()
    # bpy.ops.so.halfgrid()
    



