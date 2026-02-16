"""
BluePanda Metadata
- Version: v0.5
- Node Type: Collision Node Component
- Location: BluePanda/Nodos/CollisionShape2D.py
- Purpose: Adds overlap/collision query helpers for nodes.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
from ...core.engine import instance

class CollisionShape2D:
    """
    Componente que añade capacidades de detección de colisiones.
    Se inyecta automáticamente cuando el usuario usa @CollisionShape2D.
    """

    def is_colliding_with(self, other_node):
        """
        Comprueba si este nodo está tocando a otro nodo específico.
        """
        if hasattr(self, "rect") and hasattr(other_node, "rect"):
            return self.rect.colliderect(other_node.rect)
        return False

    def get_overlapping_bodies(self):
        """
        Devuelve una lista con todos los objetos que está tocando
        actualmente, ignorándose a sí mismo.
        """
        # Obtenemos todos los nodos del motor
        all_nodes = instance.nodes.sprites()
        
        # Filtramos para no colisionar con nosotros mismos
        # y usamos la función de Pygame para detectar colisiones en grupo
        collisions = pygame.sprite.spritecollide(self, instance.nodes, False)
        
        # Retornamos la lista quitándonos a nosotros mismos
        return [obj for obj in collisions if obj != self]

    def check_collision(self, tag_buscada=None):
        """
        Un método rápido para saber si estamos tocando algo.
        Opcionalmente, puede filtrar por una propiedad del objeto.
        """
        bodies = self.get_overlapping_bodies()
        if tag_buscada:
            return any(hasattr(b, tag_buscada) for b in bodies)
        return len(bodies) > 0

