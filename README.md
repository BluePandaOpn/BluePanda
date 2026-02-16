# BluePanda Engine

BluePanda is a 2D game engine in Python built on top of Pygame, using a node-and-component architecture powered by decorators.

Current version: `v0.5`

## Goals

- Fast 2D prototyping.
- Simple API (`Nodo2D`, `run_game`, `Config`).
- Plug-and-play components: movement, collisions, physics, UI, timers, scripts.

## Requirements

- Python `3.10+`
- `pygame`

```bash
pip install pygame
```

## Quick Start

```python
from BluePanda import *

class MyConfig(Config):
    width = "1280 px"
    height = "720 px"
    bg_color = Color2d("#14181e")
    fps = 60
    Windows = WindowSettings()
    Windows.Name = "BluePanda Demo"
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

## Structure

```text
BluePanda/
  main.py
  Config.py
  __init__.py
  Nodos/
docs/
```

## Documentation

- Project guide: [`docs/Proyecto.md`](docs/Proyecto.md)
- Runtime API: [`docs/main.md`](docs/main.md)
- Configuration: [`docs/Config.md`](docs/Config.md)
- 2D nodes guide: [`docs/Nodos2D.md`](docs/Nodos2D.md)
- UI guide: [`docs/UI.md`](docs/UI.md)
- Full node reference: [`docs/Nodos/README.md`](docs/Nodos/README.md)

## Versioning

- Full history: [`CHANGELOG.md`](CHANGELOG.md)
- Current status: `v0.5` (active development)

## Licensing

BluePanda is available under dual licensing:

1. MIT: [`LICENSE`](LICENSE)
2. Commercial attribution license: [`LICENSE-COMMERCIAL.md`](LICENSE-COMMERCIAL.md)

## Community

- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Code of Conduct: [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- Community channels: [`COMMUNITY.md`](COMMUNITY.md)
- Security policy: [`SECURITY.md`](SECURITY.md)

## Credits

- Creator: `Pato404`
- Engine name: `BluePanda`
