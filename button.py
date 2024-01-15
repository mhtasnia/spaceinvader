import pygame.mouse

screen = pygame.display.set_mode((800, 600))


class Button():

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.button_click = False

    def draw(self):
        action = False
        # mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.button_click == False:
                button_click = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            button_click = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
