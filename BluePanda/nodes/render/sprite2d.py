"""
BluePanda Metadata
- Version: v0.5
- Node Type: Visual Node Component
- Location: BluePanda/Nodos/Sprite2d.py
- Purpose: Adds runtime sprite manipulation helpers (flip, scale, tint, texture).

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
from ...utils.color import Color2d
from ...core.engine import instance


class Sprite2D:
    """
    Componente encargado de la manipulacion visual avanzada.
    Se activa cuando el usuario usa @Sprite2D.
    """

    def flip_h(self, boolean):
        """Voltea la imagen horizontalmente."""
        if hasattr(self, "image"):
            self.image = pygame.transform.flip(self.image, boolean, False)

    def flip_v(self, boolean):
        """Voltea la imagen verticalmente."""
        if hasattr(self, "image"):
            self.image = pygame.transform.flip(self.image, False, boolean)

    def set_opacity(self, alpha):
        """Cambia la transparencia del objeto (0 a 255)."""
        if hasattr(self, "image"):
            self.image.set_alpha(max(0, min(255, int(alpha))))

    def set_scale(self, scale_x, scale_y):
        """Cambia el tamano del sprite en tiempo real."""
        if hasattr(self, "image"):
            size = (int(self.rect.width * scale_x), int(self.rect.height * scale_y))
            self.image = pygame.transform.scale(self.image, size)
            self.rect = self.image.get_rect(center=self.rect.center)

    def set_color(self, color):
        """Rellena el sprite con un color (nombre, #hex, rgb, tuple)."""
        if hasattr(self, "image"):
            self.image.fill(Color2d.coerce(color, (255, 255, 255)))

    def set_texture(self, path, width=None, height=None):
        """Reemplaza la textura usando el AssetCache del motor."""
        if not hasattr(self, "rect"):
            return

        w = int(width if width is not None else self.rect.width)
        h = int(height if height is not None else self.rect.height)
        center = self.rect.center

        self.image = instance.assets.load_image(path, size=(w, h), use_alpha=True)
        self.rect = self.image.get_rect(center=center)

    def tint(self, color, alpha=100):
        """Aplica un tinte de color encima del sprite."""
        if not hasattr(self, "image"):
            return

        overlay = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        rgb = Color2d.coerce(color, (255, 255, 255))
        a = max(0, min(255, int(alpha)))
        overlay.fill((rgb[0], rgb[1], rgb[2], a))
        self.image.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)


