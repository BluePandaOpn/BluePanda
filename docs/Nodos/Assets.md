# Assets (`Assets.py`)

Gestion de recursos visuales del motor.

## Clase

- `AssetCache`

## Funcionalidad

- Cache de imagenes por ruta y tamano.
- Carga con `convert()` o `convert_alpha()`.
- Fallback a textura de error (checkerboard) cuando falla la carga.
- `clear()` para vaciar cache.

## Uso

`instance.assets` ya viene inicializado en el motor.

```python
image = instance.assets.load_image("assets/player.png", size=(64, 64), use_alpha=True)
```
