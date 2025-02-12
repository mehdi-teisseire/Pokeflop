import pygame
from game_ui import GameUI

class Pokeflop:
    def __init__(self, screen):
        self.screen = screen
        self.ui = GameUI(screen)

        self.background_image = pygame.image.load('media/picture/bg.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 400)) 

        self.logo_image = pygame.image.load('media/picture/PokeFlop-2-12-2025.png')
        self.logo_image = self.scale_image(self.logo_image, 400) 

        self.start_text_image = pygame.image.load('media/picture/Press-space-to-start-2-12-2025.png')
        self.start_text_image = self.scale_image(self.start_text_image, 400)  

    def scale_image(self, image, target_width):
        aspect_ratio = image.get_height() / image.get_width()
        target_height = int(target_width * aspect_ratio)
        return pygame.transform.scale(image, (target_width, target_height))

    def display_pokeflop(self):
        self.ui.clear_screen()
        self.screen.blit(self.background_image, (0, 0))

        logo_rect = self.logo_image.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(self.logo_image, logo_rect)


        start_text_rect = self.start_text_image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 200))
        self.screen.blit(self.start_text_image, start_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.display_menu() 


# screen should be defined in your main game file
# pokeflop = Pokeflop(screen)
# pokeflop.display_pokeflop()