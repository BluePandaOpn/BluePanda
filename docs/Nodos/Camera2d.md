# Camera2D (`Camera2d.py`)

Controla el desplazamiento de camara para seguir un objetivo.

## Constructor

```python
Camera2D(target=None)
```

## Propiedades

- `target`
- `offset`
- `smoothness` (default `0.1`)

## Metodos

- `update_camera()`
  - Calcula offset hacia el centro de pantalla con suavizado.

- `apply(rect)`
  - Retorna un `rect` desplazado segun la camara.

## Integracion

Al crearla, se asigna automaticamente a `instance.camera`.
