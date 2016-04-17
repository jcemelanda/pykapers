import pygame
from pygame import Rect
from pygame.sprite import Group

from pygame import FULLSCREEN
from pygame import DOUBLEBUF
from pygame import HWSURFACE

from camera import Camera
from camera import complex_camera
from camera import simple_camera

from sprites import Ball
from sprites import Player

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
        self.bg_size = (size[0] * 8, int(1000 / 1080 * size[1]))
        self.bg = pygame.transform.scale(
            pygame.image.load('bg.png').convert(),
            self.bg_size)
        self.screen = pygame.display.set_mode(size, FLAGS, 32)
        self.camera = Camera(complex_camera, *size)
        self.release_ball = False
        self.ball_cooldown = 20
        self.player = Player(32, 100)

    def draw(self):
        self.screen.blit(self.bg, (0, 0), self.camera.state)
        self.sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.camera.apply(self.player))

    def update(self):
        self.camera.update(self.player)
        # if self.ball_cooldown:
        #     self.ball_cooldown -= 1
        # else:
        #     self.ball_cooldown = 20
        #     self.sprites.add(Ball())
        self.sprites.update()
        self.player.update()
