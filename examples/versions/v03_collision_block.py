"""
Version 03: collision with blocks.
Run: python examples/versions/v03_collision_block.py
"""
from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    CharacterBody2D,
    CollisionShape2D,
    Input,
    run_game,
    Color2d,
    instance,
)


class V03Config(Config):
    width = 980
    height = 600
    fps = 60
    bg_color = Color2d("#111827").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V03 Collision"


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 230
        input_type = "actions"
        action_up = "up"
        action_down = "down"
        action_left = "left"
        action_right = "right"

    @CollisionShape2D
    def collider():
        pass

    @Sprite2D
    def look():
        width = 40
        height = 40
        color = Color2d("#60A5FA").to_rgb()

    def update(self):
        prev = self.pos.copy()
        super().update()
        self.pos.x = max(0, min(980 - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(600 - self.rect.height, self.pos.y))
        self.rect.topleft = (self.pos.x, self.pos.y)

        blocks = instance.tree.get_nodes_in_group("blocks")
        for block in blocks:
            if self.is_colliding_with(block):
                self.pos = prev
                self.rect.topleft = (self.pos.x, self.pos.y)
                break


class Block(Nodo2D):
    @CollisionShape2D
    def collider():
        pass

    @Sprite2D
    def look():
        width = 220
        height = 28
        color = Color2d("#F59E0B").to_rgb()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_to_group("blocks")


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

    Player(80, 90)
    Block(280, 220)
    Block(520, 420)
    ExitControl(0, 0)
    run_game(V03Config)
