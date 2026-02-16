import pygame
from BluePanda.main import instance

class Area2D:
    """
    Componente sensor. Detecta objetos pero no bloquea el paso.
    Ideal para monedas, zonas de muerte o interruptores.
    """

    def on_body_entered(self, callback):
        """
        Ejecuta una función (callback) cuando un objeto entra en el área.
        Ejemplo: self.on_body_entered(self.mi_funcion)
        """
        bodies = self.get_overlapping_bodies()
        for body in bodies:
            # Si el objeto tiene una marca de que no ha sido procesado
            if not hasattr(body, f"_in_area_{id(self)}"):
                setattr(body, f"_in_area_{id(self)}", True)
                callback(body)

    def on_body_exited(self, callback):
        """Ejecuta una función cuando un objeto sale del área."""
        # Lógica para detectar la salida (opcional para juegos simples)
        pass

    def get_overlapping_bodies(self):
        """Retorna lista de objetos tocando el área actualmente."""
        if not hasattr(self, "rect"): return []
        
        collisions = pygame.sprite.spritecollide(self, instance.nodes, False)
        return [obj for obj in collisions if obj != self]

    def overlaps(self, other_node):
        """Consulta rápida: ¿Estoy tocando a este nodo ahora mismo?"""
        return self.rect.colliderect(other_node.rect)