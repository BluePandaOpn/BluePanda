"""
BluePanda Basic 04
Clickable UI button using ButtonNode.

Run:
    python examples/basic_04_ui_button.py
"""
from BluePanda import (
    ButtonNode,
    Config,
    Input,
    Nodo2D,
    Sprite2D,
    WindowSettings,
    run_game,
    Color2d,
    instance,
)


class BasicConfig(Config):
    width = 900
    height = 560
    fps = 60
    bg_color = Color2d("#0B132B").to_rgb()

    Windows = WindowSettings()
    Windows.Name = "BluePanda Basic 04 - UI Button"
    Windows.Resizable = False


class CounterHud(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_ui = True
        self.visible = False
        self.font = instance.resources.load_font(size=30)
        self.sub = instance.resources.load_font(size=18)
        self.clicks = 0

    def draw(self, surface):
        title = self.font.render(f"Clicks: {self.clicks}", True, (240, 240, 240))
        desc = self.sub.render("Click the button  |  ESC quits", True, (190, 190, 190))
        surface.blit(title, (26, 20))
        surface.blit(desc, (26, 60))


class ClickButton(Nodo2D):
    @ButtonNode
    def button():
        color_normal = Color2d("#1C2541").to_rgb()
        color_hover = Color2d("#3A506B").to_rgb()
        color_pressed = Color2d("#5BC0BE").to_rgb()

    @Sprite2D
    def look():
        width = 260
        height = 90
        color = Color2d("#1C2541").to_rgb()

    def __init__(self, hud, *args, **kwargs):
        self._hud = hud
        super().__init__(*args, **kwargs)
        self.is_ui = True
        self.connect_click(self._on_click)
        self.font = instance.resources.load_font(size=26)

    def _on_click(self):
        self._hud.clicks += 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        text = self.font.render("PRESS", True, (245, 245, 245))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)


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
    hud = CounterHud(0, 0, name="hud")
    ClickButton(hud, 320, 220, name="button")
    ExitControl(0, 0, name="exit_control")
    run_game(BasicConfig)
