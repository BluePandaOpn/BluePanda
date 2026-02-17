"""
BluePanda Basic 01
Static box + ESC to quit.

Run:
    python examples/basic_01_hello_box.py
"""
from BluePanda import Config, Input, Nodo2D, Sprite2D, WindowSettings, run_game, Color2d, instance


class BasicConfig(Config):
    width = 960
    height = 540
    fps = 60
    bg_color = Color2d("#101820").to_rgb()

    Windows = WindowSettings()
    Windows.Name = "BluePanda Basic 01 - Hello Box"
    Windows.Resizable = False


class HelloBox(Nodo2D):
    @Sprite2D
    def look():
        width = 220
        height = 220
        color = Color2d("#5BC0EB").to_rgb()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_font = instance.resources.load_font(size=22)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        text = self.label_font.render("HELLO BLUEPANDA", True, (245, 245, 245))
        surface.blit(text, (self.rect.x + 12, self.rect.y + self.rect.height // 2 - 10))


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
    HelloBox(370, 160, name="hello_box")
    ExitControl(0, 0, name="exit_control")
    run_game(BasicConfig)
