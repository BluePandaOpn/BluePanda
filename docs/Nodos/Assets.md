# Assets (AssetCache)

Asset management in `BluePanda/Nodos/Assets.py`.

## Class

`AssetCache`

## Features

- In-memory cache by key `(path, size, alpha)`.
- Safe image loading (`load_image`).
- Checkerboard fallback texture when loading fails.

## Methods

- `load_image(path, size=None, use_alpha=True, fallback_color=(255, 0, 255))`
- `clear()`

## Note

This is used automatically by the engine through `instance.assets`.
