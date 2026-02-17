"""
BluePanda Advanced 02
Health system + patrol AI + pickups.

Run:
    python examples/advanced_02_patrol_health.py
"""
import random

from BluePanda import (
    Area2D,
    CharacterBody2D,
    CollisionShape2D,
    Color2d,
    Config,
    HealthNode,
    Input,
    Nodo2D,
    PatrolNode2D,
    Sprite2D,
    WindowSettings,
    instance,
    run_game,
)


WORLD_W = 1320
WORLD_H = 760


class AdvancedConfig(Config):
    width = 1080
    height = 640
    fps = 60
    bg_color = Color2d("#0B1021").to_rgb()

    Windows = WindowSettings()
    Windows.Name = "BluePanda Advanced 02 - Patrol Health"
    Windows.Resizable = False


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 280
        input_type = "actions"
        action_up = "up"
        action_down = "down"
        action_left = "left"
        action_right = "right"

    @CollisionShape2D
    def collider():
        pass

    @HealthNode
    def stats():
        max_health = 100
        health = 100

    @Sprite2D
    def look():
        width = 42
        height = 42
        color = Color2d("#38BDF8").to_rgb()

    def update(self):
        super().update()
        self.pos.x = max(0, min(WORLD_W - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(WORLD_H - self.rect.height, self.pos.y))
        self.rect.topleft = (self.pos.x, self.pos.y)

    def on_died(self):
        instance.running = False


class Enemy(Nodo2D):
    @PatrolNode2D
    def patrol():
        patrol_axis = "x"
        patrol_left = 240
        patrol_right = 1060
        patrol_speed = 170

    @CollisionShape2D
    def collider():
        pass

    @Sprite2D
    def look():
        width = 58
        height = 58
        color = Color2d("#EF4444").to_rgb()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_to_group("enemies")


class Medkit(Nodo2D):
    @Area2D
    def sensor():
        pass

    @Sprite2D
    def look():
        width = 22
        height = 22
        color = Color2d("#34D399").to_rgb()

    def update(self):
        super().update()
        self.on_body_entered(self._on_body_entered)

    def _on_body_entered(self, body):
        if isinstance(body, Player):
            body.heal(20)
            self.queue_free()


class GameController(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"

    def __init__(self, player, *args, **kwargs):
        self.player = player
        super().__init__(*args, **kwargs)
        self.is_ui = True
        self.visible = False
        self.font = instance.resources.load_font(size=24)
        self.small = instance.resources.load_font(size=18)
        self.damage_cooldown = 0.0

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False

        self.damage_cooldown = max(0.0, self.damage_cooldown - instance.dt)
        if self.damage_cooldown <= 0.0:
            for enemy in instance.tree.get_nodes_in_group("enemies"):
                if self.player.is_colliding_with(enemy):
                    self.player.take_damage(10)
                    self.damage_cooldown = 0.4
                    break
        super().update()

    def draw(self, surface):
        hp = self.player.health
        line1 = self.font.render(f"HP: {hp}/{self.player.max_health}", True, (235, 235, 245))
        line2 = self.small.render("Pick green medkits (+20). Avoid red patrol.", True, (190, 200, 210))
        line3 = self.small.render("WASD/Arrows move | ESC quit", True, (175, 180, 200))
        surface.blit(line1, (16, 12))
        surface.blit(line2, (16, 42))
        surface.blit(line3, (16, 68))


if __name__ == "__main__":
    Input.bind_action("up", "w", "up")
    Input.bind_action("down", "s", "down")
    Input.bind_action("left", "a", "left")
    Input.bind_action("right", "d", "right")

    player = Player(120, 140, name="player")
    Enemy(260, 320, name="enemy_patrol")

    for i in range(6):
        Medkit(random.randint(80, WORLD_W - 80), random.randint(100, WORLD_H - 80), name=f"medkit_{i}")

    GameController(player, 0, 0, name="controller")
    run_game(AdvancedConfig)
