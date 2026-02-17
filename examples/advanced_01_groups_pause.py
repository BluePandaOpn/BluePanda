"""
BluePanda Advanced 01
Groups + pause system + time scale.

Run:
    python examples/advanced_01_groups_pause.py
"""
import random

from BluePanda import (
    Config,
    Input,
    Nodo2D,
    Sprite2D,
    WindowSettings,
    Color2d,
    instance,
    run_game,
)


class AdvancedConfig(Config):
    width = 1080
    height = 640
    fps = 60
    bg_color = Color2d("#111827").to_rgb()

    Windows = WindowSettings()
    Windows.Name = "BluePanda Advanced 01 - Groups Pause TimeScale"
    Windows.Resizable = False


class Mover(Nodo2D):
    @Sprite2D
    def look():
        width = 36
        height = 36
        color = Color2d.random()
        z_index = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = random.choice([-1, 1]) * random.uniform(90.0, 220.0)
        self.add_to_group("movers")

    def randomize_color(self):
        self.set_color(Color2d.random())

    def update(self):
        self.pos.x += self.vx * instance.dt
        if self.pos.x < 0:
            self.pos.x = 0
            self.vx *= -1
        elif self.pos.x + self.rect.width > AdvancedConfig.width:
            self.pos.x = AdvancedConfig.width - self.rect.width
            self.vx *= -1
        super().update()


class Controller(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"
        z_index = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_ui = True
        self.visible = False
        self.title = instance.resources.load_font(size=22)
        self.small = instance.resources.load_font(size=18)

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        if Input.is_just_pressed("space"):
            instance.toggle_pause()
        if Input.is_just_pressed("c"):
            instance.tree.call_group("movers", "randomize_color")
        if Input.is_just_pressed("1"):
            instance.set_time_scale(0.5)
        if Input.is_just_pressed("2"):
            instance.set_time_scale(1.0)
        if Input.is_just_pressed("3"):
            instance.set_time_scale(1.5)
        super().update()

    def draw(self, surface):
        line1 = self.title.render(
            f"Paused: {instance.paused} | TimeScale: {instance.time_scale:.1f}",
            True,
            (245, 245, 245),
        )
        line2 = self.small.render(
            "SPACE pause/resume | C random colors | 1/2/3 speed | ESC quit",
            True,
            (180, 190, 210),
        )
        line3 = self.small.render(
            f"Nodes in group 'movers': {len(instance.tree.get_nodes_in_group('movers'))}",
            True,
            (170, 220, 180),
        )
        surface.blit(line1, (16, 14))
        surface.blit(line2, (16, 44))
        surface.blit(line3, (16, 72))


if __name__ == "__main__":
    for _ in range(24):
        Mover(random.randint(20, 980), random.randint(120, 560))
    Controller(0, 0, name="controller")
    run_game(AdvancedConfig)
