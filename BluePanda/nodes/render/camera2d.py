"""
BluePanda Metadata
- Version: v0.5
- Node Type: Camera Node Component
- Location: BluePanda/Nodos/Camera2d.py
- Purpose: Tracks a target and applies smooth world-to-screen offsets.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
from ...core.engine import instance

class Camera2D:
    """
    Componente que permite que la pantalla siga a un objetivo.
    """
    def __init__(self, target=None):
        self.target = target
        self.offset = pygame.Vector2(0, 0)
        self.smoothness = 0.1 # Suavizado (0.1 = lento, 1.0 = instantáneo)
        
        # Guardamos la cámara en el motor para que los demás nodos la consulten
        instance.camera = self

    def update_camera(self):
        """Calcula el desplazamiento necesario para centrar al objetivo"""
        if self.target:
            # Calculamos el centro de la pantalla
            screen_center = pygame.Vector2(instance.width / 2, instance.height / 2)
            
            # El destino es la posición del objetivo menos el centro de la pantalla
            target_pos = self.target.pos + pygame.Vector2(self.target.rect.width/2, self.target.rect.height/2)
            dest = target_pos - screen_center

            # Aplicamos un suavizado (Lerp) para que la cámara no sea brusca
            self.offset.x += (dest.x - self.offset.x) * self.smoothness
            self.offset.y += (dest.y - self.offset.y) * self.smoothness

    def apply(self, rect):
        """Mueve un rectángulo según el desplazamiento de la cámara"""
        return rect.move(-self.offset.x, -self.offset.y)

