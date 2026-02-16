"""
BluePanda Metadata
- Version: v0.5
- Node Type: Core Resource Module
- Location: BluePanda/ResourceLoader.py
- Purpose: Centralized loader/cache for textures, sounds, fonts, and text assets.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import os
import pygame

from .asset_cache import AssetCache


class ResourceLoader:
    """Cache-oriented resource manager for common game assets."""

    def __init__(self):
        self._images = AssetCache()
        self._sounds = {}
        self._fonts = {}
        self._texts = {}

    def _norm(self, path):
        return os.path.normpath(os.path.expanduser(str(path)))

    def load_texture(self, path, size=None, use_alpha=True, fallback_color=(255, 0, 255)):
        return self._images.load_image(path, size=size, use_alpha=use_alpha, fallback_color=fallback_color)

    def load_sound(self, path, volume=1.0):
        key = (self._norm(path), float(volume))
        if key in self._sounds:
            return self._sounds[key]

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            snd = pygame.mixer.Sound(key[0])
            snd.set_volume(max(0.0, min(1.0, float(volume))))
        except Exception:
            snd = None
        self._sounds[key] = snd
        return snd

    def load_font(self, path=None, size=24):
        font_path = None if path in (None, "", "default") else self._norm(path)
        key = (font_path, int(size))
        if key in self._fonts:
            return self._fonts[key]

        try:
            font = pygame.font.Font(font_path, int(size))
        except Exception:
            font = pygame.font.SysFont(None, int(size))
        self._fonts[key] = font
        return font

    def load_text(self, path, encoding="utf-8"):
        key = (self._norm(path), encoding)
        if key in self._texts:
            return self._texts[key]
        try:
            with open(key[0], "r", encoding=encoding) as f:
                content = f.read()
        except Exception:
            content = ""
        self._texts[key] = content
        return content

    def clear(self):
        self._images.clear()
        self._sounds.clear()
        self._fonts.clear()
        self._texts.clear()

