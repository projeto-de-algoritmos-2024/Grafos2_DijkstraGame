import pygame
from resources import get_font

# Função para desenhar um botão na tela
def draw_button(screen, text, x, y, width, height, color, text_color):
    font = get_font(40)  # Define a fonte para os botões
    pygame.draw.rect(screen, color, (x, y, width, height))  # Desenha o retângulo do botão
    text_surface = font.render(text, True, text_color)  # Cria a superfície do texto
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Centraliza o texto no botão
    screen.blit(text_surface, text_rect)  # Desenha o texto no botão
    return pygame.Rect(x, y, width, height)  # Retorna o retângulo do botão

# Função que exibe o menu principal
def main_menu(screen, WIDTH, HEIGHT):
    running = True
    while running:
        screen.fill((255, 255, 255))  # Cor de fundo branca

        # Carrega e ajusta a imagem de fundo
        bg_image = pygame.image.load("assets/background.jpg")
        bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
        screen.blit(bg_image, (0, 0))

        # Renderiza o título com fundo discreto
        title_font = get_font(60)
        title_surface = title_font.render("Dijkstra - Mapa da Cidade", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        # Desenha um fundo discreto atrás do título
        pygame.draw.rect(screen, (0, 0, 0, 150), title_rect.inflate(20, 10))
        screen.blit(title_surface, title_rect)

        # Renderiza os botões do menu
        start_button = draw_button(screen, "Iniciar Jogo", WIDTH // 2 - 150, HEIGHT // 2 - 50, 300, 70, (200, 200, 200), (0, 0, 0))
        instructions_button = draw_button(screen, "Como Jogar", WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 70, (200, 200, 200), (0, 0, 0))

        pygame.display.flip()

        # Captura os eventos de clique
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Se o botão de "Iniciar Jogo" for clicado
                if start_button.collidepoint(event.pos):
                    return "start_game"
                # Se o botão de "Como Jogar" for clicado
                elif instructions_button.collidepoint(event.pos):
                    return "instructions"
