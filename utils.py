import pygame

class Button:
    WHITE = (255, 255, 255) # Should be changed
    BLUE = (0, 0, 255) #Should be changed
    RED = (255, 0, 0) # Should be changed
    font = pygame.font.Font(None, 36) # Should be changed 

    def __init__ (self, text, x, y, width, height):
        self.text = text
        self.text = pygame.Rect(x, y, width, height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.BLUE, self.rect)
        label = self.font.render(self.text, True, self.WHITE)
        screen.blit(label,(self.rect.x + 10, self.rect.y + 10))
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# To render a message on the game pygame screen
def render_message(screen, message, font, position= (100, 100), color = (0, 0, 0), background_color=(255, 255, 255)):
    rendered_text = font.render(message, True, color)
    text_rect = rendered_text.get_rect(topleft = position)
    pygame.draw.rect(screen, background_color, text_rect)
    screen.blit(rendered_text, position)