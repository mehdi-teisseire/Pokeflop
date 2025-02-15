import pygame
import json

# To display the pokedex screen
class Pokedex:
    def __init__(self, screen, json_file):
        self.screen = screen
        self.pokemon_data = self.load_pokemon_data(json_file)
        self.font = pygame.font.Font(None, 36)

        self.background_image = pygame.image.load('media/picture/box_background 1.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 400))

        self.text_box_image = pygame.image.load('media/picture/MDPokemonBattle_TextBox.png')
        self.text_box_image = pygame.transform.scale(self.text_box_image, (550, 80)) 

    # To load the data
    def load_pokemon_data(self, json_file):
        with open(json_file, 'r') as file:
            return json.load(file)

    # to draw text on the screen
    def draw_text(self, text, position, color = (0, 0, 0)):
        rendered_text = self.font.render(text, True, color)
        self.screen.blit(rendered_text, position)   

    # To display the pokedex list
    def display_pokedex(self):

        self.screen.blit(self.background_image, (0, 0))
        self.draw_text("Pokédex", (100, 50), (0, 0, 0)) 

        for i, pokemon in enumerate(self.pokemon_data):
            self.draw_text(pokemon["name"], (100, 100 + i * 30))

        pygame.display.flip()
        self.handle_pokemon_selection()

