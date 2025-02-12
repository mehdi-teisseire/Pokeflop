import pygame

pygame.init()

class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

def draw_text(self, text, position, color=(0, 0, 0)):
    rendered_text= self.font.render(text,True, color, position)
    self.screen.blit(rendered_text, position)
