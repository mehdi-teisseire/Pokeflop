from model.TrainerClass import Trainer
from model.EnemyTrainerClass import EnemyTrainer

def new_game(game):
    #TODO need to display pokemon and add pokemon clicked on: game.trainer.add_pokemon(pokemon) , take pokelist buttons for pokemon
    # Player and AI object are created here. It's for deck-building/random encounter feature
    game.trainer = Trainer("Player")
    game.enemy = EnemyTrainer("Rival")
    
    #starter choose
    game.trainer.give_first_pokemon(game.POKEMON_TEMPLATE, game.MOOV_TEMPLATE)
                   
    game.game_state = "game_menu"

    for pokemon in game.trainer.pokedex:
        print(pokemon.name)

def load_game(game):
    # TODO Player and AI object are created here. It's for deck-building/random encounter feature
    game.trainer = Trainer("Player")
    game.enemy = EnemyTrainer("Rival")

    # TODO saveslot/ load different files (trainer name = filename)
    game.trainer.load_pokedex(game.MOOV_TEMPLATE)
    game.game_state = "game_menu"

    for pokemon in game.trainer.pokedex:
        print(pokemon.name)
