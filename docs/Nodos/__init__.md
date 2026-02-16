# Nodos __init__.py

`BluePanda.Nodos.__init__` exposes a lazy-loaded public API via `__getattr__`.

## Purpose

- Reduce circular import issues.
- Load modules only when requested.

## Key Exports

- `Nodo2D`
- Decorators: `CharacterBody2D`, `PhysicsBody2D`, `CollisionShape2D`, `Sprite2D`
- Components: `Timer`, `Area2D`, `Button`, `Label2D`, `Panel`, `AnimatedSprite2D`, `Script`
- Utilities: `AssetCache`, `Math2D`
