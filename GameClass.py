from back_end.TrainerClass import Trainer
from back_end.EnemyTrainerClass import EnemyTrainer
from back_end.pokemon import Pokemon
from back_end.battle import Battle
from model.display_intro import display_intro
from model.display_menu import display_menu
from model.display_game import display_game

import pygame



class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,450))
        self.clock = pygame.time.Clock()

        self.running = True
        self.game_state = "intro"
        self.POKEMON_TEMPLATE = [
    {'name':'Squirtle','type':'water','attack':50,'defence':50,'life':100,'sprite':'media/pokemon_assets/Squirtle_back.png','moov1':'Charge','moov2':'Watter gun'},
    {'name':'Pikachu','type':'electric','attack':60,'defence':45,'life':100,'sprite':'media/pokemon_assets/Pikachu_back.png','moov1':'Charge','moov2':'Thunder'},
    {'name':'Bulbasaur','type':'grass','attack':40,'defence':50,'life':100,'sprite':'media/pokemon_assets/Bulbasur_back.png','moov1':'Charge','moov2':'Leaf'},
    {'name':'Charmander','type':'fire','attack':70,'defence':30,'life':100,'sprite':'media/pokemon_assets/Charmander_back.png','moov1':'Charge','moov2':'Flamethrower'},
    {'name':'Pidgey','type':'normal','attack':45,'defence':45,'life':100,'sprite':'media/pokemon_assets/Pidgey_back.png','moov1':'Tackle','moov2':'Gust'},
    {'name':'Rattata','type':'normal','attack':48,'defence':43,'life':100,'sprite':'media/pokemon_assets/Rattata_back.png','moov1':'Tackle','moov2':'Quick Attack'}
    ]

    def start(self):
        trainer = Trainer("Player")
        enemy = EnemyTrainer("Rival")

        pygame.init()
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")
            
            match self.game_state:
                case "intro":
                    display_intro()    # first state
                case "main_menu":
                    display_main_menu()    # will return game.state depending on button clicked
                case "new_game":
                    #trainer.give_first_pokemon() -> in new_game()
                    new_game()      #will change game state to "game_menu"
                case "load_game":
                    load_game()     #will change game state to "game_menu"
                case "game_menu":
                    display_game_menu()
                case "game":
                    # enemy.choose_pokemon() -> in display_game?
                    display_game()  #from game menu and return to it
                case "pokedex":
                    display_pokedex()   #from game menu and return to it
                case "pokelist":
                    #enemy.add_pokemon_to_list(self.POKEMON_TEMPLATE) -> dans display_pokelist, "add" boutton
                    display_pokelist()  #from game menu and return to it

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

        
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