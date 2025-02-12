import pygame

pygame.init()

class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    # To draw text
    def draw_text(self, text, position, color=(0, 0, 0)):
        rendered_text= self.font.render(text,True, color, position)
        self.screen.blit(rendered_text, position)

    # To clear the screen
    def clear_screen(self, color=(255, 255, 255)):
        self.screen.fill(color)