import pygame
def display_pokedex(game):
    game.background.image_path = "media/ui-elements/box_background.png"
    game.background.draw(game)
    game.open_json("pokedex")
    pokedex_data = game.open_json('pokedex')
    
    x, y = 50, 50
    spacing = 50
    
    for pokemon in pokedex_data:
        sprite_path = pokemon['sprite']
        sprite = pygame.image.load(sprite_path)
        game.screen.blit(sprite, (x, y))
        x += spacing
        if x > game.screen.get_width() - spacing:
            x = 50
            y += spacing