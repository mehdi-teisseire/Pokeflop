import pygame


class Hitbox:
    def __init__(self, label=''):
        self.label = label
        self.color = (255,150,255)
        self.visible = False # To debug

        self.active = True

    def draw(self, surface, coord, size, label=''):
        if label:
            self.label = label
        """Draw the hitbox (and color it if visible is true)"""
        self.rect = pygame.Rect(coord[0], coord[1] (size[0], size[1]))
        if self.visible:
            pygame.draw.rect(surface, self.color, self.rect)
            
    def is_clicked(self, pos):
        return self.active and self.rect.collidepoint(pos)

class Text:
    def __init__(self, font_name, font_size, color):
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color

    def draw(self, screen, text, coords):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)

        # if a hitbox is given, center the text on it
        if type(coords) == "object": #or if Surface?
            self.rect = coords.get_rect(topleft=(coords.coord[0] + (coords.size[0] - self.surface.get_width()) /2, coords.coord[1] + (coords.size[1] - self.surface.get_height()) /2))

        else: #if type(coords) == "tuple"
            self.rect = coords #self.surface.get_rect(topleft=(self.pos_x, self.pos_y))
        
        screen.blit(self.surface, self.rect) #screen = game.screen
        
class ImageElement:
    def draw(self, screen, image_path, coords, size):
        self.image_path = image_path
        original_img = pygame.image.load(self.image_path)
        scaled_img = pygame.transform.scale(original_img, size)

        if type(coords) == "object": #or if Surface?
            self.rect = coords.get_rect(topleft=(coords.coord[0] + (coords.size[0] - self.surface.get_width()) /2, coords.coord[1] + (coords.size[1] - self.surface.get_height()) /2))

        else: #if type(coords) == "tuple"
            self.rect = coords #self.surface.get_rect(topleft=(self.pos_x, self.pos_y))
       
        screen.blit(scaled_img, self.rect)

# class ImageElement:
#     def __init__(self, image_path, coord, size, is_background = False):
#         self.image_path = image_path
#         self.coord = coord
#         self.size = size
#         self.is_background = is_background

#     def draw(self, game):
#         original_img = pygame.image.load(self.image_path)
#         self.scaled_img = pygame.transform.scale(original_img, self.size)

#         game.screen.blit(self.scaled_img, self.coord)

# class UIElement:
#     def __init__(self,label, x, y, width, height, color=(255, 255, 255)):
#         self.label = label

#         self.rect = pygame.Rect(x, y, width, height)
#         self.color = color

#         self.active = True
#         self.visible = False

#     def draw(self, surface, background = ''):        
#         if background: # Will make Hitbox follow background
#             self.rect.x = background.coord[0]
#             self.rect.y = background.coord[1]
#             self.rect.width = background.size[0]
#             self.rect.height = background.size[1]
#         if self.visible:
#             pygame.draw.rect(surface, self.color, self.rect)
    
#     def set_position(self, x, y):        
#         self.rect.x = x
#         self.rect.y = y

#     def set_size(self, width, height):
#         self.rect.width = width
#         self.rect.height = height

#     def is_clicked(self, pos):
#         return self.active and self.rect.collidepoint(pos)


# class Text:
#     """Parameters: font name, size, text content, color (RGB), x position, y position"""
#     def __init__(self, font_name, font_size, text, color, pos_x, pos_y):
#         self.font = pygame.font.Font(font_name, font_size)
#         self.text = text #TODO May want to either remove, make optional argument, or do either on draw()
#         self.color = color

#         self.pos_x = pos_x
#         self.pos_y = pos_y

#     def draw(self, game, text, background = ''):
#         self.text = text #Change button label to move name
#         self.surface = self.font.render(self.text, True, self.color)
#         if background:
#             self.rect = background.scaled_img.get_rect(topleft=(background.coord[0] + (background.size[0] - self.surface.get_width()) /2, background.coord[1] + (background.size[1] - self.surface.get_height() )/2)) #background.size[0] *0.5 background.size[1] *0.5
#         else:
#             self.rect = self.surface.get_rect(topleft=(self.pos_x, self.pos_y))
#         game.screen.blit(self.surface, self.rect)