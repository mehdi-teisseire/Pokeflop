import pygame, sys

# To allow the player to choose an attack
def choose_attack(screen, self, pokemon):
    button1 = Button(pokemon.moov1, 100, 300, 200, 50) # should be changed
    button2 = Button(pokemon.moov2, 400, 300, 200, 50) # should be changed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button1.is_clicked(mouse_pos):
                    return pokemon.moov1, pokemon.moove_type_1
                elif button2.is_clicked(mouse_pos):
                    return pokemon.moov2, pokemon.moove_type_2
        screen.fill(Button.WHITE)
        option_text = self.font.render(f"{pokemon.name}, choose your attack:", True, self.BLUE) # Should be changed
        instruction_line1 = self.font.render("Press 1 :" + pokemon.moov1, True, self.BLUE) # Should be changed
        instruction_line2 = self.font.render("Press 2 :" + pokemon.moov2, True, self.BLUE) # Should be changed        
        
        screen.blit(option_text, (100, 200))
        screen.blit(instruction_line1, (100, 250))
        screen.blit(instruction_line2 (100, 280))
        
        button1.draw(screen)
        button2.draw(screen)
        
        pygame.display.flip()