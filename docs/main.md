# main.py

Reference for BluePanda runtime internals.

## Core Elements

- `_Engine`: main runtime loop and global engine state.
- `instance`: singleton engine instance.
- `run_game(config=None)`: entry point for execution.

## _Engine

Responsibilities:

- Initialize Pygame.
- Create window (`screen`) and frame clock (`clock`).
- Hold all nodes in `nodes` (`pygame.sprite.Group`).
- Process events (`QUIT`, `VIDEORESIZE`).
- Update and render nodes.
- Apply camera offset to world nodes (non-UI).

Key fields:

- `width`, `height`
- `bg_color`
- `target_fps`
- `dt`
- `nodes`
- `_named_nodes`
- `camera`
- `assets`

Helpful methods:

- `register_node(name, node)`
- `get_node(name)`
- `get_nodes_by_class(node_class)`

## run_game(config=None)

`run_game`:

1. Loads merged settings via `Config.setup`.
2. Applies safe values for `width`, `height`, `fps`, and `bg_color`.
3. Configures window title and `Resizable` mode.
4. Starts the loop with `instance.run()`.

## Example

```python
from BluePanda import Config, WindowSettings, run_game

class MyConfig(Config):
    width = 1280
    height = 720
    fps = 60
    Windows = WindowSettings()
    Windows.Name = "My Game"
    Windows.Resizable = True

run_game(MyConfig)
```
