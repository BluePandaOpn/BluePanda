import inspect

def _extract_vars(func):
    """
    Función interna que extrae las variables definidas dentro 
    de la función decorada (como speed, gravity, etc.)
    """
    # Ejecutamos la función para obtener su espacio de nombres local
    # Creamos un diccionario vacío para capturar las variables
    contexto = {}
    
    # Obtenemos el código fuente de la función y lo ejecutamos
    # de forma controlada para capturar las variables
    try:
        exec(func.__code__, {}, contexto)
    except Exception as e:
        print(f"Error al leer la configuración en {func.__name__}: {e}")
        
    return contexto

def CharacterBody2D(func):
    """Etiqueta para objetos con movimiento y físicas"""
    func._type = "CharacterBody2D"
    func._config = _extract_vars(func)
    return func

def CollisionShape2D(func):
    """Etiqueta para definir el área de colisión"""
    func._type = "CollisionShape2D"
    func._config = _extract_vars(func)
    return func

def Sprite2D(func):
    """Etiqueta para configurar la imagen o textura"""
    func._type = "Sprite2D"
    func._config = _extract_vars(func)
    return func

def TimerNode(func):
    """Etiqueta para crear un temporizador lógico"""
    func._type = "Timer"
    func._config = _extract_vars(func)
    return func

def Area2D(func):
    """Etiqueta para zonas de detección sensorial"""
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