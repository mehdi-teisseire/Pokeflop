from model.battle import Battle
from model.JsonClass import Json

from ui.ui import Hitbox, Text, ImageElement
from ui.intro import display_intro
from ui.main_menu import display_main_menu
from ui.save_slots import new_game, load_game
from ui.game_menu import display_game_menu
from ui.ingame import display_ingame, display_battle_end, choose_pokemon_battle
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
        self.mixer = pygame.mixer
        self.mixer.init()

        #Loop variables
        self.running = True
        self.game_state = "intro"
        self.delay = 0

        self.battle_start = False

        self.sprite_positions = []

        #JSON
        self.open_json = Json().load_json
        self.save_json = Json().save_json

        #Constants
        self.MOOV_TEMPLATE = [
            {'name':'Tackle','type':'normal','accuracy':95},
            {'name':'Water Gun','type':'water','accuracy':85},
            {'name':'Thunder','type':'electric','accuracy':90},
            {'name':'Leaf','type':'grass','accuracy':90},
            {'name':'Flamethrower','type':'fire','accuracy':80},
            {'name':'Gust','type':'normal','accuracy':100},
            {'name':'Quick Attack','type':'normal','accuracy':100}
        ]
        
        self.POKEMON_TEMPLATE = [
            {'name':'Squirtle','type':'water','life':120,'attack':50,'defence':50,'moov':[self.parse_moov_dict('Tackle'),self.parse_moov_dict('Water Gun')],'ingame':True},
            {'name':'Pikachu','type':'electric','life':90,'attack':60,'defence':45,'moov':[self.parse_moov_dict('Tackle'),self.parse_moov_dict('Thunder')],'ingame':True},
            {'name':'Bulbasaur','type':'grass','life':180,'attack':40,'defence':50,'moov':[self.parse_moov_dict('Tackle'),self.parse_moov_dict('Leaf')],'ingame':True},
            {'name':'Charmander','type':'fire','life':150,'attack':70,'defence':30,'moov':[self.parse_moov_dict('Tackle'),self.parse_moov_dict('Flamethrower')],'ingame':True},
            {'name':'Pidgey','type':'normal','life':80,'attack':45,'defence':45,'moov':[self.parse_moov_dict('Tackle'),self.parse_moov_dict('Gust')],'ingame':False},
            {'name':'Rattata','type':'normal','life':50,'attack':48,'defence':43,'moov':[self.parse_moov_dict('Tackle'),self.parse_moov_dict('Quick Attack')],'ingame':False}
            ]

        # Declaration of all UI Elements
        ## First Screen - Intro
        self.button_intro = Hitbox((0,0), self.screen_size, 'main_menu')

        self.background = ImageElement("media/ui-elements/background.png")  
        self.start_text_img = ImageElement("media/ui-elements/Press-space-to-start-2-12-2025.png")  
        
        
        ## Second Screen - Main Menu
        self.button_main1 = Hitbox((450, 230), (300, 75), 'new_game')
        self.button_main2 = Hitbox((450, 330), (300, 75), 'load_game')
        self.button_main3 = Hitbox((450, 430), (300, 75), 'exit')
        self.button_main_menu = [self.button_main1, self.button_main2, self.button_main3]
        
        self.background_button_main = ImageElement("media/ui-elements/button.svg")
        
        self.text_button_main = Text("freesansbold.ttf", 36, (0,0,0))
        # New Game
        self.button_pokemon1 = Hitbox((200,200), (200,200),'Squirtle')
        self.button_pokemon2 = Hitbox((500,300), (200,200),'Bulbasaur')
        self.button_pokemon3 = Hitbox((790,200), (200,200),'Charmander')
        self.button_first_pokemon = [self.button_pokemon1, self.button_pokemon2, self.button_pokemon3]

        self.image_pokemon1 = ImageElement("media/Pokemons-assets/front/Squirtle_front.png")
        self.image_pokemon2 = ImageElement("media/Pokemons-assets/front/Bulbasaur_front.png")
        self.image_pokemon3 = ImageElement("media/Pokemons-assets/front/Charmander_front.png")

        ## Third Screen - Game Menu
        self.button_game1 = Hitbox((450, 230), (300, 75), 'ingame')
        self.button_game2 = Hitbox((450, 330), (300, 75), 'pokedex')
        self.button_game3 = Hitbox((450, 430), (300, 75), 'pokemon')
        self.button_game4 = Hitbox((450, 530), (300, 75), 'main_menu')
        self.button_game_menu = [self.button_game1, self.button_game2, self.button_game3, self.button_game4]

        self.rectangle = ImageElement("media/ui-elements/button_square_border.svg")
        
        self.background_button_game = ImageElement("media/ui-elements/button.svg")
                
        self.text_button_game = Text("freesansbold.ttf", 36, (0,0,0))

        ## Fourth Screen - Ingame
        # Moov display 
        self.button_moov1 = Hitbox((225, 500), (225, 75))
        self.button_moov2 = Hitbox((825, 500), (225, 75))
        self.button_moov = [self.button_moov1, self.button_moov2]

        self.background_button_moov = ImageElement("media/ui-elements/button_green.svg")
        self.healthbox = ImageElement("media/ui-elements/MDPokemonBattle_Healthbox.png")

        self.trainer_pokemon = ImageElement("media/Pokemons-assets/front/Squirtle_front.png")
        self.enemy_pokemon = ImageElement("media/Pokemons-assets/back/Squirtle_back.png")
        
        self.text_button_moov = Text("freesansbold.ttf", 36, (0,0,0))

        #Interface
        self.ingame_text = Text("freesansbold.ttf", 36, (0,0,0))

        #battle messages
        self.button_battle_message = Hitbox((0, 460),(1200, 215))
        self.background_battle_message = ImageElement('media/ui-elements/button.png')
        self.text_battle_message = Text("freesansbold.ttf", 36, (0,0,0))

        ## Fourth Screen - Pokedex
      
        self.button_quit = Hitbox((10,10), (30,30), 'game_menu')
        self.button_quit_image = ImageElement("media/ui-elements/button.svg")

        self.box_background = ImageElement("media/ui-elements/box_background.png") 

    def start(self):
        """Start the main loop and switch state to change screen"""
        self.main_loop()
