"""
BluePanda Metadata
- Version: v0.5
- Node Type: Core Input Module
- Location: BluePanda/Input.py
- Purpose: Provides an engine-level input API independent from direct Pygame calls.

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame


class Input:
    """Static input service updated once per frame by the engine."""

    _keys_down = set()
    _keys_pressed = set()
    _keys_released = set()

    _mouse_down = set()
    _mouse_pressed = set()
    _mouse_released = set()
    _mouse_pos = (0, 0)

    _actions = {}

    _KEY_ALIASES = {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "space": pygame.K_SPACE,
        "enter": pygame.K_RETURN,
        "escape": pygame.K_ESCAPE,
        "esc": pygame.K_ESCAPE,
    }

    @classmethod
    def _normalize_key(cls, key):
        if isinstance(key, int):
            return key
        if isinstance(key, str):
            lowered = key.strip().lower()
            if lowered in cls._KEY_ALIASES:
                return cls._KEY_ALIASES[lowered]
            return pygame.key.key_code(lowered)
        raise TypeError(f"Unsupported key format: {key!r}")

    @classmethod
    def update(cls, events):
        """Update key/mouse states from the current frame events."""
        cls._keys_pressed.clear()
        cls._keys_released.clear()
        cls._mouse_pressed.clear()
        cls._mouse_released.clear()

        for event in events:
            if event.type == pygame.KEYDOWN:
                cls._keys_down.add(event.key)
                cls._keys_pressed.add(event.key)
            elif event.type == pygame.KEYUP:
                cls._keys_down.discard(event.key)
                cls._keys_released.add(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cls._mouse_down.add(event.button)
                cls._mouse_pressed.add(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                cls._mouse_down.discard(event.button)
                cls._mouse_released.add(event.button)

        cls._mouse_pos = pygame.mouse.get_pos()

    @classmethod
    def bind_action(cls, action, *keys):
        """Bind one action name to one or more keys."""
        cls._actions[action] = [cls._normalize_key(k) for k in keys]

    @classmethod
    def unbind_action(cls, action):
        cls._actions.pop(action, None)

    @classmethod
    def is_down(cls, key):
        return cls._normalize_key(key) in cls._keys_down

    @classmethod
    def is_pressed(cls, key):
        return cls.is_down(key)

    @classmethod
    def is_just_pressed(cls, key):
        return cls._normalize_key(key) in cls._keys_pressed

    @classmethod
    def is_just_released(cls, key):
        return cls._normalize_key(key) in cls._keys_released

    @classmethod
    def action_pressed(cls, action):
        return any(key in cls._keys_down for key in cls._actions.get(action, []))

    @classmethod
    def action_just_pressed(cls, action):
        return any(key in cls._keys_pressed for key in cls._actions.get(action, []))

    @classmethod
    def action_just_released(cls, action):
        return any(key in cls._keys_released for key in cls._actions.get(action, []))

    @classmethod
    def get_axis(cls, negative_key, positive_key):
        """Return -1, 0 or 1 based on two opposing keys."""
        value = 0
        if cls.is_down(negative_key):
            value -= 1
        if cls.is_down(positive_key):
            value += 1
        return value

    @classmethod
    def mouse_position(cls):
        return cls._mouse_pos

    @classmethod
    def mouse_down(cls, button=1):
        return button in cls._mouse_down

    @classmethod
    def mouse_just_pressed(cls, button=1):
        return button in cls._mouse_pressed

    @classmethod
    def mouse_just_released(cls, button=1):
        return button in cls._mouse_released

