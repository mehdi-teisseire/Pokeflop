from model.TrainerClass import Trainer
from model.EnemyTrainerClass import EnemyTrainer
from model.pokemon import Pokemon
from model.battle import Battle
from ui.ui import UIElement, Text, ImageElement
from ui.intro import display_intro
#from ui.main_menu import display_main_menu
#from ui.save_slots import new_game, load_game
#from ui.game_menu import display_game_menu
from ui.ingame import display_ingame
#from ui.pokedex import display_pokedex
#from ui.pokelist import display_pokelist

import pygame



class Game:
    def __init__(self):
        #Pygame Variables
        self.screen = pygame.display.set_mode((800,450))
        self.clock = pygame.time.Clock()

        #Loop variables
        self.running = True
        self.game_state = "intro"

        self.battle_start = False

        #Constants
        #can make a separate file and import it (list would be long right?) - constant.py?
        self.POKEMON_TEMPLATE = [
            {'name':'Squirtle','sprite':'media/pokemon_assets/Squirtle_back.png','pkmn_type':'water','life':100,'attack':50,'defence':50,'moove1':'Charge','moove2':'Water gun'},
            {'name':'Pikachu','sprite':'media/pokemon_assets/Pikachu_back.png','pkmn_type':'electric','life':100,'attack':60,'defence':45,'moove1':'Charge','moove2':'Thunder'},
            {'name':'Bulbasaur','sprite':'media/pokemon_assets/Bulbasaur_back.png','pkmn_type':'grass','life':100,'attack':40,'defence':50,'moove1':'Charge','moove2':'Leaf'},
            {'name':'Charmander','sprite':'media/pokemon_assets/Charmander_back.png','pkmn_type':'fire','life':100,'attack':70,'defence':30,'moove1':'Charge','moove2':'Flamethrower'},
            {'name':'Pidgey','sprite':'media/pokemon_assets/Pidgey_back.png','pkmn_type':'normal','life':100,'attack':45,'defence':45,'moove1':'Tackle','moove2':'Gust'},
            {'name':'Rattata','sprite':'media/pokemon_assets/Rattata_back.png','pkmn_type':'normal','life':100,'attack':48,'defence':43,'moove1':'Tackle','moove2':'Quick Attack'}
            ]

        ##Colors - Last number is alpha
        self.TRANSPARENT = pygame.Color(0,0,0,0)
        #CUSTOM_BLUE = (0,0,0,0)
        #CUSTOM_YELLOW = (0,0,0,0)
        #ETC = (0,0,0,0)


        #All game button
        ##First Screen - Intro
        self.background = ImageElement("media/ui-elements/background.png", (800, 450), (0, 0))
        self.start_text_img = ImageElement("media/ui-elements/Press-space-to-start-2-12-2025.png", (579, 88), (120, 200))
        self.button_intro = UIElement('test', 0, 0, 400, 450, (12,12,12))

        ##Second Screen - Main Menu
        # self.button_new_game = Button(pokemon.moov1, 100, 300, 200, 50) # should be changed
        # self.button_load_game = Button(pokemon.moov2, 400, 300, 200, 50)

        ##Third Screen - Game Menu

        ##Fourth Screen - Ingame
        self.background_button_moov = ImageElement("media/ui-elements/MDPokemonBattle_Notextbox.png", (150, 50), (0, 0))
        
        self.button_moov1 = UIElement('moove1', 150, 400, 150, 50)
        self.button_moov2 = UIElement('moove2', 550, 400, 150, 50)

        ##Fourth Screen - Pokedex

        ##Fifth Screen - Pokelist


    def start(self):
        """Initialise the game and start the main loop"""
        # Player and AI object are created here. It's for deck-building/random encounter feature
        self.trainer = Trainer("Player")
        self.enemy = EnemyTrainer("Rival")

        pygame.init()

        # Texts are declared here. Have to init fonts to create them (or declare font separateley)
        self.text_button_moov1 = Text("freesansbold.ttf", 36, "", (0,0,0), 150, 400)
        self.text_button_moov2 = Text("freesansbold.ttf", 36, "", (0,0,0), 550, 400)


        self.main_loop()
     
    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_state == "intro" and self.button_intro.is_clicked(pygame.mouse.get_pos()):
                        self.game_state = "ingame"
                    if self.game_state == "ingame" and self.button_moov1.is_clicked(pygame.mouse.get_pos()):
                        self.battle.turn_pkmn.attacking(self.battle.opponent_pkmn)


            self.screen.fill("black")
            
            match self.game_state:
                case "intro":
                    display_intro(self)    # first state

                case "main_menu":
                    display_main_menu()    # will return game.state depending on button clicked

                case "new_game":
                    #trainer.give_first_pokemon() -> in new_game()
                    new_game()      #will change game state to "game_menu"

                case "load_game":
                    load_game()     #will change game state to "game_menu"

                case "game_menu":
                    display_game_menu()

                case "ingame":
                    # enemy.choose_pokemon() -> in display_game?
                    if not self.battle_start:
                        self.battle_ini()
                    display_ingame(self)  #from game menu and return to it

                case "pokedex":
                    display_pokedex()   #from game menu and return to it

                case "pokelist":
                    #enemy.add_pokemon_to_list(self.POKEMON_TEMPLATE) -> dans display_pokelist, "add" boutton
                    display_pokelist()  #from game menu and return to it

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def battle_ini(self):
        """Attributes that needs to be set only once (before battle) are here"""
        #----TEMP----
        self.trainer.add_pokemon(self.trainer.convert_pokemon_to_obj(self.POKEMON_TEMPLATE[0]))
        self.enemy.add_pokemon_to_list(self.POKEMON_TEMPLATE)
        #------------
        self.enemy.choose_pokemon()
        self.battle = Battle(self.trainer, self.enemy)
        self.battle_start = True
        
        # running = True
        # battle = Battle(trainer, enemy)

        # while True:
        #     battle.choosed_move = battle.choose_move()
        #     if battle.has_missed(): #maybe go into pokemon class
        #         print("missed!")
        #     else:
        #         battle.attack_damage() #maybe go into pokemon class
        #         running = battle.check_health_points()
        #     battle.change_turn()

        #move selected self.choosed_move
        #accuracy check if has_missed() : you missed, else:
        #damage_calc attack_damage()
        #check 0 hp check_health_points()
        #turn change change_turn()