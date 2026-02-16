import pygame
from BluePanda.main import instance

class AnimatedSprite2D:
    """
    Componente para animaciones basadas en Spritesheets/Atlas.
    """
    def __init__(self):
        self.frames = []
        self.current_frame = 0
        self.animation_speed = 0.1 # Segundos por cuadro
        self.timer = 0
        self.playing = True

    def load_atlas(self, path, frame_width, frame_height, total_frames):
        """
        Corta el atlas/spritesheet en cuadros individuales.
        """
        sheet = pygame.image.load(path).convert_alpha()
        self.frames = []
        
        # Cortar la imagen por filas/columnas
        sheet_width, sheet_height = sheet.get_size()
        cols = sheet_width // frame_width
        
        for i in range(total_frames):
            x = (i % cols) * frame_width
            y = (i // cols) * frame_height
            # Extraer el pedacito de imagen
            frame_surf = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            frame_surf.blit(sheet, (0, 0), (x, y, frame_width, frame_height))
            self.frames.append(frame_surf)
        
        if self.frames:
            self.image = self.frames[0]
            self.rect = self.image.get_rect()

    def update_animation(self):
        """Avanza los cuadros de la animación usando Delta Time"""
        if not self.playing or not self.frames:
            return

        self.timer += instance.dt
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    def play(self): self.playing = True
    def stop(self): self.playing = False