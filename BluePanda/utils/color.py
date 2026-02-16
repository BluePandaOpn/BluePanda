"""
BluePanda Metadata
- Version: v0.5
- Node Type: Utility Node Module
- Location: BluePanda/Nodos/Color2d.py
- Purpose: Normalizes color inputs and provides helper color operations.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import random
import pygame


class Color2d:
    """Normaliza colores para el motor y ofrece utilidades de color."""

    def __init__(self, value="white"):
        self._rgb = self.parse(value)

    @staticmethod
    def _clamp_channel(value):
        channel = int(value)
        if channel < 0:
            return 0
        if channel > 255:
            return 255
        return channel

    @classmethod
    def _from_sequence(cls, value):
        if len(value) < 3:
            raise ValueError("Color sequence must have at least 3 channels")
        return (
            cls._clamp_channel(value[0]),
            cls._clamp_channel(value[1]),
            cls._clamp_channel(value[2]),
        )

    @classmethod
    def parse(cls, value):
        """Convierte distintos formatos a una tupla RGB de 3 canales."""
        if isinstance(value, Color2d):
            return value.to_rgb()

        if isinstance(value, pygame.Color):
            return (value.r, value.g, value.b)

        if isinstance(value, (list, tuple)):
            return cls._from_sequence(value)

        if isinstance(value, str):
            raw = value.strip()
            lower = raw.lower()

            if lower.startswith("rgb(") and lower.endswith(")"):
                parts = lower[4:-1].split(",")
                return cls._from_sequence([int(p.strip()) for p in parts])

            if lower.startswith("rgba(") and lower.endswith(")"):
                parts = lower[5:-1].split(",")
                return cls._from_sequence([int(p.strip()) for p in parts[:3]])

            parsed = pygame.Color(raw)
            return (parsed.r, parsed.g, parsed.b)

        raise ValueError(f"Unsupported color format: {value}")

    @classmethod
    def coerce(cls, value, default=(255, 255, 255)):
        """Intenta convertir y si falla retorna un default seguro."""
        try:
            return cls.parse(value)
        except Exception:
            return cls.parse(default)

    @classmethod
    def random(cls):
        """Genera un color aleatorio RGB."""
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    @classmethod
    def lerp(cls, color_a, color_b, t):
        """Interpola dos colores. t=0 retorna A, t=1 retorna B."""
        a = cls.coerce(color_a)
        b = cls.coerce(color_b)
        amount = max(0.0, min(1.0, float(t)))
        return (
            cls._clamp_channel(a[0] + (b[0] - a[0]) * amount),
            cls._clamp_channel(a[1] + (b[1] - a[1]) * amount),
            cls._clamp_channel(a[2] + (b[2] - a[2]) * amount),
        )

    @classmethod
    def lighten(cls, color, amount=0.1):
        """Aclara un color con amount entre 0 y 1."""
        return cls.lerp(color, (255, 255, 255), amount)

    @classmethod
    def darken(cls, color, amount=0.1):
        """Oscurece un color con amount entre 0 y 1."""
        return cls.lerp(color, (0, 0, 0), amount)

    @classmethod
    def with_alpha(cls, color, alpha=255):
        """Retorna color RGBA a partir de un color base RGB."""
        rgb = cls.coerce(color)
        return (rgb[0], rgb[1], rgb[2], cls._clamp_channel(alpha))

    def to_rgb(self):
        return tuple(self._rgb)

    def __iter__(self):
        return iter(self._rgb)

    def __repr__(self):
        return f"Color2d(rgb={self._rgb})"

