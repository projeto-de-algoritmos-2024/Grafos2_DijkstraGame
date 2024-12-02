import pygame
import time

# Adicionar as variáveis globais e funções específicas do jogo aqui (locais, rotas, etc.)
from resources import draw_map, dijkstra_animation, choose_start_and_end, draw_button

def play_game(screen, WIDTH, HEIGHT):
    playing = True
    while playing:
        start, end = choose_start_and_end(screen)
        shortest_path = dijkstra_animation(screen, start, end)
        draw_map(screen, [], None, shortest_path)

        back_button = draw_button(screen, "Voltar", WIDTH - 150, HEIGHT - 70, 120, 50, (200, 200, 200), (0, 0, 0))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        waiting = False
                        playing = False
