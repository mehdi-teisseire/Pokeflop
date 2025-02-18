def display_game_menu(game):
    game.button_game1.draw(game.screen)
    game.button_game2.draw(game.screen)
    game.button_game3.draw(game.screen)
    game.button_game4.draw(game.screen)

    game.background.draw(game.screen, size=game.screen_size, image_path="media/ui-elements/background.png")
    game.rectangle.draw(game.screen, ((game.screen_size[0] - 607)/2, (game.screen_size[1] - 250)/2), (607,424)) #coords=(280, 200)

    game.background_button_game.draw(game.screen, hitbox=game.button_game1)
    game.background_button_game.draw(game.screen, hitbox=game.button_game2)
    game.background_button_game.draw(game.screen, hitbox=game.button_game3)
    game.background_button_game.draw(game.screen, hitbox=game.button_game4)

    game.text_button_game.draw(game.screen, "Battle", hitbox=game.button_game1)    
    game.text_button_game.draw(game.screen, "Pokedex", hitbox=game.button_game2)    
    game.text_button_game.draw(game.screen, "Pokelist", hitbox=game.button_game3)
    game.text_button_game.draw(game.screen, "Main Menu", hitbox=game.button_game4)
