# PhysicsBody2D

Basic 2D physics system with gravity and AABB collision resolution.

## File

`BluePanda/Nodos/PhysicsBody2D.py`

## Usage

Enable with `@PhysicsBody2D` on a `Nodo2D` class.

## Supported Config

- `velocity_x`, `velocity_y`
- `gravity_x`, `gravity_y`
- `gravity_scale`
- `mass`
- `restitution`
- `friction`
- `linear_damping`
- `is_static`
- `enable_physics`

## API

- `apply_force(x, y=None)`
- `apply_impulse(x, y=None)`
- `set_static(value=True)`
- `update_physics()`

## Note

For full collision behavior, it is automatically paired with `CollisionShape2D` when using `@PhysicsBody2D`.
