"""
BluePanda Metadata
- Version: v0.5
- Node Type: Movement Node Component
- Location: BluePanda/Nodos/CharacterBody2D.py
- Purpose: Adds keyboard-based movement and frame-rate independent motion.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
from ...core.engine import instance
from ...core.input import Input

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
        speed = getattr(self, "speed", 200)
        input_mode = getattr(self, "input_type", "wasd")
        direction = pygame.Vector2(0, 0)

        if input_mode == "wasd":
            if Input.is_down("w"): direction.y -= 1
            if Input.is_down("s"): direction.y += 1
            if Input.is_down("a"): direction.x -= 1
            if Input.is_down("d"): direction.x += 1
        elif input_mode == "arrows":
            if Input.is_down("up"): direction.y -= 1
            if Input.is_down("down"): direction.y += 1
            if Input.is_down("left"): direction.x -= 1
            if Input.is_down("right"): direction.x += 1
        elif input_mode == "actions":
            if Input.action_pressed(getattr(self, "action_up", "move_up")): direction.y -= 1
            if Input.action_pressed(getattr(self, "action_down", "move_down")): direction.y += 1
            if Input.action_pressed(getattr(self, "action_left", "move_left")): direction.x -= 1
            if Input.action_pressed(getattr(self, "action_right", "move_right")): direction.x += 1

        if direction.length() > 0:
            direction = direction.normalize()

        self.pos += direction * speed * instance.dt

    def update(self):
        """
        Sobrescribimos el update para que el movimiento sea automático.
        """
        self.move_and_slide()
        
        super().update()

