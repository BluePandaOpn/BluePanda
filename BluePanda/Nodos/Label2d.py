
import pygame
from BluePanda.main import instance

class Label2D(pygame.sprite.Sprite):
    """
    Componente para mostrar texto en pantalla.
    """
    def __init__(self, text="Texto", font_size=24, color=(255, 255, 255)):
        super().__init__() # Inicializa el Sprite de Pygame
        
        self.text = text
        self.font_size = font_size
        self.font_color = color
        self.font_name = None # Usa la fuente por defecto de sistema
        self.is_ui = True  # Para que la cámara no lo mueva
        self.pos = pygame.Vector2(0, 0)
        
        # Inicializamos la fuente de Pygame
        pygame.font.init()
        self._font_obj = pygame.font.SysFont(self.font_name, self.font_size)
        
        # Estas dos variables son OBLIGATORIAS para Pygame Sprite
        self.image = pygame.Surface((1, 1)) 
        self.rect = self.image.get_rect()
        
        self.render_text()

    def set_text(self, new_text):
        """Cambia el texto y regenera la imagen"""
        if str(new_text) != self.text:
            self.text = str(new_text)
            self.render_text()

    def render_text(self):
        """Convierte el texto en una imagen que Pygame pueda dibujar"""
        self.image = self._font_obj.render(self.text, True, self.font_color)
        # Actualizamos el rect para que las colisiones o posición sean correctas
        self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))

    def update(self):
        """Asegura que el rect siga a la posición del nodo"""
        self.rect.topleft = (self.pos.x, self.pos.y)