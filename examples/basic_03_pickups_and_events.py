"""
BluePanda Basic 03
Pickups using Area2D + global events via SceneTree.

Run:
    python examples/basic_03_pickups_and_events.py
"""
import random

from BluePanda import (
    Area2D,
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


WORLD_W = 1180
WORLD_H = 700
COIN_COUNT = 12


class BasicConfig(Config):
    width = 1000
    height = 620
    fps = 60
    bg_color = Color2d("#111827").to_rgb()

    Windows = WindowSettings()
    Windows.Name = "BluePanda Basic 03 - Pickups and Events"
    Windows.Resizable = False


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 260
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
        super().update()
        self.pos.x = max(0, min(WORLD_W - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(WORLD_H - self.rect.height, self.pos.y))
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
        self.on_body_entered(self._on_pickup)

    def _on_pickup(self, body):
        if not isinstance(body, Player):
            return
        instance.tree.emit("coin_collected")
        self.kill()


class Hud(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_ui = True
        self.visible = False
        self.score = 0
        self.font = instance.resources.load_font(size=24)
        self.small = instance.resources.load_font(size=18)

    def on_coin_collected(self):
        self.score += 1
        if self.score >= COIN_COUNT:
            instance.running = False

    def draw(self, surface):
        top = self.font.render(f"Coins: {self.score}/{COIN_COUNT}", True, (240, 240, 240))
        help_text = self.small.render("WASD/Arrows move  |  ESC quits", True, (180, 180, 180))
        surface.blit(top, (16, 12))
        surface.blit(help_text, (16, 44))


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

    player = Player(80, 80, name="player")
    hud = Hud(0, 0, name="hud")
    ExitControl(0, 0, name="exit_control")

    for i in range(COIN_COUNT):
        Coin(random.randint(60, WORLD_W - 80), random.randint(60, WORLD_H - 80), name=f"coin_{i}")

    instance.tree.connect("coin_collected", hud.on_coin_collected)

    run_game(BasicConfig)
