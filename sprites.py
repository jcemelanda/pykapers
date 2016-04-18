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


class Ladder(Sprite):
	def __init__(self, position, side='right'):
		super().__init__()
		self.image = pygame.image.load('ladder.png').convert_alpha()
		if side == 'left':
			self.image = pygame.transform.flip(self.image, True, False)
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(position)


class Platform(Sprite):

	def __init__(self, position):
		super().__init__()
		self.image = pygame.image.load('platform.png').convert()
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(position)