class Script:
    """
    Componente que permite cargar y ejecutar archivos .py externos.
    Permite desacoplar la logica del nodo principal.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attached_scripts = {}

    def load_script(self, path):
        """Carga un archivo .py dinamicamente como un modulo."""
        import importlib.util
        import os
        import sys

        if not os.path.exists(path):
            print(f"Error: No se encontro el script en {path}")
            return None

        try:
            script_name = os.path.basename(path).replace(".py", "")

            spec = importlib.util.spec_from_file_location(script_name, path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[script_name] = module
            spec.loader.exec_module(module)

            if hasattr(module, "Logic"):
                script_instance = module.Logic(self)
                self.attached_scripts[script_name] = script_instance

                if hasattr(script_instance, "_ready"):
                    script_instance._ready()

                return script_instance
        except Exception as e:
            print(f"Error cargando el script {path}: {e}")
            return None

    def update_scripts(self):
        """Ejecuta el metodo _update de todos los scripts adjuntos."""
        for script in self.attached_scripts.values():
            if hasattr(script, "_update"):
                script._update()
