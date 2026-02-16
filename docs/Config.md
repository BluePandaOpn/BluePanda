# Config.py

BluePanda configuration and fallback system.

## Classes

## `WindowSettings`

Fields:

- `Name` (default: `"BluePanda Game"`)
- `Resizable` (default: `False`)

## `Config`

Base class for user-defined settings.

Internal defaults:

- `width = 800`
- `height = 600`
- `bg_color = (30, 30, 35)`
- `fps = 60`
- `Windows = WindowSettings()`

Main methods:

- `_normalize_px_fields()`: converts strings like `"1200 px"` to `int`.
- `with_defaults(user_config)`: merges user config with defaults.
- `setup(user_config_class=None)`: builds final config for `run_game`.

## Example

```python
from BluePanda import Config, WindowSettings, Color2d

class GameConfig(Config):
    width = "1366 px"
    height = "768 px"
    bg_color = Color2d("#0f172a")
    fps = 75

    Windows = WindowSettings()
    Windows.Name = "BluePanda Example"
    Windows.Resizable = True
```
