# Nodo2D (`Nodo2d.py`)

Clase base de la mayoria de entidades del juego.

## Rol

- Hereda de `pygame.sprite.Sprite`.
- Se registra automaticamente en `instance.nodes`.
- Soporta mezcla de componentes via metaclase (`MetaNodo`).
- Mantiene config aislada por instancia (`_INTERNAL_CFG_TEMPLATE` -> copia profunda).

## Constructor

```python
Nodo2D(x=0, y=0, w=50, h=50, color=(255, 255, 255))
```

## Flujo interno

1. Lee configuracion inyectada por decoradores.
2. Crea `self.pos`.
3. Carga textura (`Texture`) via `instance.assets` o crea `Surface` con color.
4. Si existe `Atlas`, carga animacion y `animation_speed`.
5. Llama setup opcional de panel.
6. Se agrega al grupo global del motor.

## Update integrado

`update()` ejecuta subsistemas opcionales si existen:

- `update_timer`
- `update_animation`
- `update_button`
- `update_scripts`
- `update_physics`

Luego sincroniza `self.rect.topleft` con `self.pos`.

## Claves de configuracion usadas

- `width`, `height`
- `Texture`
- `color`
- `Atlas`, `frame_w`, `frame_h`, `total_frames`, `speed`

## Nota

La metaclase puede inyectar mixins segun decoradores definidos en `Tags.py`, incluido `PhysicsBody2D` (que agrega `CollisionShape2D` automaticamente).
