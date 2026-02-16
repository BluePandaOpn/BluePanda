import pygame
from BluePanda.main import instance

class Button:
    """
    Componente de Interfaz (UI). 
    """
    # Usamos *args y **kwargs para capturar x, y, color, etc., 
    # y pasárselos al siguiente (Nodo2D)
    def __init__(self, *args, **kwargs):
        # Inicializamos el siguiente en la cadena (Nodo2D / Sprite)
        super().__init__(*args, **kwargs)
        
        self.is_hovered = False
        self.is_pressed = False
        self.on_click_callback = None
        
        # Colores por defecto (se pueden sobrescribir)
        self.color_normal = (100, 100, 100)
        self.color_hover = (150, 150, 150)
        self.color_pressed = (200, 200, 200)
        
        # Si el usuario definió colores en la etiqueta @ButtonNode
        cfg = getattr(self, "_INTERNAL_CFG", {})
        if "color_normal" in cfg: self.color_normal = cfg["color_normal"]
        if "color_hover" in cfg: self.color_hover = cfg["color_hover"]
        if "color_pressed" in cfg: self.color_pressed = cfg["color_pressed"]

    def connect_click(self, func):
        self.on_click_callback = func

    def update_button(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        # Usamos el rect de Nodo2D para la colisión
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