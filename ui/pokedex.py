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
    mouse_pos = pygame.mouse.get_pos()
    x, y = 50, 50
    for pokemon in pokedex_data:
        sprite_rect = pygame.Rect(x, y, 40, 40)
        if sprite_rect.collidepoint(mouse_pos):
            game.background_pokedex.draw(game)
            font = pygame.font.Font(None, 24)
            level_text = font.render(f"Level: {pokemon['level']}", True, (0, 0, 0))
            game.screen.blit(level_text, (200, 400))
            pkmn_type_text = font.render(f"Type: {pokemon['pkmn_type']}", True, (0, 0, 0))
            game.screen.blit(pkmn_type_text, (200, 420))
            name_text = font.render(f"Name: {pokemon['name']}", True, (255, 255, 255))
            game.screen.blit(name_text, (mouse_pos[0], mouse_pos[1] + 20))
            attack_text = font.render(f"Attack: {pokemon['attack']}", True, (255, 255, 255))
            game.screen.blit(attack_text, (mouse_pos[0], mouse_pos[1] + 40))
            defense_text = font.render(f"Defense: {pokemon['defence']}", True, (255, 255, 255))
            game.screen.blit(defense_text, (mouse_pos[0], mouse_pos[1] + 60))
            life_text = font.render(f"Life: {pokemon['life']}", True, (255, 255, 255))
            game.screen.blit(life_text, (mouse_pos[0], mouse_pos[1] + 80))
            moov1_text = font.render(f"Moov1: {pokemon['moov1']}", True, (255, 255, 255))
            game.screen.blit(moov1_text, (mouse_pos[0], mouse_pos[1] + 100))
            moov2_text = font.render(f"Moov2: {pokemon['moov2']}", True, (255, 255, 255))
            game.screen.blit(moov2_text, (mouse_pos[0], mouse_pos[1] + 120))
            
        x += spacing
        if x > game.screen.get_width() - spacing:
            x = 50
            y += spacing