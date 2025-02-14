import pygame

class UIElement:
    def __init__(self, x, y, width, height, label='', color=(255, 255, 255)):
        self.label = label
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
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
    
    def draw_label(self, game):
        if self.visible:
            return game.font.render(self.label, True, self.color) # Should be changed

class UIText(UIElement):
    def __init__(self, x, y, width, height, label = '', color=(255, 255, 255)):
        super().__init__(x, y, width, height, label, color)

    def draw(self, game, text):
        if self.visible:
            self.label = text
            game.font.render(self.label, True, self.color) # Should be changed
