import copy
import pygame
from BluePanda.main import instance
from .Color2d import Color2d
from .CharacterBody2D import CharacterBody2D as CB_Logic
from .CollisionShape2D import CollisionShape2D as CS_Logic
from .Timer import Timer as Timer_Logic
from .Area2D import Area2D as Area_Logic
from .Button import Button as Button_Logic
from .Label2d import Label2D as Label_Logic
from .Panel import Panel as Panel_Logic
from .AnimatedSprite2D import AnimatedSprite2D as Anim_Logic
from .Script import Script as Script_Logic
from .PhysicsBody2D import PhysicsBody2D as Physics_Logic


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
                elif tipo == "Script":
                    if Script_Logic not in list_bases:
                        list_bases.insert(0, Script_Logic)
                elif tipo == "PhysicsBody2D":
                    if Physics_Logic not in list_bases:
                        list_bases.insert(0, Physics_Logic)
                    if CS_Logic not in list_bases:
                        list_bases.insert(0, CS_Logic)

        new_class = super().__new__(cls, name, tuple(list_bases), dct)
        new_class._INTERNAL_CFG_TEMPLATE = final_config
        return new_class


class Nodo2D(pygame.sprite.Sprite, metaclass=MetaNodo):
    """
    Clase base de la que heredan todos los objetos del usuario.
    """

    def __init__(self, x=0, y=0, w=50, h=50, color=(255, 255, 255)):
        super().__init__()

        # Copia aislada por instancia para evitar estado compartido.
        self._internal_cfg = copy.deepcopy(getattr(self, "_INTERNAL_CFG_TEMPLATE", {}))
        cfg = self._internal_cfg

        for key, value in cfg.items():
            if not hasattr(self, key):
                setattr(self, key, copy.deepcopy(value))

        self.pos = pygame.Vector2(x, y)
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

