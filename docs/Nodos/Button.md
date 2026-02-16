# Button (`Button.py`)

Mixin de boton para nodos UI con `rect` e `image`.

## Propiedades

- `is_hovered`
- `is_pressed`
- `on_click_callback`
- `color_normal`
- `color_hover`
- `color_pressed`

## Metodos

- `connect_click(func)`
- `update_button()`

## Comportamiento

- Detecta hover con `self.rect.collidepoint(mouse_pos)`.
- Ejecuta callback al presionar click izquierdo dentro del boton.
- Cambia color visual segun estado (`normal/hover/pressed`).

## Configurable por decorador

```python
@ButtonNode
def button_cfg():
    color_normal = (80, 80, 80)
    color_hover = (120, 120, 120)
    color_pressed = (180, 180, 180)
```

## Requisito

Llamar `update_button()` en cada frame del nodo.
