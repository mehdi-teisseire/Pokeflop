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
        'moov2': (30, 350),
    }
    
    text_items = {
        'level': f"Level: {pokemon['level']}",
        'type': f"Type: {pokemon['type']}",
        'name': f"Name: {pokemon['name']}",
        'attack': f"Attack: {pokemon['attack']}",
        'defence': f"Defense: {pokemon['defence']}",
        'life': f"Life: {pokemon['life']}",
        'moov1': f"Moov: {pokemon['moov'][0]["name"]}",
        'moov2': f"Moov: {pokemon['moov'][1]["name"]}",
    
    }
    for key, text in text_items.items():
        rendered_text = font.render(text, True, (255, 255, 255))
        game.screen.blit(rendered_text, info_positions[key])
        if key == 'name':
            sprite = pygame.image.load(pokemon['sprite']["front"])
            sprite = pygame.transform.scale(sprite, (250, 250))
            game.screen.blit(sprite, (40, 450))

def display_pokemon_sprites(game, pokedex_data):
    """Display all Pokemon sprites in a grid."""
    x, y = 580, 100
    spacing = 50
    sprite_positions = []
    
    for pokemon in pokedex_data:
        sprite = pygame.image.load(pokemon['sprite']["front"])  # From object: sprite = pygame.image.load(pokemon.sprite[0])
        game.screen.blit(sprite, (x, y))
        sprite_positions.append((pygame.Rect(x, y, 50, 55), pokemon))
        
        x += spacing
        if x > game.screen.get_width() - spacing:
            x = 580
            y += spacing
            
    return sprite_positions

def display_pokelist(game):
    """Main function to display the Pokedex."""
    game.background.draw(game.screen, size=game.screen_size, image_path="media/ui-elements/box.png")
    game.box_background.draw(game.screen,size=game.screen_size, image_path="media/ui-elements/box_background.png")
    game.button_quit.draw(game.screen)
    game.button_quit_image.draw(game.screen,hitbox=game.button_quit,image_path="media/ui-elements/cross.svg")

    pokedex_data = game.open_json('poke_db')
    if not pokedex_data:
        return
        
    font = pygame.font.Font(None, 40)

    sprite_positions = display_pokemon_sprites(game, pokedex_data)
    
    current_pokemon = pokedex_data[0] 
    
    mouse_pos = pygame.mouse.get_pos()
    
    if not hasattr(display_pokelist, 'last_click_time'):
        display_pokelist.last_click_time = 0
    
    current_time = pygame.time.get_ticks()
    if pygame.mouse.get_pressed()[0] and current_time - display_pokelist.last_click_time > 300:  # 300ms delay
        for sprite_rect, pokemon in sprite_positions:
            if sprite_rect.collidepoint(mouse_pos):
                existing_pokemon = game.open_json('pokemon')
                pokemon_exists = any(p['name'] == pokemon['name'] for p in existing_pokemon)
                
                if pokemon_exists:
                    existing_pokemon = [p for p in existing_pokemon if p['name'] != pokemon['name']]
                else:
                    existing_pokemon.append(pokemon)
                
                game.save_json(existing_pokemon, 'pokemon')
                display_pokelist.last_click_time = current_time  # Update last click time
                break

    existing_pokemon = game.open_json('pokemon')
    for sprite_rect, pokemon in sprite_positions:
        if sprite_rect.collidepoint(mouse_pos):
            current_pokemon = pokemon
            
        
        if any(p['name'] == pokemon['name'] for p in existing_pokemon):
            pygame.draw.rect(game.screen, (0, 0, 0), sprite_rect, 1) 

    # Render the current Pokemon's information
    render_pokemon_info(game, current_pokemon, font)