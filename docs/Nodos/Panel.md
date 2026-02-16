# Panel (`Panel.py`)

Mixin visual para paneles de interfaz.

## Propiedades

- `border_radius`
- `border_width`
- `border_color`
- `opacity`

## Metodos

- `setup_panel()`
  - Aplica config desde `_INTERNAL_CFG`.
  - Ajusta opacidad de `self.image`.

- `draw_border(surface)`
  - Dibuja borde opcional en `surface`.

## Requisitos

- `self.image` y `self.rect` deben existir.
- `draw_border` debe llamarse explicitamente donde renderices el panel.
