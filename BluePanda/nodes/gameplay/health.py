"""
Gameplay mixin: health and damage handling with optional callbacks/signals.
"""


class Health:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_hp = getattr(self, "max_health", 100)
        self.max_health = max(1, int(max_hp))
        current = getattr(self, "health", self.max_health)
        self.health = max(0, min(self.max_health, int(current)))
        self.invulnerable = bool(getattr(self, "invulnerable", False))

    def is_alive(self):
        return self.health > 0

    def set_health(self, value):
        self.health = max(0, min(self.max_health, int(value)))

    def heal(self, amount):
        amount = max(0, int(amount))
        self.set_health(self.health + amount)
        if hasattr(self, "emit_signal"):
            self.emit_signal("healed", self, amount, self.health)
        if hasattr(self, "on_healed"):
            self.on_healed(amount)

    def take_damage(self, amount):
        if self.invulnerable:
            return
        amount = max(0, int(amount))
        if amount == 0:
            return
        self.set_health(self.health - amount)
        if hasattr(self, "emit_signal"):
            self.emit_signal("damaged", self, amount, self.health)
        if hasattr(self, "on_damaged"):
            self.on_damaged(amount)
        if self.health <= 0:
            if hasattr(self, "emit_signal"):
                self.emit_signal("died", self)
            if hasattr(self, "on_died"):
                self.on_died()
