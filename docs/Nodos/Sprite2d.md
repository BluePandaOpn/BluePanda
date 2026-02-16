# Sprite2D (`Sprite2d.py`)

Mixin de transformaciones visuales para sprites.

## Metodos

- `flip_h(boolean)`
- `flip_v(boolean)`
- `set_opacity(alpha)`
- `set_scale(scale_x, scale_y)`

## Detalle

`set_scale` recalcula `self.rect` manteniendo el centro para conservar coherencia visual y de colision.

## Requisitos

- `self.image` y `self.rect` deben existir.
