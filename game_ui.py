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
        button1 = Button(pokemon['moov1'], 100, 300, 200, 50) 
        button2 = Button(pokemon['moov2'], 400, 300, 200, 50)
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
    
    # A button to surrender 
    def surrender(self, screen, pokemon, font, player):
        surrender_button = Button("Surrender", 250, 300, 200, 50)
        screen.fill(Button.WHITE)
        surrender_button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if surrender_button.is_clicked(mouse_pos):
                    message = f"{pokemon.name} has surrendered !"  
                    render_message(screen, message, font)
                    winner = self.current_pokemon_2.name if player == self.current_pokemon_1 else self.current_pokemon_1.name 
                    message = f"{winner} wins by default!"
                    return  

"""
# to place in the function or 
# in the main at the place where 
# we want this file to be called
ui = GameUI(screen)
ui.clear_screen()
pygame.display.flip()
pygame.time.delay(2000)

"""