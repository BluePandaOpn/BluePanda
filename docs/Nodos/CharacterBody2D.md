# CharacterBody2D (`CharacterBody2D.py`)

Mixin de movimiento basico por teclado.

## Metodos

- `move_and_slide()`
  - Lee `speed` (default `200`).
  - Lee `input_type` (`wasd` o `arrows`).
  - Normaliza diagonales.
  - Mueve `self.pos` con `instance.dt`.

- `update()`
  - Ejecuta `move_and_slide()`.
  - Llama `super().update()` para mantener la cadena de actualizacion.

## Requisitos

- `self.pos` debe existir (lo crea `Nodo2D`).
- `instance.dt` debe estar actualizado (lo hace el engine loop).

## Configuracion comun via decorador

```python
@CharacterBody2D
def movement():
    speed = 200
    input_type = "wasd"
```
