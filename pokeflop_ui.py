import pygame

class POKEFLOP:
    def __init__(self, screen):
        self.screen = screen
        
        self.background_image = pygame.image.load('media/picture/bg.png')
        self.logo_image = pygame.image.load('media/picture/PokeFlop-2-12-2025.png')
        self.start_text_image = pygame.image.load('media/picture/Press-space-to-start-2-12-2025.png')

        self.background_image = pygame.image.load('media/picture/bg.png')
        self.logo_image = pygame.image.load('media/picture/PokeFlop-2-12-2025.png')
        self.start_text_image = pygame.image.load('media/picture/press_space_to_start-2-12-2025.png')

    def scale_image(self, image, target_width):
        aspect_ratio = image.get_height() / image.get_width()
        target_height = int(target_width * aspect_ratio)
        return pygame.transform.scale(image, (target_width, target_height))
    
        