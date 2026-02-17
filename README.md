# BluePanda Engine

BluePanda is a 2D game engine in Python built on top of Pygame, using a node-and-component architecture powered by decorators.

Current version: `v0.16.6`

## Goals

- Fast 2D prototyping.
- Simple API (`Nodo2D`, `run_game`, `Config`).
- Plug-and-play components: movement, collisions, physics, UI, timers, scripts.
- Advanced runtime systems: SceneTree groups, pause modes, time scaling, gameplay mixins.
- New high-level systems: scheduler, tweening, finite state machine, and particle emitter.
- Declarative node APIs: `@OnReady`, `@OnEvent`, `@OnSignal`, and `component(...)`.

## Requirements

- Python `3.10+`
- `pygame`

```bash
pip install -e .
```

Alternative install (non-editable):

```bash
pip install .
```

After installing once, `import BluePanda` works from any project folder.

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
  core/
  scene/
  resources/
  utils/
  nodes/
  Nodos/         # legacy compatibility wrappers
  main.py        # legacy compatibility wrapper
  Config.py      # legacy compatibility wrapper
  __init__.py
docs/
```

## Documentation

- Project guide: [`docs/Proyecto.md`](docs/Proyecto.md)
- Runtime API: [`docs/main.md`](docs/main.md)
- Configuration: [`docs/Config.md`](docs/Config.md)
- 2D nodes guide: [`docs/Nodos2D.md`](docs/Nodos2D.md)
- UI guide: [`docs/UI.md`](docs/UI.md)
- Full node reference: [`docs/Nodos/README.md`](docs/Nodos/README.md)
- Basic projects (learning path): [`examples/BASICS.md`](examples/BASICS.md)
- Advanced projects: [`examples/ADVANCED.md`](examples/ADVANCED.md)
- 12 progressive versions: [`examples/versions/README.md`](examples/versions/README.md)

## Versioning

- Full history: [`CHANGELOG.md`](CHANGELOG.md)
- Current status: `v0.10` (active development)
- `v0.6` to `v0.10` cover the 5 major update waves completed in this cycle.

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
