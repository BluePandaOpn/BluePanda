# Math2D

Math utility helpers in `BluePanda/Nodos/Math2D.py`.

## Methods

- `clamp(value, minimum, maximum)`
- `lerp(a, b, t)`
- `remap(value, in_min, in_max, out_min, out_max)`
- `distance(a, b)`
- `move_toward(current, target, max_delta)`
- `normalized(vector)`

## Example

```python
from BluePanda import Math2D

hp = Math2D.clamp(hp, 0, 100)
alpha = Math2D.lerp(0, 255, 0.5)
```
