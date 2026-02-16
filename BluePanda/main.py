import pygame
import sys
from .Config import Config

class _Engine:
    def __init__(self):
        # Inicialización básica de Pygame
        pygame.init()
        
        # Configuración inicial por defecto
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("BluePanda Engine")
        
        # Tiempo y FPS
        self.clock = pygame.time.Clock()
        self.dt = 0  # Delta Time
        
        # --- Gestión de Nodos ---
        self.nodes = pygame.sprite.Group()
        self._named_nodes = {} # Diccionario para register_node
        
        self.running = True
        self.bg_color = (30, 30, 35) 
        self.camera = None

    # --- NUEVOS MÉTODOS DE REGISTRO ---
    def register_node(self, name, node):
        """Registra un nodo con un nombre único para encontrarlo luego"""
        self._named_nodes[name] = node
        # Aseguramos que el nodo esté en el grupo de actualización si no lo está
        if node not in self.nodes:
            self.nodes.add(node)

    def get_node(self, name):
        """Retorna un nodo registrado por su nombre"""
        return self._named_nodes.get(name)

    def get_nodes_by_class(self, node_class):
        """Retorna una lista de todos los nodos de un tipo específico (ej: Enemigos)"""
        return [node for node in self.nodes if isinstance(node, node_class)]

    def run(self):
        """Bucle principal del juego"""
        print(f"BluePanda Engine: Ejecutando a {self.width}x{self.height}")
        
        while self.running:
            # Calculamos Delta Time
            self.dt = self.clock.tick(60) / 1000.0

            # 1. Gestión de Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # 2. Lógica de los Nodos (Update)
            self.nodes.update()
            if self.camera:
                self.camera.update_camera()

            # 3. Dibujado (Render)
            self.screen.fill(self.bg_color)
            
            for sprite in self.nodes:
                # Si el nodo tiene una propiedad 'is_ui', se dibuja sin cámara
                is_ui = getattr(sprite, 'is_ui', False)
                
                if self.camera and not is_ui:
                    offset_pos = self.camera.apply(sprite.rect)
                    self.screen.blit(sprite.image, offset_pos)
                else:
                    self.screen.blit(sprite.image, sprite.rect)
            
            pygame.display.flip()

        pygame.quit()
        sys.exit()

# Creamos la instancia única
instance = _Engine()

def run_game(config=None):
    """Función para arrancar el juego con la configuración del usuario"""
    print("BluePanda Engine Cargando...")
    
    if config:
        # Usamos el método setup que creamos en Config.py
        settings = Config.setup(config)
        
        instance.width = settings.width
        instance.height = settings.height
        
        # Aplicamos el nombre de la ventana si existe
        if hasattr(settings, 'Windows'):
            pygame.display.set_caption(settings.Windows.Name)
            
        # Ajustamos el color de fondo si está definido
        if hasattr(settings, 'bg_color'):
            instance.bg_color = settings.bg_color
            
    # Re-aplicar modo de pantalla con los valores finales
    instance.screen = pygame.display.set_mode((instance.width, instance.height))
    
    # Iniciar bucle
    instance.run()