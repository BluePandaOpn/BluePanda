# Tags (Decorators)

File: `BluePanda/Nodos/Tags.py`

## Behavior

Each decorator marks an inner function with:

- `_type`
- `_config`

Then `MetaNodo` reads those values to inject mixins and configuration.

## Available Decorators

- `CharacterBody2D`
- `CollisionShape2D`
- `Sprite2D`
- `TimerNode`
- `Area2D`
- `ButtonNode`
- `Label`
- `PanelNode`
- `AnimatedSprite`
- `ScriptNode`
- `PhysicsBody2D`

## Example

```python
class Enemy(Nodo2D):
    @Sprite2D
    def look():
        width = 32
        height = 32
        color = "#ef4444"
```
