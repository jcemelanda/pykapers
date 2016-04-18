import pygame
from pygame import Color
from pygame import Rect
from pygame import Surface
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface([10, 10])
        self.image.fill(Color('red'))

        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.rect.move(10, 0)


class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.xvel = 0
        self.yvel = 0
        self.onGround = True
        self.image = Surface((32, 32))
        self.image.fill(Color("#00FFFF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        self.rect = self.rect.move(3, 0)
        # if up:
        #     # only jump if on the ground
        #     if self.onGround:
        #         self.yvel -= 10
        # if down:
        #     pass
        # if left:
        #     self.xvel = -8
        # if right:
        #     self.xvel = 8
        # if not self.onGround:
        #     # only accelerate with gravity if in the air
        #     self.yvel += 0.3
        #     # max falling speed
        #     if self.yvel > 100:
        #         self.yvel = 100
        # if not(left or right):
        #     self.xvel = 0
        # # increment in x direction
        # self.rect.left += self.xvel
        # # increment in y direction
        # self.rect.top += self.yvel
        # # assuming we're in the air
        # self.onGround = False


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
