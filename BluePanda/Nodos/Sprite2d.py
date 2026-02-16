import pygame

class Sprite2D:
    """
    Componente encargado de la manipulación visual avanzada.
    Se activa cuando el usuario usa @Sprite2D.
    """

    def flip_h(self, boolean):
        """Voltea la imagen horizontalmente (útil para girar al personaje)"""
        if hasattr(self, "image"):
            self.image = pygame.transform.flip(self.image, boolean, False)

    def flip_v(self, boolean):
        """Voltea la imagen verticalmente"""
        if hasattr(self, "image"):
            self.image = pygame.transform.flip(self.image, False, boolean)

    def set_opacity(self, alpha):
        """
        Cambia la transparencia del objeto (0 a 255).
        0 es invisible, 255 es sólido.
        """
        if hasattr(self, "image"):
            self.image.set_alpha(alpha)

    def set_scale(self, scale_x, scale_y):
        """Cambia el tamaño del sprite en tiempo real"""
        if hasattr(self, "image"):
            size = (int(self.rect.width * scale_x), int(self.rect.height * scale_y))
            self.image = pygame.transform.scale(self.image, size)
            # Actualizamos el rect para que la colisión coincida con el nuevo tamaño
            self.rect = self.image.get_rect(center=self.rect.center)