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
    bg_color = (20, 24, 30)
    Windows = WindowSettings()
    Windows.Name = "Mi juego BluePanda"

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

## Documentacion completa

- [Guia del proyecto](docs/Proyecto.md)
- [Guia UI](docs/UI.md)
- [Guia Nodos 2D](docs/Nodos2D.md)
- [Indice completo de Nodos](docs/Nodos/README.md)

## Estado actual

- El motor esta en desarrollo activo.
- La API puede cambiar entre versiones.
