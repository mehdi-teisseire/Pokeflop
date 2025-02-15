import pygame
import json

class Pokedex:
    def __init__(self, screen, json_file):
        self.screen = screen
        self.pokemon_data = self.load_pokemon_data(json_file)
        self.font = pygame.font.Font(None, 36)

        self.background_image = pygame.image.load('media/picture/box_background 1.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 400))

        self.text_box_image = pygame.image.load('media/picture/MDPokemonBattle_TextBox.png')
        self.text_box_image = pygame.transform.scale(self.text_box_image, (550, 80)) 

