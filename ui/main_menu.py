def display_main_menu(game):
    game.button_main1.draw(game.screen)
    game.button_main2.draw(game.screen)
    game.button_main3.draw(game.screen)

    game.background.draw(game.screen, size=game.screen_size)
    game.background_button_main.draw(game.screen, hitbox=game.button_main1)
    game.background_button_main.draw(game.screen, hitbox=game.button_main2)
    game.background_button_main.draw(game.screen, hitbox=game.button_main3)

    game.text_button_main.draw(game.screen, "New Game", hitbox=game.button_main1)    
    game.text_button_main.draw(game.screen, "Load Game", hitbox=game.button_main2)    
    game.text_button_main.draw(game.screen, "Exit", hitbox=game.button_main3)
