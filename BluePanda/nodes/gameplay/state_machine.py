"""
Lightweight finite state machine mixin.
"""
from ...core.engine import instance


class StateMachine:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._states = {}
        self.current_state = None
        self.state_time = 0.0
        initial = getattr(self, "initial_state", None)
        if isinstance(initial, str) and initial:
            self.current_state = initial

    def add_state(self, name, on_enter=None, on_update=None, on_exit=None):
        self._states[str(name)] = {
            "enter": on_enter,
            "update": on_update,
            "exit": on_exit,
        }

    def has_state(self, name):
        return str(name) in self._states

    def change_state(self, name):
        target = str(name)
        if target == self.current_state:
            return
        previous = self.current_state
        if previous in self._states:
            cb = self._states[previous]["exit"]
            if callable(cb):
                cb()
        self.current_state = target
        self.state_time = 0.0
        if target in self._states:
            cb = self._states[target]["enter"]
            if callable(cb):
                cb()
        if hasattr(self, "emit_signal"):
            self.emit_signal("state_changed", self, previous, target)

    def update_state_machine(self):
        if self.current_state in self._states:
            cb = self._states[self.current_state]["update"]
            if callable(cb):
                cb()
        self.state_time += instance.dt

    def update(self):
        self.update_state_machine()
        super().update()
