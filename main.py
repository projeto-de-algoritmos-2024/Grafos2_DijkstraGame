import pygame
from menu import main_menu
from game import play_game
from help import instructions_screen

pygame.init()

# Configurações de tela
WIDTH, HEIGHT = 1400, 980
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritmo de Dijkstra - Mapa da Cidade")

# Função principal que controla o fluxo do jogo
def main():
    while True:
        # Exibe o menu principal e captura a escolha do usuário
        choice = main_menu(screen, WIDTH, HEIGHT)

        # Inicia o jogo quando a opção "start_game" é selecionada
        if choice == "start_game":
            play_game(screen, WIDTH, HEIGHT)
        
        # Exibe as instruções quando a opção "instructions" é selecionada
        elif choice == "instructions":
            instructions_screen(screen, WIDTH, HEIGHT)

if __name__ == "__main__":
    main()
