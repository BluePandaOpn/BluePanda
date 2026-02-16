"""
Elaborate BluePanda demo for SceneTree + ResourceLoader.

Run:
    python examples/scene_tree_resources_demo.py
"""
import random

from BluePanda import (
    Area2D,
    Camera2D,
    CharacterBody2D,
    CollisionShape2D,
    Config,
    Input,
    Nodo2D,
    Sprite2D,
    WindowSettings,
    instance,
    run_game,
)


WORLD_W = 2200
WORLD_H = 1400
STAR_COUNT = 16


class DemoConfig(Config):
    width = 1280
    height = 720
    fps = 60
    bg_color = (18, 24, 35)

    Windows = WindowSettings()
    Windows.Name = "BluePanda SceneTree + Resources Demo"
    Windows.Resizable = True


class World(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)


class Player(Nodo2D):
    @CharacterBody2D
    def movement():
        speed = 290
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
        width = 42
        height = 42
        color = (70, 175, 255)

    def update(self):
        prev = self.pos.copy()
        super().update()

        # Keep inside world bounds.
        self.pos.x = max(0, min(WORLD_W - self.rect.width, self.pos.x))
        self.pos.y = max(0, min(WORLD_H - self.rect.height, self.pos.y))
        self.rect.topleft = (self.pos.x, self.pos.y)

        # Blocking walls.
        walls = instance.get_node_by_path("/world/level/walls")
        if walls is not None:
            for wall in walls.get_children():
                if self.is_colliding_with(wall):
                    self.pos = prev
                    self.rect.topleft = (self.pos.x, self.pos.y)
                    break


class Star(Nodo2D):
    @Area2D
    def sensor():
        pass

    @Sprite2D
    def look():
        width = 22
        height = 22
        color = (255, 220, 90)

    def update(self):
        super().update()
        self.on_body_entered(self._picked)

    def _picked(self, body):
        if not isinstance(body, Player):
            return
        instance.tree.emit("star_collected", self)
        self.kill()


class Sentinel(Nodo2D):
    @Area2D
    def sensor():
        pass

    @Sprite2D
    def look():
        width = 64
        height = 64
        color = (230, 80, 80)

    def update(self):
        # Simple patrol logic.
        self.pos.x += self.vx * instance.dt
        if self.pos.x < self.left_x or self.pos.x > self.right_x:
            self.vx *= -1
        super().update()

        self.on_body_entered(self._touch_player)

    def _touch_player(self, body):
        if isinstance(body, Player):
            instance.tree.emit("player_hit", body)


class Wall(Nodo2D):
    @CollisionShape2D
    def collider():
        pass

    @Sprite2D
    def look():
        color = (45, 65, 100)


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
        self.font = instance.resources.load_font(size=24)
        self.small = instance.resources.load_font(size=18)
        self.pickup_sfx = instance.resources.load_sound("examples/assets/pickup.wav", volume=0.3)
        self.score = 0
        self.remaining = STAR_COUNT
        self.state = "Collect all stars"
        self.lore = instance.resources.load_text("examples/data/lore.txt").strip()

    def on_star_collected(self, _star):
        self.score += 1
        self.remaining = max(0, STAR_COUNT - self.score)
        self.state = "Good run"
        if self.pickup_sfx is not None:
            self.pickup_sfx.play()
        if self.remaining == 0:
            self.state = "Stage complete"
            instance.running = False

    def on_player_hit(self, _player):
        self.state = "You were hit"
        instance.running = False

    def draw(self, surface):
        line1 = self.font.render(f"Score: {self.score}/{STAR_COUNT}", True, (245, 245, 250))
        line2 = self.small.render(f"State: {self.state}", True, (200, 220, 255))
        line3 = self.small.render(self.lore[:90], True, (200, 200, 200))
        line4 = self.small.render("Controls: WASD/Arrows | ESC to quit", True, (180, 190, 220))
        surface.blit(line1, (16, 14))
        surface.blit(line2, (16, 44))
        surface.blit(line3, (16, 70))
        surface.blit(line4, (16, 94))


class CameraAnchor(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)


class EngineControls(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        super().update()


def make_wall(parent, x, y, w, h, name=None):
    wall = Wall(x, y, w, h, name=name)
    parent.add_child(wall)
    return wall


def build_scene():
    # Custom input mappings through engine input layer.
    Input.bind_action("move_up", "w", "up")
    Input.bind_action("move_down", "s", "down")
    Input.bind_action("move_left", "a", "left")
    Input.bind_action("move_right", "d", "right")

    # Resource system usage.
    _ = instance.resources.load_texture("examples/assets/player.png", size=(42, 42))
    _ = instance.resources.load_sound("examples/assets/pickup.wav", volume=0.3)

    world = World(0, 0, name="world")
    level = World(0, 0, name="level")
    world.add_child(level)

    walls = World(0, 0, name="walls")
    stars = World(0, 0, name="stars")
    actors = World(0, 0, name="actors")
    level.add_child(walls)
    level.add_child(stars)
    level.add_child(actors)

    make_wall(walls, 0, 0, WORLD_W, 36, "north")
    make_wall(walls, 0, WORLD_H - 36, WORLD_W, 36, "south")
    make_wall(walls, 0, 0, 36, WORLD_H, "west")
    make_wall(walls, WORLD_W - 36, 0, 36, WORLD_H, "east")

    make_wall(walls, 500, 300, 600, 32)
    make_wall(walls, 960, 580, 32, 480)
    make_wall(walls, 1300, 920, 500, 32)

    player = Player(180, 150, name="player")
    actors.add_child(player)

    sentinel = Sentinel(780, 480, name="sentinel")
    sentinel.left_x = 640
    sentinel.right_x = 1200
    sentinel.vx = 170
    actors.add_child(sentinel)

    for i in range(STAR_COUNT):
        star = Star(random.randint(70, WORLD_W - 90), random.randint(70, WORLD_H - 90), name=f"star_{i}")
        stars.add_child(star)

    hud = Hud(0, 0, name="hud")
    controls = EngineControls(0, 0, name="controls")

    # SceneTree global events.
    instance.tree.connect("star_collected", hud.on_star_collected)
    instance.tree.connect("player_hit", hud.on_player_hit)

    # Scene path lookup.
    path_player = instance.get_node_by_path("/world/level/actors/player")
    if path_player is None:
        raise RuntimeError("SceneTree path lookup failed for player")

    # Camera target node.
    anchor = CameraAnchor(path_player.pos.x, path_player.pos.y, name="camera_anchor")
    actors.add_child(anchor)

    class AnchorSync(Nodo2D):
        @Sprite2D
        def look():
            width = 1
            height = 1
            color = (0, 0, 0, 0)

        def update(self):
            anchor.pos.x = path_player.pos.x + path_player.rect.width * 0.5
            anchor.pos.y = path_player.pos.y + path_player.rect.height * 0.5
            super().update()

    sync = AnchorSync(0, 0, name="anchor_sync")
    actors.add_child(sync)

    Camera2D(target=anchor)


if __name__ == "__main__":
    build_scene()
    run_game(DemoConfig)
