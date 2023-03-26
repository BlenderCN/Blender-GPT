bl_info = {
    "name": "GPT-4 Blender Assistant",
    "blender": (2, 93, 0),
    "category": "AI",
    "author": "TREE Industries",
    "version": (1, 0, 0),
    "location": "View3D > Tool Shelf > GPT-4 Blender Assistant",
    "description": "A Blender editor assistant powered by GPT-4"
}

import bpy
from . import ui, operators, dependencies

class GPT4AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    api_key: bpy.props.StringProperty(
        name="API Key",
        description="Enter your GPT-4 API key",
        default="",
        subtype="PASSWORD",
    )

    model: bpy.props.StringProperty(
        name="Model To Use",
        description="Enter the GPT model to use",
        default="gpt-3.5-turbo",

    )

    audio_path: bpy.props.StringProperty(
        name="Whisper Save Path",
        description="Path to save whisper transcription",
        default="recorded_audio.wav",

    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "audio_path")
        layout.prop(self, "model")
        layout.prop(self, "api_key")

def register():
    bpy.utils.register_class(GPT4AddonPreferences)
    ui.register()
    operators.register()

    dependencies.check_and_install_dependencies()

def unregister():
    bpy.utils.unregister_class(GPT4AddonPreferences)
    ui.unregister()
    operators.unregister()


if __name__ == "__main__":
    unregister()
    register()