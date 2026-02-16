# BluePanda Project

Central guide for architecture, repository structure, and GitHub publishing.

## Goal

BluePanda provides a simple 2D engine for prototypes and small-to-medium Python game projects.

## Repository Structure

```text
BluePanda/
  __init__.py
  main.py
  Config.py
  Nodos/
docs/
README.md
CHANGELOG.md
LICENSE
LICENSE-COMMERCIAL.md
```

## Basic Usage Flow

1. Define configuration (optional) with `Config`.
2. Create entities by inheriting from `Nodo2D`.
3. Enable components with decorators (`@CharacterBody2D`, `@Sprite2D`, etc.).
4. Instantiate your nodes.
5. Start with `run_game(MyConfig)`.

## Related Documentation

- [`main.md`](main.md)
- [`Config.md`](Config.md)
- [`BluePanda__init__.md`](BluePanda__init__.md)
- [`Nodos2D.md`](Nodos2D.md)
- [`UI.md`](UI.md)
- [`Nodos/README.md`](Nodos/README.md)

## GitHub Release Checklist

Before creating a release:

- Review `CHANGELOG.md`.
- Verify licenses (`LICENSE`, `LICENSE-COMMERCIAL.md`).
- Confirm `README.md` and `docs/` match the release version.

## Credits

- Engine: `BluePanda`
- Lead author: `Pato404`
