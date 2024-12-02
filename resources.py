import pygame
import time

# Cores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Fonte para texto
font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 30)

locations = {
    "Zoológico": (160, 83),
    "Escola": (409, 195),
    "Cinema": (660, 50),
    "Praça Central": (910, 195),
    "Parque": (1160, 84),

    "Universidade": (160, 293),
    "Hospital": (410, 410),
    "Teatro": (660, 293),
    "Aeroporto": (910, 410),
    "Faculdade": (1160, 293),

    "Farmácia": (160, 502),
    "Museu": (410, 610),
    "Biblioteca": (660, 502),
    "Hotel": (910, 607),
    "Shopping": (1160, 502),

    "Restaurante": (160, 711),
    "Supermercado": (410, 816),
    "Mercado": (660, 780),
    "Estádio": (910, 816),
    "Estação": (1160, 711)
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
    ("Cinema", "Restaurante", 3),
    ("Teatro", "Cinema", 4),
    ("Hotel", "Restaurante", 2),
    ("Faculdade", "Hotel", 6),
    ("Praça Central", "Faculdade", 7),
    ("Aeroporto", "Estádio", 8),
    ("Aeroporto", "Supermercado", 5),
    ("Estádio", "Zoológico", 3),
    ("Farmácia", "Biblioteca", 4),
    ("Universidade", "Faculdade", 2),
    ("Estação", "Aeroporto", 6),                 
    ("Zoológico", "Praça Central", 5),  
    ("Restaurante", "Estádio", 4),     
    ("Universidade", "Shopping", 3),    
    ("Farmácia", "Escola", 5),          
    ("Museu", "Teatro", 6),            
    ("Supermercado", "Biblioteca", 3)
]

# Dimensão padrão para as imagens
IMAGE_SIZE = (80, 80)

# Carregar e redimensionar imagens dos locais e do personagem
location_images = {
    "Praça Central": pygame.transform.scale(pygame.image.load("assets/praca.png"), IMAGE_SIZE),
    "Hospital": pygame.transform.scale(pygame.image.load("assets/hospital.png"), IMAGE_SIZE),
    "Escola": pygame.transform.scale(pygame.image.load("assets/escola.png"), IMAGE_SIZE),
    "Shopping": pygame.transform.scale(pygame.image.load("assets/shopping.png"), IMAGE_SIZE),
    "Estação": pygame.transform.scale(pygame.image.load("assets/estacao.png"), IMAGE_SIZE),
    "Parque": pygame.transform.scale(pygame.image.load("assets/parque.png"), IMAGE_SIZE),
    "Museu": pygame.transform.scale(pygame.image.load("assets/museu.png"), IMAGE_SIZE),
    "Biblioteca": pygame.transform.scale(pygame.image.load("assets/biblioteca.png"), IMAGE_SIZE),
    "Mercado": pygame.transform.scale(pygame.image.load("assets/mercado.png"), IMAGE_SIZE),
    "Cinema": pygame.transform.scale(pygame.image.load("assets/cinema.png"), IMAGE_SIZE),
    "Restaurante": pygame.transform.scale(pygame.image.load("assets/restaurante.png"), IMAGE_SIZE),
    "Teatro": pygame.transform.scale(pygame.image.load("assets/teatro.png"), IMAGE_SIZE),
    "Hotel": pygame.transform.scale(pygame.image.load("assets/hotel.png"), IMAGE_SIZE),
    "Faculdade": pygame.transform.scale(pygame.image.load("assets/faculdade.png"), IMAGE_SIZE),
    "Aeroporto": pygame.transform.scale(pygame.image.load("assets/aeroporto.png"), IMAGE_SIZE),
    "Estádio": pygame.transform.scale(pygame.image.load("assets/estadio.png"), IMAGE_SIZE),
    "Farmácia": pygame.transform.scale(pygame.image.load("assets/farmacia.png"), IMAGE_SIZE),
    "Supermercado": pygame.transform.scale(pygame.image.load("assets/supermercado.png"), IMAGE_SIZE),
    "Universidade": pygame.transform.scale(pygame.image.load("assets/universidade.png"), IMAGE_SIZE),
    "Zoológico": pygame.transform.scale(pygame.image.load("assets/zoologico.png"), IMAGE_SIZE),
}

character_image = pygame.transform.scale(pygame.image.load("assets/encanador.png"), IMAGE_SIZE)

# Função para desenhar o mapa
def draw_map(screen, visited_nodes, current_node, shortest_path=None):
    screen.fill(WHITE)

    # Desenhar rotas
    for route in routes:
        start, end, weight = route
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
def move_character_along_path(screen, start, end, shortest_path=None):
    start_pos = locations[start]
    end_pos = locations[end]

    # Configurar passos para o movimento
    steps = 50
    for step in range(steps + 1):
        x = start_pos[0] + (end_pos[0] - start_pos[0]) * step / steps
        y = start_pos[1] + (end_pos[1] - start_pos[1]) * step / steps
        draw_map(screen, [], None, shortest_path)  # Recarregar o mapa com o menor caminho
        screen.blit(character_image, (x - IMAGE_SIZE[0] // 2, y - IMAGE_SIZE[1] // 2))  # Desenhar personagem
        pygame.display.flip()
        time.sleep(0.02)  # Pausa curta para animação

# Algoritmo de Dijkstra animado
def dijkstra_animation(screen, start, end):
    distances = {node: float('inf') for node in locations}
    distances[start] = 0
    visited = set()
    path = {}

    while visited != set(locations.keys()):
        current_node = min(
            (node for node in distances if node not in visited),
            key=lambda x: distances[x]
        )

        visited.add(current_node)

        for route in routes:
            if current_node in route:
                neighbor = route[1] if route[0] == current_node else route[0]
                if neighbor not in visited:
                    move_character_along_path(screen, current_node, neighbor)
                    new_distance = distances[current_node] + route[2]
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        path[neighbor] = current_node

    current_node = end
    shortest_path = []
    while current_node != start:
        if current_node not in path:  # Verifica se o nó existe no path
            print(f"Erro: caminho não encontrado para {current_node}")
            return []  # Retorna uma lista vazia se não houver caminho válido
        shortest_path.append((path[current_node], current_node))
        current_node = path[current_node]
    shortest_path.reverse()

    return shortest_path

# Função para selecionar pontos de partida e destino
def choose_start_and_end(screen):
    start, end = None, None
    choosing = True

    while choosing:
        draw_map(screen, [], None)
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

# Função para desenhar um botão
def draw_button(screen, text, x, y, width, height, color, text_color, action=None):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return pygame.Rect(x, y, width, height)
