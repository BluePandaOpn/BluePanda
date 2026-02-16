# BluePanda Internal Structure

## New Modular Layout

- `core/`: engine runtime, config, input.
- `scene/`: scene tree, node paths, global events.
- `resources/`: textures, sounds, fonts, text loading/cache.
- `utils/`: color and math utilities.
- `nodes/base/`: base `Nodo2D`.
- `nodes/decorators/`: decorator/tag system.
- `nodes/physics/`: movement, collisions, physics, sensors.
- `nodes/render/`: camera and sprite rendering.
- `nodes/ui/`: UI node components.
- `nodes/time/`: timer systems.
- `nodes/scripting/`: runtime script attachment.

## Legacy Compatibility

Old paths are still available through wrappers:

- `BluePanda/main.py`
- `BluePanda/Config.py`
- `BluePanda/Input.py`
- `BluePanda/SceneTree.py`
- `BluePanda/ResourceLoader.py`
- `BluePanda/Nodos/*.py`

This allows existing projects to keep running while the new architecture is adopted.
