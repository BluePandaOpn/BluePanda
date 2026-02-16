"""
BluePanda Metadata
- Version: v0.5
- Node Type: Physics Node Component
- Location: BluePanda/Nodos/PhysicsBody2D.py
- Purpose: Adds gravity, velocity, forces, damping, and collision resolution.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
from ...core.engine import instance
from ...utils.math2d import Math2D


class PhysicsBody2D:
    """
    Nodo de fisica 2D con gravedad, masa, friccion, rebote y resolucion
    basica de colisiones AABB. Requiere CollisionShape2D para detectar solapes.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cfg = getattr(self, "_internal_cfg", {})

        self.velocity = pygame.Vector2(cfg.get("velocity_x", 0.0), cfg.get("velocity_y", 0.0))
        self.gravity = pygame.Vector2(cfg.get("gravity_x", 0.0), cfg.get("gravity_y", 980.0))
        self.gravity_scale = float(cfg.get("gravity_scale", 1.0))
        self.mass = max(0.001, float(cfg.get("mass", 1.0)))
        self.restitution = Math2D.clamp(float(cfg.get("restitution", 0.05)), 0.0, 1.0)
        self.friction = Math2D.clamp(float(cfg.get("friction", 0.15)), 0.0, 1.0)
        self.linear_damping = Math2D.clamp(float(cfg.get("linear_damping", 0.02)), 0.0, 1.0)

        self.is_static = bool(cfg.get("is_static", False))
        self.enable_physics = bool(cfg.get("enable_physics", True))
        self._force_accumulator = pygame.Vector2(0, 0)

    def apply_force(self, x, y=None):
        if y is None:
            vec = pygame.Vector2(x)
        else:
            vec = pygame.Vector2(x, y)
        self._force_accumulator += vec

    def apply_impulse(self, x, y=None):
        if y is None:
            impulse = pygame.Vector2(x)
        else:
            impulse = pygame.Vector2(x, y)
        self.velocity += impulse / self.mass

    def set_static(self, value=True):
        self.is_static = bool(value)
        if self.is_static:
            self.velocity.update(0, 0)

    def _integrate_forces(self, dt):
        if self.is_static or not self.enable_physics:
            return

        acceleration = self._force_accumulator / self.mass
        self.velocity += (self.gravity * self.gravity_scale + acceleration) * dt

        damping = max(0.0, 1.0 - self.linear_damping * dt)
        self.velocity *= damping
        self._force_accumulator.update(0, 0)

    def _resolve_collision_with(self, other):
        if not hasattr(other, "rect"):
            return

        overlap = self.rect.clip(other.rect)
        if overlap.width <= 0 or overlap.height <= 0:
            return

        other_is_static = bool(getattr(other, "is_static", True))

        # Separamos por el eje de menor penetracion.
        if overlap.width < overlap.height:
            direction = -1 if self.rect.centerx < other.rect.centerx else 1
            separation = overlap.width
            if other_is_static:
                self.pos.x += direction * separation
            else:
                half = separation * 0.5
                self.pos.x += direction * half
                if hasattr(other, "pos"):
                    other.pos.x -= direction * half
            self.velocity.x = -self.velocity.x * self.restitution
            self.velocity.y *= max(0.0, 1.0 - self.friction)
        else:
            direction = -1 if self.rect.centery < other.rect.centery else 1
            separation = overlap.height
            if other_is_static:
                self.pos.y += direction * separation
            else:
                half = separation * 0.5
                self.pos.y += direction * half
                if hasattr(other, "pos"):
                    other.pos.y -= direction * half
            self.velocity.y = -self.velocity.y * self.restitution
            self.velocity.x *= max(0.0, 1.0 - self.friction)

        self.rect.topleft = (self.pos.x, self.pos.y)

    def _solve_collisions(self):
        if not hasattr(self, "get_overlapping_bodies"):
            return

        for other in self.get_overlapping_bodies():
            self._resolve_collision_with(other)

    def update_physics(self):
        dt = instance.dt
        if dt <= 0.0 or self.is_static or not self.enable_physics:
            return

        self._integrate_forces(dt)
        self.pos += self.velocity * dt
        self.rect.topleft = (self.pos.x, self.pos.y)
        self._solve_collisions()


