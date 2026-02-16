# Label2D (UI)

`Label2D` renders text on screen.

## Constructor

```python
Label2D(text="Text", font_size=24, color=(255, 255, 255))
```

## Methods

- `set_text(new_text)`
- `set_color(color)`
- `update()`

## Example

```python
from BluePanda import Label2D

score = Label2D("Score: 0", font_size=28, color="white")
score.pos.x = 20
score.pos.y = 20
```
