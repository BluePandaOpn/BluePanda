"""
Version 07: groups, pause and time scale.
Run: python examples/versions/v07_groups_pause_timescale.py
"""
import random

from BluePanda import Config, WindowSettings, Nodo2D, Sprite2D, Input, run_game, Color2d, instance


class V07Config(Config):
    width = 1080
    height = 640
    fps = 60
    bg_color = Color2d("#111827").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V07 Groups/Pause/TimeScale"


class Mover(Nodo2D):
    @Sprite2D
    def look():
        width = 34
        height = 34
        color = Color2d.random()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = random.choice([-1, 1]) * random.uniform(80, 220)
        self.add_to_group("movers")

    def recolor(self):
        self.set_color(Color2d.random())

    def update(self):
        self.pos.x += self.vx * instance.dt
        if self.pos.x < 0:
            self.pos.x = 0
            self.vx *= -1
        if self.pos.x + self.rect.width > 1080:
            self.pos.x = 1080 - self.rect.width
            self.vx *= -1
        super().update()


class Control(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        if Input.is_just_pressed("space"):
            instance.toggle_pause()
        if Input.is_just_pressed("c"):
            instance.tree.call_group("movers", "recolor")
        if Input.is_just_pressed("1"):
            instance.set_time_scale(0.5)
        if Input.is_just_pressed("2"):
            instance.set_time_scale(1.0)
        if Input.is_just_pressed("3"):
            instance.set_time_scale(1.5)
        super().update()


if __name__ == "__main__":
    for i in range(18):
        Mover(30 + i * 55, random.randint(140, 560), name=f"m{i}")
    Control(0, 0)
    run_game(V07Config)
