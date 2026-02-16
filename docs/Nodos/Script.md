# Script (`Script.py`)

Mixin para cargar logica externa desde archivos `.py`.

## Metodos

- `load_script(path)`
  - Importa dinamicamente el archivo.
  - Busca clase `Logic` dentro del modulo.
  - Instancia `Logic(self)` y la guarda en `attached_scripts`.
  - Si existe `_ready`, lo ejecuta.

- `update_scripts()`
  - Ejecuta `_update()` de cada script adjunto (si existe).

## Convencion esperada del script externo

```python
class Logic:
    def __init__(self, owner):
        self.owner = owner

    def _ready(self):
        pass

    def _update(self):
        pass
```
