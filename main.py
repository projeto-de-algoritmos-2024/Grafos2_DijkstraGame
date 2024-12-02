import pygame
from menu import main_menu
from game import play_game
from help import instructions_screen

# Inicializar Pygame
pygame.init()

# Configurações de tela
WIDTH, HEIGHT = 1400, 980
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritmo de Dijkstra - Mapa da Cidade")

# Função principal
def main():
    while True:
        choice = main_menu(screen, WIDTH, HEIGHT)

        if choice == "start_game":
            play_game(screen, WIDTH, HEIGHT)
        elif choice == "instructions":
            instructions_screen(screen, WIDTH, HEIGHT)

if __name__ == "__main__":
    main()
