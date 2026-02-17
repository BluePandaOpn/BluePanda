"""
BluePanda decorator system:
- Component decorators (@Sprite2D, @CharacterBody2D, ...)
- Declarative lifecycle/event decorators (@OnReady, @OnEvent, @OnSignal)
"""


def _extract_vars(func):
    """Extract assignment-style config blocks from decorated functions."""
    context = {}
    try:
        exec(func.__code__, dict(func.__globals__), context)
    except Exception as e:
        raise RuntimeError(
            f"No se pudo leer la configuracion del decorador '{func.__name__}': {e}"
        ) from e
    context.pop("__builtins__", None)
    return context


def _coerce_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in ("true", "1", "yes", "on"):
            return True
        if lowered in ("false", "0", "no", "off"):
            return False
    return bool(value)


def _coerce_int(value):
    return int(value)


def _coerce_float(value):
    return float(value)


_SCHEMAS = {
    "CharacterBody2D": {
        "speed": _coerce_float,
    },
    "Timer": {
        "wait_time": _coerce_float,
        "one_shot": _coerce_bool,
    },
    "ParticleEmitter2D": {
        "emitting": _coerce_bool,
        "emit_rate": _coerce_float,
        "particle_lifetime": _coerce_float,
        "particle_size": _coerce_int,
        "particle_speed": _coerce_float,
        "gravity": _coerce_float,
    },
    "HealthNode": {
        "max_health": _coerce_int,
        "health": _coerce_int,
        "invulnerable": _coerce_bool,
    },
    "Patrol2D": {
        "patrol_speed": _coerce_float,
        "patrol_left": _coerce_float,
        "patrol_right": _coerce_float,
        "patrol_top": _coerce_float,
        "patrol_bottom": _coerce_float,
    },
}


def _validate_component(component_type, config):
    validators = _SCHEMAS.get(component_type, {})
    if not validators:
        return config
    normalized = dict(config)
    for key, caster in validators.items():
        if key not in normalized:
            continue
        try:
            normalized[key] = caster(normalized[key])
        except Exception as e:
            raise ValueError(
                f"Valor invalido para '{component_type}.{key}': {normalized[key]!r}"
            ) from e
    return normalized


def _register_component(func, component_type, config):
    func._type = str(component_type)
    func._config = _validate_component(str(component_type), config)
    return func


def component(name, **config):
    """Factory for explicit component declarations."""

    def _decorator(func):
        return _register_component(func, name, dict(config))

    return _decorator


def _component_from_block(component_type, func):
    return _register_component(func, component_type, _extract_vars(func))


def CharacterBody2D(func):
    return _component_from_block("CharacterBody2D", func)


def CollisionShape2D(func):
    return _component_from_block("CollisionShape2D", func)


def Sprite2D(func):
    return _component_from_block("Sprite2D", func)


def TimerNode(func):
    return _component_from_block("Timer", func)


def Area2D(func):
    return _component_from_block("Area2D", func)


def ButtonNode(func):
    return _component_from_block("Button", func)


def Label(func):
    return _component_from_block("Label", func)


def PanelNode(func):
    return _component_from_block("Panel", func)


def AnimatedSprite(func):
    return _component_from_block("AnimatedSprite", func)


def ScriptNode(func):
    return _component_from_block("Script", func)


def PhysicsBody2D(func):
    return _component_from_block("PhysicsBody2D", func)


def HealthNode(func):
    return _component_from_block("HealthNode", func)


def PatrolNode2D(func):
    return _component_from_block("Patrol2D", func)


def ParticleEmitterNode2D(func):
    return _component_from_block("ParticleEmitter2D", func)


def StateMachineNode(func):
    return _component_from_block("StateMachine", func)


def OnReady(func):
    """Mark method to be called once after node initialization."""
    setattr(func, "_bp_on_ready", True)
    return func


def OnEvent(event_name, once=False):
    """Bind method to SceneTree global events declaratively."""

    def _decorator(func):
        hooks = list(getattr(func, "_bp_on_events", []))
        hooks.append((str(event_name), bool(once)))
        setattr(func, "_bp_on_events", hooks)
        return func

    return _decorator


def OnSignal(signal_name, once=False):
    """Bind method to node-local signals declaratively."""

    def _decorator(func):
        hooks = list(getattr(func, "_bp_on_signals", []))
        hooks.append((str(signal_name), bool(once)))
        setattr(func, "_bp_on_signals", hooks)
        return func

    return _decorator
