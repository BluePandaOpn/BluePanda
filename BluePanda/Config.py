class WindowSettings:
    """Sub-clase para organizar los datos de la ventana"""
    def __init__(self):
        self.Name = "BluePanda Game"
        self.Resizable = False

class Config:
    """La clase base que el usuario heredará"""
    def __init__(self):
        # Procesamos la clase para convertir '1200 px' en 1200 (int)
        for attr in dir(self):
            if not attr.startswith("__"):
                val = getattr(self, attr)
                if isinstance(val, str) and 'px' in val:
                    # Limpieza automática: '1200 px' -> 1200
                    num = int(val.replace('px', '').strip())
                    setattr(self, attr, num)

    @staticmethod
    def setup(user_config_class):
        """Método estático para procesar la clase del usuario"""
        instance = user_config_class()
        return instance