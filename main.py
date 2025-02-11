import pygame
from front_end import game

pygame.init()
screen = pygame.display.set_mode((800,450))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    game()



    # title.title()
    # name = name()
    # player1 = Trainer(name, [])
    # menu()
    #     if "game"
    #         game()
    #     if "stats"
    #         stats()
    #     if "pokemon_list"
    #         pokemon_list()
    #     default
    #         continue

    # choose_name() | (save_slot())
    # player1 = Trainer(""),  pokemon_list[3_pokemon] 
    # 





    pygame.display.flip()
    clock.tick(60)

pygame.quit()