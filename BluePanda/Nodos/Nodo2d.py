import pygame
from BluePanda.main import instance
from .CharacterBody2D import CharacterBody2D as CB_Logic
from .CollisionShape2D import CollisionShape2D as CS_Logic
from .Timer import Timer as Timer_Logic
from .Area2D import Area2D as Area_Logic
from .Button import Button as Button_Logic
from .Label2d import Label2D as Label_Logic
from .Panel import Panel as Panel_Logic
from .AnimatedSprite2D import AnimatedSprite2D as Anim_Logic
from .Script import Script as Script_Logic

class MetaNodo(type):
    """
    Esta metaclase se ejecuta ANTES de que el objeto se cree.
    Lee las funciones con @ y mezcla la lógica necesaria.
    """
    def __new__(cls, name, bases, dct):
        list_bases = list(bases)
        final_config = {}

        # 1. Escanear funciones en busca de etiquetas (@)
        for item in dct.values():
            if hasattr(item, "_type"):
                # Extraemos la configuración (speed, Texture, etc.)
                final_config.update(getattr(item, "_config", {}))
                
                # 2. Inyectar la clase de lógica según el tipo de etiqueta
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

        # Crear la clase final con las nuevas bases y la configuración guardada
        new_class = super().__new__(cls, name, tuple(list_bases), dct)
        new_class._INTERNAL_CFG = final_config
        return new_class

class Nodo2D(pygame.sprite.Sprite, metaclass=MetaNodo):
    """
    La clase base de la que heredarán todos los objetos del usuario.
    """
    def __init__(self, x=0, y=0, w=50, h=50, color=(255, 255, 255)):
        super().__init__()
        
        # Recuperar la configuración de los decoradores
        cfg = getattr(self, "_INTERNAL_CFG", {})
        
        # Configuración de Transform (Posición y Tamaño)
        self.pos = pygame.Vector2(x, y)
        width = cfg.get("width", w)
        height = cfg.get("height", h)
        
        # Configuración Visual (Sprite2D)
        if "Texture" in cfg:
            self.image = pygame.image.load(cfg["Texture"]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill(cfg.get("color", color))

        self.rect = self.image.get_rect()
        
        # Configuración de AnimatedSprite
        if "Atlas" in cfg:
            self.load_atlas(
                cfg["Atlas"], 
                cfg.get("frame_w", 32), 
                cfg.get("frame_h", 32), 
                cfg.get("total_frames", 1)
            )
            self.animation_speed = cfg.get("speed", 0.1)
        
        # Registrarse automáticamente en el motor principal
        instance.nodes.add(self)

    def update(self):
        """Actualiza la posición del Rect para que coincida con self.pos"""
        self.rect.topleft = (self.pos.x, self.pos.y)