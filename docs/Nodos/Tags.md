# Tags (`Tags.py`)

Define decoradores que etiquetan funciones para inyectar componentes en `Nodo2D`.

## Funcion interna

- `_extract_vars(func)`: ejecuta el cuerpo de la funcion decorada para capturar variables locales en `_config`.

## Decoradores disponibles

- `@CharacterBody2D`
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
class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 220
        input_type = "wasd"
```
