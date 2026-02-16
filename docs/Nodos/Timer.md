# Timer

Logical timer for delayed or repeating callbacks.

## File

`BluePanda/Nodos/Timer.py`

## Usage

Enable with `@TimerNode`.

## API

- `start(seconds=None)`
- `stop()`
- `connect(func)`
- `update_timer()`

## Fields

- `wait_time`
- `time_left`
- `is_stopped`
- `one_shot`
- `callback`
