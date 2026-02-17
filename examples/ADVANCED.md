# BluePanda Advanced Projects

Proyectos de referencia para sistemas avanzados del motor.

## Ejecutar

```bash
python examples/advanced_01_groups_pause.py
python examples/advanced_02_patrol_health.py
python examples/advanced_03_particles_fsm_scheduler.py
python examples/advanced_04_declarative_events_signals.py
```

## Que muestran

- `advanced_01_groups_pause.py`
  - Grupos de SceneTree (`add_to_group`, `call_group`, `get_nodes_in_group`)
  - Pausa global del motor (`instance.pause/resume/toggle_pause`)
  - Escalado de tiempo (`instance.set_time_scale`)
  - Nodos que siguen procesando en pausa (`process_mode = "always"`)

- `advanced_02_patrol_health.py`
  - Nodo de vida con decorador `@HealthNode`
  - IA de patrulla con decorador `@PatrolNode2D`
  - Daño, curación y final de partida por muerte
  - Recolección usando `Area2D` + `queue_free()`

- `advanced_03_particles_fsm_scheduler.py`
  - `@StateMachineNode` para comportamiento por estados
  - `@ParticleEmitterNode2D` para FX sin assets externos
  - `instance.schedule(...)` para tareas temporizadas
  - `instance.tween(...)` para animar propiedades en runtime

- `advanced_04_declarative_events_signals.py`
  - `@OnReady` para inicializacion declarativa
  - `@OnEvent` para conectar eventos globales de `SceneTree`
  - `@OnSignal` para conectar senales locales del nodo
