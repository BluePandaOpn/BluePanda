"""
Version 06: camera follow.
Run: python examples/versions/v06_camera_follow.py
"""
from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    CharacterBody2D,
    Camera2D,
    Input,
    run_game,
    Color2d,
    instance,
)

WORLD_W = 2200
WORLD_H = 1400


class V06Config(Config):
    width = 1000
    height = 620
    fps = 60
    bg_color = Color2d("#0F172A").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V06 Camera"


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 280
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
        self.pos.x = max(0, min(WORLD_W - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(WORLD_H - self.rect.height, self.pos.y))
        self.rect.topleft = (self.pos.x, self.pos.y)


class WorldGrid(Nodo2D):
    @Sprite2D
    def look():
        width = WORLD_W
        height = WORLD_H
        color = Color2d("#111827").to_rgb()


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
    Input.bind_action("up", "w", "up")
    Input.bind_action("down", "s", "down")
    Input.bind_action("left", "a", "left")
    Input.bind_action("right", "d", "right")

    WorldGrid(0, 0)
    player = Player(300, 300)
    Camera2D(target=player)
    ExitControl(0, 0)
    run_game(V06Config)
