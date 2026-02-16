import pygame
from BluePanda.main import instance

class CharacterBody2D:
    """
    Esta clase no hereda de nada, es un 'Mixin'. 
    Su lógica se inyecta en el Nodo2D cuando se usa el @CharacterBody2D.
    """
    
    def move_and_slide(self):
        """
        Maneja el movimiento básico basado en la configuración 
        extraída por el decorador.
        """
        # Obtenemos los valores que el usuario puso en el @ o valores por defecto
        speed = getattr(self, "speed", 200)
        input_mode = getattr(self, "input_type", "wasd")
        
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)

        # Control por WASD
        if input_mode == "wasd":
            if keys[pygame.K_w]: direction.y -= 1
            if keys[pygame.K_s]: direction.y += 1
            if keys[pygame.K_a]: direction.x -= 1
            if keys[pygame.K_d]: direction.x += 1
            
        # Control por Flechas
        elif input_mode == "arrows":
            if keys[pygame.K_UP]: direction.y -= 1
            if keys[pygame.K_DOWN]: direction.y += 1
            if keys[pygame.K_LEFT]: direction.x -= 1
            if keys[pygame.K_RIGHT]: direction.x += 1

        # Normalizar vector para que no camine más rápido en diagonal
        if direction.length() > 0:
            direction = direction.normalize()

        # Aplicar el movimiento usando Delta Time (dt) para suavidad
        self.pos += direction * speed * instance.dt

    def update(self):
        """
        Sobrescribimos el update para que el movimiento sea automático.
        """
        self.move_and_slide()
        
        # Llamamos al update del Nodo2D (que actualiza el rect)
        # Usamos super() para seguir la cadena de herencia
        super().update()