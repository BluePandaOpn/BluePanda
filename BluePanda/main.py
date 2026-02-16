import pygame
import sys
from .Config import Config
from .Nodos.Color2d import Color2d
from .Nodos.Assets import AssetCache


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

        self.running = True
        self.camera = None
        self.assets = AssetCache()

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

    def _display_flags(self):
        return pygame.RESIZABLE if self.resizable else 0

    def run(self):
        """Bucle principal del juego."""
        print(f"BluePanda Engine: Ejecutando a {self.width}x{self.height}")

        while self.running:
            self.dt = self.clock.tick(self.target_fps) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.VIDEORESIZE and self.resizable:
                    self.width, self.height = event.w, event.h
                    self.screen = pygame.display.set_mode((self.width, self.height), self._display_flags())

            self.nodes.update()
            if self.camera:
                self.camera.update_camera()

            self.screen.fill(self.bg_color)

            for sprite in self.nodes:
                is_ui = getattr(sprite, "is_ui", False)

                if self.camera and not is_ui:
                    offset_pos = self.camera.apply(sprite.rect)
                    self.screen.blit(sprite.image, offset_pos)
                else:
                    self.screen.blit(sprite.image, sprite.rect)

            pygame.display.flip()

        pygame.quit()
        sys.exit()


instance = _Engine()


def _safe_positive_int(value, default):
    try:
        parsed = int(value)
        return parsed if parsed > 0 else default
    except Exception:
        return default


def run_game(config=None):
    """Arranca el juego con configuracion de usuario y fallback a defaults."""
    print("BluePanda Engine Cargando...")

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
