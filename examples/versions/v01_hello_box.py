"""
Version 01: hello box.
Run: python examples/versions/v01_hello_box.py
"""
from BluePanda import Config, WindowSettings, Nodo2D, Sprite2D, Input, instance, run_game, Color2d


class V01Config(Config):
    width = 900
    height = 520
    fps = 60
    bg_color = Color2d("#111827").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V01 Hello"


class Box(Nodo2D):
    @Sprite2D
    def look():
        width = 180
        height = 180
        color = Color2d("#38BDF8").to_rgb()


class ExitControl(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        super().update()


if __name__ == "__main__":
    Box(360, 170)
    ExitControl(0, 0)
    run_game(V01Config)
