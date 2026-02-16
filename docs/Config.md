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

- En `__init__`, convierte strings como `"1280 px"` a enteros (`1280`).
- `setup(user_config_class)` crea y retorna una instancia de config del usuario.

## Ejemplo

```python
class MyConfig(Config):
    width = "1280 px"
    height = "720 px"
    bg_color = (20, 20, 30)
    Windows = WindowSettings()
    Windows.Name = "Mi Juego"
```
