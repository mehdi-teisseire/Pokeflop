import pygame

class UIElement:
    def __init__(self, x, y, width, height, label='', color=(255, 255, 255), text_color=(0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

        self.label = label
        self.text_color = text_color

        self.active = True
        self.visible = True

    def draw(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.color, self.rect)
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_size(self, width, height):
        self.rect.width = width
        self.rect.height = height

    def is_clicked(self, pos):
        return self.active and self.rect.collidepoint(pos)
    
    def draw_label(self, game, x, y):
        if self.visible:
            text = game.font.render(self.label, True, self.text_color) # Should be changed
            game.button_moove1.draw(game.screen)
            game.screen.blit(text, (x, y))
