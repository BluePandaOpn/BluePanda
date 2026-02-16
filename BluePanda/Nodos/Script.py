import importlib.util
import os
import sys

class Script:
    """
    Componente que permite cargar y ejecutar archivos .py externos.
    Permite desacoplar la lógica del nodo principal.
    """
    def __init__(self):
        self.attached_scripts = {} # Diccionario de scripts cargados

    def load_script(self, path):
        """Carga un archivo .py dinámicamente como un módulo"""
        if not os.path.exists(path):
            print(f"Error: No se encontró el script en {path}")
            return None

        try:
            # Generar un nombre único para el módulo basado en la ruta
            script_name = os.path.basename(path).replace(".py", "")
            
            # Magia de Python para importar archivos por ruta
            spec = importlib.util.spec_from_file_location(script_name, path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[script_name] = module
            spec.loader.exec_module(module)

            # Instanciar la clase principal del script (debe llamarse igual que el archivo o 'Logic')
            if hasattr(module, 'Logic'):
                script_instance = module.Logic(self) # Le pasamos el nodo dueño (self)
                self.attached_scripts[script_name] = script_instance
                
                # Ejecutar el _ready del script si existe
                if hasattr(script_instance, '_ready'):
                    script_instance._ready()
                
                return script_instance
        except Exception as e:
            print(f"Error cargando el script {path}: {e}")
            return None

    def update_scripts(self):
        """Ejecuta el método _update de todos los scripts adjuntos"""
        for script in self.attached_scripts.values():
            if hasattr(script, '_update'):
                script._update()