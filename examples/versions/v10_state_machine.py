"""
Version 10: state machine.
Run: python examples/versions/v10_state_machine.py
"""
import random

from BluePanda import (
    Config,
    WindowSettings,
    Nodo2D,
    Sprite2D,
    StateMachineNode,
    Input,
    run_game,
    Color2d,
    instance,
)


class V10Config(Config):
    width = 980
    height = 560
    fps = 60
    bg_color = Color2d("#0E1323").to_rgb()
    Windows = WindowSettings()
    Windows.Name = "BluePanda V10 StateMachine"


class BrainBox(Nodo2D):
    @StateMachineNode
    def machine():
        initial_state = "idle"

    @Sprite2D
    def look():
        width = 70
        height = 70
        color = Color2d("#60A5FA").to_rgb()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_state("idle", on_enter=self.enter_idle, on_update=self.update_idle)
        self.add_state("move", on_enter=self.enter_move, on_update=self.update_move)
        self.change_state("idle")

    def enter_idle(self):
        self.set_color(Color2d("#60A5FA").to_rgb())
        instance.schedule(0.8, lambda: self.change_state("move"))

    def update_idle(self):
        pass

    def enter_move(self):
        self.set_color(Color2d("#F59E0B").to_rgb())
        self.target_x = random.randint(60, 900)
        self.target_y = random.randint(120, 500)
        instance.schedule(0.7, lambda: self.change_state("idle"))

    def update_move(self):
        self.pos.x += (self.target_x - self.pos.x) * 3.5 * instance.dt
        self.pos.y += (self.target_y - self.pos.y) * 3.5 * instance.dt


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
    BrainBox(420, 260)
    ExitControl(0, 0)
    run_game(V10Config)
