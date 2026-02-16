import os
import pygame
from .Color2d import Color2d


class AssetCache:
    """Cargador de assets con cache y fallback visual si un archivo falla."""

    def __init__(self):
        self._image_cache = {}

    def _normalize_path(self, path):
        if not isinstance(path, str):
            return path
        expanded = os.path.expanduser(path)
        return os.path.normpath(expanded)

    def _missing_texture(self, size=(64, 64), color_a=(255, 0, 255), color_b=(0, 0, 0)):
        width = max(2, int(size[0]))
        height = max(2, int(size[1]))
        surface = pygame.Surface((width, height), pygame.SRCALPHA)

        block = max(4, min(width, height) // 4)
        for y in range(0, height, block):
            for x in range(0, width, block):
                use_a = ((x // block) + (y // block)) % 2 == 0
                surface.fill(color_a if use_a else color_b, (x, y, block, block))

        return surface

    def load_image(self, path, size=None, use_alpha=True, fallback_color=(255, 0, 255)):
        """Carga una imagen con cache. Si falla, retorna textura fallback."""
        normalized = self._normalize_path(path)
        size_key = tuple(size) if size else None
        key = (normalized, size_key, bool(use_alpha))

        if key in self._image_cache:
            return self._image_cache[key].copy()

        try:
            image = pygame.image.load(normalized)
            image = image.convert_alpha() if use_alpha else image.convert()
            if size_key:
                image = pygame.transform.scale(image, size_key)
        except Exception:
            safe_color = Color2d.coerce(fallback_color, (255, 0, 255))
            fallback_size = size_key if size_key else (64, 64)
            image = self._missing_texture(size=fallback_size, color_a=safe_color)

        self._image_cache[key] = image
        return image.copy()

    def clear(self):
        self._image_cache.clear()

