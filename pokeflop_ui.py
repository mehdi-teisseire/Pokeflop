import pygame

class POKEFLOP:
    def __init__(self, screen):
        self.screen = screen
        
        self.background_image = pygame.image.load('media/picture/bg.png')
        self.logo_image = pygame.image.load('media/picture/PokeFlop-2-12-2025.png')
        self.start_text_image = pygame.image.load('media/picture/Press-space-to-start-2-12-2025.png')
