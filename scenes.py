import pygame
from pygame import Rect
from pygame.sprite import Group

from pygame import FULLSCREEN
from pygame import DOUBLEBUF
from pygame import HWSURFACE

from camera import Camera
from camera import complex_camera

from sprites import Ball, Platform, Ladder

FLAGS = FULLSCREEN | HWSURFACE | DOUBLEBUF


class Scene:
    def __init__(self):
        self.sprites = Group()

    def draw(self):
        pass

    def update(self):
        pass

    def handle_events(self):
        pass


class GameScene(Scene):
    def __init__(self, size):
        super().__init__()
        self.score = 0
        self.lifes = 4
        self.movement = -10
        self.bg_size = (size[0] * 3, int(1000 / 1080 * size[1]))
        self.bg = pygame.transform.scale(
            pygame.image.load('bg.png').convert(),
            self.bg_size)
        self.screen = pygame.display.set_mode(size, FLAGS, 32)
        self.camera = Rect(self.bg_size[0]-size[0], 0, *size)
        self.release_ball = False
        self.ball_cooldown = 20
        self.sprites.add(
            Ladder((30, self.bg_size[1] - 115)),
            Platform((0, self.bg_size[1] - 140)),
            Ladder((650, self.bg_size[1] - 260), side='left'),
            Platform((0, self.bg_size[1] - 280)),
            Platform((0, self.bg_size[1] - 420)),
            Ladder((30, self.bg_size[1] - 400)),
            Platform((0, self.bg_size[1])))

    def draw(self):
        self.screen.blit(self.bg, (0, 0), self.camera)
        self.sprites.draw(self.screen)

    def update(self):
        if self.camera.x <= 0:
            print('invert')
            self.movement *= -1
        elif self.camera.x > self.bg_size[0]-self.camera.width:
            print('invert')
            self.movement *= -1
        self.camera = self.camera.move(self.movement, 0)
        if self.ball_cooldown:
            self.ball_cooldown -= 1
        else:
            self.ball_cooldown = 20
            self.sprites.add(Ball())
        self.sprites.update()
