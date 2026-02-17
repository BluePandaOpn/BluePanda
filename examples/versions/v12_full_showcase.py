"""
Version 12: full showcase.
Run: python examples/versions/v12_full_showcase.py
"""
import random

from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    CharacterBody2D,
    CollisionShape2D,
    Area2D,
    HealthNode,
    PatrolNode2D,
    ParticleEmitterNode2D,
    OnEvent,
    OnReady,
    Input,
    Camera2D,
    run_game,
    Color2d,
    instance,
)

WORLD_W = 1800
WORLD_H = 1200
STAR_TOTAL = 12


class V12Config(Config):
    width = 1100
    height = 680
    fps = 60
    bg_color = Color2d("#090F1F").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V12 Full Showcase"


class World(Nodo2D):
    @Sprite2D
    def look():
        width = WORLD_W
        height = WORLD_H
        color = Color2d("#0F172A").to_rgb()


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 300
        input_type = "actions"
        action_up = "up"
        action_down = "down"
        action_left = "left"
        action_right = "right"

    @CollisionShape2D
    def collider():
        pass

    @HealthNode
    def hp():
        max_health = 100
        health = 100

    @ParticleEmitterNode2D
    def fx():
        emitting = True
        emit_rate = 12
        particle_lifetime = 0.55
        particle_size = 2
        particle_speed = 80
        gravity = 12
        particle_color = Color2d("#7DD3FC").to_rgb()

    @Sprite2D
    def look():
        width = 42
        height = 42
        color = Color2d("#38BDF8").to_rgb()

    def update(self):
        prev = self.pos.copy()
        super().update()
        self.pos.x = max(0, min(WORLD_W - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(WORLD_H - self.rect.height, self.pos.y))
        self.rect.topleft = (self.pos.x, self.pos.y)
        for w in instance.tree.get_nodes_in_group("walls"):
            if self.is_colliding_with(w):
                self.pos = prev
                self.rect.topleft = (self.pos.x, self.pos.y)
                break


class Enemy(Nodo2D):
    @PatrolNode2D
    def patrol():
        patrol_axis = "x"
        patrol_left = 240
        patrol_right = 1500
        patrol_speed = 180

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


class Star(Nodo2D):
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
        self.on_body_entered(self._pick)

    def _pick(self, body):
        if isinstance(body, Player):
            instance.tree.emit("star_collected")
            self.queue_free()


class Wall(Nodo2D):
    @CollisionShape2D
    def collider():
        pass

    @Sprite2D
    def look():
        color = Color2d("#334155").to_rgb()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_to_group("walls")


class Hud(Nodo2D):
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
        self.score = 0

    @OnReady
    def boot(self):
        instance.schedule(0.35, self._damage_check, repeat=True, interval=0.35)

    @OnEvent("star_collected")
    def on_star(self):
        self.score += 1
        if self.score >= STAR_TOTAL:
            instance.running = False

    def _damage_check(self):
        for e in instance.tree.get_nodes_in_group("enemies"):
            if self.player.is_colliding_with(e):
                self.player.take_damage(8)
                break
        if self.player.health <= 0:
            instance.running = False

    def draw(self, surface):
        line1 = self.font.render(f"HP: {self.player.health}/100  Stars: {self.score}/{STAR_TOTAL}", True, (245, 245, 250))
        line2 = self.small.render("WASD/Arrows move | SPACE pause | ESC quit", True, (180, 190, 210))
        surface.blit(line1, (14, 12))
        surface.blit(line2, (14, 42))


class Control(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        if Input.is_just_pressed("space"):
            instance.toggle_pause()
        super().update()


if __name__ == "__main__":
    Input.bind_action("up", "w", "up")
    Input.bind_action("down", "s", "down")
    Input.bind_action("left", "a", "left")
    Input.bind_action("right", "d", "right")

    World(0, 0)
    player = Player(140, 140, name="player")
    Enemy(420, 420)

    Wall(0, 0, WORLD_W, 30)
    Wall(0, WORLD_H - 30, WORLD_W, 30)
    Wall(0, 0, 30, WORLD_H)
    Wall(WORLD_W - 30, 0, 30, WORLD_H)
    Wall(650, 280, 500, 28)
    Wall(920, 580, 28, 360)

    for i in range(STAR_TOTAL):
        Star(random.randint(80, WORLD_W - 100), random.randint(80, WORLD_H - 100), name=f"star_{i}")

    Hud(player, 0, 0)
    Control(0, 0)
    Camera2D(target=player)
    run_game(V12Config)
