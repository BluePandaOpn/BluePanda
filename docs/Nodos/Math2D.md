# Math2D (`Math2D.py`)

Utilidades matematicas para uso interno del motor y scripts de juego.

## Funciones

- `Math2D.clamp(value, minimum, maximum)`
- `Math2D.lerp(a, b, t)`
- `Math2D.remap(value, in_min, in_max, out_min, out_max)`
- `Math2D.distance(a, b)`
- `Math2D.move_toward(current, target, max_delta)`
- `Math2D.normalized(vector)`

## Ejemplo

```python
speed = Math2D.clamp(speed, 0, 500)
alpha = Math2D.remap(hp, 0, 100, 0.2, 1.0)
```
