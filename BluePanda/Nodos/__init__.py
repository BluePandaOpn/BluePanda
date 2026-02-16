"""API publica de BluePanda.Nodos con carga lazy para evitar ciclos de import."""

from importlib import import_module

__all__ = [
    "Nodo2D",
    "CharacterBody2D",
    "PhysicsBody2D",
    "CollisionShape2D",
    "Sprite2D",
    "Timer",
    "Area2D",
    "Button",
    "Label2D",
    "Panel",
    "AnimatedSprite2D",
    "Script",
    "Sprite2DComponent",
    "PhysicsBody2DNode",
    "AssetCache",
    "Math2D",
]

_EXPORT_MAP = {
    "Nodo2D": (".Nodo2d", "Nodo2D"),
    "CharacterBody2D": (".Tags", "CharacterBody2D"),
    "PhysicsBody2D": (".Tags", "PhysicsBody2D"),
    "CollisionShape2D": (".Tags", "CollisionShape2D"),
    "Sprite2D": (".Tags", "Sprite2D"),
    "Timer": (".Timer", "Timer"),
    "Area2D": (".Area2D", "Area2D"),
    "Button": (".Button", "Button"),
    "Label2D": (".Label2d", "Label2D"),
    "Panel": (".Panel", "Panel"),
    "AnimatedSprite2D": (".AnimatedSprite2D", "AnimatedSprite2D"),
    "Script": (".Script", "Script"),
    "Sprite2DComponent": (".Sprite2d", "Sprite2D"),
    "PhysicsBody2DNode": (".PhysicsBody2D", "PhysicsBody2D"),
    "AssetCache": (".Assets", "AssetCache"),
    "Math2D": (".Math2D", "Math2D"),
}


def __getattr__(name):
    if name not in _EXPORT_MAP:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_path, attr_name = _EXPORT_MAP[name]
    module = import_module(module_path, __name__)
    value = getattr(module, attr_name)
    globals()[name] = value
    return value
