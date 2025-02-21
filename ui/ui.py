import pygame


class Hitbox:
    def __init__(self, coord, size, label=''):
        self.label = label
        self.color = (255,150,255)
        self.size = size
        self.coord = coord
        """Draw the hitbox (and color it if visible is true)"""
        self.rect = pygame.Rect(self.coord[0], self.coord[1], self.size[0], self.size[1])
       
        self.visible = False # To debug

        self.active = True

    def draw(self, surface, label=''):
        
        if label:
            self.label = label
        if self.visible:
            pygame.draw.rect(surface, self.color, self.rect)
            
    def is_clicked(self, pos):
        return self.active and self.rect.collidepoint(pos)
        
class ImageElement:
    """(image_path)"""
    def __init__(self, image_path=''):
        self.image_path = image_path

    def draw(self, screen, coords = (0,0), size=(0,0), image_path='', hitbox=''):
        """(screen, coords(opt), size(opt), image_path(opt))"""
        if image_path:
            self.image_path = image_path
        original_img = pygame.image.load(self.image_path)

        if hitbox: 
            self.size = hitbox.size
            self.rect = hitbox.coord

        else: 
            self.size = size
            self.rect = coords #self.surface.get_rect(topleft=(self.pos_x, self.pos_y))
       
        scaled_img = pygame.transform.scale(original_img, self.size)

        screen.blit(scaled_img, self.rect)

class Text:
    def __init__(self, font_name, font_size, color):
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color

    def draw(self, screen, text, coords=(0,0), hitbox=''):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)

        # if a hitbox is given, center the text on it
        if hitbox:
            self.rect = (hitbox.coord[0] + (hitbox.size[0] - self.surface.get_width()) /2, hitbox.coord[1] + (hitbox.size[1] - self.surface.get_height()) /2)

        else:
            self.rect = coords #self.surface.get_rect(topleft=(self.pos_x, self.pos_y))
        
        screen.blit(self.surface, self.rect) #screen = game.screen
