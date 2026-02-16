# main.py

`BluePanda/main.py` contiene el motor principal y el game loop.

## Componentes

- Clase `_Engine`
- Instancia global `instance`
- Funcion `run_game(config=None)`

## `_Engine`

### Estado principal

- `width`, `height`, `screen`
- `clock`, `dt`
- `nodes` (`pygame.sprite.Group`)
- `_named_nodes` (registro por nombre)
- `running`, `bg_color`, `camera`

### Metodos

- `register_node(name, node)`
- `get_node(name)`
- `get_nodes_by_class(node_class)`
- `run()`

## Render y camara

En cada frame:

1. Procesa eventos.
2. Ejecuta `self.nodes.update()`.
3. Si hay camara, llama `update_camera()`.
4. Dibuja sprites con o sin offset segun `is_ui`.

## `run_game(config=None)`

- Carga configuracion de usuario con `Config.setup`.
- Aplica resolucion, titulo y color de fondo.
- Inicializa pantalla final y arranca `instance.run()`.
