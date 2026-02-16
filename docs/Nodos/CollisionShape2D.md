# CollisionShape2D (`CollisionShape2D.py`)

Mixin con utilidades de colision por `rect`.

## Metodos

- `is_colliding_with(other_node)`
  - Retorna `True` si `self.rect` colisiona con `other_node.rect`.

- `get_overlapping_bodies()`
  - Retorna lista de nodos colisionando con `self`.
  - Excluye al propio `self`.

- `check_collision(tag_buscada=None)`
  - Sin filtro: `True` si colisiona con cualquier nodo.
  - Con filtro: verifica si algun nodo colisionando tiene el atributo `tag_buscada`.

## Requisitos

- El nodo debe tener `rect` valido.
