# BluePanda __init__.py

This module defines the public API used by:

```python
from BluePanda import *
```

## Main Exports

- Runtime: `run_game`, `instance`
- Core: `Nodo2D`, `Config`, `WindowSettings`
- Decorators: `CharacterBody2D`, `PhysicsBody2D`, `CollisionShape2D`, `Sprite2D`, `TimerNode`, `Area2D`, `ButtonNode`, `Label`, `PanelNode`, `AnimatedSprite`, `ScriptNode`
- Utilities: `Color2d`, `AssetCache`, `Math2D`
- Direct classes: `Camera2D`, `Label2D`

## Note

`__all__` controls which symbols are exposed by wildcard imports.
