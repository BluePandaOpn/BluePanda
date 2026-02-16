from BluePanda.main import instance


class Timer:
    """
    Componente para gestionar el tiempo.
    Permite ejecutar funciones despues de un retraso o de forma ciclica.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wait_time = 1.0
        self.time_left = 0.0
        self.is_stopped = True
        self.one_shot = False
        self.callback = None

    def start(self, seconds=None):
        """Inicia el temporizador."""
        if seconds is not None:
            self.wait_time = seconds
        self.time_left = self.wait_time
        self.is_stopped = False

    def stop(self):
        """Detiene el temporizador."""
        self.is_stopped = True

    def connect(self, func):
        """Conecta la funcion que queremos ejecutar al terminar."""
        self.callback = func

    def update_timer(self):
        """Debe llamarse en cada frame para descontar el tiempo."""
        if self.is_stopped:
            return

        self.time_left -= instance.dt

        if self.time_left <= 0:
            if self.callback:
                self.callback()

            if self.one_shot:
                self.stop()
            else:
                self.time_left = self.wait_time
