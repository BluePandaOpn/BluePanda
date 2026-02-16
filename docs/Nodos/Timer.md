# Timer (`Timer.py`)

Mixin para ejecutar callbacks por tiempo.

## Propiedades

- `wait_time`
- `time_left`
- `is_stopped`
- `one_shot`
- `callback`

## Metodos

- `start(seconds=None)`
- `stop()`
- `connect(func)`
- `update_timer()`

## Comportamiento

- Si `one_shot = True`, el timer se detiene tras disparar.
- Si `one_shot = False`, se reinicia automaticamente.

## Requisito clave

Llamar `update_timer()` en cada frame para que el contador avance.
