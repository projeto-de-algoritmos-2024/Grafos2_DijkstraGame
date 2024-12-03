import pygame
import time
from resources import draw_map, dijkstra_animation, choose_start_and_end, draw_button

# Função para iniciar o jogo e executar a lógica principal
def play_game(screen, WIDTH, HEIGHT):
    playing = True
    while playing:
        # Escolher os pontos de início e fim do caminho
        start, end = choose_start_and_end(screen)
        
        # Executar a animação do algoritmo de Dijkstra
        shortest_path, total_distance = dijkstra_animation(screen, start, end)

        # Desenhar o mapa com o caminho mais curto e a distância total
        draw_map(screen, shortest_path, total_distance)

        # Desenhar o botão de "Voltar" para sair do jogo
        back_button = draw_button(screen, "Voltar", WIDTH - 150, HEIGHT - 70, 120, 50, (200, 200, 200), (0, 0, 0))
        pygame.display.flip()

        # Esperar pelo evento de clique para voltar
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Encerra o jogo
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):  
                        waiting = False  # Encerra a tela de jogo
                        playing = False  # Encerra o jogo
