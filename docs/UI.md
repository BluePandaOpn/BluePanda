# UI in BluePanda

BluePanda provides a lightweight UI layer with text and panel components.

## Components

- `Label2D`: on-screen text.
- `Button` (via `@ButtonNode`): mouse-interactive button.
- `Panel` (via `@PanelNode`): container/background with border and opacity options.

## Render Rules

- Nodes with `is_ui = True` are rendered without camera offset.
- World nodes are rendered with `Camera2D` offset.

## UI References

- Label guide: [`UI/Label2d.md`](UI/Label2d.md)
- Full UI node API: [`Nodos/Label2d.md`](Nodos/Label2d.md), [`Nodos/Button.md`](Nodos/Button.md), [`Nodos/Panel.md`](Nodos/Panel.md)
