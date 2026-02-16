# CharacterBody2D

Input-driven movement component.

## File

`BluePanda/Nodos/CharacterBody2D.py`

## Usage

Enabled with `@CharacterBody2D` inside a `Nodo2D` class.

## Supported Config

- `speed` (default: `200`)
- `input_type` (`"wasd"` or `"arrows"`)

## Behavior

- Reads keyboard direction.
- Normalizes diagonal movement.
- Applies displacement using `instance.dt`.

## Example

```python
class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 260
        input_type = "wasd"
```
