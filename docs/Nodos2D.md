# Nodos2D

Practical guide for gameplay using `Nodo2D` and decorators.

## Base Node

`Nodo2D` is the main class for 2D entities.

- Owns `pos` (`pygame.Vector2`), `image`, and `rect`.
- Auto-registers into global `instance.nodes`.
- Executes optional subsystems inside `update()`.

## Available Decorators

- `@CharacterBody2D`: input movement.
- `@PhysicsBody2D`: gravity-based physics and collision solving.
- `@CollisionShape2D`: collision query helpers.
- `@Sprite2D`: visual setup and sprite tools.
- `@AnimatedSprite`: atlas/frame animation.
- `@Area2D`: sensor area behavior.
- `@TimerNode`: timer behavior.
- `@ScriptNode`: external script loading.

## Example

```python
from BluePanda import *

class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 240
        input_type = "wasd"

    @CollisionShape2D
    def collider():
        pass

    @Sprite2D
    def look():
        width = 32
        height = 48
        color = "#38bdf8"
```

## Full Reference

See [`docs/Nodos/README.md`](Nodos/README.md).
