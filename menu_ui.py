import pygame
from utils import Button

class Menu:
    def __init__(self, screen):

        self.background_image = pygame.image.load('media/picture/bg.png')
        self.background_image = pygame.transform.scale(self.background_image, (800,400))

        self.buttons = [
            Button("Button 1", 300, 100, 200, 50),
            Button("Button 2", 300, 160, 200, 50),
            Button("Button 3", 300, 220, 200, 50),
            Button("Button 4", 300, 280, 200, 50),
        ]
    


    