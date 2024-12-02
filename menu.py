import pygame

# Fonte para texto
pygame.font.init()
font = pygame.font.SysFont(None, 50)

def draw_button(screen, text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return pygame.Rect(x, y, width, height)

def main_menu(screen, WIDTH, HEIGHT):
    running = True
    while running:
        screen.fill((255, 255, 255))  # Branco
        title_surface = font.render("Dijkstra - Mapa da Cidade", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_surface, title_rect)

        start_button = draw_button(screen, "Iniciar Jogo", WIDTH // 2 - 150, HEIGHT // 2 - 50, 300, 70, (200, 200, 200), (0, 0, 0))
        instructions_button = draw_button(screen, "Como Jogar", WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 70, (200, 200, 200), (0, 0, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start_game"
                elif instructions_button.collidepoint(event.pos):
                    return "instructions"
