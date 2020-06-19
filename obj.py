import pygame

class Display:

    def __init__(self, lar, alt, text,local_image):

        self.windows = pygame.display.set_mode((lar, alt))
        self.title = pygame.display.set_caption(text)
        self.bg = pygame.image.load(local_image)



class Element:

    def __init__(self, l_x, a_y, speed, local_image, hp = 0):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(local_image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = l_x
        self.sprite.rect[1] = a_y
        self.sprite.speed = speed
        self.speed_y = speed
        self.hp = hp





