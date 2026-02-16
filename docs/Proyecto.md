# Proyecto (Guia completa)

Esta guia centraliza toda la documentacion del proyecto BluePanda.

## Modulos principales

- [main.py](main.md)
- [Config.py](Config.md)
- [BluePanda __init__.py](BluePanda__init__.md)
- [Nodos (indice completo)](Nodos/README.md)

## Documentacion por seccion

- [UI](UI.md)
- [Nodos 2D](Nodos2D.md)

## Convencion de uso

1. Definir una clase de `Config` opcional.
2. Crear entidades heredando de `Nodo2D` o `Label2D`.
3. Activar componentes con decoradores de `Tags`.
4. Instanciar nodos.
5. Ejecutar `run_game(MyConfig)` o `run_game()`.

## Cambios recientes

- `AssetCache` ahora vive en `BluePanda/Nodos/Assets.py`.
- Nuevo nodo de fisica `PhysicsBody2D` con soporte de colision via `CollisionShape2D`.
- Nuevo utilitario `Math2D` para operaciones matematicas del motor.
- `Color2d` se mantiene como utilidad del motor, no como nodo.
