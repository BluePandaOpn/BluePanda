"""
BluePanda Metadata
- Version: v0.5
- Node Type: Utility Node Module
- Location: BluePanda/Nodos/Math2D.py
- Purpose: Provides reusable math helpers for movement, interpolation, and vectors.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import math
import pygame


class Math2D:
    """Utilidades matematicas para mantenimiento del motor."""

    @staticmethod
    def clamp(value, minimum, maximum):
        return max(minimum, min(maximum, value))

    @staticmethod
    def lerp(a, b, t):
        return a + (b - a) * Math2D.clamp(float(t), 0.0, 1.0)

    @staticmethod
    def remap(value, in_min, in_max, out_min, out_max):
        if in_max == in_min:
            return out_min
        amount = (value - in_min) / (in_max - in_min)
        return Math2D.lerp(out_min, out_max, amount)

    @staticmethod
    def distance(a, b):
        va = pygame.Vector2(a)
        vb = pygame.Vector2(b)
        return va.distance_to(vb)

    @staticmethod
    def move_toward(current, target, max_delta):
        diff = target - current
        if abs(diff) <= max_delta:
            return target
        return current + math.copysign(max_delta, diff)

    @staticmethod
    def normalized(vector):
        v = pygame.Vector2(vector)
        if v.length_squared() == 0:
            return pygame.Vector2(0, 0)
        return v.normalize()


