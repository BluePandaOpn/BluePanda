"""
Version 04: pickups and events.
Run: python examples/versions/v04_pickups_events.py
"""
import random

from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    CharacterBody2D,
    Area2D,
    Input,
    run_game,
    Color2d,
    instance,
)


COINS = 10


class V04Config(Config):
    width = 1000
    height = 620
    fps = 60
    bg_color = Color2d("#0F172A").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V04 Events"


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 240
        input_type = "actions"
        action_up = "up"
        action_down = "down"
        action_left = "left"
        action_right = "right"

    @Sprite2D
    def look():
        width = 40
        height = 40
        color = Color2d("#38BDF8").to_rgb()

    def update(self):
        super().update()
        self.pos.x = max(0, min(1000 - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(620 - self.rect.height, self.pos.y))
        self.rect.topleft = (self.pos.x, self.pos.y)


class Coin(Nodo2D):
    @Area2D
    def sensor():
        pass

    @Sprite2D
    def look():
        width = 20
        height = 20
        color = Color2d("#FDE047").to_rgb()

    def update(self):
        super().update()
        self.on_body_entered(self._picked)

    def _picked(self, body):
        if isinstance(body, Player):
            instance.tree.emit("coin_picked")
            self.queue_free()


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
        self.score = 0
        self.font = instance.resources.load_font(size=24)
        instance.tree.connect("coin_picked", self.on_coin)

    def on_coin(self):
        self.score += 1
        if self.score >= COINS:
            instance.running = False

    def draw(self, surface):
        txt = self.font.render(f"Coins: {self.score}/{COINS}", True, (240, 240, 245))
        surface.blit(txt, (12, 12))


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

    Player(90, 100)
    Hud(0, 0)
    ExitControl(0, 0)

    for i in range(COINS):
        Coin(random.randint(60, 940), random.randint(90, 560), name=f"coin_{i}")

    run_game(V04Config)
