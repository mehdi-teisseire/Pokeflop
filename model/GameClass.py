from model.TrainerClass import Trainer
from model.EnemyTrainerClass import EnemyTrainer
from model.pokemon import Pokemon
from model.battle import Battle
from model.JsonClass import Json
from ui.ui import UIElement, Text, ImageElement
from ui.intro import display_intro

#from ui.main_menu import display_main_menu
#from ui.save_slots import new_game, load_game
from ui.main_menu import display_main_menu
from ui.ingame import display_ingame
from ui.pokedex import display_pokedex
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

        self.battle_start = False # For the Battle_ini(). Makes it so you don't repeat it. Revert to false when battle ends.

        #Constants
        #can make a separate file and import it (list would be long right?) - constant.py?
        self.POKEMON_TEMPLATE = [
            {'name':'Squirtle','sprite':'media/Pokemons-assets/front/Squirtle_back.png','pkmn_type':'water','life':100,'attack':50,'defence':50,'moov1':'Charge','moov2':'Water gun'},
            {'name':'Pikachu','sprite':'media/pokemon_assets/Pikachu_back.png','pkmn_type':'electric','life':100,'attack':60,'defence':45,'moov1':'Charge','moov2':'Thunder'},
            {'name':'Bulbasaur','sprite':'media/pokemon_assets/Bulbasaur_back.png','pkmn_type':'grass','life':100,'attack':40,'defence':50,'moov1':'Charge','moov2':'Leaf'},
            {'name':'Charmander','sprite':'media/pokemon_assets/Charmander_back.png','pkmn_type':'fire','life':100,'attack':70,'defence':30,'moov1':'Charge','moov2':'Flamethrower'},
            {'name':'Pidgey','sprite':'media/pokemon_assets/Pidgey_back.png','pkmn_type':'normal','life':100,'attack':45,'defence':45,'moov1':'Tackle','moov2':'Gust'},
            {'name':'Rattata','sprite':'media/pokemon_assets/Rattata_back.png','pkmn_type':'normal','life':100,'attack':48,'defence':43,'moov1':'Tackle','moov2':'Quick Attack'}
            ]

        ##Colors - Last number is alpha
        #self.TRANSPARENT = pygame.Color(0,0,0,0)
        #CUSTOM_BLUE = (0,0,0,0)
        #CUSTOM_YELLOW = (0,0,0,0)
        #ETC = (0,0,0,0)


        #All game button
        ##First Screen - Intro
        self.background = ImageElement("media/ui-elements/background.png", (0, 0), (800, 450))
        self.start_text_img = ImageElement("media/ui-elements/Press-space-to-start-2-12-2025.png", (120, 200), (579, 88))
        
        self.button_intro = UIElement('test', 0, 0, 800, 450)
        
        self.open_json = Json().load_json
        self.save_json = Json().save_json

        

        ##Second Screen - Main Menu
        # self.button_new_game = Button(pokemon.moov1, 100, 300, 200, 50) # should be changed
        # self.button_load_game = Button(pokemon.moov2, 400, 300, 200, 50)

        ##Third Screen - Game Menu

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

        # Texts are declared here. Have to init fonts to create them (or declare font separateley)
       
        ## Ingame Text
        self.life_trainer_text = Text("freesansbold.ttf", 36, "", (0,0,0), 20, 50)
        self.life_opponent_text = Text("freesansbold.ttf", 36, "", (0,0,0), 320, 50)
       
        self.text_button_moov1 = Text("freesansbold.ttf", 36, "", (0,0,0), 150, 400)
        self.text_button_moov2 = Text("freesansbold.ttf", 36, "", (0,0,0), 550, 400)


        self.main_loop()
     
    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #----- Intro screen events
                    if self.game_state == "intro" and self.button_intro.is_clicked(pygame.mouse.get_pos()):
                        self.game_state = "ingame"
                    #-----

                    #----- Ingame screen events
                    for button in self.button_moov:
                        if self.game_state == "ingame" and button.is_clicked(pygame.mouse.get_pos()):
                            # TODO maybe refractor this into ingame.py? I don't know
                            self.battle.mooving = True
                            self.battle.moov_missed = self.battle.turn_pkmn.attacking(self)
                            self.battle.mooving = False
                            if self.battle.opponent_pokemon_ko():
                                print("Battle Finished! Return to main menu")
                                self.enemy.give_pokemon(self.trainer)
                                pygame.time.wait(1000)
                                self.battle_start = False
                                self.game_state = "intro"
                            self.battle.change_turn()
                    #-----
                    
                    # if self.game_state == "ingame" and self.button_moov1.is_clicked(pygame.mouse.get_pos()):
                    #     self.battle.turn_pkmn.attacking(self.battle.opponent_pkmn, self.text_button_moov1.text)
                    #     self.battle.change_turn()
                    # if self.game_state == "ingame" and self.button_moov2.is_clicked(pygame.mouse.get_pos()):
                    #     self.battle.turn_pkmn.attacking(self.battle.opponent_pkmn, self.text_button_moov2.text)
                        
                    #     if self.battle.opponent_pkmn_ko():
                    #         pygame.time.wait(1000)
                    #         self.game_state = "intro"
                            
                    #     self.battle.change_turn()

            self.screen.fill("black")
            
            match self.game_state:
                case "intro":
                    display_pokedex(self)    # first state

                case "main_menu":
                    display_main_menu()     #will change game state to "game_menu"
                case "new_game":
                    #trainer.give_first_pokemon() -> in new_game()
                    new_game()      #will change game state to "game_menu"

                case "load_game":
                    load_game()     #will change game state to "game_menu"

                case "game_menu":
                    display_game_menu()

                case "ingame":
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
        self.trainer.load_pokedex() #It's for healink!!

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