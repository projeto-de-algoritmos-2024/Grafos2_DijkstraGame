import pygame

pygame.font.init()
small_font = pygame.font.SysFont(None, 30)

# Função para desenhar um botão na tela
def draw_button(screen, text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))  # Desenha o retângulo do botão
    text_surface = small_font.render(text, True, text_color)  # Cria a superfície do texto
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Centraliza o texto
    screen.blit(text_surface, text_rect)  # Desenha o texto no botão
    return pygame.Rect(x, y, width, height)  # Retorna o retângulo do botão

# Função que exibe a tela de instruções
def instructions_screen(screen, WIDTH, HEIGHT):
    running = True
    # Carrega e ajusta a imagem de fundo
    background = pygame.image.load("assets/background.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Ajusta o tamanho da tela

    while running:
        screen.blit(background, (0, 0))  # Coloca o fundo na tela

        # Texto das instruções
        instructions_text = [
            "Você é um encanador experiente,",
            "conhecendo cada canto da cidade.",
            "Seu objetivo é chegar aos locais de trabalho",
            "no menor tempo possível, passando pelas rotas",
            "mais rápidas e evitando o tráfego.",
            "Use o algoritmo de Dijkstra para encontrar o",
            "caminho mais curto e completar seus serviços!",
            "Selecione o Local de Início e o Final",
            "E veja o algoritmo de Dijkstra traçar o menor caminho",
        ]

        # Calcular a posição inicial para centralizar o texto verticalmente
        total_text_height = len(instructions_text) * 40  # Cada linha tem 40px de altura
        start_y = (HEIGHT - total_text_height) // 2  # Centraliza o texto na tela

        # Desenha cada linha de texto centralizada
        for i, line in enumerate(instructions_text):
            text_surface = small_font.render(line, True, (0, 0, 0))  # Cor preta para o texto
            text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * 40))  # Centraliza o texto
            pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(20, 10))  # Fundo branco para o texto
            screen.blit(text_surface, text_rect)  # Coloca o texto na tela

        # Desenha o botão de "Voltar"
        back_button = draw_button(screen, "Voltar", WIDTH // 2 - 100, HEIGHT - 100, 200, 50, (200, 200, 200), (0, 0, 0))

        pygame.display.flip()

        # Lidar com os eventos de interação
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):  # Verifica se o botão "Voltar" foi clicado
                    running = False  # Encerra a tela de instruções
