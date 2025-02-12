import pygame
from pokeflop_ui import Pokeflop 


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PokeFlop Game")


pokeflop = Pokeflop(screen)


running = True
while running:

    pokeflop.display_pokeflop()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()