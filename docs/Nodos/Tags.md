# Tags (`Tags.py`)

Define decoradores que etiquetan funciones para inyectar componentes en `Nodo2D`.

## Funcion interna

- `_extract_vars(func)`: ejecuta el cuerpo de la funcion decorada para capturar variables locales en `_config`.
- Usa los `globals` reales de la funcion para permitir constantes/imports del modulo usuario.

## Decoradores disponibles

- `@CharacterBody2D`
- `@PhysicsBody2D`
- `@CollisionShape2D`
- `@Sprite2D`
- `@TimerNode`
- `@Area2D`
- `@ButtonNode`
- `@Label`
- `@PanelNode`
- `@AnimatedSprite`
- `@ScriptNode`

## Como funciona

Cada decorador agrega dos atributos a la funcion:

- `func._type`: tipo de componente.
- `func._config`: configuracion capturada.

`MetaNodo` (en `Nodo2d.py`) lee estos datos para construir la clase final.

## Ejemplo

```python
class Box(Nodo2D):
    @PhysicsBody2D
    def physics():
        mass = 1.0
        gravity_y = 980

    @CollisionShape2D
    def collider():
        pass
```
