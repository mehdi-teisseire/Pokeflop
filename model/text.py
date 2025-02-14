import pygame

class Text:
    def __init__(self, font_name, font_size, text, color, pos_x, pos_y):
        self.font = pygame.font.Font(font_name, font_size)
        self.text = text
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.pos_x, self.pos_y))

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    #def update_text(self, new_text): // TODO need fix on this
     #   self.text = new_text
      #  self.surface = self.font.render(self.text, True, self.color)
       # self.rect = self.surface.get_rect(center=(self.pos_x, self.pos_y))

pygame.init()

screen = pygame.display.set_mode((800, 600))
# Parameters: font name, size, text content, color (RGB), x position, y position
game_text = Text("freesansbold.ttf", 36, "Hello World", (255, 255, 255), 400, 300)
game_text_2 = Text("freesansbold.ttf", 34,"Hello The World",(255,0,0),200,300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    game_text.draw(screen)
    game_text_2.draw(screen)
    pygame.display.flip()

pygame.quit()