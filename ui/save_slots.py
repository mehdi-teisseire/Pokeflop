def new_game(game):
    #TODO need to display pokemon and add pokemon clicked on: game.trainer.add_pokemon(pokemon) , take pokelist buttons for pokemon
    game.trainer.give_first_pokemon(game.POKEMON_TEMPLATE, game.MOOV_TEMPLATE)
                   
    game.game_state = "game_menu"

def load_game(game):
    game.trainer.load_pokedex(game.MOOV_TEMPLATE)
    game.game_state = "game_menu"
