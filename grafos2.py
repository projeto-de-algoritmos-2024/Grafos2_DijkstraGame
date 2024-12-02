import pygame
import time

# Inicializar Pygame
pygame.init()

# Configurações de tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritmo de Dijkstra - Mapa da Cidade")

# Cores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonte para texto
font = pygame.font.SysFont(None, 30)

# Locais e suas posições
locations = {
    "Praça Central": (400, 200),
    "Hospital": (700, 200),
    "Escola": (100, 100),
    "Shopping": (600, 350),
    "Estação": (600, 550),
    "Parque": (200, 300),
    "Museu": (150, 550),
    "Biblioteca": (400, 450),
    "Mercado": (700, 500),
}

# Rotas e pesos
routes = [
    ("Praça Central", "Hospital", 2),
    ("Praça Central", "Escola", 3),
    ("Hospital", "Shopping", 4),
    ("Escola", "Parque", 6),
    ("Shopping", "Estação", 1),
    ("Parque", "Museu", 2),
    ("Museu", "Biblioteca", 5),
    ("Biblioteca", "Mercado", 3),
    ("Praça Central", "Estação", 5),
    ("Shopping", "Mercado", 4),
]

# Dimensão padrão para as imagens
IMAGE_SIZE = (100, 100)

# Carregar e redimensionar imagens dos locais e do personagem
location_images = {
    "Praça Central": pygame.transform.scale(pygame.image.load("assets/praca_central.png"), IMAGE_SIZE),
    "Hospital": pygame.transform.scale(pygame.image.load("assets/hospital.png"), IMAGE_SIZE),
    "Escola": pygame.transform.scale(pygame.image.load("assets/escola.png"), IMAGE_SIZE),
    "Shopping": pygame.transform.scale(pygame.image.load("assets/shopping.png"), IMAGE_SIZE),
    "Estação": pygame.transform.scale(pygame.image.load("assets/estacao.png"), IMAGE_SIZE),
    "Parque": pygame.transform.scale(pygame.image.load("assets/parque.png"), IMAGE_SIZE),
    "Museu": pygame.transform.scale(pygame.image.load("assets/museu.png"), IMAGE_SIZE),
    "Biblioteca": pygame.transform.scale(pygame.image.load("assets/biblioteca.png"), IMAGE_SIZE),
    "Mercado": pygame.transform.scale(pygame.image.load("assets/mercado.png"), IMAGE_SIZE),
}

character_image = pygame.transform.scale(pygame.image.load("assets/character.png"), IMAGE_SIZE)

# Função para desenhar o mapa
def draw_map(visited_nodes, current_node, shortest_path=None):
    screen.fill(WHITE)

    # Desenhar rotas
    for route in routes:
        start, end, weight = route
        # Verificar se o menor caminho está definido antes de iterar
        if shortest_path and ((start, end) in shortest_path or (end, start) in shortest_path):
            color = BLUE
        else:
            color = GRAY
        pygame.draw.line(screen, color, locations[start], locations[end], 3)

        # Desenhar pesos no meio da linha
        mid_x = (locations[start][0] + locations[end][0]) // 2
        mid_y = (locations[start][1] + locations[end][1]) // 2
        weight_text = font.render(str(weight), True, GRAY)
        screen.blit(weight_text, (mid_x - 10, mid_y - 10))

    # Desenhar imagens dos locais
    for location, pos in locations.items():
        image = location_images[location]
        image_rect = image.get_rect(center=pos)
        screen.blit(image, image_rect)

# Função para animar o personagem ao longo de uma aresta
def move_character_along_path(start, end, shortest_path=None):
    start_pos = locations[start]
    end_pos = locations[end]

    # Configurar passos para o movimento
    steps = 50
    for step in range(steps + 1):
        x = start_pos[0] + (end_pos[0] - start_pos[0]) * step / steps
        y = start_pos[1] + (end_pos[1] - start_pos[1]) * step / steps
        draw_map([], None, shortest_path)  # Recarregar o mapa com o menor caminho
        screen.blit(character_image, (x - IMAGE_SIZE[0] // 2, y - IMAGE_SIZE[1] // 2))  # Desenhar personagem
        pygame.display.flip()
        time.sleep(0.02)  # Pausa curta para animação

# Algoritmo de Dijkstra animado
def dijkstra_animation(start, end):
    distances = {node: float('inf') for node in locations}
    distances[start] = 0
    visited = set()
    path = {}

    while visited != set(locations.keys()):
        # Encontrar o nó não visitado com a menor distância
        current_node = min(
            (node for node in distances if node not in visited),
            key=lambda x: distances[x]
        )

        visited.add(current_node)

        # Atualizar distâncias dos vizinhos
        for route in routes:
            if current_node in route:
                neighbor = route[1] if route[0] == current_node else route[0]
                if neighbor not in visited:
                    move_character_along_path(current_node, neighbor)
                    new_distance = distances[current_node] + route[2]
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        path[neighbor] = current_node

    # Construir o menor caminho
    current_node = end
    shortest_path = []
    while current_node != start:
        shortest_path.append((path[current_node], current_node))
        current_node = path[current_node]
    shortest_path.reverse()

    return shortest_path

# Loop para seleção inicial
def choose_start_and_end():
    start, end = None, None
    choosing = True

    while choosing:
        draw_map([], None)
        text = font.render("Clique no local de partida e depois no destino.", True, GRAY)
        screen.blit(text, (20, 20))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for location, coords in locations.items():
                    if (coords[0] - pos[0]) ** 2 + (coords[1] - pos[1]) ** 2 <= 30 ** 2:
                        if not start:
                            start = location
                        elif not end:
                            end = location
                            choosing = False

    return start, end

# Execução do programa
running = True

while running:
    # Selecionar locais de partida e destino
    start_node, end_node = choose_start_and_end()

    # Obter animação do Dijkstra
    shortest_path = dijkstra_animation(start_node, end_node)

    # Exibir o menor caminho com destaque
    draw_map([], None, shortest_path)
    pygame.display.flip()

    # Pausa para exibição final
    time.sleep(3)
