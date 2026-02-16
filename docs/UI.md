# UI

Documentacion de nodos de interfaz de usuario (HUD y elementos en pantalla).

## Nodos UI

- [Label2D](Nodos/Label2d.md)
- [Button](Nodos/Button.md)
- [Panel](Nodos/Panel.md)

## Reglas generales

- Los nodos UI deben usar `is_ui = True` para no moverse con la camara.
- `Label2D` ya define `is_ui = True` por defecto.
- `Button` y `Panel` son mixins; deben activarse en nodos compatibles via decoradores.

## Indice completo

- [Nodos (indice total)](Nodos/README.md)
