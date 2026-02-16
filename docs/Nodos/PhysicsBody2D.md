# PhysicsBody2D (`PhysicsBody2D.py`)

Componente de fisica 2D con gravedad y respuesta basica de colision AABB.

## Objetivo

Permitir comportamiento mas realista para cuerpos dinamicos y estaticos usando nodos.

## Requisitos

- Usar el decorador `@PhysicsBody2D`.
- Para colisiones, el sistema inyecta `CollisionShape2D` automaticamente.

## Propiedades de configuracion

- `velocity_x`, `velocity_y`
- `gravity_x`, `gravity_y`
- `gravity_scale`
- `mass`
- `restitution` (rebote)
- `friction`
- `linear_damping`
- `is_static`
- `enable_physics`

## Metodos principales

- `apply_force(x, y)`
- `apply_impulse(x, y)`
- `set_static(value=True)`
- `update_physics()`

## Ejemplo

```python
class Box(Nodo2D):
    @PhysicsBody2D
    def physics():
        mass = 1.0
        gravity_y = 980
        restitution = 0.1
        friction = 0.2

    @CollisionShape2D
    def collider():
        pass
```
