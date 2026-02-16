"""
BluePanda Metadata
- Version: v0.5
- Node Type: UI Node Component
- Location: BluePanda/Nodos/Button.py
- Purpose: Implements clickable button behavior with hover/press visual states.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
from ...utils.color import Color2d


class Button:
    """
    Componente de interfaz (UI).
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_hovered = False
        self.is_pressed = False
        self.on_click_callback = None

        self.color_normal = (100, 100, 100)
        self.color_hover = (150, 150, 150)
        self.color_pressed = (200, 200, 200)

        cfg = getattr(self, "_internal_cfg", {})
        if "color_normal" in cfg:
            self.color_normal = Color2d.coerce(cfg["color_normal"], self.color_normal)
        if "color_hover" in cfg:
            self.color_hover = Color2d.coerce(cfg["color_hover"], self.color_hover)
        if "color_pressed" in cfg:
            self.color_pressed = Color2d.coerce(cfg["color_pressed"], self.color_pressed)

    def connect_click(self, func):
        self.on_click_callback = func

    def update_button(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        self.is_hovered = self.rect.collidepoint(mouse_pos)

        if self.is_hovered:
            if mouse_buttons[0]:
                if not self.is_pressed:
                    self.is_pressed = True
                    if self.on_click_callback:
                        self.on_click_callback()
            else:
                self.is_pressed = False

            self.image.fill(self.color_pressed if self.is_pressed else self.color_hover)
        else:
            self.is_pressed = False
            self.image.fill(self.color_normal)


