import pygame
from pygame import Color
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(Color('red'))

        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.rect.move(10, 0)
