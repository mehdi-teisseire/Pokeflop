import pygame, sys
from ui.ButtonClass import Button 

from model.TrainerClass import Trainer
from model.EnemyTrainerClass import EnemyTrainer

def game():
    
    trainer1 = Trainer("Hello")
    enemy1 = EnemyTrainer("Rival")

    pokemon_template = [
    {'name':'Squirtle','type':'water','attack':50,'defence':50,'life':100,'sprite':'media/pokemon_assets/Squirtle_back.png','moov1':'Charge','moov2':'Watter gun'},
    {'name':'Pikachu','type':'electric','attack':60,'defence':45,'life':100,'sprite':'media/pokemon_assets/Pikachu_back.png','moov1':'Charge','moov2':'Thunder'},
    {'name':'Bulbasaur','type':'grass','attack':40,'defence':50,'life':100,'sprite':'media/pokemon_assets/Bulbasur_back.png','moov1':'Charge','moov2':'Leaf'},
    {'name':'Charmander','type':'fire','attack':70,'defence':30,'life':100,'sprite':'media/pokemon_assets/Charmander_back.png','moov1':'Charge','moov2':'Flamethrower'},
    {'name':'Pidgey','type':'normal','attack':45,'defence':45,'life':100,'sprite':'media/pokemon_assets/Pidgey_back.png','moov1':'Tackle','moov2':'Gust'},
    {'name':'Rattata','type':'normal','attack':48,'defence':43,'life':100,'sprite':'media/pokemon_assets/Rattata_back.png','moov1':'Tackle','moov2':'Quick Attack'}
    ]

    # while running:
    #     pass


# To allow the player to choose an attack
def display_attack_choice(screen, pokemon):
    button1 = Button(pokemon.moov1, 100, 300, 200, 50) # should be changed
    button2 = Button(pokemon.moov2, 400, 300, 200, 50) # should be changed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button1.is_clicked(mouse_pos):
                    return pokemon.moov1, pokemon.moove_type_1
                elif button2.is_clicked(mouse_pos):
                    return pokemon.moov2, pokemon.moove_type_2
        screen.fill("white")
        option_text = self.font.render(f"{pokemon.name}, choose your attack:", True, self.BLUE) # Should be changed
        instruction_line1 = self.font.render("Press 1 :" + pokemon.moov1, True, self.BLUE) # Should be changed
        instruction_line2 = self.font.render("Press 2 :" + pokemon.moov2, True, self.BLUE) # Should be changed        
        
        screen.blit(option_text, (100, 200))
        screen.blit(instruction_line1, (100, 250))
        screen.blit(instruction_line2 (100, 280))
        
        button1.draw(screen)
        button2.draw(screen)
        
        pygame.display.flip()