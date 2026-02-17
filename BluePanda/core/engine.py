"""
BluePanda Metadata
- Version: v0.5
- Node Type: Core Runtime Module
- Location: BluePanda/main.py
- Purpose: Runs the engine loop, event processing, rendering, and game startup via run_game().

Customization Notes:
- This file is intended to be edited by engine users.
- Keep public method names stable when possible to avoid API breakage.
- If you change behavior, also update the matching docs in /docs.
"""
import pygame
import sys
from .config import Config
from ..utils.color import Color2d
from ..resources.asset_cache import AssetCache
from .input import Input
from ..scene.tree import SceneTree
from ..resources.loader import ResourceLoader


class GameLoop:
    """
    Formal loop pipeline for deterministic update/draw order:
    1) gather events + update input
    2) process engine/window events
    3) recursive node update
    4) camera update
    5) recursive node drawing
    """

    def __init__(self, engine):
        self.engine = engine

    def _sort_nodes(self, nodes):
        return sorted(
            nodes,
            key=lambda n: (int(getattr(n, "z_index", 0)), int(getattr(n, "_bp_order", 0))),
        )

    def _root_nodes(self):
        roots = []
        for node in self.engine.nodes:
            parent = getattr(node, "parent", None)
            if parent is None or not getattr(parent, "alive", lambda: False)():
                roots.append(node)
        return self._sort_nodes(roots)

    def _process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.engine.running = False

            if event.type == pygame.VIDEORESIZE and self.engine.resizable:
                self.engine.width, self.engine.height = event.w, event.h
                self.engine.screen = pygame.display.set_mode(
                    (self.engine.width, self.engine.height),
                    self.engine._display_flags(),
                )

    def _update_node_recursive(self, node):
        if not getattr(node, "active", True):
            return
        if hasattr(node, "can_process") and not node.can_process():
            return

        if hasattr(node, "update"):
            node.update()

        for child in self._sort_nodes(getattr(node, "children", [])):
            self._update_node_recursive(child)

    def _draw_node_recursive(self, node):
        if not getattr(node, "visible", True):
            return

        if hasattr(node, "draw") and callable(node.draw):
            node.draw(self.engine.screen)
        elif hasattr(node, "image") and hasattr(node, "rect"):
            is_ui = getattr(node, "is_ui", False)
            if self.engine.camera and not is_ui:
                offset_pos = self.engine.camera.apply(node.rect)
                self.engine.screen.blit(node.image, offset_pos)
            else:
                self.engine.screen.blit(node.image, node.rect)

        for child in self._sort_nodes(getattr(node, "children", [])):
            self._draw_node_recursive(child)

    def step(self):
        raw_dt = self.engine.clock.tick(self.engine.target_fps) / 1000.0
        self.engine.dt = raw_dt * self.engine.time_scale
        events = pygame.event.get()
        Input.update(events)
        self._process_events(events)

        roots = self._root_nodes()
        for root in roots:
            self._update_node_recursive(root)

        if self.engine.camera:
            self.engine.camera.update_camera()

        self.engine.screen.fill(self.engine.bg_color)
        for root in roots:
            self._draw_node_recursive(root)
        pygame.display.flip()


class _Engine:
    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 600
        self.resizable = False
        self.bg_color = (30, 30, 35)
        self.target_fps = 60

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("BluePanda Engine")

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.nodes = pygame.sprite.Group()
        self._named_nodes = {}
        self._draw_order_counter = 0

        self.running = True
        self.paused = False
        self.time_scale = 1.0
        self.camera = None
        self.assets = AssetCache()
        self.resources = ResourceLoader()
        self.tree = SceneTree(self)
        self.loop = GameLoop(self)

    def allocate_draw_order(self):
        order = self._draw_order_counter
        self._draw_order_counter += 1
        return order

    def register_node(self, name, node):
        """Registra un nodo con un nombre unico para encontrarlo luego."""
        self._named_nodes[name] = node
        if node not in self.nodes:
            self.nodes.add(node)

    def get_node(self, name):
        """Retorna un nodo registrado por su nombre."""
        return self._named_nodes.get(name)

    def get_nodes_by_class(self, node_class):
        """Retorna una lista de nodos de un tipo especifico."""
        return [node for node in self.nodes if isinstance(node, node_class)]

    def get_node_by_path(self, path, start=None):
        """Resolve a node in the scene tree using a node path."""
        return self.tree.get_node(path, start=start)

    def _display_flags(self):
        return pygame.RESIZABLE if self.resizable else 0

    def run(self):
        """Start the main engine loop."""
        print(f"BluePanda Engine: Running at {self.width}x{self.height}")

        while self.running:
            self.loop.step()

        pygame.quit()
        sys.exit()

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    def set_time_scale(self, value):
        try:
            parsed = float(value)
        except Exception:
            return
        self.time_scale = max(0.0, parsed)


instance = _Engine()


def _safe_positive_int(value, default):
    try:
        parsed = int(value)
        return parsed if parsed > 0 else default
    except Exception:
        return default


def run_game(config=None):
    """Start the game using user config with safe defaults."""
    print("BluePanda Engine loading...")

    settings = Config.setup(config)

    instance.width = _safe_positive_int(settings.get("width"), instance.width)
    instance.height = _safe_positive_int(settings.get("height"), instance.height)
    instance.target_fps = _safe_positive_int(settings.get("fps"), instance.target_fps)

    instance.bg_color = Color2d.coerce(settings.get("bg_color"), instance.bg_color)

    window_cfg = settings.get("Windows")
    window_name = getattr(window_cfg, "Name", "BluePanda Engine")
    instance.resizable = bool(getattr(window_cfg, "Resizable", False))

    pygame.display.set_caption(window_name)
    instance.screen = pygame.display.set_mode((instance.width, instance.height), instance._display_flags())

    instance.run()

