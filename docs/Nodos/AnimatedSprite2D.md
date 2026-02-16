# AnimatedSprite2D (`AnimatedSprite2D.py`)

Mixin para animacion por atlas/spritesheet.

## Propiedades

- `frames`
- `current_frame`
- `animation_speed`
- `timer`
- `playing`

## Metodos

- `load_atlas(path, frame_width, frame_height, total_frames)`
  - Carga atlas y recorta frames.
  - Inicializa `self.image` y `self.rect` con el primer frame.

- `update_animation()`
  - Avanza frames usando `instance.dt`.

- `play()` / `stop()`
  - Control del estado de reproduccion.

## Requisitos

- Debe existir un atlas valido en disco.
- Llamar `update_animation()` en el loop del nodo para animar continuamente.
