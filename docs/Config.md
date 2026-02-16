# Config.py

Define la configuracion base del proyecto.

## Clases

- `WindowSettings`
- `Config`

## `WindowSettings`

Campos por defecto:

- `Name = "BluePanda Game"`
- `Resizable = False`

## `Config`

Incluye defaults integrados del motor:

- `width = 800`
- `height = 600`
- `bg_color = (30, 30, 35)`
- `fps = 60`
- `Windows = WindowSettings()`

Flujo de uso:

- Convierte strings como `"1280 px"` a enteros.
- `with_defaults(user_config)` mezcla config de usuario con defaults sin romper claves faltantes.
- `setup(user_config_class=None)` retorna el diccionario final que usa `run_game`.

## Ejemplo

```python
class MyConfig(Config):
    width = "1280 px"
    height = "720 px"
    bg_color = (20, 20, 30)
    fps = 75

    Windows = WindowSettings()
    Windows.Name = "Mi Juego"
    Windows.Resizable = True
```
