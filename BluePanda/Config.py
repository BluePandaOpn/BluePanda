from copy import deepcopy


class WindowSettings:
    """Sub-clase para organizar los datos de la ventana."""

    def __init__(self):
        self.Name = "BluePanda Game"
        self.Resizable = False


class Config:
    """Clase base de configuracion con fallback completo a defaults."""

    DEFAULTS = {
        "width": 800,
        "height": 600,
        "bg_color": (30, 30, 35),
        "fps": 60,
        "Windows": WindowSettings(),
    }

    def __init__(self):
        self._normalize_px_fields()

    def _normalize_px_fields(self):
        """Convierte valores como '1200 px' a enteros."""
        for attr in dir(self):
            if attr.startswith("__"):
                continue

            val = getattr(self, attr)
            if isinstance(val, str) and "px" in val:
                num = int(val.replace("px", "").strip())
                setattr(self, attr, num)

    @classmethod
    def with_defaults(cls, user_config):
        """Mezcla defaults con la config del usuario sin romper atributos faltantes."""
        merged = deepcopy(cls.DEFAULTS)

        for key in merged:
            if hasattr(user_config, key):
                merged[key] = deepcopy(getattr(user_config, key))

        default_window = deepcopy(cls.DEFAULTS["Windows"])
        user_window = getattr(user_config, "Windows", None)
        if user_window is not None:
            if hasattr(user_window, "Name"):
                default_window.Name = user_window.Name
            if hasattr(user_window, "Resizable"):
                default_window.Resizable = user_window.Resizable
        merged["Windows"] = default_window
        return merged

    @staticmethod
    def setup(user_config_class=None):
        """Crea y procesa la configuracion de usuario o retorna solo defaults."""
        if user_config_class is None:
            return Config.with_defaults(Config())

        instance = user_config_class()
        if isinstance(instance, Config):
            instance._normalize_px_fields()
        return Config.with_defaults(instance)
