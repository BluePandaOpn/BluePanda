"""
Version 02: player movement.
Run: python examples/versions/v02_player_move.py
"""
from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    CharacterBody2D,
    Input,
    run_game,
    Color2d,
    instance,
)


class V02Config(Config):
    width = 960
    height = 560
    fps = 60
    bg_color = Color2d("#0B1220").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V02 Movement"


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 250
        input_type = "actions"
        action_up = "up"
        action_down = "down"
        action_left = "left"
        action_right = "right"

    @Sprite2D
    def look():
        width = 44
        height = 44
        color = Color2d("#22D3EE").to_rgb()

    def update(self):
        super().update()
        self.pos.x = max(0, min(960 - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(560 - self.rect.height, self.pos.y))
        self.rect.topleft = (self.pos.x, self.pos.y)


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
    Input.bind_action("up", "w", "up")
    Input.bind_action("down", "s", "down")
    Input.bind_action("left", "a", "left")
    Input.bind_action("right", "d", "right")

    Player(120, 120)
    ExitControl(0, 0)
    run_game(V02Config)
