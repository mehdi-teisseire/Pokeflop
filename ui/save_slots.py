def new_game(game):
    #TODO need to display pokemon and add pokemon clicked on: game.trainer.add_pokemon(pokemon) , take pokelist buttons for pokemon
    game.trainer.add_pokemon(game.trainer.convert_pokemon_to_obj(game.POKEMON_TEMPLATE[0]))
    game.game_state = "game_menu"

def load_game(game):
    game.trainer.load_pokedex()
    game.game_state = "game_menu"
