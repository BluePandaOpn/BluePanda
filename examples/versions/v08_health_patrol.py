"""
Version 08: health + patrol enemy.
Run: python examples/versions/v08_health_patrol.py
"""
import random

from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    CharacterBody2D,
    CollisionShape2D,
    HealthNode,
    PatrolNode2D,
    Area2D,
    Input,
    run_game,
    Color2d,
    instance,
)


class V08Config(Config):
    width = 1080
    height = 640
    fps = 60
    bg_color = Color2d("#0B1021").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V08 Health Patrol"


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

    @HealthNode
    def stats():
        max_health = 100
        health = 100

    @Sprite2D
    def look():
        width = 40
        height = 40
        color = Color2d("#38BDF8").to_rgb()

    def update(self):
        super().update()
        self.pos.x = max(0, min(1080 - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(640 - self.rect.height, self.pos.y))
        self.rect.topleft = (self.pos.x, self.pos.y)

    def on_died(self):
        instance.running = False


class Enemy(Nodo2D):
    @PatrolNode2D
    def patrol():
        patrol_axis = "x"
        patrol_left = 180
        patrol_right = 940
        patrol_speed = 180

    @CollisionShape2D
    def collider():
        pass

    @Sprite2D
    def look():
        width = 56
        height = 56
        color = Color2d("#EF4444").to_rgb()


class Medkit(Nodo2D):
    @Area2D
    def sensor():
        pass

    @Sprite2D
    def look():
        width = 20
        height = 20
        color = Color2d("#34D399").to_rgb()

    def update(self):
        super().update()
        self.on_body_entered(self._heal)

    def _heal(self, body):
        if isinstance(body, Player):
            body.heal(20)
            self.queue_free()


class Control(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"

    def __init__(self, player, enemy, *args, **kwargs):
        self.player = player
        self.enemy = enemy
        super().__init__(*args, **kwargs)
        self.cooldown = 0.0

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        self.cooldown = max(0.0, self.cooldown - instance.dt)
        if self.cooldown <= 0 and self.player.is_colliding_with(self.enemy):
            self.player.take_damage(10)
            self.cooldown = 0.4
        super().update()


if __name__ == "__main__":
    Input.bind_action("up", "w", "up")
    Input.bind_action("down", "s", "down")
    Input.bind_action("left", "a", "left")
    Input.bind_action("right", "d", "right")

    player = Player(100, 100)
    enemy = Enemy(260, 320)
    for i in range(5):
        Medkit(random.randint(100, 980), random.randint(120, 580), name=f"med{i}")
    Control(player, enemy, 0, 0)
    run_game(V08Config)
