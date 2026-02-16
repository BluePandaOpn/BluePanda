"""
BluePanda Metadata
- Version: v0.5
- Node Type: UI Node Component
- Location: BluePanda/Nodos/Panel.py
- Purpose: Provides panel styling features like border radius, border, and opacity.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
from .Color2d import Color2d


class Panel:
    """
    Componente decorativo para la interfaz.
    Permite crear fondos con bordes, redondeados o transparencias.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.border_radius = 0
        self.border_width = 0
        self.border_color = (255, 255, 255)
        self.opacity = 255

    def setup_panel(self):
        """Aplica los efectos visuales al panel."""
        cfg = getattr(self, "_internal_cfg", {})
        self.border_radius = cfg.get("border_radius", 0)
        self.border_width = cfg.get("border_width", 0)
        self.opacity = cfg.get("opacity", 255)
        self.border_color = Color2d.coerce(cfg.get("border_color", self.border_color), self.border_color)

        if self.opacity < 255:
            self.image.set_alpha(self.opacity)

    def draw_border(self, surface):
        """Dibuja un borde opcional alrededor del panel."""
        if self.border_width > 0:
            pygame.draw.rect(
                surface,
                self.border_color,
                self.rect,
                self.border_width,
                self.border_radius,
            )

