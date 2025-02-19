import pygame

def render_pokemon_info(game, pokemon, font):
    """Render information for a single Pokemon."""
    info_positions = {
        'name': (30, 130),
        'level': (300, 130),
        'type': (30, 180),
        'attack': (300, 300),
        'defence': (300, 350),
        'life': (300, 250),
        'moov1': (30, 300),
        'moov2': (30, 350)
    }
    
    text_items = {
        'level': f"Level: {pokemon['level']}",
        'type': f"Type: {pokemon['type']}",
        'name': f"Name: {pokemon['name']}",
        'attack': f"Attack: {pokemon['attack']}",
        'defence': f"Defense: {pokemon['defence']}",
        'life': f"Life: {pokemon['life']}",
        'moov1': f"Moov: {pokemon['moov'][0]}",
        'moov2': f"Moov: {pokemon['moov'][1]}"
    }
    
    for key, text in text_items.items():
        rendered_text = font.render(text, True, (255, 255, 255))
        game.screen.blit(rendered_text, info_positions[key])

def display_pokemon_sprites(game, pokedex_data):
    """Display all Pokemon sprites in a grid."""
    x, y = 580, 100
    spacing = 50
    sprite_positions = []
    
    for pokemon in pokedex_data:
        sprite = pygame.image.load(pokemon['sprite']["front"])  # From object: sprite = pygame.image.load(pokemon.sprite[0])
        game.screen.blit(sprite, (x, y))
        sprite_positions.append((pygame.Rect(x, y, 40, 40), pokemon))
        
        x += spacing
        if x > game.screen.get_width() - spacing:
            x = 50
            y += spacing
            
    return sprite_positions

def display_pokedex(game):
    """Main function to display the Pokedex."""
    game.background.draw(game.screen, size=game.screen_size, image_path="media/ui-elements/box.png")
    game.box_background.draw(game.screen,size=game.screen_size, image_path="media/ui-elements/box_background.png")
    game.button_quit.draw(game.screen)
    game.button_quit_image.draw(game.screen,hitbox=game.button_quit,image_path="media/ui-elements/cross.svg")

    pokedex_data = game.open_json('pokedex') # from object: # pokedex_data = game.trainer.pokedex
    if not pokedex_data:
        return
        
    font = pygame.font.Font(None, 40)

    sprite_positions = display_pokemon_sprites(game, pokedex_data)
    
    current_pokemon = pokedex_data[0]
    
    mouse_pos = pygame.mouse.get_pos()
    for sprite_rect, pokemon in sprite_positions:
        if sprite_rect.collidepoint(mouse_pos):
            current_pokemon = pokemon
            break
    
    # Render the current Pokemon's information
    render_pokemon_info(game, current_pokemon, font)