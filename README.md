# BluePanda Engine

Motor de videojuegos 2D en Python, construido sobre Pygame y basado en nodos.

## Objetivo

BluePanda busca acelerar prototipos 2D con una API simple:

- Nodos con `update()` automatico.
- Componentes por decoradores (`@CharacterBody2D`, `@Sprite2D`, etc.).
- Soporte para UI, camara, colisiones y animacion.

## Requisitos

- Python 3.10+
- `pygame`

Instalacion rapida:

```bash
pip install pygame
```

## Estructura del proyecto

```text
BluePanda/
  main.py
  Config.py
  Nodos/
docs/
  Proyecto.md
  UI.md
  Nodos2D.md
  Nodos/
```

## Inicio rapido

```python
from BluePanda import *

class MyConfig(Config):
    width = "1280 px"
    height = "720 px"
    bg_color = Color2d("#14181e")
    fps = 60
    Windows = WindowSettings()
    Windows.Name = "Mi juego BluePanda"
    Windows.Resizable = True

class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 220
        input_type = "wasd"

    @Sprite2D
    def look():
        color = (80, 160, 255)
        width = 48
        height = 48

    def update(self):
        super().update()

player = Player(100, 100)
camera = Camera2D(target=player)

run_game(MyConfig)
```

`Config` ahora soporta fallback automatico: si no defines `width`, `height`, `bg_color`, `fps` o `Windows`, el motor usa valores por defecto seguros.

## Sistema de color (`Color2d`)

```python
Color2d("white")
Color2d("#ffffff")
Color2d("rgb(255, 255, 255)")
Color2d((255, 255, 255))
```

## Fisicas y matematicas

```python
class Box(Nodo2D):
    @PhysicsBody2D
    def physics():
        mass = 1.0
        gravity_y = 980
        restitution = 0.2
        friction = 0.15
        is_static = False

    @CollisionShape2D
    def collider():
        pass
```

Utilidades de soporte:
- `Math2D.clamp`, `Math2D.lerp`, `Math2D.remap`
- `Math2D.distance`, `Math2D.normalized`

## Documentacion completa

- [Guia del proyecto](docs/Proyecto.md)
- [Guia UI](docs/UI.md)
- [Guia Nodos 2D](docs/Nodos2D.md)
- [Indice completo de Nodos](docs/Nodos/README.md)

## Estado actual

- El motor esta en desarrollo activo.
- La API puede cambiar entre versiones.
