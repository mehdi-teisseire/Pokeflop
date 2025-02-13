import pygame
from ui.ui import UIElement

def display_intro():

    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()
    running = True
    background = pygame.image.load("media/ui-elements/background.png")
    img = pygame.image.load("media/ui-elements/Press-space-to-start-2-12-2025.png")
    img = pygame.transform.scale(img, (579,88 ))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
        background = pygame.transform.scale(background, (800, 400))
        screen.blit(background, (0, 0))
        screen.blit(img, (120, 200))

