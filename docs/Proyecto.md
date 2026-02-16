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

## Cobertura actual de docs

- Documentacion individual de todos los archivos `.py` en `BluePanda/Nodos`.
- Documentacion de modulos principales del motor.
- Indices por categoria (UI y mundo 2D).
- Ejemplos basicos de arranque.