# -1 means loop indefinitely
     
    def main_loop(self):
        self.mixer.music.load('media/audio/bgm_menu.mp3')
        self.mixer.music.play(-1)
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
        if not self.trainer.pokedex:
            print("You can't start without pokemon!")
            return
        
        self.mixer.music.load('media/audio/bgm_fight.mp3')
        self.mixer.music.play(-1)
        """Attributes that needs to be set only once (before battle) are here"""
        #Rival adds pokemon.json into his list and choose one pokemon from it
        self.enemy.load_pokedex()
        self.enemy.choose_pokemon()


        self.battle = Battle(self.trainer, self.enemy)
        self.battle_start = True
        self.ingame_state = "choose_pkmn"

    def events(self):                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.K_SPACE:
                if self.game_state == "intro":
                    self.game_state = self.button_intro.label

            if event.type == pygame.MOUSEBUTTONDOWN:
                #----- Ingame screen events
                mouse_pos = pygame.mouse.get_pos()
                for sprite_rect, pokemon in self.sprite_positions:
                    if sprite_rect.collidepoint(mouse_pos):
                        for pokedex_pokemon in self.trainer.pokedex:
                            if pokedex_pokemon == pokemon:
                                index = self.trainer.pokedex.index(pokemon)
                                if pokemon != self.trainer.pokedex[0]:
                                    self.trainer.pokedex[index], self.trainer.pokedex[0] = self.trainer.pokedex[0], self.trainer.pokedex[index]
                                    self.trainer.update_json()
                                self.battle.trainer_pokemon = pokemon
                                self.battle.trainer_current_hp = pokemon.life
                                self.battle.turn_pkmn = pokemon
                                self.ingame_state = "attacking"

                for button in self.button_moov:
                    if self.game_state == "ingame" and button.is_clicked(pygame.mouse.get_pos()):
                        for moov in self.battle.turn_pkmn.moov:
                            if moov.name == button.label: 
                                self.battle.chosen_moov = moov
                                self.delay = pygame.time.get_ticks() + 1500   
                                self.battle.ingame_state = "attacking" 
                #-----
                #----- Pokelist screen events
                if (self.game_state == "pokedex" or self.game_state == "pokemon") and self.button_quit.is_clicked(pygame.mouse.get_pos()):
                    self.game_state = self.button_quit.label
                #-----
                #----- Game Menu screen events
                for button in self.button_game_menu:
                    if self.game_state == "game_menu" and button.is_clicked(pygame.mouse.get_pos()):
                        self.game_state = button.label
                #-----
                #----- New Game screen events
                for button in self.button_first_pokemon:
                    if self.game_state == "new_game" and button.is_clicked(pygame.mouse.get_pos()):
                        self.game_state = "game_menu"
                        pokedex_data = self.open_json('poke_db')
                        for pokemon in pokedex_data:
                            if pokemon["name"] == button.label:
                                self.trainer.give_first_pokemon(pokemon)
                #-----
                #----- Main Menu screen events
                for button in self.button_main_menu:
                    if self.game_state == "main_menu" and button.is_clicked(pygame.mouse.get_pos()):
                        self.game_state = button.label
                #-----
                #----- Intro screen events
                if self.game_state == "intro" and self.button_intro.is_clicked(pygame.mouse.get_pos()):
                    self.game_state = self.button_intro.label
                #-----

    def parse_moov_dict(self, moov):
        for moovs in self.MOOV_TEMPLATE:
            if moovs["name"] == moov:
                return moovs