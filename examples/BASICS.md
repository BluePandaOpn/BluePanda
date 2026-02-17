# BluePanda Basic Projects

Coleccion de mini proyectos para aprender BluePanda de forma incremental.

## Requisitos

```bash
pip install -e .
```

## Orden recomendado (para personas e IA)

1. `examples/basic_01_hello_box.py`
2. `examples/basic_02_player_movement.py`
3. `examples/basic_03_pickups_and_events.py`
4. `examples/basic_04_ui_button.py`

## Que enseña cada ejemplo

- `basic_01_hello_box.py`: estructura minima (`Config`, `Nodo2D`, `run_game`, salida con ESC).
- `basic_02_player_movement.py`: input por acciones, `CharacterBody2D`, limites del mundo.
- `basic_03_pickups_and_events.py`: `Area2D`, `SceneTree.emit/connect`, HUD y contador.
- `basic_04_ui_button.py`: `ButtonNode`, UI clickeable y callbacks.

## Patrones recomendados para prompts de IA

- "Crea un nodo `Player` con `@CharacterBody2D` y color `Color2d('#22D3EE')`."
- "Agrega un `Hud` que escuche `instance.tree.connect('evento', callback)`."
- "Termina el juego con ESC usando `Input.is_just_pressed('escape')`."
- "Mantén el jugador dentro de `WORLD_W` y `WORLD_H`."
