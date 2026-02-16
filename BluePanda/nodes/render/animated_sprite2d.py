"""
BluePanda Metadata
- Version: v0.5
- Node Type: Animation Node Component
- Location: BluePanda/Nodos/AnimatedSprite2D.py
- Purpose: Handles atlas frame slicing and animation playback.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
from ...core.engine import instance


class AnimatedSprite2D:
    """
    Componente para animaciones basadas en Spritesheets/Atlas.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frames = []
        self.current_frame = 0
        self.animation_speed = 0.1
        self.timer = 0
        self.playing = True

    def load_atlas(self, path, frame_width, frame_height, total_frames):
        """Corta el atlas/spritesheet en cuadros individuales."""
        sheet = instance.assets.load_image(path, use_alpha=True)
        self.frames = []

        sheet_width, sheet_height = sheet.get_size()
        cols = max(1, sheet_width // frame_width)

        for i in range(max(1, total_frames)):
            x = (i % cols) * frame_width
            y = (i // cols) * frame_height
            frame_surf = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            frame_surf.blit(sheet, (0, 0), (x, y, frame_width, frame_height))
            self.frames.append(frame_surf)

        if self.frames:
            self.image = self.frames[0]
            self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))

    def update_animation(self):
        """Avanza los cuadros de la animacion usando Delta Time."""
        if not self.playing or not self.frames:
            return

        self.timer += instance.dt
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    def play(self):
        self.playing = True

    def stop(self):
        self.playing = False

