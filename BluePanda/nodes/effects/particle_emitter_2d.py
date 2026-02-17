"""
Particle emitter mixin for simple effects without external dependencies.
"""
import random
import pygame
from ...core.engine import instance
from ...utils.color import Color2d


class ParticleEmitter2D:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cfg = getattr(self, "_internal_cfg", {})
        self.particles = []
        self.emitting = bool(cfg.get("emitting", True))
        self.emit_rate = float(cfg.get("emit_rate", 8.0))
        self.particle_lifetime = float(cfg.get("particle_lifetime", 0.8))
        self.particle_size = int(cfg.get("particle_size", 3))
        self.spread = float(cfg.get("spread", 100.0))
        self.particle_speed = float(cfg.get("particle_speed", 140.0))
        self.particle_color = Color2d.coerce(cfg.get("particle_color", "#ffffff"), (255, 255, 255))
        self.gravity = float(cfg.get("gravity", 0.0))
        self._emit_accum = 0.0

    def emit_particles(self, count=1):
        for _ in range(max(0, int(count))):
            angle = random.uniform(0.0, 360.0)
            speed = random.uniform(self.particle_speed * 0.5, self.particle_speed)
            vx = pygame.math.Vector2(1, 0).rotate(angle).x * speed
            vy = pygame.math.Vector2(1, 0).rotate(angle).y * speed
            self.particles.append(
                {
                    "x": float(self.rect.centerx),
                    "y": float(self.rect.centery),
                    "vx": vx,
                    "vy": vy,
                    "life": self.particle_lifetime,
                    "max_life": self.particle_lifetime,
                }
            )

    def clear_particles(self):
        self.particles.clear()

    def update_particles(self):
        if self.emitting:
            self._emit_accum += self.emit_rate * instance.dt
            if self._emit_accum >= 1.0:
                burst = int(self._emit_accum)
                self._emit_accum -= burst
                self.emit_particles(burst)

        for p in list(self.particles):
            p["life"] -= instance.dt
            if p["life"] <= 0:
                self.particles.remove(p)
                continue
            p["vy"] += self.gravity * instance.dt
            p["x"] += p["vx"] * instance.dt
            p["y"] += p["vy"] * instance.dt

    def draw_particles(self, surface):
        for p in self.particles:
            alpha_ratio = max(0.0, min(1.0, p["life"] / max(0.0001, p["max_life"])))
            alpha = int(255 * alpha_ratio)
            color = (self.particle_color[0], self.particle_color[1], self.particle_color[2], alpha)
            rect = pygame.Rect(
                int(p["x"]) - self.particle_size // 2,
                int(p["y"]) - self.particle_size // 2,
                self.particle_size,
                self.particle_size,
            )
            if instance.camera and not getattr(self, "is_ui", False):
                offset = instance.camera.apply(rect)
                surface.fill(color, offset)
            else:
                surface.fill(color, rect)

    def update(self):
        self.update_particles()
        super().update()

    def draw(self, surface):
        if hasattr(self, "image") and hasattr(self, "rect"):
            if instance.camera and not getattr(self, "is_ui", False):
                surface.blit(self.image, instance.camera.apply(self.rect))
            else:
                surface.blit(self.image, self.rect)
        self.draw_particles(surface)
