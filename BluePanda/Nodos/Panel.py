import pygame

class Panel:
    """
    Componente decorativo para la interfaz.
    Permite crear fondos con bordes, redondeados o transparencias.
    """
    def __init__(self):
        # Valores por defecto que se pueden cambiar en @Panel
        self.border_radius = 0
        self.border_width = 0
        self.border_color = (255, 255, 255)
        self.opacity = 255

    def setup_panel(self):
        """Aplica los efectos visuales al panel"""
        # Obtenemos la configuración
        cfg = getattr(self, "_INTERNAL_CFG", {})
        self.border_radius = cfg.get("border_radius", 0)
        self.opacity = cfg.get("opacity", 255)
        
        # Aplicamos la transparencia al sprite
        if self.opacity < 255:
            self.image.set_alpha(self.opacity)

    def draw_border(self, surface):
        """Dibuja un borde opcional alrededor del panel"""
        if self.border_width > 0:
            pygame.draw.rect(
                surface, 
                self.border_color, 
                self.rect, 
                self.border_width, 
                self.border_radius
            )