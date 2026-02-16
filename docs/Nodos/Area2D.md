# Area2D (`Area2D.py`)

Mixin sensor para detectar entradas a una zona.

## Metodos

- `on_body_entered(callback)`
  - Ejecuta `callback(body)` para cada objeto que entra.
  - Marca internamente cuerpos ya procesados por area.

- `on_body_exited(callback)`
  - Placeholder (sin implementacion actual).

- `get_overlapping_bodies()`
  - Retorna cuerpos que estan tocando el area.

- `overlaps(other_node)`
  - Consulta directa de solapamiento por `rect`.

## Requisitos

- `self.rect` debe existir.

## Nota de uso

`on_body_entered` debe llamarse periodicamente (por ejemplo, en `update`) para detectar entradas en tiempo real.
