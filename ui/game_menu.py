def display_game_menu(game):
    game.background.image_path = "media/ui-elements/background.png"
    game.background.draw(game)
    game.background_button_game1.draw(game)
    game.background_button_game2.draw(game)
    game.background_button_game3.draw(game)
    game.background_button_game4.draw(game)

    game.text_button_game1.draw(game, "Battle", game.background_button_game1)    
    game.text_button_game2.draw(game, "Pokedex", game.background_button_game2)    
    game.text_button_game3.draw(game, "Pokelist", game.background_button_game3)
    game.text_button_game4.draw(game, "Main Menu", game.background_button_game4)

    game.button_game1.draw(game.screen, game.background_button_game1)
    game.button_game2.draw(game.screen, game.background_button_game2)
    game.button_game3.draw(game.screen, game.background_button_game3)
    game.button_game4.draw(game.screen, game.background_button_game4)