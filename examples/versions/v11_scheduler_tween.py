"""
Version 11: scheduler + tween.
Run: python examples/versions/v11_scheduler_tween.py
"""
from BluePanda import Config, WindowSettings, Nodo2D, Sprite2D, Input, run_game, Color2d, instance


class V11Config(Config):
    width = 1000
    height = 600
    fps = 60
    bg_color = Color2d("#0F172A").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V11 Scheduler Tween"


class Orb(Nodo2D):
    @Sprite2D
    def look():
        width = 60
        height = 60
        color = Color2d("#22D3EE").to_rgb()


class Control(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"

    def __init__(self, orb, *args, **kwargs):
        self.orb = orb
        super().__init__(*args, **kwargs)
        instance.schedule(0.3, self._pulse, repeat=True, interval=0.3)

    def _pulse(self):
        nx = 120 if self.orb.pos.x > 500 else 840
        ny = 120 if self.orb.pos.y > 300 else 460
        instance.tween(self.orb, "pos.x", nx, 0.28, ease="ease_in_out")
        instance.tween(self.orb, "pos.y", ny, 0.28, ease="ease_in_out")

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        super().update()


if __name__ == "__main__":
    orb = Orb(120, 120)
    Control(orb, 0, 0)
    run_game(V11Config)
