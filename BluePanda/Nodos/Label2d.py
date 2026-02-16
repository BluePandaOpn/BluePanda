import pygame
from .Color2d import Color2d


class Label2D(pygame.sprite.Sprite):
    """
    Componente para mostrar texto en pantalla.
    """

    def __init__(self, text="Texto", font_size=24, color=(255, 255, 255)):
        super().__init__()

        self.text = text
        self.font_size = font_size
        self.font_color = Color2d.coerce(color, (255, 255, 255))
        self.font_name = None
        self.is_ui = True
        self.pos = pygame.Vector2(0, 0)

        pygame.font.init()
        self._font_obj = pygame.font.SysFont(self.font_name, self.font_size)

        self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.render_text()

    def set_text(self, new_text):
        """Cambia el texto y regenera la imagen."""
        if str(new_text) != self.text:
            self.text = str(new_text)
            self.render_text()

    def set_color(self, color):
        """Permite usar Color2d, #hex, rgb(...) o nombre para el texto."""
        self.font_color = Color2d.coerce(color, self.font_color)
        self.render_text()

    def render_text(self):
        """Convierte el texto en una imagen que Pygame pueda dibujar."""
        self.image = self._font_obj.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))

    def update(self):
        """Asegura que el rect siga a la posicion del nodo."""
        self.rect.topleft = (self.pos.x, self.pos.y)

