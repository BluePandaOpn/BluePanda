"""
BluePanda Advanced 03
State machine + particle emitter + scheduler/tween.

Run:
    python examples/advanced_03_particles_fsm_scheduler.py
"""
import random

from BluePanda import (
    Color2d,
    Config,
    Input,
    Nodo2D,
    ParticleEmitterNode2D,
    Sprite2D,
    StateMachineNode,
    WindowSettings,
    instance,
    run_game,
)


class AdvancedConfig(Config):
    width = 1100
    height = 680
    fps = 60
    bg_color = Color2d("#090F1F").to_rgb()

    Windows = WindowSettings()
    Windows.Name = "BluePanda Advanced 03 - FSM Particles Scheduler"
    Windows.Resizable = False


class Drone(Nodo2D):
    @StateMachineNode
    def ai():
        initial_state = "idle"

    @ParticleEmitterNode2D
    def fx():
        emitting = True
        emit_rate = 20
        particle_lifetime = 0.7
        particle_size = 3
        particle_speed = 120
        gravity = 10
        particle_color = Color2d("#A7F3D0").to_rgb()

    @Sprite2D
    def look():
        width = 42
        height = 42
        color = Color2d("#22D3EE").to_rgb()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_to_group("drones")
        self.target_x = self.pos.x
        self.target_y = self.pos.y
        self.speed = 180.0
        self._install_states()

    def _install_states(self):
        self.add_state("idle", on_enter=self._on_idle_enter, on_update=self._on_idle_update)
        self.add_state("dash", on_enter=self._on_dash_enter, on_update=self._on_dash_update)
        self.change_state("idle")

    def _on_idle_enter(self):
        self.emitting = False
        self.set_color(Color2d("#60A5FA").to_rgb())
        delay = random.uniform(0.8, 1.6)
        instance.schedule(delay, lambda: self.change_state("dash"))

    def _on_idle_update(self):
        pass

    def _on_dash_enter(self):
        self.emitting = True
        self.set_color(Color2d("#F59E0B").to_rgb())
        self.target_x = random.randint(80, AdvancedConfig.width - 80)
        self.target_y = random.randint(110, AdvancedConfig.height - 80)
        instance.schedule(0.55, lambda: self.change_state("idle"))

    def _on_dash_update(self):
        dx = self.target_x - self.pos.x
        dy = self.target_y - self.pos.y
        dist = (dx * dx + dy * dy) ** 0.5
        if dist > 0.1:
            self.pos.x += (dx / dist) * self.speed * instance.dt
            self.pos.y += (dy / dist) * self.speed * instance.dt


class Controller(Nodo2D):
    @Sprite2D
    def look():
        width = 1
        height = 1
        color = (0, 0, 0, 0)
        process_mode = "always"
        z_index = 20

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_ui = True
        self.visible = False
        self.font = instance.resources.load_font(size=22)
        self.small = instance.resources.load_font(size=18)

        # Global pulse effect with tween scheduler.
        self._pulse_up = True
        self._pulse_task = instance.schedule(1.0, self._pulse_all, repeat=True, interval=1.0)

    def _pulse_all(self):
        offset = -16.0 if self._pulse_up else 16.0
        self._pulse_up = not self._pulse_up
        for drone in instance.tree.get_nodes_in_group("drones"):
            target_y = max(120.0, min(620.0, drone.pos.y + offset))
            instance.tween(drone, "pos.y", target_y, 0.35, ease="ease_in_out")

    def update(self):
        if Input.is_just_pressed("escape"):
            instance.running = False
        if Input.is_just_pressed("space"):
            instance.toggle_pause()
        if Input.is_just_pressed("r"):
            instance.tree.call_group("drones", "clear_particles")
        super().update()

    def draw(self, surface):
        info = self.font.render(
            f"Drones: {len(instance.tree.get_nodes_in_group('drones'))} | Paused: {instance.paused}",
            True,
            (240, 240, 245),
        )
        help_line = self.small.render(
            "SPACE pause | R clear particles | ESC quit",
            True,
            (180, 190, 210),
        )
        surface.blit(info, (14, 14))
        surface.blit(help_line, (14, 44))


if __name__ == "__main__":
    for i in range(12):
        Drone(100 + i * 70, random.randint(160, 560), name=f"drone_{i}")
    Controller(0, 0, name="controller")
    run_game(AdvancedConfig)
