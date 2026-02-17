"""
Version 09: particle emitter.
Run: python examples/versions/v09_particle_emitter.py
"""
from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    ParticleEmitterNode2D,
    Input,
    run_game,
    Color2d,
    instance,
)


class V09Config(Config):
    width = 980
    height = 560
    fps = 60
    bg_color = Color2d("#0A1020").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V09 Particles"


class Emitter(Nodo2D):
    @ParticleEmitterNode2D
    def fx():
        emitting = True
        emit_rate = 26
        particle_lifetime = 0.8
        particle_size = 3
        particle_speed = 150
        gravity = 20
        particle_color = Color2d("#A7F3D0").to_rgb()

    @Sprite2D
    def look():
        width = 42
        height = 42
        color = Color2d("#22D3EE").to_rgb()

    def update(self):
        self.pos.x, self.pos.y = Input.mouse_position()
        self.pos.x -= self.rect.width * 0.5
        self.pos.y -= self.rect.height * 0.5
        if Input.mouse_down(1):
            self.emitting = True
        if Input.mouse_down(3):
            self.emitting = False
        super().update()


class ExitControl(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        super().update()


if __name__ == "__main__":
    Emitter(440, 240)
    ExitControl(0, 0)
    run_game(V09Config)
