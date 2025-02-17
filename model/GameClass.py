from model.TrainerClass import Trainer
from model.EnemyTrainerClass import EnemyTrainer
from model.battle import Battle
from model.JsonClass import Json

from ui.ui import UIElement, Text, ImageElement
from ui.intro import display_intro
from ui.main_menu import display_main_menu
from ui.save_slots import new_game, load_game
from ui.game_menu import display_game_menu
from ui.ingame import display_ingame
from ui.pokedex import display_pokedex
from ui.pokelist import display_pokelist

import pygame



class Game:
    def __init__(self):
        #Pygame Variables
        self.screen = pygame.display.set_mode((800,450))
        self.clock = pygame.time.Clock()

        #Loop variables
        self.running = True
        self.game_state = "intro"

        self.battle_start = False # For the Battle_ini(). Makes it so you don't repeat it. Revert to false when battle ends.

        #Constants
        #can make a separate file and import it (list would be long right?) - constant.py?
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
            {'name':'Squirtle','sprite':'media/Pokemons-assets/front/Squirtle_back.png','type':'water','life':100,'attack':50,'defence':50,'moov':['Tackle','Water Gun']},
            {'name':'Pikachu','sprite':'media/pokemon_assets/Pikachu_back.png','type':'electric','life':100,'attack':60,'defence':45,'moov':['Tackle','Thunder']},
            {'name':'Bulbasaur','sprite':'media/pokemon_assets/Bulbasaur_back.png','type':'grass','life':100,'attack':40,'defence':50,'moov':['Tackle','Leaf']},
            {'name':'Charmander','sprite':'media/pokemon_assets/Charmander_back.png','type':'fire','life':100,'attack':70,'defence':30,'moov':['Tackle','Flamethrower']},
            {'name':'Pidgey','sprite':'media/pokemon_assets/Pidgey_back.png','type':'normal','life':100,'attack':45,'defence':45,'moov':['Tackle','Gust']},
            {'name':'Rattata','sprite':'media/pokemon_assets/Rattata_back.png','type':'normal','life':100,'attack':48,'defence':43,'moov':['Tackle','Quick Attack']}
            ]

        #All game button
        ##First Screen - Intro
        self.background = ImageElement("media/ui-elements/background.png", (0, 0), (800, 450))
        self.start_text_img = ImageElement("media/ui-elements/Press-space-to-start-2-12-2025.png", (120, 200), (579, 88))
        
        self.button_intro = UIElement('main_menu', 0, 0, 800, 450)
        
        # self.open_json = Json().load_json
        # self.save_json = Json().save_json

        ##Second Screen - Main Menu
        self.button_main1 = UIElement('new_game', 300, 100, 200, 50)
        self.button_main2 = UIElement('load_game', 300, 200, 200, 50)
        self.button_main3 = UIElement('exit', 300, 300, 200, 50)
        
        self.background_button_main1 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (300, 100), (200, 50))
        self.background_button_main2 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (300, 200), (200, 50))
        self.background_button_main3 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (300, 300), (200, 50))

        self.button_main_menu = [self.button_main1, self.button_main2, self.button_main3]

        ##Third Screen - Game Menu
        self.button_game1 = UIElement('ingame', 300, 100, 200, 50)
        self.button_game2 = UIElement('pokedex', 300, 200, 200, 50)
        self.button_game3 = UIElement('pokemon', 300, 300, 200, 50)
        self.button_game4 = UIElement('main_menu', 300, 400, 200, 50)
        
        self.background_button_game1 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (300, 100), (200, 50))
        self.background_button_game2 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (300, 200), (200, 50))
        self.background_button_game3 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (300, 300), (200, 50))
        self.background_button_game4 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (300, 400), (200, 50))
        
        self.button_game_menu = [self.button_game1, self.button_game2, self.button_game3, self.button_game4]

        ##Fourth Screen - Ingame      
        self.background_button_moov1 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (100, 300), (250, 75))
        self.background_button_moov2 = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (450, 300), (250, 75))
        
        self.button_moov1 = UIElement('moov1', 150, 200, 150, 50)
        self.button_moov2 = UIElement('moov2', 550, 200, 150, 50)

        self.button_moov = [self.button_moov1, self.button_moov2]
        ##Fourth Screen - Pokedex
        self.background_pokedex = ImageElement("media/ui-elements/button.png", (130, 350), (536, 91))
        ##Fifth Screen - Pokelist

    def start(self):
        """Initialise the game and start the main loop"""
        # Player and AI object are created here. It's for deck-building/random encounter feature
        self.trainer = Trainer("Player")
        self.enemy = EnemyTrainer("Rival")

        pygame.init()

        ##Colors - Last number is alpha
        #self.TRANSPARENT = pygame.Color(0,0,0,0)
        #CUSTOM_BLUE = (0,0,0,0)
        #CUSTOM_YELLOW = (0,0,0,0)
        #ETC = (0,0,0,0)

        # Texts are declared here. Have to init fonts to create them (or declare font separateley)
       
        ## Main Menu Text
        self.text_button_main1 = Text("freesansbold.ttf", 36, "", (0,0,0), 20, 50)
        self.text_button_main2 = Text("freesansbold.ttf", 36, "", (0,0,0), 320, 50)
        self.text_button_main3 = Text("freesansbold.ttf", 36, "", (0,0,0), 320, 50)
       
        ## Game Menu Text
        self.text_button_game1 = Text("freesansbold.ttf", 36, "", (0,0,0), 20, 50)
        self.text_button_game2 = Text("freesansbold.ttf", 36, "", (0,0,0), 320, 50)
        self.text_button_game3 = Text("freesansbold.ttf", 36, "", (0,0,0), 20, 50)
        self.text_button_game4 = Text("freesansbold.ttf", 36, "", (0,0,0), 320, 50)
       
        ## Ingame Text
        self.life_trainer_text = Text("freesansbold.ttf", 36, "", (0,0,0), 20, 50)
        self.life_opponent_text = Text("freesansbold.ttf", 36, "", (0,0,0), 320, 50)
       
        self.text_button_moov1 = Text("freesansbold.ttf", 36, "", (0,0,0), 150, 400)
        self.text_button_moov2 = Text("freesansbold.ttf", 36, "", (0,0,0), 550, 400)

        self.main_loop()
     
    def main_loop(self):
        while self.running:
            self.events()

            self.screen.fill("black")
            
            match self.game_state:
                case "intro":
                    display_intro(self)    # first state

                case "main_menu":
                    display_main_menu(self)    # will return game.state depending on button clicked

                case "new_game":
                     new_game(self)      #will change game state to "game_menu"

                case "load_game":
                    load_game(self)     #will change game state to "game_menu"

                case "game_menu":
                    display_game_menu(self)

                case "ingame":
                    if not self.battle_start:
                        self.battle_ini()
                    display_ingame(self)  #from game menu and return to it

                case "pokedex":
                    display_pokedex(self)   #from game menu and return to it

                case "pokelist":
                    #enemy.add_pokemon_to_list(self.POKEMON_TEMPLATE) -> dans display_pokelist, "add" boutton
                    display_pokelist(self)  #from game menu and return to it

                case _:
                    pygame.quit()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def battle_ini(self):
        """Attributes that needs to be set only once (before battle) are here"""
        #----TEMP----
        self.enemy.add_pokemon_to_list(self.POKEMON_TEMPLATE[0], self.MOOV_TEMPLATE)
        #------------
        self.enemy.choose_pokemon()
        self.trainer.load_pokedex(self.MOOV_TEMPLATE) #It's for healink!!

        self.battle = Battle(self.trainer, self.enemy)
        self.battle_start = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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
                #----- Ingame screen events
                for button in self.button_moov:
                    if self.game_state == "ingame" and button.is_clicked(pygame.mouse.get_pos()):
                        # TODO maybe refractor this into ingame.py? I don't know
                        for moov in self.battle.turn_pkmn.moov:
                            if moov.name == button.label: ###
                                self.battle.chosen_moov = moov
                        #TODO should just change chosen_move and chosen_move back to False after the attack
                        #TODO Begin_move should happen in the display
                        
                #-----
