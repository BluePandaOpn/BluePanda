# 1. Importamos la función para arrancar y la instancia desde main.py
from .main import run_game, instance
from .Config import Config, WindowSettings
from .Nodos.Color2d import Color2d
from .Nodos.Assets import AssetCache
from .Nodos.Math2D import Math2D

# 2. Importamos el Nodo base desde la subcarpeta Nodos
# Nota: Buscamos en la carpeta .Nodos (punto) y el archivo .Nodo2d (punto)
from .Nodos.Nodo2d import Nodo2D
from .Nodos.Camera2d import Camera2D
from .Nodos.Label2d import Label2D
# Y añadirla a __all__

# 3. Importamos los decoradores (tags) para las clases
from .Nodos.Tags import CharacterBody2D, CollisionShape2D, Sprite2D, TimerNode, Area2D, ButtonNode, Label, PanelNode, AnimatedSprite, ScriptNode, PhysicsBody2D

# 4. Definimos qué nombres estarán disponibles al hacer 'from BluePanda import *'
__all__ = [
    'run_game',
    'instance',
    'Nodo2D',
    'CharacterBody2D',
    'PhysicsBody2D',
    'CollisionShape2D',
    'Sprite2D',
    'Camera2D',
    'TimerNode',
    'Area2D',
    'Label2D',
    'ButtonNode',
    'Label',
    'PanelNode',
    'AnimatedSprite',
    'Config',
    'WindowSettings',
    'Color2d',
    'AssetCache',
    'Math2D',
    'ScriptNode'
]

print('BluePanda Engine Cargando ...')
