"""
BluePanda Metadata
- Version: v0.5
- Node Type: Base Node Module
- Location: BluePanda/Nodos/Nodo2d.py
- Purpose: Defines MetaNodo and Nodo2D, the base entity system for gameplay objects.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import copy
import pygame
from ...core.engine import instance
from ...utils.color import Color2d
from ..physics.character_body_2d import CharacterBody2D as CB_Logic
from ..physics.collision_shape_2d import CollisionShape2D as CS_Logic
from ..time.timer import Timer as Timer_Logic
from ..physics.area2d import Area2D as Area_Logic
from ..ui.button import Button as Button_Logic
from ..ui.label2d import Label2D as Label_Logic
from ..ui.panel import Panel as Panel_Logic
from ..render.animated_sprite2d import AnimatedSprite2D as Anim_Logic
from ..render.sprite2d import Sprite2D as Sprite_Logic
from ..scripting.script import Script as Script_Logic
from ..physics.physics_body_2d import PhysicsBody2D as Physics_Logic
from ..gameplay.health import Health as Health_Logic
from ..gameplay.patrol2d import Patrol2D as Patrol_Logic


class MetaNodo(type):
    """
    Metaclase que detecta etiquetas y mezcla la logica necesaria.
    """

    def __new__(cls, name, bases, dct):
        list_bases = list(bases)
        final_config = {}

        for item in dct.values():
            if hasattr(item, "_type"):
                final_config.update(copy.deepcopy(getattr(item, "_config", {})))

                tipo = item._type
                if tipo == "CharacterBody2D":
                    if CB_Logic not in list_bases:
                        list_bases.insert(0, CB_Logic)
                elif tipo == "CollisionShape2D":
                    if CS_Logic not in list_bases:
                        list_bases.insert(0, CS_Logic)
                elif tipo == "Timer":
                    if Timer_Logic not in list_bases:
                        list_bases.insert(0, Timer_Logic)
                elif tipo == "Area2D":
                    if Area_Logic not in list_bases:
                        list_bases.insert(0, Area_Logic)
                elif tipo == "Button":
                    if Button_Logic not in list_bases:
                        list_bases.insert(0, Button_Logic)
                elif tipo == "Label":
                    if Label_Logic not in list_bases:
                        list_bases.insert(0, Label_Logic)
                elif tipo == "Panel":
                    if Panel_Logic not in list_bases:
                        list_bases.insert(0, Panel_Logic)
                elif tipo == "AnimatedSprite":
                    if Anim_Logic not in list_bases:
                        list_bases.insert(0, Anim_Logic)
                elif tipo == "Sprite2D":
                    if Sprite_Logic not in list_bases:
                        list_bases.insert(0, Sprite_Logic)
                elif tipo == "Script":
                    if Script_Logic not in list_bases:
                        list_bases.insert(0, Script_Logic)
                elif tipo == "PhysicsBody2D":
                    if Physics_Logic not in list_bases:
                        list_bases.insert(0, Physics_Logic)
                    if CS_Logic not in list_bases:
                        list_bases.insert(0, CS_Logic)
                elif tipo == "HealthNode":
                    if Health_Logic not in list_bases:
                        list_bases.insert(0, Health_Logic)
                elif tipo == "Patrol2D":
                    if Patrol_Logic not in list_bases:
                        list_bases.insert(0, Patrol_Logic)

        new_class = super().__new__(cls, name, tuple(list_bases), dct)
        new_class._INTERNAL_CFG_TEMPLATE = final_config
        return new_class


class Nodo2D(pygame.sprite.Sprite, metaclass=MetaNodo):
    """
    Clase base de la que heredan todos los objetos del usuario.
    """

    def __init__(self, x=0, y=0, w=50, h=50, color=(255, 255, 255), name=None):
        super().__init__()

        # Copia aislada por instancia para evitar estado compartido.
        self._internal_cfg = copy.deepcopy(getattr(self, "_INTERNAL_CFG_TEMPLATE", {}))
        cfg = self._internal_cfg

        for key, value in cfg.items():
            if not hasattr(self, key):
                setattr(self, key, copy.deepcopy(value))

        self.pos = pygame.Vector2(x, y)
        self.parent = None
        self.children = []
        self.active = True
        self.visible = True
        self.process_mode = str(cfg.get("process_mode", "pausable")).lower()
        self._groups = set()
        self.name = name if name is not None else self.__class__.__name__
        self.z_index = int(cfg.get("z_index", 0))
        self._bp_order = instance.allocate_draw_order()
        self._signals = {}
        width = int(cfg.get("width", w))
        height = int(cfg.get("height", h))

        if "Texture" in cfg:
            self.image = instance.assets.load_image(cfg["Texture"], size=(width, height), use_alpha=True)
        else:
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            fill_color = Color2d.coerce(cfg.get("color", color), color)
            self.image.fill(fill_color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos.x, self.pos.y)

        if "Atlas" in cfg:
            self.load_atlas(
                cfg["Atlas"],
                cfg.get("frame_w", 32),
                cfg.get("frame_h", 32),
                cfg.get("total_frames", 1),
            )
            self.animation_speed = cfg.get("speed", 0.1)

        if hasattr(self, "setup_panel"):
            self.setup_panel()

        instance.nodes.add(self)
        instance.tree.add_child(self)

    def add_child(self, child):
        """Attach another node under this node for recursive update/draw."""
        if child is self:
            return
        instance.tree.add_child(child, parent=self)

    def remove_child(self, child):
        """Detach a child node."""
        if getattr(child, "parent", None) is self:
            instance.tree.remove_child(child)

    def set_parent(self, parent):
        """Set or clear parent relation."""
        if parent is None:
            if self.parent is not None:
                self.parent.remove_child(self)
            return
        parent.add_child(self)

    def get_children(self):
        return list(self.children)

    def get_node(self, path):
        """Resolve a node path relative to this node."""
        return instance.tree.get_node(path, start=self)

    def connect(self, signal_name, callback):
        """Connect a callback to this node signal."""
        listeners = self._signals.setdefault(str(signal_name), [])
        listeners.append(callback)

    def disconnect(self, signal_name, callback):
        listeners = self._signals.get(str(signal_name), [])
        if callback in listeners:
            listeners.remove(callback)

    def emit_signal(self, signal_name, *args, **kwargs):
        """Emit a local node signal."""
        for callback in list(self._signals.get(str(signal_name), [])):
            callback(*args, **kwargs)

    def can_process(self):
        """Evaluate if this node should run update in the current frame."""
        mode = str(getattr(self, "process_mode", "pausable")).lower()
        if mode == "disabled":
            return False
        if mode == "always":
            return True
        return not bool(getattr(instance, "paused", False))

    def set_color(self, color):
        """Fallback color setter available on every node with an image."""
        if hasattr(self, "image"):
            self.image.fill(Color2d.coerce(color, (255, 255, 255)))

    def set_size(self, width, height):
        """Resize node image while preserving top-left world position."""
        if not hasattr(self, "image") or not hasattr(self, "rect"):
            return
        w = max(1, int(width))
        h = max(1, int(height))
        pos = self.rect.topleft
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect(topleft=pos)

    def set_position(self, x, y):
        """Set position and sync rect in one call."""
        self.pos.x = float(x)
        self.pos.y = float(y)
        if hasattr(self, "rect"):
            self.rect.topleft = (self.pos.x, self.pos.y)

    def queue_free(self):
        """Godot-like convenience alias to safely remove this node."""
        self.kill()

    def add_to_group(self, group_name):
        return instance.tree.add_to_group(self, group_name)

    def remove_from_group(self, group_name):
        return instance.tree.remove_from_group(self, group_name)

    def is_in_group(self, group_name):
        return instance.tree.is_in_group(self, group_name)

    def kill(self):
        """Keep hierarchy references consistent when node is removed."""
        for group_name in list(self._groups):
            instance.tree.remove_from_group(self, group_name)
        if self.parent is not None:
            instance.tree.remove_child(self)
        for child in list(self.children):
            child.parent = None
        self.children.clear()
        super().kill()

    def update(self):
        """Actualiza subsistemas opcionales y sincroniza rect con pos."""
        if hasattr(self, "update_timer"):
            self.update_timer()
        if hasattr(self, "update_animation"):
            self.update_animation()
        if hasattr(self, "update_button"):
            self.update_button()
        if hasattr(self, "update_scripts"):
            self.update_scripts()
        if hasattr(self, "update_physics"):
            self.update_physics()

        self.rect.topleft = (self.pos.x, self.pos.y)


