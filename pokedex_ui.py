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
    
    # To handle player interaction
    def handle_pokemon_selection(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    index = (mouse_pos[1] - 100) //30
                    if 0 <= index <len(self.pokemon_data):
                        self.display_pokemon_details(self.pokemon_data[index])
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.go_to_previous_screen() 

    # To display pokemon details
    def display_pokemon_details(self, pokemon):
        self.screen.blit(self.background_image, (0,0))

        self.screen.blit(self.text_box_image, (130, 292))

        self.draw_text(f"Name: {pokemon['name']}", (100, 120))
        self.draw_text(f"Type: {pokemon['pkm_type']}", (100, 160))
        self.draw_text(f"Attack: {pokemon['attack']}", (100, 200))
        self.draw_text(f"Defence: {pokemon['defence']}", (100, 280))
        self.draw_text(f"Life: {pokemon['life']}", (100, 280))
        self.draw_text(f"Moves: {pokemon['moov1']}, {pokemon['moov2']}", (100, 320))

        self.draw_text("Press Space to go back", (100, 350))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
                    if event.key == pygame.K_SPACE:
                        self.go_to_previous_screen()

    # To go to the previous screen
    def go_to_previous_screen(self):
        self.display_pokedex() # Change here to go to the desired screen

# To call the pokedex:
#pokedex = Pokedex(scree, 'pokedex.json')
#pokedex.display_pokedex()

# Also to do the intire pokemon list copy this file, rename it and 
# change the source



