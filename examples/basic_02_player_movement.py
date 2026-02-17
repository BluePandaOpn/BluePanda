"""
BluePanda Basic 02
Player movement with actions and world bounds.

Run:
    python examples/basic_02_player_movement.py
"""
from BluePanda import (
    CharacterBody2D,
    CollisionShape2D,
    Config,
    Input,
    Nodo2D,
    Sprite2D,
    WindowSettings,
    run_game,
    Color2d,
    instance,
)


WORLD_W = 1200
WORLD_H = 760


class BasicConfig(Config):
    width = 1000
    height = 640
    fps = 60
    bg_color = Color2d("#0F172A").to_rgb()

    Windows = WindowSettings()
    Windows.Name = "BluePanda Basic 02 - Movement"
    Windows.Resizable = False


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 280
        input_type = "actions"
        action_up = "move_up"
        action_down = "move_down"
        action_left = "move_left"
        action_right = "move_right"

    @CollisionShape2D
    def collider():
        pass

    @Sprite2D
    def look():
        width = 48
        height = 48
        color = Color2d("#22D3EE").to_rgb()

    def update(self):
        super().update()
        self.pos.x = max(0, min(WORLD_W - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(WORLD_H - self.rect.height, self.pos.y))
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
    Input.bind_action("move_up", "w", "up")
    Input.bind_action("move_down", "s", "down")
    Input.bind_action("move_left", "a", "left")
    Input.bind_action("move_right", "d", "right")

    Player(120, 120, name="player")
    ExitControl(0, 0, name="exit_control")
    run_game(BasicConfig)
