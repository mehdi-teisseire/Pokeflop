def display_intro(game):
    """Display The first screen of the game"""  
    game.button_intro.draw(game.screen) #Hitbox to click for next screen
    game.background.draw(game.screen, size=game.screen_size, image_path="media/ui-elements/background.png")
    game.start_text_img.draw(game.screen, (180, 300), (869, 132))
    