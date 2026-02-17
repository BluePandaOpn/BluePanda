"""
BluePanda Advanced 04
Declarative decorators: OnReady, OnEvent, OnSignal.

Run:
    python examples/advanced_04_declarative_events_signals.py
"""
from BluePanda import (
    Color2d,
    Config,
    Input,
    Nodo2D,
    OnEvent,
    OnReady,
    OnSignal,
    Sprite2D,
    WindowSettings,
    instance,
    run_game,
)


class DemoConfig(Config):
    width = 980
    height = 560
    fps = 60
    bg_color = Color2d("#0E1323").to_rgb()

    Windows = WindowSettings()
    Windows.Name = "BluePanda Advanced 04 - Declarative Events/Signals"
    Windows.Resizable = False


class PulseBox(Nodo2D):
    @Sprite2D
    def look():
        width = 120
        height = 120
        color = Color2d("#38BDF8").to_rgb()

    @OnReady
    def setup(self):
        # Emit local signal repeatedly via scheduler.
        instance.schedule(0.5, lambda: self.emit_signal("pulse", self), repeat=True, interval=0.5)

    @OnSignal("pulse")
    def on_pulse(self, _node):
        self.set_color(Color2d.random())

    @OnEvent("shake")
    def on_shake(self):
        instance.tween(self, "pos.x", self.pos.x + 20, 0.08, ease="ease_out")
        instance.tween(self, "pos.x", self.pos.x - 20, 0.16, ease="ease_in_out")
        instance.tween(self, "pos.x", self.pos.x, 0.08, ease="ease_in")


class Controller(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"

    @OnReady
    def initialize(self):
        self.is_ui = True
        self.visible = False
        self.font = instance.resources.load_font(size=22)
        self.small = instance.resources.load_font(size=18)

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        if Input.is_just_pressed("space"):
            instance.tree.emit("shake")
        super().update()

    def draw(self, surface):
        line1 = self.font.render("Declarative Hooks Active", True, (240, 240, 250))
        line2 = self.small.render("SPACE emits global 'shake' event | ESC quit", True, (180, 190, 210))
        surface.blit(line1, (16, 14))
        surface.blit(line2, (16, 46))


if __name__ == "__main__":
    PulseBox(430, 220, name="pulse_box")
    Controller(0, 0, name="controller")
    run_game(DemoConfig)
