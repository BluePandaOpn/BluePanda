# CollisionShape2D

Collision detection helper component.

## File

`BluePanda/Nodos/CollisionShape2D.py`

## Methods

- `is_colliding_with(other_node)`
- `get_overlapping_bodies()`
- `check_collision(tag_buscada=None)`

## Typical Use

Usually combined with `@CharacterBody2D` or `@PhysicsBody2D`.

```python
class Wall(Nodo2D):
    @CollisionShape2D
    def collider():
        pass
```
