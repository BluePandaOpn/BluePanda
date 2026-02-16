# Nodo2D

Base class for gameplay entities.

## File

`BluePanda/Nodos/Nodo2d.py`

## What It Does

- Inherits from `pygame.sprite.Sprite`.
- Uses `MetaNodo` metaclass to inject mixins from decorators.
- Creates `image`, `rect`, and `pos`.
- Auto-registers into `instance.nodes`.
- Runs optional subsystems inside `update()`.

## Constructor

```python
Nodo2D(x=0, y=0, w=50, h=50, color=(255, 255, 255))
```

## Decorator Configuration

Values extracted by tags (for example: `width`, `height`, `Texture`, `Atlas`, `speed`) are stored per instance in `_internal_cfg`.

## Update Chain

`update()` calls these methods when present:

- `update_timer()`
- `update_animation()`
- `update_button()`
- `update_scripts()`
- `update_physics()`
