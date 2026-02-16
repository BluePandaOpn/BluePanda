# Script

Loads external Python logic modules at runtime.

## File

`BluePanda/Nodos/Script.py`

## API

- `load_script(path)`
- `update_scripts()`

## Expected Script Contract

External scripts should define `Logic(node)` and may optionally include:

- `_ready()`
- `_update()`

## Activation

Use `@ScriptNode` in your node class.
