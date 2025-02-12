import pygame
from utils import *

pygame.init()

class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    # To draw text
    def draw_text(self, text, position, color=(0, 0, 0)):
        rendered_text= self.font.render(text,True, color, position)
        self.screen.blit(rendered_text, position)

    # To clear the screen
    def clear_screen(self, color=(255, 255, 255)):
        self.screen.fill(color)

    # To allow the player to choose an attack
    def choose_attack(screen, pokemon):
        button1 = Button(pokemon['moov1'], 100, 300, 200, 50) # should be changed
        button2 = Button(pokemon['moov2'], 400, 300, 200, 50) # should be changed
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button1.is_clicked(mouse_pos):
                        return pokemon['moov1'], pokemon.moove_type_1
                    elif button2.is_clicked(mouse_pos):
                        return pokemon['moov2'], pokemon.moove_type_2
            screen.fill(Button.WHITE)
            render_message(screen, font, f"{pokemon['name']}, choose your attack!")
            render_message(screen, font, "Press 1 :" + pokemon['moov1'])
            render_message(screen, font,"Press 2 :" + pokemon['moov2'])

            button1.draw(screen)
            button2.draw(screen)
            pygame.display.flip()