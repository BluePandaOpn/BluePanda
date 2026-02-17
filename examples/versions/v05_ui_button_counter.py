"""
Version 05: UI button counter.
Run: python examples/versions/v05_ui_button_counter.py
"""
from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    ButtonNode,
    Input,
    run_game,
    Color2d,
    instance,
)


class V05Config(Config):
    width = 900
    height = 560
    fps = 60
    bg_color = Color2d("#0B132B").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V05 UI"


class Hud(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_ui = True
        self.visible = False
        self.count = 0
        self.font = instance.resources.load_font(size=28)

    def draw(self, surface):
        surface.blit(self.font.render(f"Clicks: {self.count}", True, (240, 240, 245)), (20, 20))


class Btn(Nodo2D):
    @ButtonNode
    def btn():
        color_normal = Color2d("#1C2541").to_rgb()
        color_hover = Color2d("#3A506B").to_rgb()
        color_pressed = Color2d("#5BC0BE").to_rgb()

    @Sprite2D
    def look():
        width = 250
        height = 90
        color = Color2d("#1C2541").to_rgb()

    def __init__(self, hud, *args, **kwargs):
        self.hud = hud
        super().__init__(*args, **kwargs)
        self.is_ui = True
        self.connect_click(self.on_click)

    def on_click(self):
        self.hud.count += 1


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
    hud = Hud(0, 0)
    Btn(hud, 320, 220)
    ExitControl(0, 0)
    run_game(V05Config)
