"""
BluePanda Metadata
- Version: v0.5
- Node Type: Decorator Metadata Module
- Location: BluePanda/Nodos/Tags.py
- Purpose: Reads decorator config blocks and tags nodes for mixin injection.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""

def _extract_vars(func):
    """
    FunciÃ³n interna que extrae las variables definidas dentro 
    de la funciÃ³n decorada (como speed, gravity, etc.)
    """
    contexto = {}

    # Ejecutamos con los globals reales de la funcion para permitir
    # referencias como Color2d(), constantes o imports del modulo usuario.
    try:
        exec(func.__code__, dict(func.__globals__), contexto)
    except Exception as e:
        raise RuntimeError(
            f"No se pudo leer la configuracion del decorador '{func.__name__}': {e}"
        ) from e

    # Limpieza de claves internas inyectadas por exec.
    contexto.pop("__builtins__", None)
    return contexto

def CharacterBody2D(func):
    """Etiqueta para objetos con movimiento y fÃ­sicas"""
    func._type = "CharacterBody2D"
    func._config = _extract_vars(func)
    return func

def CollisionShape2D(func):
    """Etiqueta para definir el Ã¡rea de colisiÃ³n"""
    func._type = "CollisionShape2D"
    func._config = _extract_vars(func)
    return func

def Sprite2D(func):
    """Etiqueta para configurar la imagen o textura"""
    func._type = "Sprite2D"
    func._config = _extract_vars(func)
    return func

def TimerNode(func):
    """Etiqueta para crear un temporizador lÃ³gico"""
    func._type = "Timer"
    func._config = _extract_vars(func)
    return func

def Area2D(func):
    """Etiqueta para zonas de detecciÃ³n sensorial"""
    func._type = "Area2D"
    func._config = _extract_vars(func)
    return func

def ButtonNode(func):
    """Etiqueta para crear botones interactivos"""
    func._type = "Button"
    func._config = _extract_vars(func)
    return func

def Label(func):
    """Etiqueta para nodos que muestran texto"""
    func._type = "Label"
    func._config = _extract_vars(func)
    return func

def PanelNode(func):
    """Etiqueta para crear fondos y contenedores de UI"""
    func._type = "Panel"
    func._config = _extract_vars(func)
    return func

def AnimatedSprite(func):
    """Etiqueta para nodos con animaciones por cuadros"""
    func._type = "AnimatedSprite"
    func._config = _extract_vars(func)
    return func

def ScriptNode(func):
    """Etiqueta para nodos que pueden ejecutar scripts externos"""
    func._type = "Script"
    func._config = _extract_vars(func)
    return func


def PhysicsBody2D(func):
    """Etiqueta para nodos con fisica 2D realista (gravedad/masa/colision)."""
    func._type = "PhysicsBody2D"
    func._config = _extract_vars(func)
    return func


def HealthNode(func):
    """Etiqueta para nodos con vida y dano/curacion."""
    func._type = "HealthNode"
    func._config = _extract_vars(func)
    return func


def PatrolNode2D(func):
    """Etiqueta para nodos que patrullan automaticamente."""
    func._type = "Patrol2D"
    func._config = _extract_vars(func)
    return func

