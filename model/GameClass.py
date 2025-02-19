from model.battle import Battle
from model.JsonClass import Json

from ui.ui import Hitbox, Text, ImageElement
from ui.intro import display_intro
from ui.main_menu import display_main_menu
from ui.save_slots import new_game, load_game
from ui.game_menu import display_game_menu
from ui.ingame import display_ingame, display_battle_end
from ui.pokedex import display_pokedex
from ui.pokelist import display_pokelist

import pygame

class Game:
    def __init__(self):
        pygame.init()
        #Pygame Variables
        self.screen_size = (1200,675)
        self.screen = pygame.display.set_mode(self.screen_size)  # Nouvelle résolution
        self.clock = pygame.time.Clock()

        #Loop variables
        self.running = True
        self.game_state = "intro"
        self.ingame_state = "attacking"
        self.delay = 0

        self.battle_start = False

        #JSON
        self.open_json = Json().load_json
        self.save_json = Json().save_json

        #Constants
        self.MOOV_TEMPLATE = [
            {'name':'Tackle','type':'normal','accuracy':95},
            {'name':'Water Gun','type':'water','accuracy':80},
            {'name':'Thunder','type':'electric','accuracy':100},
            {'name':'Leaf','type':'grass','accuracy':60},
            {'name':'Flamethrower','type':'fire','accuracy':30},
            {'name':'Gust','type':'normal','accuracy':95},
            {'name':'Quick Attack','type':'normal','accuracy':100}
        ]
        
        self.POKEMON_TEMPLATE = [
            {'name':'Squirtle','type':'water','life':120,'attack':50,'defence':50,'moov':['Tackle','Water Gun']},
            {'name':'Pikachu','type':'electric','life':90,'attack':60,'defence':45,'moov':['Tackle','Thunder']},
            {'name':'Bulbasaur','type':'grass','life':180,'attack':40,'defence':50,'moov':['Tackle','Leaf']},
            {'name':'Charmander','type':'fire','life':150,'attack':70,'defence':30,'moov':['Tackle','Flamethrower']},
            {'name':'Pidgey','type':'normal','life':80,'attack':45,'defence':45,'moov':['Tackle','Gust']},
            {'name':'Rattata','type':'normal','life':50,'attack':48,'defence':43,'moov':['Tackle','Quick Attack']}
            ]

        # Declaration of all UI Elements
        ## First Screen - Intro
        self.button_intro = Hitbox((0,0), self.screen_size, 'main_menu')

        self.background = ImageElement("media/ui-elements/background.png")  
        self.start_text_img = ImageElement("media/ui-elements/Press-space-to-start-2-12-2025.png")  
        
        
        ## Second Screen - Main Menu
        self.button_main1 = Hitbox((450, 150), (300, 75), 'new_game')
        self.button_main2 = Hitbox((450, 300), (300, 75), 'load_game')
        self.button_main3 = Hitbox((450, 450), (300, 75), 'exit')
        self.button_main_menu = [self.button_main1, self.button_main2, self.button_main3]
        
        self.background_button_main = ImageElement("media/ui-elements/button.svg")
        
        self.text_button_main = Text("freesansbold.ttf", 36, (0,0,0))

        ## Third Screen - Game Menu
        self.button_game1 = Hitbox((350, 230), (500, 150), 'ingame')
        self.button_game2 = Hitbox((330, 400), (250, 75), 'pokedex')
        self.button_game3 = Hitbox((620, 400), (250, 75), 'pokemon')
        self.button_game4 = Hitbox((350, 500), (500, 100), 'main_menu')
        self.button_game_menu = [self.button_game1, self.button_game2, self.button_game3, self.button_game4]

        self.rectangle = ImageElement("media/ui-elements/RectangleSettings.png")
        
        self.background_button_game = ImageElement("media/ui-elements/button.png")
                
        self.text_button_game = Text("freesansbold.ttf", 36, (0,0,0))

        ## Fourth Screen - Ingame
        # Moov display 
        self.button_moov1 = Hitbox((225, 500), (225, 75))
        self.button_moov2 = Hitbox((825, 500), (225, 75))
        self.button_moov = [self.button_moov1, self.button_moov2]

        self.background_button_moov = ImageElement("media/ui-elements/button.png")

        self.text_button_moov = Text("freesansbold.ttf", 36, (0,0,0))

        #Interface
        #TODO add name and place it into frame
        self.life_text = Text("freesansbold.ttf", 36, (0,0,0))

        #battle messages
        self.button_battle_message = Hitbox((0, 500),(1200, 175))
        self.background_battle_message = ImageElement('media/ui-elements/button.png')
        self.text_battle_message = Text("freesansbold.ttf", 36, (0,0,0))

        ## Fourth Screen - Pokedex
        self.button_pokedex = Hitbox((195, 525), (804, 136), 'game_menu')

        self.box_background = ImageElement("media/ui-elements/box_background.png") 

    def start(self):
        """Start the main loop and switch state to change screen"""
        self.main_loop()
     
    def main_loop(self):
        while self.running:
            self.events()
            self.screen.fill("black")

            match self.game_state:
                case "intro":
                    display_intro(self)
                case "main_menu":
                    display_main_menu(self)
                case "new_game":
                     new_game(self)      #will change game state to "game_menu"
                case "load_game":
                    load_game(self)
                case "game_menu":
                    display_game_menu(self)
                case "ingame":
                    if not self.battle_start:
                        self.battle_ini()
                    display_ingame(self)
                case "battle_end":
                    display_battle_end(self)
                case "pokedex":
                    display_pokedex(self)
                case "pokemon":
                    display_pokelist(self)
                case _:
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def battle_ini(self):
        """Attributes that needs to be set only once (before battle) are here"""
        #----TEMP----
        #TODO remove this; this should be in pokemon.py
        for pokemon in self.POKEMON_TEMPLATE:
            self.enemy.add_pokemon_to_list(pokemon, self.MOOV_TEMPLATE)
        #------------
        self.enemy.choose_pokemon()
        self.trainer.load_pokedex(self.MOOV_TEMPLATE)

        self.battle = Battle(self.trainer, self.enemy)
        self.battle_start = True

    def events(self):                    
        # TODO refractor some events in their files or put ticks after a state change

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.K_SPACE:
                if self.game_state == "intro":
                    self.game_state = self.button_intro.label

            if event.type == pygame.MOUSEBUTTONDOWN:
                #----- Intro screen events
                if self.game_state == "intro" and self.button_intro.is_clicked(pygame.mouse.get_pos()):
                    self.game_state = self.button_intro.label

                #-----
                #----- Main Menu screen events
                for button in self.button_main_menu:
                    if self.game_state == "main_menu" and button.is_clicked(pygame.mouse.get_pos()):
                        self.game_state = button.label
                #-----
                #----- Game Menu screen events
                for button in self.button_game_menu:
                    if self.game_state == "game_menu" and button.is_clicked(pygame.mouse.get_pos()):
                        self.game_state = button.label
                #-----
                #----- Pokelist screen events
                # TODO add a state for enable/disabled pokemon + create button_pokemon_list (button on each pokemon)
                # for button in self.button_pokemon_list:
                #     if self.game_state == "pokelist" and button.is_clicked(pygame.mouse.get_pos()):
                #         self.enemy.add_pokemon_to_list()

                if (self.game_state == "pokedex" or self.game_state == "pokelist") and self.button_pokedex.is_clicked(pygame.mouse.get_pos()):
                    self.game_state = button.label
                #-----
                #----- Ingame screen events
                for button in self.button_moov:
                    if self.game_state == "ingame" and button.is_clicked(pygame.mouse.get_pos()):
                        for moov in self.battle.turn_pkmn.moov:
                            if moov.name == button.label: 
                                self.battle.chosen_moov = moov
                                self.delay = pygame.time.get_ticks() + 1500   
                                self.battle.ingame_state = "attacking" 
                #-----
