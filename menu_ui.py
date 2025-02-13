import pygame
from utils import Button

# The menu screen
class Menu:
    def __init__(self, screen):
        self.screen = screen

        self.background_image = pygame.image.load('media/picture/bg.png')
        self.background_image = pygame.transform.scale(self.background_image, (800,400))

        self.buttons = [
            Button("Button 1", 300, 100, 200, 50),
            Button("Button 2", 300, 160, 200, 50),
            Button("Button 3", 300, 220, 200, 50),
            Button("Button 4", 300, 280, 200, 50),
        ]
    
    # To display the menu screen
    def display_menu(self):
        self.screen.blit(self.background_image, (0, 0))

        for button in self.buttons:
            button.draw(self.screen)
        
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if button.is_clicked(mouse_pos):
                            self.handle_button_click(button.text)
        
    


    