import pygame

pygame.font.init()
small_font = pygame.font.SysFont(None, 30)

def draw_button(screen, text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = small_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return pygame.Rect(x, y, width, height)

def instructions_screen(screen, WIDTH, HEIGHT):
    running = True
    while running:
        screen.fill((255, 255, 255))  # Branco
        instructions_text = [
            "Você é um encanador experiente,",
            "conhecendo cada canto da cidade.",
            "Seu objetivo é chegar aos locais de trabalho",
            "no menor tempo possível, passando pelas rotas",
            "mais rápidas e evitando o tráfego.",
            "Use o algoritmo de Dijkstra para encontrar o",
            "caminho mais curto e completar seus serviços!",
            "Selecione o Local de Início e o Final",
            "E veja o algoritmo de Djikstra traçar o menor caminho",
        ]

        for i, line in enumerate(instructions_text):
            text_surface = small_font.render(line, True, (0, 0, 0))
            screen.blit(text_surface, (50, 50 + i * 40))

        back_button = draw_button(screen, "Voltar", WIDTH // 2 - 100, HEIGHT - 100, 200, 50, (200, 200, 200), (0, 0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False
