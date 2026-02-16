# Changelog

All notable changes to BluePanda are listed in this file.

Format inspired by Keep a Changelog.

## [0.10.0] - 2026-02-16

### Changed

- Reorganized `BluePanda/` into a scalable modular architecture:
  - `core/`, `scene/`, `resources/`, `utils/`, `nodes/` with category-based subpackages.
- Preserved backward compatibility through legacy wrapper modules:
  - `BluePanda/main.py`, `BluePanda/Config.py`, `BluePanda/Input.py`, `BluePanda/SceneTree.py`, `BluePanda/ResourceLoader.py`, and `BluePanda/Nodos/*`.
- Updated package-level exports to point at the new internal architecture.

### Added

- Internal architecture reference: `BluePanda/ARCHITECTURE.md`.

## [0.9.0] - 2026-02-16

### Added

- `SceneTree` system with:
  - `add_child()`
  - `remove_child()`
  - `get_node(path)` with absolute/relative traversal
  - global event bus (`connect`, `disconnect`, `emit`)
- Node-level hierarchy and local signals in `Nodo2D`:
  - `add_child`, `remove_child`, `set_parent`, `get_children`, `get_node`, `connect`, `emit_signal`.
- Resource pipeline via `ResourceLoader`:
  - texture, sound, font, and text loading with caching/fallback behavior.
- Elaborate showcase example:
  - `examples/scene_tree_resources_demo.py`
  - `examples/data/lore.txt`

## [0.8.0] - 2026-02-16

### Added

- Formal `GameLoop` pipeline with deterministic stage order:
  1. event collection + input update
  2. engine/window event processing
  3. recursive node update
  4. camera update
  5. recursive draw
- Engine-level input abstraction in `Input`:
  - key states, just-pressed/just-released, action bindings, axis API, mouse helpers.
- Playable sample:
  - `examples/playable_demo.py`

### Changed

- `CharacterBody2D` now uses BluePanda `Input` instead of direct `pygame.key.get_pressed()`.
- `_Engine.run()` delegates frame execution to `GameLoop.step()`.

## [0.7.0] - 2026-02-16

### Changed

- Converted project documentation to English across `README.md`, `docs/`, and community files.
- Added standardized metadata headers to Python source modules with:
  - version
  - node/module type
  - location
  - purpose
  - customization notes

## [0.6.0] - 2026-02-16

### Added

- Full documentation refresh aligned to `v0.5` baseline.
- Open-source/community baseline files:
  - `CONTRIBUTING.md`
  - `CODE_OF_CONDUCT.md`
  - `COMMUNITY.md`
  - `SECURITY.md`
  - `NOTICE.md`
- Dual licensing:
  - MIT (`LICENSE`)
  - Commercial attribution (`LICENSE-COMMERCIAL.md`)

### Changed

- Introduced structured version history file (`CHANGELOG.md`) and project-level documentation indexing.

## [0.5.0] - 2026-02-16

### Added

- `PhysicsBody2D` mixin with gravity, mass, friction, restitution, damping and impulse/force APIs.
- Automatic collision solving for `PhysicsBody2D` via `CollisionShape2D` integration.
- `Math2D` utility module (`clamp`, `lerp`, `remap`, `distance`, `move_toward`, `normalized`).
- `AssetCache` robust fallback texture generation when image loading fails.

### Changed

- `run_game` now validates and normalizes core settings more safely.
- `Config` defaults and merge flow were improved to avoid missing attribute crashes.
- `Color2d` parser now supports string, tuple/list, `pygame.Color`, and `Color2d` inputs.

### Fixed

- Better fallback behavior when config fields are omitted by user projects.
- More reliable sprite/image handling when texture path is invalid.

## [0.4.0] - 2026-02-10

### Added

- Decorator tag system expanded (`TimerNode`, `Area2D`, `ButtonNode`, `Label`, `PanelNode`, `AnimatedSprite`, `ScriptNode`).
- `Script` component for loading external Python logic classes (`Logic`).
- `AnimatedSprite2D` atlas-based frame animation support.

### Changed

- `Nodo2D` metaclass (`MetaNodo`) now composes mixins automatically from tags.
- Internal config template system added for per-instance safe config cloning.

## [0.3.0] - 2026-02-05

### Added

- UI foundations: `Label2D`, `Button`, `Panel`.
- Camera tracking with `Camera2D` and world offset rendering.
- Area/sensor logic with `Area2D` callbacks.

### Changed

- Main render loop separates UI nodes (`is_ui`) from world nodes for camera handling.

## [0.2.0] - 2026-01-30

### Added

- Collision helpers via `CollisionShape2D` (`is_colliding_with`, overlap queries).
- `CharacterBody2D` movement logic with `wasd` and arrow input modes.

### Changed

- Node update chain standardized around `super().update()`.

## [0.1.0] - 2026-01-20

### Added

- Initial BluePanda core architecture.
- `run_game`, global engine `instance`, base `Nodo2D`, and `Config`/`WindowSettings`.
- Pygame game loop, sprite group update/render pipeline and resize handling.

## Notes

- Versions `0.1.0` to `0.4.0` are reconstructed from repository evolution.
- `0.6.0` to `0.10.0` document the five major update waves completed in the current cycle.
