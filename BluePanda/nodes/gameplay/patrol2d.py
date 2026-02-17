"""
Gameplay mixin: simple 2D patrol behaviour.
"""
from ...core.engine import instance


class Patrol2D:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patrol_axis = str(getattr(self, "patrol_axis", "x")).lower()
        self.patrol_speed = float(getattr(self, "patrol_speed", 100.0))
        self.patrol_left = float(getattr(self, "patrol_left", 0.0))
        self.patrol_right = float(getattr(self, "patrol_right", 100.0))
        self.patrol_top = float(getattr(self, "patrol_top", 0.0))
        self.patrol_bottom = float(getattr(self, "patrol_bottom", 100.0))
        self.patrol_dir = 1.0
        if self.patrol_right < self.patrol_left:
            self.patrol_left, self.patrol_right = self.patrol_right, self.patrol_left
        if self.patrol_bottom < self.patrol_top:
            self.patrol_top, self.patrol_bottom = self.patrol_bottom, self.patrol_top

    def update_patrol(self):
        if self.patrol_axis == "y":
            self.pos.y += self.patrol_dir * self.patrol_speed * instance.dt
            if self.pos.y < self.patrol_top:
                self.pos.y = self.patrol_top
                self.patrol_dir *= -1.0
            elif self.pos.y > self.patrol_bottom:
                self.pos.y = self.patrol_bottom
                self.patrol_dir *= -1.0
        else:
            self.pos.x += self.patrol_dir * self.patrol_speed * instance.dt
            if self.pos.x < self.patrol_left:
                self.pos.x = self.patrol_left
                self.patrol_dir *= -1.0
            elif self.pos.x > self.patrol_right:
                self.pos.x = self.patrol_right
                self.patrol_dir *= -1.0

    def update(self):
        self.update_patrol()
        super().update()
