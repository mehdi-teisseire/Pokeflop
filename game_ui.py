import pygame

pygame.init()

class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    