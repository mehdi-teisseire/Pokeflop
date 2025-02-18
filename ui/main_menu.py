def display_main_menu(game):
    
    game.background.image_path = "media/ui-elements/background.png"
    game.background.draw(game)
    game.background_button_main1.draw(game)
    game.background_button_main2.draw(game)
    game.background_button_main3.draw(game)

    game.text_button_main1.draw(game, "New Game", game.background_button_main1)    
    game.text_button_main2.draw(game, "Load Game", game.background_button_main2)    
    game.text_button_main3.draw(game, "Exit", game.background_button_main3)

    game.button_main1.draw(game.screen, game.background_button_main1)
    game.button_main2.draw(game.screen, game.background_button_main2)
    game.button_main3.draw(game.screen, game.background_button_main3)