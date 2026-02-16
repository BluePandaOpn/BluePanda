# Changelog

All notable changes to BluePanda are listed in this file.

Format inspired by Keep a Changelog.

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

- Versions `0.1.0` to `0.4.0` are reconstructed from current repository state and internal module evolution.
- `0.5.0` is the current documented release target.
