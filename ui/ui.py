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

class Text:
    """Parameters: font name, size, text content, color (RGB), x position, y position"""
    def __init__(self, font_name, font_size, text, color, pos_x, pos_y):
        self.font = font_name
        self.size = font_size
        self.text = text
        self.color = color

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.pos_x, self.pos_y))

    def draw(self, game):
        self.font = game.font_button
        game.screen.blit(self.surface, self.rect)

        #def update_text(self, new_text): // TODO need fix on this
        #self.text = new_text
        #self.surface = self.font.render(self.text, True, self.color)
        #self.rect = self.surface.get_rect(center=(self.pos_x, self.pos_y))