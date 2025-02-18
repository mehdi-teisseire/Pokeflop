import pygame
def display_pokelist(game):
    
    game.background.image_path = "media/ui-elements/box_background.png"
    game.background.draw(game)
    game.open_json("pokemon")
    pokedex_data = game.open_json('pokemon')
    game.button_pokedex.draw(game)
    
    x, y = 50, 50
    spacing = 50
    
    for pokemon in pokedex_data:
        sprite_path = pokemon['sprite'][0]
        sprite = pygame.image.load(sprite_path)
        game.screen.blit(sprite, (x, y))
        x += spacing
        if x > game.screen.get_width() - spacing:
            x = 50
            y += spacing
    mouse_pos = pygame.mouse.get_pos()
    x, y = 50, 50
    for pokemon in pokedex_data:
        sprite_rect = pygame.Rect(x, y, 40, 40)
        if sprite_rect.collidepoint(mouse_pos):
            game.background_pokedex.draw(game)
            font = pygame.font.Font(None, 24)
            level_text = font.render(f"Level: {pokemon['level']}", True, (0, 0, 0))
            game.screen.blit(level_text, (145, 360))
            pkmn_type_text = font.render(f"Type: {pokemon['type']}", True, (0, 0, 0))
            game.screen.blit(pkmn_type_text, (145, 390))
            name_text = font.render(f"Name: {pokemon['name']}", True, (255, 255, 255))
            game.screen.blit(name_text, (310,360))
            attack_text = font.render(f"Attack: {pokemon['attack']}", True, (255, 255, 255))
            game.screen.blit(attack_text, (500,410))
            defense_text = font.render(f"Defense: {pokemon['defence']}", True, (255, 255, 255))
            game.screen.blit(defense_text, (500,390))
            life_text = font.render(f"Life: {pokemon['life']}", True, (255, 255, 255))
            game.screen.blit(life_text, (500,360))
            moov1_text = font.render(f"Moov1: {pokemon['moov'][0]}", True, (255, 255, 255))
            game.screen.blit(moov1_text, (310,390))
            moov2_text = font.render(f"Moov2: {pokemon['moov'][1]}", True, (255, 255, 255))
            game.screen.blit(moov2_text, (310,410))
        x += spacing
        if x > game.screen.get_width() - spacing:
            x = 50
            y += spacing